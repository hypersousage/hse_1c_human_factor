import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

random_noise = distrs.Normal(0.0, 0.05)  # mean = 0.0, sigma = 0.05

class FactorStress:
    def __init__(self, stress: float):
        self.stress = stress
        
    def get_accel(self)->float:
        accel = 0.0
        # depends on sex!
        accel = distrs.Normal(-0.1, 0.05)().item() + self.stress / 5  # mean = self.stress / 5 - 0.1, sigma = 0.05
        
        return accel
    
    def get_decel(self)->float:
        decel = 0.0
        # depends on sex!
        decel = distrs.Normal(0.0, 0.05)().item() + self.stress / 10  # mean = self.stress / 10, sigma = 0.05
        
        return decel
    
    def get_sigma(self)->float:
        sigma = 0.0
        sigma = random_noise().item() + abs(self.stress - 0.5) / 5
        
        return sigma
    
    def get_speedFactor(self)->float:
        speedFactor = 0.0
        if self.stress >= 0.5:
            speedFactor = distrs.Exponential(2.0)().item() / 2.5 - 0.1   # mean = 0.1, sigma = 0.2
        else:
            speedFactor = distrs.Normal(-0.05, 0.15)().item()  # mean = -0.05, sigma = 0.15
        
        return speedFactor    
    
    def get_minGap(self)->float:
        minGap = 0.0
        stress_type = { 0: "Calm", 1: "Agressive" }[distrs.Bernoulli(self.stress)().item()]
        if stress_type == "Agressive":
            minGap = distrs.Normal(-0.12, 0.07)().item()  # mean = -0.12, sigma = 0.07
        else:
            minGap = random_noise().item()
        
        return minGap
    
    def get_actionStepLength(self)->float:
        actionStepLength = 0.0
        stress_type = { 0: "Calm", 1: "Agressive" }[distrs.Bernoulli(0.6)().item()]
        if stress_type == "Agressive":
            actionStepLength = distrs.Uniform(-0.2, 0.05)().item()  # lower_bound = -0.2, upper_bound = 0.05
        else:
            actionStepLength = random_noise().item()

        return actionStepLength
        
    def get_jmCrossingGap(self)->float:
        jmCrossingGap = 0.0
        if self.stress >= 0.75:
            jmCrossingGap = distrs.Normal(-0.1, 0.04)().item()  # mean = -0.1, sigma = 0.04
        else:
            jmCrossingGap = random_noise().item() 
        
        return jmCrossingGap
