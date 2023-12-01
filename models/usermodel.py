from mongoengine import Document, StringField, DateTimeField,BooleanField,ListField,ReferenceField



class UserModel(Document):
    username=StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(choices=["employer", "jobseeker"],required=True)
    bio=StringField()
    verified = BooleanField(default=False)
    skills = ListField(StringField(),default=[])
    experience=StringField(choices=["Entry Level", "Mid Level", "Senior"])
    status=StringField(choices=["active","inactive"],default="inactive")
    application=ListField(ReferenceField("JobModel"))
 


from models.jobmodel import JobModel

# from ..db import client
# print(client)
# UserModel = client['users']

# user_schema = {
#     'username': {'type': 'string', 'required': True},
#     'email': {'type': 'string', 'required': True, 'unique': True},
#     'password': {'type': 'string', 'required': True},
#     'role': {'type': 'string', 'choices': ["employer", "jobseeker"], 'required': True},
#     'bio': {'type': 'string'},
#     'verified': {'type': 'bool', 'default': False},
#     'skills': {'type': 'list', 'schema': {'type': 'string'}},
#     'experience': {'type': 'string', 'choices': ["Entry Level", "Mid Level", "Senior"]},
#     'status': {'type': 'string', 'choices': ["active", "inactive"], 'default': "inactive"}
# }