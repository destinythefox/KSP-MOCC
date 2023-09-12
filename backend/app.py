from flask import Flask, jsonify
import krpc

app = Flask(__name__)

# Establish a connection to the KRPC server running in KSP
conn = krpc.connect(name='KSP Mission Control')
space_center = conn.space_center
vessel = conn.space_center.active_vessel
celestial_body = vessel.orbit.body
flight = vessel.flight(vessel.orbit.body.reference_frame)
orbit = conn.space_center.active_vessel.orbit
control = vessel.control

@app.route('/ut_time', methods=['GET'])
def get_ut_time():
    return jsonify({"ut_time": space_center.ut})

@app.route('/thrust_data', methods=['GET'])
def get_thrust_data():
    current_thrust = vessel.thrust
    max_thrust = vessel.max_thrust
    return jsonify({"current_thrust": current_thrust, "max_thrust": max_thrust})

@app.route('/flight_data', methods=['GET'])
def get_flight_data():
    flight_info = vessel.flight()
    altitude = flight_info.mean_altitude
    speed = flight_info.speed
    return jsonify({"altitude": altitude, "speed": speed})

@app.route('/battery_levels', methods=['GET'])
def get_battery_levels():
    electric_charge = vessel.resources.amount('ElectricCharge')
    return jsonify({"electric_charge": electric_charge})

@app.route('/orbital_parameters', methods=['GET'])
def get_orbital_parameters():
    orbit = vessel.orbit
    apoapsis = orbit.apoapsis
    periapsis = orbit.periapsis
    inclination = orbit.inclination
    eccentricity = orbit.eccentricity
    return jsonify({"apoapsis": apoapsis, "periapsis": periapsis, "inclination": inclination, "eccentricity": eccentricity})

@app.route('/atmospheric_density', methods=['GET'])
def get_atmospheric_density():
    flight_info = vessel.flight()
    atmospheric_density = flight_info.atmosphere_density
    return jsonify({"atmospheric_density": atmospheric_density})

@app.route('/pitch_and_roll', methods=['GET'])
def get_pitch_and_roll():
    flight_info = vessel.flight()
    pitch = flight_info.pitch
    roll = flight_info.roll
    return jsonify({"pitch": pitch, "roll": roll})

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify({"alerts": []})

@app.route('/fuel_levels', methods=['GET'])
def get_fuel_levels():
    current_stage = vessel.control.current_stage
    liquid_fuel = vessel.resources_in_decouple_stage(stage=current_stage, cumulative=False).amount('LiquidFuel')
    oxidizer = vessel.resources_in_decouple_stage(stage=current_stage, cumulative=False).amount('Oxidizer')
    mono_propellant = vessel.resources_in_decouple_stage(stage=current_stage, cumulative=False).amount('MonoPropellant')
    return jsonify({"LiquidFuel": liquid_fuel, "Oxidizer": oxidizer, "MonoPropellant": mono_propellant})

@app.route('/flight_engineer_data', methods=['GET'])
def get_flight_engineer_data():
    heat_shield_status = vessel.resources.amount('Ablator')
    parachutes = vessel.parts.parachutes
    stages = vessel.control.current_stage
    landing_gear = control.gear
    pressure_at_altitude = celestial_body.pressure_at(flight.mean_altitude)
    atmospheric_density = get_atmospheric_density()
    dynamic_pressure = flight.dynamic_pressure
    return jsonify({
        "heat_shield_status": heat_shield_status,
        "parachutes": parachutes,
        "stages": stages,
        "landing_gear": landing_gear,
        "pressure_at_altitude": pressure_at_altitude,
        "dynamic_pressure": dynamic_pressure,
        "atmospheric_density": atmospheric_density
    })

if __name__ == '__main__':
    app.run(debug=True)
