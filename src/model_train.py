from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import yaml
from sklearn import metrics
import logging
import os
import pickle
import boto3
import datetime

logger = logging.getLogger()


def fitting_local(config):
	"""Loads the input data and trains the model
	
	The trained model is saved in <s3-bucket-name>/models/<model-name>
	Args:  
		config: config dictionary
 
	Returns: None
	"""
	try: 
		df = pd.read_csv("./data/clean/cleaned_data.csv")
		y = df ["state"]
		df = df.drop( "state", 1)

		# Encoding category  and main_ category
		df = pd.get_dummies(df, columns = ['category'])
		df = pd.get_dummies(df, columns = ['main_category'])
		df = pd.get_dummies(df, columns = ['currency'])
		df = pd.get_dummies(df, columns=['country'])

		
		ingest_parameters = config["train_model"]["start"]
		seed = ingest_parameters["seed"]
		split_coeff = ingest_parameters[ "split"]


		X_train, X_test, Y_train, Y_test = train_test_split(
			df, y, test_size=  split_coeff, random_state = seed)
		

		params = config["train_model"]["start"]["params"]
		clf = GradientBoostingClassifier(**params)
		FittedModel = clf.fit(X_train, Y_train)

		pickle.dump(FittedModel, open("models/GradientBoosting.pkl", 'wb'))
		X_train.to_csv("models/X_train.csv", index = False, header = True)
		X_test.to_csv("models/X_test.csv", index = False, header = True)
		Y_train.to_csv("models/Y_train.csv", index = False, header = True)
		Y_test.to_csv("models/Y_test.csv", index = False, header = True)

		ypred_proba_test =pd.DataFrame(clf.predict_proba(X_test)[:,1])
		ypred_bin_test = pd.DataFrame(clf.predict(X_test)) 
		ypred_proba_test.to_csv("models/ypred_proba_test.csv", index = False,header = True)
		ypred_bin_test.to_csv("models/ypred_bin_test.csv", index = False,header = True)
	except:
		logger.warning("Not able to train the modellocally. ")

def train_model_AWS(config, bucket_name):
	"""Loads the input data and trains the model
	
	The trained model is saved in <s3-bucket-name>/models/<model-name>
	Args:  
		config: config dictionary
 
	Returns: None
	"""
	logger.debug('Running the train_model_AWS function')
	#Loading the file
	logger.debug("Loading the raw file.")
	try:    
		client = boto3.client('s3')
		resource = boto3.resource('s3')
		obj = client.get_object(Bucket=bucket_name, Key=config['clean']['save_location'] + "/" + config['clean']['output_file_name'])
		my_bucket = resource.Bucket(bucket_name)
		df = pd.read_csv(obj['Body'])
	 

	except Exception as e:
		logger.error(e)
		return
	 #Training model
	logger.debug('Successfully loaded the input file. Training the model now.')
	try:
		# Encoding category  and main_ category
		y = df ["state"]
		df = df.drop( "state", 1)
		df = pd.get_dummies(df, columns = ['category'])
		df = pd.get_dummies(df, columns = ['main_category'])
		df = pd.get_dummies(df, columns = ['currency'])
		df = pd.get_dummies(df, columns=['country'])

	   
		ingest_parameters = config["train_model"]["start"]
		seed = ingest_parameters["seed"]
		split_coeff = ingest_parameters[ "split"]

		
		X_train, X_test, Y_train, Y_test = train_test_split(
			df, y, test_size=  split_coeff, random_state = seed)
		

		params = config["train_model"]["start"]["params"]
	   
		
		clf = GradientBoostingClassifier(**params)
		FittedModel = clf.fit(X_train, Y_train)
		acc = clf.score(X_test, Y_test)

		model_name = config['train_model']['model'] + "_" + config['train_model']['version'] + ".pkl"

		model_eval_name = config['train_model']['model'] + "_" + config['train_model']['version'] + ".txt"
 

		pickle.dump(FittedModel , open(os.path.join(config['train_model']['save_location'], model_name),'wb'))

		f = open(os.path.join(config['train_model']['save_location'], model_eval_name),"w+")
		f.write('Performance measures for model: {}\n'.format(model_name))
		f.write('Date of run: {} \n'.format(str(datetime.datetime.now())))
		f.write(' Accuracy: %0.3f\n' % acc)
		f.close()

		print(os.path.join(config['train_model']['save_location'], model_name))

		my_bucket.upload_file(os.path.join(config['train_model']['save_location'], model_name),Key=config['train_model']['save_location'] + "/" + model_name)
		os.remove(os.path.join(config['train_model']['save_location'], model_name))

		logger.debug('Model Written. Writing model performance metric')
 
		my_bucket.upload_file(os.path.join(config['train_model']['save_location'], model_eval_name),Key=config['train_model']['save_location'] + "/" + model_eval_name)
		os.remove(os.path.join(config['train_model']['save_location'], model_eval_name))
		logger.info('Model has been successfully trained and the model and the performance metric has been written in {}'.format(bucket_name + "/" + config['train_model']['save_location']))

	except Exception as e:
		logger.error(e)
		return

def train_model(args):
	'''Trains the model based on the configurations provided
	
	Args:
		args: Argparse args - includes args.where
		
	Returns:
		None
	'''
	logger.debug('Running the train_model function')

	with open(os.path.join("config","config.yml"), "r") as f:
		config = yaml.safe_load(f)

	if args.where == "Local":
		fitting_local(config)

	elif args.where == "AWS":
		train_model_AWS(config, args.bucket)
			
	else:
		logger.error('Kindly check the arguments and rerun. To understand different arguments, run `python run.py --help`')
		return
