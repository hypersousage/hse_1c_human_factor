import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

class HumanFactorAge:
    def __init__(self, age: int):
        self.age = age
        
    def get_accel(self)->float:
        accel = None
        if 17 <= self.age < 21:
            accel = distrs.Laplace(0.17, 0.2)().item()  # mean = 0.17, sigma = 0.2
        elif 21 <= self.age < 26:
            accel = distrs.Normal(0.12, 0.22)().item()  # mean = 0.12, sigma = 0.22
        elif 26 <= self.age < 45:
            accel = distrs.Normal(0.0, 0.3)().item()  # mean = 0, sigma = 0.3
        elif 45 <= self.age < 65:
            accel = distrs.Uniform(-0.15, 0.15)().item()  # lower_bound = -0.15, upper_bound = 0.15
        else:
            condition = { 0: "Slow", 1: "Fast" }[distrs.Bernoulli(0.3)().item()]  # success_prob = 0.3
            if condition == "Slow":
                accel = distrs.Normal(0.0, 0.2)().item()  # mean = 0, sigma = 0.2
            else:
                accel = distrs.Uniform(0.2, 0.35)().item()  # lower_bound = 0.2, upper_bound = 0.35
        
        return accel

    def get_decel(self)->float:
        current_distribution = None
        if 17 <= self.age < 55:
            current_distribution = distrs.Uniform(-0.15, 0.15)  # lower_bound = -0.15, upper_bound = 0.15
        else:
            current_distribution = distrs.Uniform(-0.3, 0.15)  # lower_bound = -0.3, upper_bound = 0.15
        
        decel = current_distribution().item()
        return decel

    def get_sigma(self)->float:
        sigma = None
        if 17 <= self.age < 40:
            sigma = distrs.Normal(0, 0.05)().item()  # mean = 0, sigma = 0.05
        elif 40 <= self.age < 55:
            sigma = distrs.Normal(0.1, 0.1)().item()  # mean = 0.1, sigma = 0.1
        else:
            sigma = distrs.Chi2(2)().item() / 10 - 0.235  # k = 2 -> mean = -0.035, sigma ~ 0.2
    
        return sigma
        
    def get_maxSpeed(self)->float:
        speed = None
        if 17 <= self.age < 21:
            speed = distrs.Laplace(0.2, 0.25)().item()  # mean = 0.2, sigma = 0.25
        elif 21 <= self.age < 65:
            speed = distrs.Normal(0.0, 0.5)().item()  # mean = 0, sigma = 0.5
        else:
            condition = { 0: "Slow", 1: "Fast" }[distrs.Bernoulli(0.3)().item()]  # success_prob = 0.3
            if condition == "Slow":
                speed = distrs.Normal(0.0, 0.2)().item()  # mean = 0, sigma = 0.2
            else:
                speed = distrs.Uniform(0.25, 0.35)().item()  # lower_bound = 0.25, upper_bound = 0.35
        
        return speed

    def get_minGap(self)->float:
        minGap = None
        if 17 <= self.age < 30:
            minGap = distrs.Normal(-0.1, 0.05)().item()  # mean = -0.1, sigma = 0.05
        elif 30 <= self.age < 60:
            minGap = distrs.Uniform(-0.1, 0.1)().item()  # lower_bound = -0.1, upper_bound = 0.1
        else:
            condition = { 0: "Slow", 1: "Fast"}[distrs.Bernoulli(0.4)().item()]  # success_prob = 0.4
            if condition == "Slow":
                minGap = distrs.Uniform(-0.05, 0.15)().item()  # lower_bound = -0.15, upper_bound = 0.05
            else:
                minGap = distrs.Normal(0.1, 0.03)().item()  # mean = 0.1, sigma = 0.03
    
        return minGap

    def get_actionStepLength(self)->float:
        actionStepLength = None
        if 17 <= self.age < 50:
            actionStepLength = distrs.Uniform(-0.25, 0.1)().item()  # lower_bound = -0.2, upper_bound = 0.05
        else:
            actionStepLength = distrs.Chi2(2)().item() / 16 - 0.025  # k = 2 -> mean = 0.125, sigma = 0.125
    
        return actionStepLength

    def get_jmCrossingGap(self)->float:
        jmCrossingGap = None
        if 17 <= self.age < 30:
            jmCrossingGap = distrs.Normal(-0.15, 0.05)().item()  # mean = -0.15, sigma = 0.05
        else:
            jmCrossingGap = distrs.Uniform(-0.05, 0.05)().item()  # lower_bound = -0.05, upper_bound = 0.05
        
        return jmCrossingGap
