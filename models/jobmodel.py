from mongoengine import Document, StringField, DateTimeField,BooleanField,ListField,ReferenceField

from datetime import datetime
from models.usermodel import UserModel

class JobModel(Document):
    title = StringField()
    status = StringField(choices=["Open", "In Progress", "Filled"], default="Open")
    start_date = DateTimeField(default=datetime.utcnow)
    end_date = DateTimeField()
    skills = ListField(StringField())
    about= StringField()
    applicant= ListField(ReferenceField(UserModel))
    employer=ReferenceField(UserModel)



    
