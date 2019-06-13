WHERE=Local
MODEL_NAME=GradientBoosting.pkl
CONFIG=config.yml
BUCKET=bin

.PHONY: venv load_data clean_data create_db train_model run_app

Kickstarter/${BUCKET}/activate: requirements.txt
	test -d Kickstarter || virtualenv Kickstarter
	. Kickstarter/${BUCKET}/activate; pip install -r requirements.txt
	touch Kickstarter/${BUCKET}/activate

venv: Kickstarter/${BUCKET}/activate
	
load_data: venv
	. Kickstarter/${BUCKET}/activate; python run.py loadS3 --where=${WHERE} --bucket=${YOUR_S3_BUCKET}

clean_data: load_data venv
	. Kickstarter/${BUCKET}/activate; python run.py Returns_cleaned_data --where=${WHERE} --bucket=${YOUR_S3_BUCKET}

create_db: venv
	. Kickstarter/${BUCKET}/activate; python run.py create_db --where=${WHERE}

train_model: clean_data venv
	. Kickstarter/${BUCKET}/activate; python run.py Model_fitting --where=${WHERE} --bucket=${YOUR_S3_BUCKET}

app: train_model venv
	. Kickstarter/${BUCKET}/activate; python run.py run_app

all: app venv
