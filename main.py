from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Abuja, Nigeria',
  'salary': 'N.100,000'
}, {
  'id': 2,
  'title': 'Database Administrator',
  'location': 'New York, USA',
  'salary': '$.10,000'
}, {
  'id': 3,
  'title': 'Front End Developer',
  'location': 'Nasarawa, Nigeria'
}, {
  'id': 4,
  'title': 'Computer Scientist',
  'location': 'Abuja, Nigeria',
  'salary': 'N.10,000'
}]


@app.route("/")
def hellow_world():
  return render_template('home.html', jobs=JOBS, company_name='Modern')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
