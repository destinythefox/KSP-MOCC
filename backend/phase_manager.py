from app.py import get_flight_data, get_thrust_data  # Import other necessary functions

class PhaseManager:
    def __init__(self):
        self.current_phase = "Pre-Launch"

    def update_phase(self):
        altitude, speed = get_flight_data()
        current_thrust, max_thrust = get_thrust_data()
        # Add other data points as needed

        # Pre-Launch
        if altitude == 0 and current_thrust == 0:
            self.current_phase = "Pre-Launch"

        # Liftoff
        elif current_thrust > 0 and altitude > 200:
            self.current_phase = "Liftoff"

        # Ascent
        elif altitude > 1000 and speed > 300:
            self.current_phase = "Ascent"

        # Earth Parking Orbit
        elif altitude > 70000 and speed > 2200:
            self.current_phase = "Earth Parking Orbit"

        # Trans-Lunar Injection
        elif altitude > 70000 and speed > 3000:
            self.current_phase = "Trans-Lunar Injection"

        # Lunar Approach
        elif altitude > 300000:
            self.current_phase = "Lunar Approach"

        # Lunar Orbit
        elif altitude > 340000:
            self.current_phase = "Lunar Orbit"

        # Lunar Descent
        elif altitude > 340000 and speed < 100:
            self.current_phase = "Lunar Descent"

        # Lunar Landing
        elif altitude == 340000 and speed == 0:
            self.current_phase = "Lunar Landing"

        # Lunar Ascent
        elif altitude == 340000 and speed > 0:
            self.current_phase = "Lunar Ascent"

        # Trans-Earth Injection
        elif altitude > 340000 and speed > 1000:
            self.current_phase = "Trans-Earth Injection"

        # Earth Reentry
        elif altitude < 70000 and speed > 3000:
            self.current_phase = "Earth Reentry"

        # Splashdown
        elif altitude == 0 and speed == 0:
            self.current_phase = "Splashdown"

    def get_current_phase(self):
        return self.current_phase
