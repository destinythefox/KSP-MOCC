from flask import Flask
from stations import boost_station, flight_station, capcom_station, control_station, eecom_telmu_station, flight_engineer_station, gnc_station

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(boost_station.bp)
app.register_blueprint(flight_station.bp)
app.register_blueprint(capcom_station.bp)
app.register_blueprint(control_station.bp)
app.register_blueprint(eecom_telmu_station.bp)
app.register_blueprint(flight_engineer_station.bp)
app.register_blueprint(gnc_station.bp)

if __name__ == '__main__':
    app.run(debug=True)
