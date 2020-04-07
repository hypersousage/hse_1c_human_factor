from Age import FactorAge
from Stress import FactorStress
from HumanFactor import HumanFactor

# Default SUMO values:
default_minGap = 2.5  # m 
default_accel = 2.9  # m/s^2
default_decel = 7.5  # m/s^2
default_emergencyDecel = 9  # m/s^2
default_maxSpeed = 180  # km/h
default_sigma = 0.5  # (sigma in [0, 1])
default_actionStepLength = 1  # chosen by myself
default_jmCrossingGap = 10  # m

# Simulation

def print_stats(generator, n_iterations: int):
    accel_delta = 0
    decel_delta = 0
    sigma_delta = 0
    speedFactor_delta = 0
    minGap_delta = 0
    actionStepLength_delta = 0
    jmCrossingGap_delta = 0
    for _ in range(n_iterations):
        accel_delta += generator.get_accel()
        decel_delta += generator.get_decel()
        sigma_delta += generator.get_sigma()
        speedFactor_delta += generator.get_speedFactor()
        minGap_delta += generator.get_minGap()
        actionStepLength_delta += generator.get_actionStepLength()
        jmCrossingGap_delta += generator.get_jmCrossingGap()
    
    print("Experiment stats:")
    print("Mean accel delta:", round(accel_delta / n_iterations, 4))
    print("Mean decel delta:", round(decel_delta / n_iterations, 4))
    print("Mean sigma delta:", round(sigma_delta / n_iterations, 4))
    print("Mean speedFactor_delta:", round(speedFactor_delta / n_iterations, 4))
    print("Mean minGap_delta:", round(minGap_delta / n_iterations, 4))
    print("Mean actionStepLength_delta:", round(actionStepLength_delta / n_iterations, 4))
    print()

        
def make_age_experiment(age: int, n_iterations: int):
    tmp = FactorAge(age)
    print("Age =", age)
    print_stats(tmp, n_iterations)
    
def make_stress_experiment(stress: float, n_iterations: int):
    tmp = FactorStress(stress)
    print("Stress =", stress)
    print_stats(tmp, n_iterations)
    
age = int(input())
stress = float(input())
make_age_experiment(age, 1000)
make_stress_experiment(stress, 1000)