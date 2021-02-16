# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    if desired_state == food_state():
        return True
    else:
        return False

def food_state(time, temperature, pressure):
    factors = time * temperature * pressure * COOKED_CONSTANT
    if factors >= WELL_DONE:
        return "well-done"
    elif factors >= MEDIUM:
        return "medium"
    else:
        return "State not tracked"