import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

random_noise = distrs.Normal(0.0, 0.05)  # mean = 0.0, sigma = 0.05

def exp(lam : float)->float:
    return distrs.Exponential(lam)().item()

def norm(mean: float, sigma: float)->float:
    return distrs.Normal(mean, sigma)().item()

def lap(mean: float, sigma: float)->float:
    return distrs.Laplace(mean, sigma)().item()

def uni(a:float, b: float)->float:
    return distrs.Uniform(a, b)().item()

class PersonalityFactor:
    def __init__(self, personality: str):
        self.personality = personality

    def get_accel(self)->float:
        accel = 0.0
        if self.personality == "phlegmatic":
            accel = norm(-0.2, 0.17)
        elif self.personality == "sanguine":
            accel = norm(0.2, 0.13)
        elif self.personality == "holeric":
            accel = lap(0.3, 0.15)
        elif self.personality == "melancholic":
            accel = norm(-0.3, 0.2)
        else:
            accel = random_noise().item()
        
        
        return accel

    def get_decel(self)->float:
        decel = 0.0
        if self.personality == "phlegmatic":
            decel = norm(-0.1, 0.07)
        elif self.personality == "sanguine":
            decel = norm(0.1, 0.06)
        elif self.personality == "holeric":
            decel = lap(0.15, 0.06)
        elif self.personality == "melancholic":
            decel = norm(-0.15, 0.08)
        else:
           decel = random_noise().item()
        
        return decel

    def get_sigma(self)->float:
        sigma = 0.0
        if self.personality == "phlegmatic":
            sigma = -0.25 + exp(3.7) / 2.5
        elif self.personality == "sanguine":
            sigma = uni(0.0, 0.2)
        elif self.personality == "holeric":
            sigma = uni(0.1, 0.4)
        elif self.personality == "melancholic":
            sigma = -0.1 + exp(2) / 2.5
        else:
            sigma = random_noise().item()
    
        return sigma - 0.5
        
    def get_speedFactor(self)->float:
        # depends on sex in some cases
        speedFactor = 0.0
        if self.personality == "phlegmatic":
            speedFactor = random_noise().item()
        elif self.personality == "sanguine":
            speedFactor = norm(0.1, 0.07)
        elif self.personality == "holeric":
            speedFactor = 0.15 + exp(10.0) / 3.0
        elif self.personality == "melancholic":
            speedFactor = norm(-0.13, 0.06)
        else:
            speedFactor = random_noise().item()
        
        return speedFactor

    def get_minGap(self)->float:
        minGap = 0.0
        if self.personality == "phlegmatic":
            minGap = random_noise().item()
        elif self.personality == "sanguine":
            minGap = -0.15 + exp(10.0) / 7.0
        elif self.personality == "holeric":
            minGap = -0.25 + exp(8.5) / 9.0
        elif self.personality == "melancholic":
            minGap = 0.15 + exp(11.0) / 6.0
        else:
            minGap = random_noise().item()
    
        return minGap

    def get_actionStepLength(self)->float:
        actionStepLength = 0.0
        if self.personality == "phlegmatic":
            actionStepLength = uni(0.1, 0.2)
        elif self.personality == "sanguine":
            actionStepLength = uni(-0.19, -0.1)
        elif self.personality == "holeric":
            actionStepLength = uni(-0.3, -0.15)
        elif self.personality == "melancholic":
            actionStepLength = uni(0.18, 0.3)
        else:
            actionStepLength = random_noise().item()
    
        return actionStepLength

    def get_jmCrossingGap(self)->float:
        jmCrossingGap = 0.0
        if self.personality == "phlegmatic":
            jmCrossingGap = uni(0.1, 0.2)
        elif self.personality == "sanguine":
            jmCrossingGap = uni(-0.16, -0.05)
        elif self.personality == "holeric":
            jmCrossingGap = uni(-0.3, -0.15)
        elif self.personality == "melancholic":
            jmCrossingGap = uni(0.18, 0.3)
        else:
            jmCrossingGap = random_noise().item()
        
        return jmCrossingGap
    
