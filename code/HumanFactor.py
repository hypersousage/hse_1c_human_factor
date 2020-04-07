import pyro
import pyro.distributions as distrs
from Age import FactorAge
from Stress import FactorStress
# ... other factor classes

pyro.set_rng_seed(100)

class HumanFactor:
    # Default SUMO values:
    default_accel = 2.9  # m/s^2
    default_decel = 7.5  # m/s^2
    default_sigma = 0.5  # (sigma in [0, 1])
    default_minGap = 2.5  # m 
    default_speedFactor = 1 # temp value
    default_actionStepLength = 1  # chosen by myself
    default_jmCrossingGap = 10  # m
    
    def __init__(self, age: int, sex: int, has_higher_education: bool, stress_level: float, social_deviation: int, 
                 experience_level: float, personality: int, is_foreigner: bool, kids_on_board: bool):
        self.age = age
        self.sex = sex

        # Extended:
        # self.has_education = has_higher_education
        # self.stress = stress
        # self.socila_deviation = social_deviation
        # self.experience = experience
        # self.personality = personality
        # self.is_foreigner = is_foreigner
        # self.has_kids = kids_on_board
        
        self.generator_age = FactorAge(age)
        self.generator_stress = FactorStress(stress_level)
        # other factor generators

    def get_accel(self, absolute_val=False)->float:
        accel = 0
        # our code
        
        # Example:
        accel = self.generator_age.get_accel() + \
                self.generator_stress.get_accel()
        
        # our code
        if absolute_val:
            return self.default_accel * (1.0 + accel)
        else:
            return accel
    
    def get_decel(self, absolute_val=False)->float:
        decel = 0
        # our code
        
        # Example:
        decel = self.generator_age.get_decel() + \
                self.generator_stress.get_decel()
        
        # our code
        if absolute_val:
            return self.default_decel * (1.0 + decel)
        else:
            return decel
    
    def get_apparentDecel(self, absolute_val=False)->float:
        apparentDecel = 0
        # our code
        if absolute_val:
            return self.default_apparentDecel * (1.0 + apparentDecel)
        else:
            return apparentDecel
    
    def get_sigma(self, absolute_val=False)->float:
        sigma = 0
        # our code
        if absolute_val:
            return self.default_sigma * (1.0 + sigma)
        else:
            return sigma
    
    def get_minGap(self, absolute_val=False)->float:
        minGap = 0
        # our code
        if absolute_val:
            return self.default_minGap * (1.0 + minGap)
        else:
            return minGap
    
    def get_speedFactor(self, absolute_val=False)->float:
        speedFactor = 0
        # our code
        if absolute_val:
            return self.default_speedFactor * (1.0 + speedFactor)
        else:
            return speedFactor
