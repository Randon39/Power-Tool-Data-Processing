import numpy as np

# Converts RMS electrical current into mechanical torque using a linear model.
# The value of kₜ (the electromechanical gain) was obtained through linear regression performed during motor-brake dynamometer tests on power tools.
# slope = K_T 
# intercept = B_T 

def electrical_to_mechanical_torque(current, K_T, B_T):
    return K_T * current - B_T