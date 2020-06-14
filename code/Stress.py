import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

random_noise = distrs.Normal(0.0, 0.15)  # mean = 0.0, sigma = 0.15

class FactorStress:
    def __init__(self, stress: float):
        self.stress = stress
        
    def get_accel(self)->float:
        accel = 0.0
        # depends on sex!
        accel = distrs.Normal(-0.1, 0.15)().item() + self.stress / 5  # mean = self.stress / 5 - 0.1, sigma = 0.05
        
        return accel
    
    def get_decel(self)->float:
        decel = 0.0
        # depends on sex!
        decel = distrs.Normal(0.0, 0.1)().item() + self.stress / 10  # mean = self.stress / 10, sigma = 0.05
        
        return decel
    
    def get_sigma(self)->float:
        sigma = 0.0
        sigma = random_noise().item() + abs(self.stress - 0.5) / 5
        
        return sigma
    
    def get_minGap(self)->float:
        minGap = 0.0
        stress_type = { 0: "Calm", 1: "Agressive" }[distrs.Bernoulli(self.stress)().item()]
        if stress_type == "Agressive":
            minGap = distrs.Normal(-0.15, 0.05)().item()  # mean = -0.15, sigma = 0.07
        else:
            minGap = random_noise().item()
        
        return minGap
    
    def get_actionStepLength(self)->float:
        actionStepLength = 0.0
        stress_type = { 0: "Calm", 1: "Agressive" }[distrs.Bernoulli(self.stress)().item()]
        if stress_type == "Agressive":
            actionStepLength = distrs.Uniform(-0.2, 0.05)().item()  # lower_bound = -0.2, upper_bound = 0.05
        else:
            actionStepLength = random_noise().item()

        return actionStepLength
        
    def get_jmCrossingGap(self)->float:
        jmCrossingGap = 0.0
        if self.stress >= 0.75:
            jmCrossingGap = distrs.Normal(-0.15, 0.1)().item()  # mean = -0.15, sigma = 0.1
        else:
            jmCrossingGap = random_noise().item() 
        
        return jmCrossingGap

    def get_collisionMinGapFactor(self)->float:
        collisionMinGapFactor = 0.0
        if self.stress >= 0.5:
            collisionMinGapFactor = distrs.Normal(0.15, self.stress / 10)().item()
        else:
            collisionMinGapFactor = distrs.Uniform(0.0, 0.05)().item()
        
        return collisionMinGapFactor
    
    def get_minGapLat(self)->float:
        minGapLat = 0.0
        if self.stress < 0.3:
            minGapLat = distrs.Normal(0.0, 0.2)().item()  # mean = 0.0, sigma = 0.2
        elif 0.3 <= self.stress < 0.75:
            minGapLat = distrs.Exponential(5.0)().item()  # mean = 0.2, sigma = 0.04
        else:
            minGapLat = distrs.Normal(0.3, 0.06)().item()  # mean = 0.3, sigma = 0.06
        
        return minGapLat
    
    def get_maxSpeedLat(self)->float:
        maxSpeedLat = 0.0
        maxSpeedLat = random_noise().item()
        
        return maxSpeedLat

    def get_jmIgnoreFoeProb(self)->float:
        jmIgnoreFoeProb = 0.0
        jmIgnoreFoeProb = random_noise().item()
        
        return jmIgnoreFoeProb
    
    def get_jmIgnoreFoeSpeed(self)->float:
        raise NotImplementedError
        
    def get_impatience(self)->float:
        impatience = 0.0
        impatience = distrs.Normal(self.stress / 6, 0.1)().item()  # mean = stress / 6, sigma = 0.1
        
        return impatience
