import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

random_noise = distrs.Normal(0.0, 0.05)  # mean = 0.0, sigma = 0.05

class FactorAge:
    def __init__(self, age: int):
        self.age = age
    
    def get_accel(self)->float:
        # depends on sex in some cases
        accel = 0.0
        if 17 <= self.age < 21:
            accel = distrs.Laplace(0.22, 0.12)().item()  # mean = 0.22, sigma = 0.12
        elif 21 <= self.age < 26:
            accel = distrs.Normal(0.15, 0.15)().item()  # mean = 0.15, sigma = 0.15
        elif 26 <= self.age < 45:
            accel = distrs.Normal(0.0, 0.4)().item()  # mean = 0, sigma = 0.4
        elif 45 <= self.age < 65:
            accel = random_noise().item()
        else:
            condition = { 0: "Normal", 1: "Fast" }[distrs.Bernoulli(0.3)().item()]  # success_prob = 0.3
            if condition == "Normal":
                accel = random_noise().item()
            else:
                accel = distrs.Uniform(0.15, 0.35)().item()  # lower_bound = 0.15, upper_bound = 0.35
        
        return accel

    def get_decel(self)->float:
        decel = 0.0
        if 17 <= self.age < 55:
            decel = random_noise().item()
        else:
            decel = distrs.Uniform(-0.3, 0.15)().item()  # lower_bound = -0.3, upper_bound = 0.15
        
        return decel

    def get_sigma(self)->float:
        sigma = 0.0
        if 17 <= self.age < 45:
            sigma = random_noise().item()
        elif 45 <= self.age < 55:
            sigma = distrs.Normal(0.1, 0.15)().item()  # mean = 0.1, sigma = 0.15
        else:
            sigma = distrs.Chi2(2)().item() / 10  # k = 2 -> mean = 0.1, sigma = 0.2
    
        return sigma
        
    def get_speedFactor(self)->float:
        # depends on sex in some cases
        speedFactor = 0.0
        if 17 <= self.age < 21:
            speedFactor = distrs.Laplace(0.2, 0.25)().item()  # mean = 0.2, sigma = 0.25
        elif 21 <= self.age < 65:
            speedFactor = distrs.Normal(0.0, 0.5)().item()  # mean = 0, sigma = 0.5
        else:
            condition = { 0: "Slow", 1: "Fast" }[distrs.Bernoulli(0.3)().item()]  # success_prob = 0.3
            if condition == "Slow":
                speedFactor = distrs.Normal(0.0, 0.2)().item()  # mean = 0, sigma = 0.2
            else:
                speedFactor = distrs.Uniform(0.25, 0.35)().item()  # lower_bound = 0.25, upper_bound = 0.35
        
        return speedFactor

    def get_minGap(self)->float:
        minGap = 0.0
        if 17 <= self.age < 30:
            minGap = random_noise().item()
        elif 30 <= self.age < 60:
            minGap = distrs.Uniform(-0.2, 0.2)().item()  # lower_bound = -0.2, upper_bound = 0.2
        else:
            condition = { 0: "Normal", 1: "Fast"}[distrs.Bernoulli(0.4)().item()]  # success_prob = 0.4
            if condition == "Normal":
                minGap = distrs.Uniform(-0.05, 0.15)().item()  # lower_bound = -0.05, upper_bound = 0.15
            else:
                minGap = distrs.Normal(-0.12, 0.05)().item()  # mean = -0.12, sigma = 0.05
    
        return minGap

    def get_actionStepLength(self)->float:
        actionStepLength = 0.0
        if 17 <= self.age < 45:
            actionStepLength = distrs.Uniform(-0.25, 0.1)().item()  # lower_bound = -0.25, upper_bound = 0.1
        else:
            actionStepLength = distrs.Chi2(2)().item() / 16 - 0.025  # k = 2 -> mean = 0.125, sigma = 0.125
    
        return actionStepLength

    def get_jmCrossingGap(self)->float:
        jmCrossingGap = 0.0
        if 17 <= self.age < 30:
            jmCrossingGap = distrs.Normal(-0.12, 0.1)().item()  # mean = -0.12, sigma = 0.1
        else:
            jmCrossingGap = random_noise().item()
        
        return jmCrossingGap
