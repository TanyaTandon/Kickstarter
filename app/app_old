import pickle
import traceback
import os
#import xgboost
import pandas as pd
from flask import render_template, request, redirect, url_for
import logging.config
#from app import db, app
from flask import Flask
import sys
sys.path.insert(0, '../src')
from model import Userinput
sys.path.insert(0, '../app')
from flask_sqlalchemy import SQLAlchemy


# Initialize the Flask application
app = Flask(__name__)

# Configure flask app from config.py
app.config.from_pyfile('../config/config.py')

# Define LOGGING_CONFIG in config.py - path to config file for setting
# up the logger (e.g. config/logging/local.conf)
#logging.config.fileConfig(app.config["LOGGING_CONFIG"])
#logger = logging.getLogger("kickstarter-predictor")
#logger.debug('Test log')

# Initialize the database
db = SQLAlchemy(app)


@app.route('/')
def homepage():
    """Homepage of this prediction system.
    
    Returns: rendered html template
    """

    try:
        return render_template('homepage.html')
    except:
        logger.warning("Not able to display homepage, error page returned")
        return render_template('error.html')

@app.route('/index', methods=['POST','GET'])
def index():
    """Main view that get customer information for evaluation.
    
    Create view into evaluation page that allows to input information and predict price
    
    Returns: rendered html template
    """
    
    #ogger.debug('index called.')
    #Trying to load the index page
    try:
       return render_template('index.html')
    except Exception as e:
        #logger.error(e)
        return render_template('error.html')


@app.route('/add', methods=['POST','GET'])
def add_entry():
    """View that process a POST with new customer input
    Returns: rendered html template with evaluation results.
    """

    try:
        # retrieve features
        #logger.info("Begining to retrieving")
        Name = request.form['name']
        Country = request.form['country']
        Main_Category = request.form['main_category']
        Category = request.form['category']
        Currency = request.form['currency']
        Date_Started = request.form['date_started']
        Date_Ended = request.form['date_ended']
        Goal = request.form['goal']
        print(Goal)
        print("FUCK YEA")
        #logger.info("Successfully retrieved all inputs ")

        # load trained model
        path_to_tmo = app.config["PATH_TO_MODEL"]
        print(path_to_tmo)
        with open(path_to_tmo, "rb") as f:
            model = pickle.load(f)
        print("model input")
        #logger.info("model loaded!")

        # create a dataframe to store inputs for prediction
        test_f = pd.DataFrame(columns= ['goal', 'usd_goal_real', 'duration', 'month_launched', 'length_name', 'category_3D Printing', 'category_Academic', 'category_Accessories', 'category_Action', 'category_Animals', 'category_Animation', 'category_Anthologies', 'category_Apparel', 'category_Apps', 'category_Architecture', 'category_Art', 'category_Art Books', 'category_Audio', 'category_Bacon', 'category_Blues', 'category_Calendars', 'category_Camera Equipment', 'category_Candles', 'category_Ceramics', "category_Children's Books", 'category_Childrenswear', 'category_Chiptune', 'category_Civic Design', 'category_Classical Music', 'category_Comedy', 'category_Comic Books', 'category_Comics', 'category_Community Gardens', 'category_Conceptual Art', 'category_Cookbooks', 'category_Country & Folk', 'category_Couture', 'category_Crafts', 'category_Crochet', 'category_DIY', 'category_DIY Electronics', 'category_Dance', 'category_Design', 'category_Digital Art', 'category_Documentary', 'category_Drama', 'category_Drinks', 'category_Electronic Music', 'category_Embroidery', 'category_Events', 'category_Experimental', 'category_Fabrication Tools', 'category_Faith', 'category_Family', 'category_Fantasy', "category_Farmer's Markets", 'category_Farms', 'category_Fashion', 'category_Festivals', 'category_Fiction', 'category_Film', 'category_Fine Art', 'category_Flight', 'category_Food', 'category_Food Trucks', 'category_Footwear', 'category_Gadgets', 'category_Games', 'category_Gaming Hardware', 'category_Glass', 'category_Graphic Design', 'category_Graphic Novels', 'category_Hardware', 'category_Hip-Hop', 'category_Horror', 'category_Illustration', 'category_Immersive', 'category_Indie Rock', 'category_Installations', 'category_Interactive Design', 'category_Jazz', 'category_Jewelry', 'category_Journalism', 'category_Kids', 'category_Knitting', 'category_Latin', 'category_Letterpress', 'category_Literary Journals', 'category_Literary Spaces', 'category_Live Games', 'category_Makerspaces', 'category_Metal', 'category_Mixed Media', 'category_Mobile Games', 'category_Movie Theaters', 'category_Music', 'category_Music Videos', 'category_Musical', 'category_Narrative Film', 'category_Nature', 'category_Nonfiction', 'category_Painting', 'category_People', 'category_Performance Art', 'category_Performances', 'category_Periodicals', 'category_Pet Fashion', 'category_Photo', 'category_Photobooks', 'category_Photography', 'category_Places', 'category_Playing Cards', 'category_Plays', 'category_Poetry', 'category_Pop', 'category_Pottery', 'category_Print', 'category_Printing', 'category_Product Design', 'category_Public Art', 'category_Publishing', 'category_Punk', 'category_Puzzles', 'category_Quilts', 'category_R&B', 'category_Radio & Podcasts', 'category_Ready-to-wear', 'category_Residencies', 'category_Restaurants', 'category_Robots', 'category_Rock', 'category_Romance', 'category_Science Fiction', 'category_Sculpture', 'category_Shorts', 'category_Small Batch', 'category_Software', 'category_Sound', 'category_Space Exploration', 'category_Spaces', 'category_Stationery', 'category_Tabletop Games', 'category_Taxidermy', 'category_Technology', 'category_Television', 'category_Textiles', 'category_Theater', 'category_Thrillers', 'category_Translations', 'category_Typography', 'category_Vegan', 'category_Video', 'category_Video Art', 'category_Video Games', 'category_Wearables', 'category_Weaving', 'category_Web', 'category_Webcomics', 'category_Webseries', 'category_Woodworking', 'category_Workshops', 'category_World Music', 'category_Young Adult', 'category_Zines', 'main_category_Art', 'main_category_Comics', 'main_category_Crafts', 'main_category_Dance', 'main_category_Design', 'main_category_Fashion', 'main_category_Film & Video', 'main_category_Food', 'main_category_Games', 'main_category_Journalism', 'main_category_Music', 'main_category_Photography', 'main_category_Publishing', 'main_category_Technology', 'main_category_Theater', 'currency_AUD', 'currency_CAD', 'currency_CHF', 'currency_DKK', 'currency_EUR', 'currency_GBP', 'currency_HKD', 'currency_JPY', 'currency_MXN', 'currency_NOK', 'currency_NZD', 'currency_SEK', 'currency_SGD', 'currency_USD', 'country_AT', 'country_AU', 'country_BE', 'country_CA', 'country_CH', 'country_DE', 'country_DK', 'country_ES', 'country_FR', 'country_GB', 'country_HK', 'country_IE', 'country_IT', 'country_JP', 'country_LU', 'country_MX', 'country_NL', 'country_NO', 'country_NZ', 'country_SE', 'country_SG', 'country_US'])

            
        test = pd.DataFrame(columns = ["Name", "Country", "Currency","Main_Category", "Category", "Date_Started",
                           "Date_Ended", "Goal"])
        test.loc[0] = [Name, Country, Currency, Main_Category, Category, Date_Started,
                           Date_Ended, Goal]
        print(test)
        print(test_f)
        print(test["Date_Started"])
        print(test.dtypes)
        
        test["Date_Started"] = pd.to_datetime( test['Date_Started'] )
        test["Date_Ended"] = pd.to_datetime( test['Date_Ended'] )
        test_f["length_name"] = test["Name"].str.len()
        test_f[ "month_launched"] = test["Date_Started"].dt.month
        test_f[ "duration"] = (test["Date_Ended"] - test['Date_Started']).dt.days
        test_f[ "goal"] = test["Goal"]

        # To create dummy variables for the test data
        f = test.iloc[0]["Category"]
        for i in test_f.columns:
            if( i[0:9] == "category_" ):
                if( f == i[9:]):
                    test_f.loc[0, i] = 1
        
        g = test.iloc[0]["Main_Category"]
        for i in test_f.columns:
            if( i[0:14] == "main_category_" ):
                if( g == i[14:]):
                    test_f.loc[0, i] = 1
        h = test.iloc[0]["Country"]
        for i in test_f.columns:
            if( i[0:8] == "country_" ):
                if( h == i[8:]):
                    test_f.loc[0, i] = 1
        j = test.iloc[0]["Currency"]
        for i in test_f.columns:
            if( i[0:9] == "currency_" ):
                if( j == i[9:]):
                    test_f.loc[0, i] = 1
        test_f = test_f.fillna(0)

        # make a prediction
        print(test_f) 
        prob = model.predict_proba(test_f)[:,1]
        print(prob)
        #logger.info("prediction made: {:0.3f}".format(prob))

        if prob >= 0.8:
            evaluation = "You are getting the money!!! Hype up and start sprinting work on your dream project. "
        elif prob >= 0.5 and prob < 0.8:
            evaluation = "It's possible your campaign is a hit. But I am not sure  "
        elif prob >= 0.2 and prob < 0.5:
            evaluation = "Pretty difficult"
        else:
            evaluation = "bad news"
        print(evaluation)

        # customer1 = Userinput(Name=String(Name), activeMember=float(Date_Ended), numProducts=float(Category),
        #     fromGermany=float(Germany), gender=float(Male), Main_Category=float(Main_Category), Date_Started=float(Date_Started),
        #     Country=float(Country), predicted_score=float(prob))
        # db.session.add(customer1)
        # db.session.commit()

        #logger.info("New customer evaluated as: %s", evaluation)
        
        #result = "This customer will churn with probability {:0.3f} - classified as {}".format(prob, evaluation)
        result = prob
        #return redirect(url_for('index'))
        return render_template('index.html', result=result)
    except:
        traceback.print_exc()
        #logger.warning("Not able to display evaluations, error page returned")
        return render_template('error.html')

def run_app(args):
    '''Runs the app
    
    Args:
        args: Argparse args - includes args.where, args.manual
        
    Returns:
        None
    '''
    #logger.debug('Running the run_app function')
    with open(os.path.join("config","config.yml"), "r") as f:
        config = yaml.safe_load(f)
    
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host=app.config["HOST"])


    

