Mid point review

Project Owner: Tanya Tandon 
QA Owner: Saurabh Annadate
# Dear Genie - Kickstarter

**Vision**: In the history of the world, today is the best time for a dream to come true. With distances in the world shrinking by the internet, Kickstarter is one of the fastest and easiest ways to kickstart a great idea. This project aligns with Kickstarters mission to "help bring creative projects to life" by predicting if a kickstarter campaign will be successful or not. It will help any and everyone launching a campaign on Kickstarter. Users with failed campaigns can leverage the platform by exploring alternate goals as well as alternate completion dates to understand the tweaks needed for a more likely success. 

**Mission**:  Developing a classifier algorithm that predicts whether a Kickstarter project will be successful or not. This will help users evaluate whether their campaign will be able to raise money or not even before they do it. It will further suggest alternate completion dates as well as alternate goals to users that will be more likely to succeed. This will help users modify their campaign for a sure shot success.

**Success criteria**:  
- Accuracy of at least 60% ( Using AUC or Misclassification rate) 
- Inbound traffic of at least 100 Kickstarter campaign starters
- Above 70 % positive feedback on UI design

# Planned work 

### Theme 1: Model Development

***Epic 1:*** Design data set that best represents  all aspects needed to classify a Kickstarter project
-  **Story 1:** Downloading the relevant dataset from Kaggle keeping in mind that it would be possible to join them later 
- **Story 2:** Connect all these data sets
- **Story 3:** Design new features

***Epic 2:*** Data preparation 
- **Story 1:** Exploratory Data Analysis
- **Story 2:** Data Cleaning 

***Epic 3:*** Model Development

- **Story 1:** Build logistic regression model
- **Story 2:** Build boosted trees
- **Story 3:** Build Random Forest
- **Story 4:** Compare measures of success (AOC, missclass rate, recall, etc) (%) for each on new data 
- **Story 5:** Reiterate the model for improvement

***Epic 4:*** Create unit test scripts to test model functionality 

### Theme2 : App Development 
***Epic 1:*** Setup Deployment pipeline
- **Story 1:** Setting up the requirements.txt from the current environment state to make reproducible environment
- **Story 2:**  Set up S3 instance 
- **Story 3:**  Initialize RDS database
- **Story 4:**  Deploy the flask app

***Epic 2:*** Setup front end interface UI where the users will interact with the model built
- **Story1:**  Setup a basic front end interface with all the required options
- **Story 2:**  Improve the basic front end interface to include engaging gifs on the Home page

***Epic 3:*** Create UAT test scripts to test that UI is working as expected to intake selections and output accordingly
- **Story1:**  Check for model functionality 
- **Story 2:** Check for exception handling by UI 

***Epic 4:***  Create logging for easy debugging and error notifications



# Backlog 
**Sprint Sizing Legend:**

-   0 points - quick chore
-   1 point ~ 1 hour (small)
-   2 point ~ 2.5 hour ( slightly bigger than small) 
-   3 points ~ 1/2 day (medium)
-   4 points ~ 1 day (large)
-   8 points - big and needs to be broken down more when it comes to execution (okay as placeholder for future work though)
    
1.  **Theme1.epic1.story1**  (2pts) - (completed)
    
2.  **Theme1.epic1.story2**  (2pts) - (completed)
    
3.  **Theme1.epic1.story3**  (2pts) - (completed)
    
4.  **Theme1.epic2.story1**  (2pts) - (completed)

5.  **Theme1.epic2.story2**  (2pts) - (completed)
    
6.  **Theme1.epic3.story1**  (2pts) - (completed)
    
7.  **Theme1.epic3.story2**  (2pts) - (completed)
    
8.  **Theme1.epic3.story3**  (2pts) - (completed)
    
9.  **Theme1.epic3.story4**  (1pts) - (completed)
    
10.  **Theme1.epic3.story5**  (2pts) - (completed)
    
11.  **Theme1.epic4**  (3pts)
    
12.  **Theme2.epic1.story1**  (2pts) (completed)
    
13.  **Theme2.epic1.story2**  (1pts) (completed)
    
14.  **Theme2.epic1.story3**  (1pts) (completed)
 
15.  **Theme2.epic1.story4**  (1pts) (completed)

16.  **Theme2.epic1.story5**  (1pts) (completed)

17.  **Theme2.epic2.story1**  (3pts) (completed)
    
18.  **Theme2.epic2.story2**  (4pts) (completed)

19.  **Theme2.epic3.story1**  (1pts) (completed)

20.  **Theme2.epic3.story2**  (1pts) (completed)
    
21.  **Theme2.epic4.story1**  (2pts) (completed)
    
22.  **Theme2.epic4**  (2pts)
    


# Icebox 

***Epic 1 :*** Develop a recommendation bar to suggest alternate goals and alternate completion dates for success of the projects  
- **Story 1:** Integrate the model with this functionality 
- **Story 2:** Integrate the UI with this functionality 



# Repo Structure

```
├── README.md                         <- You are here
│
├── app
│   ├── static/                       <- CSS, JS files that remain static 
│   ├── templates/                    <- HTML (or other code) that is templated and changes based on a set of inputs
│   ├── models.py                     <- Creates the data model for the database connected to the Flask app 
│   ├── __init__.py                   <- Initializes the Flask app and database connection
│
├── config                            <- Directory for yaml configuration files for model training, scoring, etc
│   ├── logging/                      <- Configuration files for python loggers
│
├── data                              <- Folder that contains data used or generated. Only the external/ and sample/ subdirectories are tracked by git. 
│   ├── archive/                      <- Place to put archive data is no longer usabled. Not synced with git. 
│   ├── external/                     <- External data sources, will be synced with git
│   ├── sample/                       <- Sample data used for code development and testing, will be synced with git
│
├── docs                              <- A default Sphinx project; see sphinx-doc.org for details.
│
├── figures                           <- Generated graphics and figures to be used in reporting.
│
├── models                            <- Trained model objects (TMOs), model predictions, and/or model summaries
│   ├── archive                       <- No longer current models. This directory is included in the .gitignore and is not tracked by git
│
├── notebooks
│   ├── develop                       <- Current notebooks being used in development.
│   ├── deliver                       <- Notebooks shared with others. 
│   ├── archive                       <- Develop notebooks no longer being used.
│   ├── template.ipynb                <- Template notebook for analysis with useful imports and helper functions. 
│
├── src                               <- Source data for the project 
│   ├── archive/                      <- No longer current scripts.
│   ├── helpers/                      <- Helper scripts used in main src files 
│   ├── sql/                          <- SQL source code
│   ├── add_songs.py                  <- Script for creating a (temporary) MySQL database and adding songs to it 
│   ├── ingest_data.py                <- Script for ingesting data from different sources 
│   ├── generate_features.py          <- Script for cleaning and transforming data and generating features used for use in training and scoring.
│   ├── train_model.py                <- Script for training machine learning model(s)
│   ├── score_model.py                <- Script for scoring new predictions using a trained model.
│   ├── postprocess.py                <- Script for postprocessing predictions and model results
│   ├── evaluate_model.py             <- Script for evaluating model performance 
│
├── test                              <- Files necessary for running model tests (see documentation below) 

├── run.py                            <- Simplifies the execution of one or more of the src scripts 
├── app.py                            <- Flask wrapper for running the model 
├── config.py                         <- Configuration file for Flask app
├── requirements.txt                  <- Python package dependencies 
```

# Instructions to run the application

Ths application can be run on both local system as well as on AWS. Steps on how to deploy the app for both settings is given below.

## 1. Setting up AWS
Either you run on `AWS` or `Local`, you need to set up your aws account. There are two ways to do it. 
#### 1.1. Download .pem file from AWS 
You can check if you own it by going to your terminal and typing `cd ~/.aws` . If it exists, then you are good otherwise, follow 1.2. 
#### 1.2. Set up configure using terminal 
```bash
pip install awscli
aws configure
```
Input values in `AWS Access key ID` and `AWS Secret Access Key`. 
Press enter on region and output format. 

## 2. Specify in configure file(s) if the app will be run locally or on AWS

#### 2.1. Running on a local machine

 **config/config.py**
* Make sure that the `WHERE` variable is set to `Local`
* Ensure that the `HOST` variable is set to  `127.0.0.1`
* Keep the default `PORT` of `3000` ; However, change it if this port is not available

**Makefile**
* Ensure that the `WHERE` variable is set to `Local`
* Ensure that the variable `BUCKET` is set to `Scipts` if running on Windows, else `bin` if on Linux or MacOS

#### 2.2. Running on AWS

**RDS configurations**
In order to use RDS, the RDS credentials need to be added to the os environment. Add the following variables to the environment:
* `MYSQL_USER `: *Username to access the RDS instance*
* `MYSQL_PASSWORD` : *Password to access the RDS instance*
* `MYSQL_HOST` : *RDS instance endpoinr*
* `MYSQL_PORT` : *Port number to access the instance*
* `MYSQL_DB` : *Name of the database*

**Makefile**
* Make sure that the `WHERE` variable is set to `AWS`
* Set the variable `YOUR_S3_BUCKET` to the S3 bucket that you intend to use
* Make sure that the variable `BUCKET` is set to `AWS` if running on Windows server, else "bin" if on Linux server

## 3. Run all the functions in one step

In command line, type 
`make all`

## 4. Run each function seperately

### 4.1. Set up environment

#### With `virtualenv`

```bash
pip install virtualenv

virtualenv Kickstarter

source Kickstarter/bin/activate

pip install -r requirements.txt

```
#### With `conda`

```bash
conda create -n Kickstarter python=3.7.3
conda activate Kickstarter
pip install -r requirements.txt

```

#### With `Make`

```bash
make venv
```


### 4.2. Download the data

Original source: [https://www.kaggle.com/kemical/kickstarter-projects](https://www.kaggle.com/kemical/kickstarter-projects)
The data has also been loaded on a public AWS bucket called: `bossbucket`

### Local
#### Local: Using run file
Run the following command in bash:
```bash
python run.py loadS3
```
Running this code will download the raw data from the s3 bucket and will put it in **/Data/raw/**

#### Local: With `Make`
```
make load_data
```


#### AWS
####  AWS: Using run file
Run the following command in bash:
```bash
python run.py loadS3 --where=AWS --bucket=<destination_bucket_name>
```
Running this code will download the raw data from the s3 bucket and will put it in **<destination_bucket_name>/raw/**
#### AWS: With `Make`
```
make load_data
```
### 4.3. Initialize the database

#### Local
Run the following command in bash:
```bash
python run.py create_db
```
Running this code will create a sqlite database to log the app usage at: **/Database/msia423.db**
The table name is `Userinput`

With `Make`
```
make create_db
```

#### AWS

Make sure the environment varia
Run the following command in command line:
```bash
python run.py create_db --where=AWS
```

With `Make`
```
make create_db
```

Running this code will create the database specified in the given RDS instance 

### 4.4. Clean the data

#### Local
Run the following command in command line:
```bash
python run.py clean_data
```

With `Make`
```
make clean_data
```
Running this code will clean the raw data and create a cleaned dataset at: **/Data/clean/**

#### AWS
Run the following command in command line:
```bash
python run.py clean_data --where=AWS --bucket=<destination_bucket_name>
```

With `Make`
```
make clean_data
```
Running this code will clean the raw data from the S3 bucket and will put it in **<destination_bucket_name>/clean/**

### 4.5. Train Model

#### Local
Run the following command in command line:
```bash
python run.py Model_fitting
``` 

With `Make`
```
make train_model
```
Running this code will train the prediction model and will dump it at: **/models/**

#### AWS
Run the following command in command line:
```bash
python run.py Model_fitting --where=AWS --bucket=<destination_bucket_name>
```

With `Make`
```
make train_model
```
Running this code will clean the raw data from the S3 bucket and will put it in **<destination_bucket_name>/models/**

### 4.6. Launch app

#### Local or AWS
Run the following command in command line:
```bash
python run.py run_app
``` 

With `Make`
```
make app
```
Running this code will start the flask app at the IP specified in **config/config.py**

## Testing

In order to unit test the functions, follow the following steps:
1. Navigate to the tests folder
2. Run the following command on the command line:
```
pytest test_all_functions.py
```

## Logging
All logs are saved at **logs/logfile.log**

