import pyro
import pyro.distributions as distrs
import logging

format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='logs.log', level=logging.DEBUG, filemode='a', format=format)

from Age import FactorAge
from Stress import FactorStress
from Children import FactorChildren
from Personality import FactorPersonality
from Phone import FactorPhone
from Education import FactorEducation

from constants import default_vals, coeffs, config
# ... other factor classes

pyro.set_rng_seed(100)

generators = {
    'age': FactorAge,
    'stress': FactorStress,
    'children': FactorChildren,
    'personality': FactorPersonality,
    'phone': FactorPhone,
    'education': FactorEducation
}

# Default SUMO values:
default_accel = 2.6  # m/s^2
default_decel = 7.5  # m/s^2
default_sigma = 0.5  # (sigma in [0, 1])
default_minGap = 2.5  # m 
default_collisionMinGapFactor = 1.0
default_minGapLat = 0.6
default_maxSpeedLat = 1.0
default_actionStepLength = 0.0
default_jmCrossingGap = 10.0
default_jmIgnoreKeepClearTime = -1.0
default_jmDriveAfterRedTime = -1.0
default_jmDriveAfterYellowTime = -1.0
default_jmIgnoreFoeProb = 0.0
default_jmIgnoreFoeSpeed = 0.0
default_jmTimegapMinor = 1.0
default_impatience = 0.0

class HumanFactor:
    def __init__(self, factors: dict):
        for fname, value in factors.items():
            generator = generators[fname](value)
            setattr(self, f'generator_{fname}', generator)

    # @brief
    # The acceleration ability of vehicles of this type
    def generate_param(self, pname):
        value = 0.0
        for fname, generator in self.__dict__.items():
            try:
                value += getattr(generator, f'get_{pname}')() * coeffs.get(pname, {}).get(fname, 1)
            except (AttributeError, NotImplementedError):
                logging.warning(f'Warning: {fname} has no get_{pname} method')
        denominator = coeffs.get(pname, {}).get('denominator', 1)

        return value / denominator

    def get_accel(self, absolute_val=False)->float:
        accel = self.generate_param('accel')
        
        if accel <= -1:
            accel = 0.0
        if absolute_val:
            return default_accel * (1.0 + accel)
        else:
            return accel
    
    # @brief
    # The deceleration ability of vehicles of this type
    def get_decel(self, absolute_val=False)->float:
        decel = self.generate_param('decel')
        
        if decel <= -1:
            decel = 0.0
        if absolute_val:
            return default_decel * (1.0 + decel)
        else:
            return decel
    
    # @brief
    # The driver imperfection (0 denotes perfect driving)
    def get_sigma(self, absolute_val=False)->float:
        sigma = self.generate_param('sigma')

        if not 0 <= default_sigma * (1.0 + sigma) <= 1:
            sigma = 0.0
        
        if absolute_val:
            return default_sigma * (1.0 + sigma)
        else:
            return sigma
    
    # @brief
    # This class' free space in front of the vehicle itself
    def get_minGap(self, absolute_val=False)->float:
        minGap = self.generate_param('minGap')
        if minGap <= -1:
            minGap = 0.0
        
        if absolute_val:
            return default_minGap * (1.0 + minGap)
        else:
            return minGap
    
    # @brief
    # The vehicle type's default actionStepLength, i.e. the interval between two control actions.
    def get_actionStepLength(self)->float:
        actionStepLength = self.generate_param('actionStepLength')
        
        return max(0.0, actionStepLength)
    
    # @brief
    # Minimum distance to pedestrians that are walking towards the conflict point with the ego vehicle. 
    # If the pedestrians are further away the vehicle may drive across the pedestrian crossing.
    def get_jmCrossingGap(self, absolute_val=False)->float:
        jmCrossingGap = self.generate_param('jmCrossingGap')

        if jmCrossingGap <= -1:
            jmCrossingGap = 0.0

        if absolute_val:
            return default_jmCrossingGap * (1.0 + jmCrossingGap)
        else:
            return jmCrossingGap
    
    # @brief
    # The minimum fraction of minGap that must be maintained to the leader vehicle to avoid a collision event
    def get_collisionMinGapFactor(self)->float:
        collisionMinGapFactor = self.generate_param('collisionMinGapFactor')
        
        if not 0.0 <= collisionMinGapFactor <= 1.0:
            return default_collisionMinGapFactor
        else:
            return collisionMinGapFactor        
    
    # @brief
    # The vehicle type's minimum lateral gap
    def get_minGapLat(self, absolute_val=False)->float:
        minGapLat = self.generate_param('minGapLat')
        
        if minGapLat <= -1:
            minGapLat = 0.0
        
        if absolute_val:
            return default_minGapLat * (1.0 + minGapLat)
        else:
            return minGapLat
    
    # @brief
    # The vehicle type's maximum lateral speed
    def get_maxSpeedLat(self, absolute_val=False)->float:
        maxSpeedLat = self.generate_param('maxSpeedLat')
        
        if maxSpeedLat <= -1:
            maxSpeedLat = 0.0
        
        if absolute_val:
            return default_maxSpeedLat * (1.0 + maxSpeedLat)
        else:
            return maxSpeedLat
    
    # @brief
    # This value causes vehicles to ignore foe vehicles that have right-of-way with the 
    # given probability. The check is performed anew every simulation step.
    def get_jmIgnoreFoeProb(self)->float:
        jmIgnoreFoeProb = self.generate_param('jmIgnoreFoeProb')

        if 0.0 <= jmIgnoreFoeProb <= 1.0:
            return jmIgnoreFoeProb
        else:
            return default_jmIgnoreFoeProb
    
    # @brief
    # This value is used in conjunction with jmIgnoreFoeProb. Only vehicles with a speed 
    # below or equal to the given value may be ignored.
    def get_jmIgnoreFoeSpeed(self)->float:
        jmIgnoreFoeSpeed = self.generate_param('jmIgnoreFoeSpeed')
        IgnoreSpeed = 30.0
        
        if jmIgnoreFoeSpeed <= -1:
            jmIgnoreFoeSpeed = 0.0
        
        condition = { 0: "Normal", 1: "Fast"}[distrs.Bernoulli(0.2)().item()]
        if condition == "Normal":
            return default_jmIgnoreFoeSpeed
        else:
            return IgnoreSpeed * (1.0 + jmIgnoreFoeSpeed)
            
    # @brief
    # The vehicle's i# union:mpatience (willingness to obstruct others)
    def get_impatience(self)->float:
        impatience = self.generate_param('impatience')
        if 0.0 <= impatience <= 1.0:
            return impatience
        else:
            return default_impatience
