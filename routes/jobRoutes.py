from flask import Blueprint,request,jsonify,make_response

from models.jobmodel import JobModel
from models.usermodel import UserModel

job_bp=Blueprint("jobs",__name__)

@job_bp.route("/createjob/<user_id>",methods=["POST"])
def createjob(user_id):
  try:
    data=request.get_json()
    required_keys=["title","status","end_date","skills","about"]
    print(data)
    if all(key in data for key in required_keys):
        new_job=JobModel(
            title=data["title"],
            status=data["status"],
            end_date=data["end_date"],
            skills=data["skills"],
            about=data["about"],
            employer=user_id
        )
        new_job.save()
        return make_response(jsonify({'message':"job created successfully"}),200)
    else:
        return make_response(jsonify({"message":"all feilds are required"}),404)
  except Exception as e:
        return make_response(jsonify({"message": f"Error creating job: {str(e)}"}), 500)
  
@job_bp.route("/editjob/<job_id>",methods=["PATCH"])
def editjob(job_id):
  try:
    data=request.get_json()
    print(data)
    required_keys=["title","status","end_date","skills","about"] 
    title =data["title"]
    skills=data["skills"]
    about=data["about"]
    end_date=data["end_date"]
    status=data['status']
  
    
    JobModel.objects(id=job_id).first().update(
            set__title=title,
            set__skills=skills,
            set__about=about,
            set__end_date=end_date,
            set__status=status,

    )
       
    return make_response(jsonify({'message':"successfully updated"}),200)
  except Exception as e:
        return make_response(jsonify({"message": f"Error updating job: {str(e)}"}), 500)
 

@job_bp.route("/deletejob/<job_id>",methods=["DELETE"])
def deletejob(job_id):
  try:
    job=JobModel.objects(id=job_id).first()
    if job:
       job.delete()
       return make_response(jsonify({'message':"successfully updated"}),200)
    else:
       return make_response(jsonify({'message':"documenet not found"}),400)
  except Exception as e:
        return make_response(jsonify({"message": f"Error deleting job: {str(e)}"}), 500)

@job_bp.route("/createdjobs/<user_id>", methods=["GET"])
def created_jobs(user_id):
    try:
        # Assuming user_id is the employer's user_id
        jobs = JobModel.objects(employer=user_id)
        jobs_data = [
            {
                "id": str(job.id),
                "title": job.title,
                "status": job.status,
                "start_date": job.start_date.isoformat(),
                "end_date": job.end_date.isoformat(),
                "skills": job.skills,
                "about": job.about,
                "applicant": [
                    {
                        "user_id": str(applicant.id),
                        "username": applicant.username,
                        "email": applicant.email,
                        "bio": applicant.bio,
                        "skills":applicant.skills
                        # Add other user fields as needed
                    }
                    for applicant in job.applicant
                ]
            }
            for job in jobs
        ]
        return make_response(jsonify({"message": "successfully fetched created jobs", "data": jobs_data}), 200)
    except Exception as e:
        return make_response(jsonify({"message": f"Error for getting created jobs: {str(e)}"}), 500)

 

@job_bp.route("/apply/<job_id>",methods=["PATCH"])
def applyjob(job_id):
  try:
    data=request.get_json()
    
    if "user_id" in data:
     user_id = data["user_id"]
     user=UserModel.objects(id=user_id).first()
     application_list=user["application"]
     application_list.append(job_id)
     print(application_list)
     job=JobModel.objects(id=job_id).first()
     aplicant_list=job["applicant"]
     aplicant_list.append(user_id)
     print(application_list)
     job.update(
        add_to_set__applicant=user_id
     )
     user.update(
         add_to_set__application=job_id
     )

     return make_response(jsonify({'message':"applyed successfully"}),200)
    else:
       return make_response(jsonify({'message':"userid is not valid"}),404)
  except Exception as e:
        print(e)
        return make_response(jsonify({"message": f"Error applying job: {str(e)}"}), 500)
  

@job_bp.route("/recomentation/<user_id>",methods=["GET"])
def recomentation(user_id):
  try:
    user=UserModel.objects(id=user_id).first()
    skill_set=user["skills"]
    

    matching_jobs = JobModel.objects(skills__in=skill_set)
    print(matching_jobs,"***")
    job_data=[
       {
         "id": str(job.id),
          "title": job.title,
          "status": job.status,
          "start_date": job.start_date.isoformat() if job.start_date else None, 
          "end_date": job.end_date.isoformat() if job.start_date else None, 
          "skills":job.skills,
          "about":job.about,
          "applicant":[{
             "id":str(applicant.id)
          }
          for applicant in job.applicant
          ],
          "employer": {
                    "id": str(job.employer.id),
                    "username": job.employer.username,
                    "email": job.employer.email,
                    "bio": job.employer.bio,
                    
                },
          
       }

       for job in matching_jobs
    ]
    if not job_data:
       return make_response(jsonify({'message':"there is no recomented jobs","data":job_data}),404)
       
    return make_response(jsonify({'message':"recomented jobs","data":job_data}),200)
  
  except Exception as e:
        return make_response(jsonify({"message": f"Error for job recomentation: {str(e)}"}), 500)
  

     




