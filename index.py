from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
import os
mongourl=os.getenv("mongourl")
from mongoengine import connect
# Configure the default database connection
connect(
    db='chatbot',
    host=mongourl,
    alias='default',  # Optional: Give the connection an alias
)

from routes.userRoutes import user_bp

from routes.jobRoutes import job_bp


app=Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, Flask!'

app.register_blueprint(user_bp,url_prefix="/user")
app.register_blueprint(job_bp,url_prefix="/job")


if(__name__=="__main__"):
    app.run(debug=True)
