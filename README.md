# chiNetworkProject

delployed link  https://chiproject.onrender.com/

# Your Project Name

This project is a [brief description of your project].

## Setup Instructions

1. Navigate to the project directory:

    ```bash
    cd your_project_directory
    ```

2. Initialize a Virtual Environment:

    ```bash
    python -m venv venv
    ```

3. Activate the Virtual Environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix/Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

4. Install Project Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

To run the server, use the following command:

```bash
python index.py

Routes
Register User
http

POST /job/user/register
Login User
http

POST /job/user/login
Update User Data
http

PATCH /job/user/updateprofile/<user_id>
Create Job
http

POST /job/createjob/<user_id>
Edit Job Data
http

PUT /job/editjob/<job_id>
Delete Job
http

DELETE /job/deletejob/<job_id>
Get All Created Jobs
http

GET /job/createdjobs/<user_id>
Apply for Job
http
Copy code
PATCH /job/apply/<job_id>
Get Job Recommendation
http
Copy code
GET /job/recomendation/<user_id>
