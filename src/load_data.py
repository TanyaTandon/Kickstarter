

"""
This module contains functions to load the raw data from the source and dump it into the desired location
"""
import os
import logging
import boto3
import config.config as config


logger = logging.getLogger(__name__)

def run_loading_local():
    '''Fetches the data from the raw source and dumps it on the local drive
    
    Args:
        None
        
    Returns:
        None
    '''
    logger.debug('Running the run_loading_local function')
    s3 = boto3.client('s3')

    for object in s3.list_objects_v2(Bucket=config.SOURCE_BUCKET)['Contents']:
        try: 

            logger.info("Downloading %s from bucket %s", object['Key'], config.SOURCE_BUCKET)
            s3.download_file(config.SOURCE_BUCKET, object['Key'], os.path.join("data", "raw", object['Key']))
            logger.info("File successfully downloaded to %s", os.path.join("data", "raw"))

        except Exception as e:
            logger.error(e)
            return

def run_loading_AWS(bucket_name):
    '''Fetches the data from the raw source and dumps it on the AWS s3 bucket provided
    
    All data is dumped at <s3-bucket name>/data/raw
    
    Args:
        args: Argparse args - should include args.where, args.bucket
        
    Returns:
        None
    '''
    logger.debug('Running the run_loading_AWS function')
    s31 = boto3.client('s3')
    s32 = boto3.resource('s3')
    for object in s31.list_objects_v2(Bucket=config.SOURCE_BUCKET)['Contents']:
        try:
            copy_source = {'Bucket': config.SOURCE_BUCKET, 'Key': object['Key']}
            bucket = s32.Bucket(bucket_name)
            logger.info("Copying %s from bucket %s to bucket %s", object['Key'], config.SOURCE_BUCKET, bucket_name)
            bucket.copy(copy_source, "data/raw/" + object['Key'])
            logger.info("File successfully copied.")
        
        except Exception as e:
            logger.error(e)

def run_loading(args):
    '''Fetches the data from the raw source and dumps it at the location specified
    
    Args:
        args: Argparse args - includes args.where, args.manual
        
    Returns:
        None
    '''
    logger.debug('Running the run_loading function')
      
    if args.where == "Local":
        run_loading_local()
    
    elif args.where == "AWS":
        run_loading_AWS(args.bucket)
            
    else:
        raise ValueError('Kindly check the arguments and rerun. To understand different arguments, run `python run.py --help`')