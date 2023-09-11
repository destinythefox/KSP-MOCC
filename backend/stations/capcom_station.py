from flask import Blueprint, jsonify
from krpc_interface import get_mission_phase, get_command_queue, get_special_messages  # Import necessary functions

bp = Blueprint('capcom_station', __name__)

# API Endpoint for mission phase
@bp.route('/api/capcom/mission_phase', methods=['GET'])
def mission_phase():
    return jsonify({"mission_phase": get_mission_phase()})

# API Endpoint for command queue
@bp.route('/api/capcom/command_queue', methods=['GET'])
def command_queue():
    return jsonify({"command_queue": get_command_queue()})

# API Endpoint for special messages
@bp.route('/api/capcom/special_messages', methods=['GET'])
def special_messages():
    return jsonify({"special_messages": get_special_messages()})
