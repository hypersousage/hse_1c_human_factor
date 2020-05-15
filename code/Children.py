import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

random_noise = distrs.Normal(0.0, 0.05)  # mean = 0.0, sigma = 0.05

def exp(lam : float)->float:
    return distrs.Exponential(lam)().item()

def norm(mean: float, sigma: float):
    return distrs.Normal(mean, sigma)().item()

def uni(a:float, b: float):
    return distrs.Uniform(a, b)().item()

class ChildrenFactor:
    def __init__(self, has_children: bool):
        self.has_children = has_children

    def get_accel(self)->float:
        accel = 0.0
        if self.has_children:
            accel = norm(0.15, 0.15)
        else:
            accel = random_noise().item()

        return accel

    def get_decel(self)->float:
        decel = 0.0
        if self.has_children:
            pass
            decel = norm(-0.1, 0.1)
        else:
            decel = random_noise().item()

        return decel

    def get_sigma(self)->float:
        sigma = 0.0
        if self.has_children:
            sigma = norm(-0.25, 0.25)
        else:
            sigma = random_noise().item()

        return sigma

    def get_minGap(self)->float:
        sigma = 0.0
        if self.has_children:
            sigma = uni(0.0, 0.25)
        else:
            sigma = random_noise().item()

        return sigma

    def get_speedFactor(self)->float:
        sigma = 0.0
        
        sigma = random_noise().item()

        return sigma

    def get_actionStepLength(self)->float:
        sigma = 0.0
        
        sigma = random_noise().item()

        return sigma
    
    def get_jmCrossingGap(self)->float:
        sigma = 0.0
        if self.has_children:
            sigma = uni(0.0, 0.25)
        else:
            sigma = random_noise().item()

        return sigma