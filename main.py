from flask import Flask, render_template, jsonify, request 
from database import load_jobs_from_db, load_job_from_db,add_application_to_db

app = Flask(__name__)


@app.route("/")
def hellow_world():
   jobs=load_jobs_from_db()
   return render_template('home.html', 
                         jobs_list=jobs
                         )


@app.route("/api/jobs")
def list_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)
  
@app.route("/job/<id>")
def show_job(id):
  job=load_job_from_db(id)
  if not job:
    return "Job not Found", 404
  return render_template('jobpage.html', 
                          job=job)
@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data=request.form
   #store data in the Db
  job=load_job_from_db(id)
  add_application_to_db(id,data)
 
  # send Email
  #display acknowlodgment
  return  render_template('application-submitted.html', 
                          application=data, job=job) 

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
