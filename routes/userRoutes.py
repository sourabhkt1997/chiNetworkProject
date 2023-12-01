from flask import Blueprint, render_template, request,jsonify,make_response
from  models.usermodel import UserModel
import bcrypt
# import jwt
# import datetime
# from dotenv import load_dotenv
# load_dotenv()
# import os
# secretkey=os.getenv("secretkey")

user_bp=Blueprint("user",__name__)

# user_bp.config['SECRET_KEY'] = secretkey

@user_bp.route("/register",methods=["POST"])
def register():
    data=request.get_json()
    required_keys=['username', 'email', 'password','role']
    if all(key in data for key in required_keys):
        username=data["username"]
        password=data["password"]
        email=data["email"]
        role=data["role"]

        existing_user=UserModel.objects(email=email).first()
        if existing_user:
          response = make_response(jsonify({"message": "User already exists"}), 409)
          return response
        else:
          salt=bcrypt.gensalt()
          password_bytes = password.encode('utf-8')
          hashed_password = bcrypt.hashpw(password_bytes, salt)
          if hashed_password:
             new_user=UserModel(
                username=username,
                password=hashed_password.decode('utf-8'),
                email=email,
                role=role
                )
             new_user.save()
             return make_response(jsonify({'message':"signin successfull"}),200)
          else:
             return make_response(jsonify({'message':"internal error"}),400)
          
@user_bp.route("/login",methods=["POST"])
def login():
   data=request.get_json()
   if "password" in data and "email" in data:
      password=data["password"]
      email=data["email"]
      print(email,password)
      user=UserModel.objects(email=email).first()
      if not user:
         return make_response(jsonify({"message":"you need to signup first"}),405)
      else:
         user_id=str(user["id"])
         user_role =user["role"]
         if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            # expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5)
            # payload = {'user_id': user_id, 'user_role': user_role, 'exp': expiration_time}
            # access_token = jwt.encode(payload, user_bp.config['SECRET_KEY'], algorithm='HS256')
            response=make_response(jsonify({"message":"login successfull","data":{"userid":user_id,"role":user["role"],"user":user["username"]}}),200)
            # response.set_cookie('access_token', access_token, expires=expiration_time)

            return response
         else:
            return make_response(jsonify({"message":"wrong password"}),400)
   else:
       return make_response(jsonify({"message":"these fields are required"}),404)



  
@user_bp.route("/updateprofile/<user_id>",methods=["PATCH"])
def updateprofile(user_id):
  data=request.get_json()
  user = UserModel.objects(id=user_id).first()
  bio=data["bio"] if data["bio"] !="" else user["bio"]
  skills=data["skills"] if data["skills"] !="" else user["skills"]
  experience=data["experience"] if data['experience'] !="" else user['experience']
  if not user:
       return make_response(jsonify({'message': "User not found"}), 404)
    
  user.update(
      set__bio=bio,
      add_to_set__skills=skills,
      set__experience=experience
    )
  return make_response(jsonify({'message': "Profile updated successfully"}), 200)
  


      
     
      
      
      


      
      

   

     


   
   
            
            
            
         
         
         
             
             

                
           

  