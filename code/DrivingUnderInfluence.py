import pyro
import pyro.distributions as distrs


pyro.set_rng_seed(100)

random_noise = distrs.Normal(0.0, 0.05)  # mean = 0.0, sigma = 0.05


class FactorDrivingUnderInfluence: #DrivingUnderInfluence - dui

    def __init__(self, dui: float):
        self.dui = dui
    
    
    
    def get_accel(self)->float:
        if self.dui < 0.15:
            return distrs.Normal(0.0, 0.1)().item() 
        elif self.dui < 0.45:
            return distrs.Normal(0.15, 0.11)().item() 
        else:
            return distrs.Exponential(3)().item()
        return 0
        
        
        
    def get_decel(self)->float:
        if self.dui < 0.15:
            return distrs.Normal(0.0, 0.1)().item() 
        elif self.dui < 0.45:
            return distrs.Normal(0.15, 0.15)().item() 
        else:
            return distrs.Exponential(3)().item()
        return 0
    
    
    
    def get_sigma(self)->float:
        if self.dui < 0.5:
            return distrs.Normal(0.0, 0.1)().item() 
        else:
            return distrs.Normal(0.2, 0.17)().item() 
        return 0
        
        
        
    def get_minGap(self)->float:
        if self.dui < 0.3:
            return distrs.Normal(0.0, 0.15)().item()    
        else:
            return distrs.Normal(-0.1, 0.07)().item() 
    
    
    
    def get_actionStepLength(self)->float:
        if self.dui == 0:
            return distrs.Normal(0.05, 0.1)().item()    
        elif self.dui < 0.15:
            return distrs.Normal(0.1, 0.11)().item()    
        elif self.dui < 0.25:
            return distrs.Normal(0.12, 0.12)().item()    
        elif self.dui < 0.5:
            return distrs.Normal(0.15, 0.1)().item()    
        else:
            return distrs.Normal(0.2, 0.11)().item()    
        
        
        
    def get_jmCrossingGap(self)->float:
        return distrs.Normal(0.0, 0.05)().item()
        
        
    
