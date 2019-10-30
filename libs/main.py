import torch
import pyro

pyro.set_rng_seed(100)

def weather(): 
    cloudy = torch.distributions.Bernoulli(0.3).sample() 
    cloudy = 'cloudy' if cloudy.item()  ==  1.0  else 'sunny'
    mean_temp = {'cloudy': 55.0, 'sunny': 75.0}[cloudy] 
    scale_temp = {'cloudy': 10.0, 'sunny': 15.0}[cloudy] 
    temp = torch.distributions.Normal(mean_temp, scale_temp).rsample() 
    return cloudy, temp.item()

def ice_cream_sales():
    cloudy, temp = weather()
    expected_sales = 200. if cloudy == 'sunny' and temp > 80.0 else 50.
    ice_cream = pyro.sample('ice_cream', pyro.distributions.Normal(expected_sales, 10.0))
    return ice_cream

print(ice_cream_sales())