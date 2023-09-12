from flask import Flask, jsonify, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from flask_sqlalchemy import SQLAlchemy
import krpc
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flight_data.db'
db = SQLAlchemy(app)

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # Add other fields as needed

db.create_all()

# Initialize KRPC connection
conn = krpc.connect(name='KSP Mission Control')
space_center = conn.space_center
vessel = conn.space_center.active_vessel

# Create a new flight entry
new_flight = Flight()
db.session.add(new_flight)
db.session.commit()

def fetch_and_store_data():
    ut_time = space_center.ut
    current_thrust = vessel.thrust
    max_thrust = vessel.max_thrust
    # Fetch other data as needed

    # Store data in the database
    # Your logic here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ut_time', methods=['GET'])
def get_ut_time():
    return jsonify({"ut_time": space_center.ut})

# Add other API routes as needed

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_and_store_data, 'interval', seconds=0.5)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
