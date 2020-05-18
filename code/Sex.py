import pyro
import pyro.distributions as distrs
import random


pyro.set_rng_seed(100)

random_noise = distrs.Normal(0.0, 0.05) 

# depends on age sooo much!!!!!!

class FactorSex:
    
    def __init__(self, sex: int):
        self.sex = sex
        
        
        
    def get_accel(self)->float:
        if self.sex == 0:
            return distrs.Normal(0.15, 0.15)().item()
        elif self.sex == 1:
            return distrs.Normal(0.05, 0.17)().item()
        
        
        
    def get_decel(self)->float:
        if self.sex == 0:
            return distrs.Normal(0.15, 0.15)().item()
        elif self.sex == 1:
            return distrs.Normal(0.05, 0.07)().item()
    
    
    
    def get_sigma(self)->float:
        if self.sex == 0:
            return distrs.Normal(0.1, 0.05)().item() 
        elif self.sex == 1:
            return distrs.Normal(0.04, 0.11)().item() 
        
        
        
    def get_minGap(self)->float:
        if self.sex == 0:
            return distrs.Normal(0.0, 0.08)().item() 
        elif self.sex == 1:
            return distrs.Normal(-0.04, 0.08)().item() 
    
    
    
    def get_actionStepLength(self)->float:
        if self.sex == 0:
            return distrs.Exponential(2)().item()
        elif self.sex == 1:
            return distrs.Normal(-0.1, 0.08)().item() 
        
        
        
    def get_jmCrossingGap(self)->float:
        if self.sex == 0:
            return distrs.Uniform(0.0, 0.05)().item()
        elif self.sex == 1:
            return distrs.Normal(0.1, 0.1)().item()  
        
        
