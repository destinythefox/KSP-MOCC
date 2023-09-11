from flask import Blueprint, jsonify
import krpc

bp = Blueprint('boost_station', __name__)

# Initialize KRPC connection
conn = krpc.connect(name='KSP Mission Control')
vessel = conn.space_center.active_vessel

@bp.route('/api/thrust_data', methods=['GET'])
def thrust_data():
    current_thrust = vessel.thrust
    max_thrust = vessel.max_thrust
    return jsonify({"current_thrust": current_thrust, "max_thrust": max_thrust})
