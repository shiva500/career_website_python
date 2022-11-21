from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': "Data Analyst",
  'location': 'Banglaru, India',
  'salary': 'Rs 10,000,00'
}, {
  'id': 1,
  'title': "Data scientist",
  'location': 'Goa, India',
  'salary': 'Rs 40,000,00'
}, {
  'id': 1,
  'title': "Frontend developer",
  'location': 'Sanfransisco',
  'salary': '$ 20,000,00'
}]


@app.route("/")
def helo_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='Kick start your Career!!')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
