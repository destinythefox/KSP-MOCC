import krpc




# Establish a connection to the KRPC server running in KSP
conn = krpc.connect(name='KSP Mission Control')

# Access the space center
space_center = conn.space_center


vessel = conn.space_center.active_vessel
celestial_body = vessel.orbit.body
flight = vessel.flight(vessel.orbit.body.reference_frame)
orbit = conn.space_center.active_vessel.orbit
control = vessel.control

# Function to get UT time
def get_ut_time():
    return space_center.ut

# Function to get current and max thrust of the vessel
def get_thrust_data():
    current_thrust = vessel.thrust
    max_thrust = vessel.max_thrust
    return current_thrust, max_thrust

# Function to get altitude and speed
def get_flight_data():
    flight_info = vessel.flight()
    altitude = flight_info.mean_altitude
    speed = flight_info.speed
    return altitude, speed

# Function to get battery levels
def get_battery_levels():
    electric_charge = vessel.resources.amount('ElectricCharge')
    return electric_charge

# Function to get orbital parameters
def get_orbital_parameters():
    orbit = vessel.orbit
    apoapsis = orbit.apoapsis
    periapsis = orbit.periapsis
    inclination = orbit.inclination
    eccentricity = orbit.eccentricity
    return apoapsis, periapsis, inclination, eccentricity

# Function to get atmospheric density
def get_atmospheric_density():
    flight_info = vessel.flight()
    atmospheric_density = flight_info.atmosphere_density
    return atmospheric_density

# Function to get vessel pitch and roll
def get_pitch_and_roll():
    flight_info = vessel.flight()
    pitch = flight_info.pitch
    roll = flight_info.roll
    return pitch, roll

# Function to get fuel levels
def get_fuel_levels():
    # You can implement this to fetch fuel levels for different resources
    # This is just a placeholder
    return {"LiquidFuel": 0, "Oxidizer": 0, "MonoPropellant": 0}

# Function to get alerts or warnings
def get_alerts():
    # You can implement this to fetch any alerts or warnings
    # This is just a placeholder
    return []

# Function to get specific data for Flight Engineer Station
def get_flight_engineer_data():
    heat_shield_status =  vessel.resources.amount('Ablator'),
    parachutes = vessel.parts.parachutes
    stages =  vessel.control.current_stage
    landing_gear = control.gear
    pressure_at_altitude = celestial_body.pressure_at(flight.mean_altitude)
    atmospheric_density=atmospheric_density,
    dynamic_pressure = flight.dynamic_pressure
    # You can fetch more specific data for the Flight Engineer Station as needed
    return heat_shield_status, parachutes, stages, landing_gear, pressure_at_altitude,dynamic_pressure, atmospheric_density,
