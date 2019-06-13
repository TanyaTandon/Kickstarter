"""
Enables the command line execution of multiple modules within src/
This module combines the argparsing of each module within src/ and enables the execution of the corresponding scripts
so that all module imports can be absolute with respect to the main project directory.
To understand different arguments, run `python run.py --help`
"""


import os
import argparse
import config.config as config
import logging
import logging.config

# The logging configurations are called from local.conf
logging.config.fileConfig(os.path.join("config","logging_local.conf"))
logger = logging.getLogger()

from src.load_data import run_loading
from src.model import create_db
from src.clean import clean_loading
from src.model_train import train_model
from app.app import run_app

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Data processes")
    subparsers = parser.add_subparsers()

    #Sub parser for loading the data
    sub_process = subparsers.add_parser('loadS3')
    sub_process.add_argument("--where", type=str, default="Local", help="'Local' or 'AWS'; The destination bucket name needs to be provided in case of AWS")
    sub_process.add_argument("--bucket", default="None", help="Destination S3 bucket name")
    sub_process.set_defaults(func= run_loading)

    #Sub parser for cleaning the data
    sub_process = subparsers.add_parser('Returns_cleaned_data')
    sub_process.add_argument("--where", type=str, default="Local", help="'Local' or 'AWS'; The destination bucket name needs to be provided in case of AWS")
    sub_process.add_argument("--bucket", default="None", help="Destination S3 bucket name")
    sub_process.set_defaults(func=clean_loading)

    # Sub parser for creating database 
    sb_create = subparsers.add_parser("create_db", description="Create database to track usage logs")
    sb_create.add_argument("--where", default="Local", help="'Local' or 'AWS'")
    sb_create.set_defaults(func=create_db)


    # Sub-parser for training the model
    sb_train_model = subparsers.add_parser("Model_fitting", description="Trains the model")
    sb_train_model.add_argument("--where", default="Local", help="'Local' or 'AWS'; The destination bucket name needs to be provided in case of AWS")
    sb_train_model.add_argument("--bucket", default="None", help="Destination S3 bucket name")
    sb_train_model.set_defaults(func=train_model)

    # Sub-parser for starting the app
    sb_run_app = subparsers.add_parser("run_app", description="Runs the app")
    sb_run_app.add_argument("--where", default="Local", help="'Local' or 'AWS'; The S3 bucket name needs to be provided in case of AWS")
    sb_run_app.add_argument("--bucket", default="None", help="S3 bucket name from where to source the model")
    sb_run_app.set_defaults(func=run_app)

    
    args = parser.parse_args()
    args.func(args)






