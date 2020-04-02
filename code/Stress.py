import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

standart_variation = distrs.Uniform(-0.05, 0.05)  # lower_bound = -0.05, upper_bound = 0.05

class HumanFactorStress:
    def __init__(self, stress: float):
        self.stress = stress
        
    def get_accel(self)->float:
        accel = 0
        # depends on sex!
        accel = distrs.Normal(-0.1, 0.05)().item() + self.stress / 5  # mean = self.stress / 5 - 0.1, sigma = 0.05
        
        return accel
    
    def get_decel(self)->float:
        decel = 0
        # depends on sex!
        decel = distrs.Normal(0.0, 0.05)().item() + self.stress / 10  # mean = self.stress / 10, sigma = 0.05
        
        return decel
    
    def get_sigma(self)->float:
        sigma = 0
        sigma = standart_variation().item() + abs(self.stress - 0.5) / 5
        
        return sigma
    
    def get_minGap(self)->float:
        minGap = 0
        condition = { 0: "Calm", 1: "Agressive" }[distrs.Bernoulli(self.stress)().item()]  # success_prob = 0.6
        if condition == "Agressive":
            minGap = distrs.Normal(-0.08, 0.07)().item()  # mean = -0.08, sigma = 0.07
        else:
            minGap = standart_variation().item()
        
        return minGap
    
    def get_maxSpeed(self)->float:
        maxSpeed = 0
        if self.stress >= 0.5:
            maxSpeed = distrs.Exponential(2.0)().item() / 2.5 - 0.1   # mean = 0.1, sigma = 0.2
        else:
            maxSpeed = distrs.Normal(-0.05, 0.07)().item()  # mean = -0.05, sigma = 0.07
        
        return maxSpeed
    
    def get_jmCrossingGap(self)->float:
        jmCrossingGap = 0
        if self.stress >= 0.75:
            jmCrossingGap = distrs.Normal(-0.1, 0.04)().item()  # mean = -0.1, sigma = 0.04
        else:
            jmCrossingGap = standart_variation().item() 
        
        return jmCrossingGap
