import pyro
import pyro.distributions as distrs
from Age import FactorAge
from Stress import FactorStress
# ... other factor classes

pyro.set_rng_seed(100)

# Default SUMO values:
default_accel = 2.6  # m/s^2
default_decel = 7.5  # m/s^2
default_sigma = 0.5  # (sigma in [0, 1])
default_minGap = 2.5  # m 
default_collisionMinGapFactor = 1.0
default_laneChangeModel = "LC2013"
default_carFollowingModel = "Krauss"
default_latAlignment = "center"
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
    def __init__(self, age: int, stress_level: float):
        self.age = age
        self.stress = stress_level
        
        self.generator_age = FactorAge(age)
        self.generator_stress = FactorStress(stress_level)

    # @brief
    # The acceleration ability of vehicles of this type
    def get_accel(self, absolute_val=False)->float:
        accel = 0.0
        # union:
        accel = self.generator_age.get_accel() + \
                self.generator_stress.get_accel()
        
        if absolute_val:
            return default_accel * (1.0 + accel)
        else:
            return accel
    
    # @brief
    # The deceleration ability of vehicles of this type
    def get_decel(self, absolute_val=False)->float:
        decel = 0.0
        # union:
        decel = self.generator_age.get_decel() + \
                self.generator_stress.get_decel()
        
        if absolute_val:
            return default_decel * (1.0 + decel)
        else:
            return decel
    
    # @brief
    # The driver imperfection (0 denotes perfect driving)
    def get_sigma(self, absolute_val=False)->float:
        sigma = 0.0
        # union:
        sigma = self.generator_age.get_sigma() + \
                self.generator_stress.get_sigma()

        if not (0.0 <= sigma <= 1.0):
            sigma = default_sigma
        
        if absolute_val:
            return default_sigma * (1.0 + sigma)
        else:
            return sigma
    
    # @brief
    # This class' free space in front of the vehicle itself
    def get_minGap(self, absolute_val=False)->float:
        minGap = 0.0
        # union:
        minGap = self.generator_age.get_minGap() + \
                 self.generator_stress.get_minGap()

        if absolute_val:
            return default_minGap * (1.0 + minGap)
        else:
            return minGap
    
    # @brief
    # The vehicle type's default actionStepLength, i.e. the interval between two control actions.
    def get_actionStepLength(self)->float:
        actionStepLength = 0.0
        # union:
        actionStepLength = self.generator_age.get_actionStepLength() + \
                           self.generator_stress.get_actionStepLength()
        
        return max(0, actionStepLength)
    
    # @brief
    # Minimum distance to pedestrians that are walking towards the conflict point with the ego vehicle. 
    # If the pedestrians are further away the vehicle may drive across the pedestrian crossing.
    def get_jmCrossingGap(self, absolute_val=False)->float:
        jmCrossingGap = 0.0
        # union:
        jmCrossingGap = self.generator_age.get_jmCrossingGap() + \
                        self.generator_stress.get_jmCrossingGap()

        if absolute_val:
            return default_jmCrossingGap * (1.0 + jmCrossingGap)
        else:
            return jmCrossingGap
    
    # @brief
    # The minimum fraction of minGap that must be maintained to the leader vehicle to avoid a collision event
    def get_collisionMinGapFactor(self)->float:
        collisionMinGapFactor = 0.0
        # union:
        collisionMinGapFactor = 0.7 * self.generator_age.get_collisionMinGapFactor() + \
                                0.3 * self.generator_stress.get_collisionMinGapFactor()
        
        if not 0.0 <= collisionMinGapFactor <= 1.0:
            return default_collisionMinGapFactor
        else:
            return collisionMinGapFactor        
    
    # @brief
    # The vehicle type's minimum lateral gap
    def get_minGapLat(self, absolute_val=False)->float:
        minGapLat = 0.0
        # union:
        minGapLat = self.generator_age.get_minGapLat() + \
                    self.generator_stress.get_minGapLat()
        
        if absolute_val:
            return default_minGapLat * (1.0 + minGapLat)
        else:
            return minGapLat
    
    # @brief
    # The vehicle type's maximum lateral speed
    def get_maxSpeedLat(self, absolute_val=False)->float:
        maxSpeedLat = 0.0
        # union:
        maxSpeedLat = self.generator_age.get_maxSpeedLat() + \
                      self.generator_stress.get_maxSpeedLat()
        
        if absolute_val:
            return default_maxSpeedLat * (1.0 + maxSpeedLat)
        else:
            return maxSpeedLat
    
    # @brief
    # This value causes vehicles to ignore foe vehicles that have right-of-way with the 
    # given probability. The check is performed anew every simulation step.
    def get_jmIgnoreFoeProb(self)->float:
        jmIgnoreFoeProb = 0.0
        # union:
        jmIgnoreFoeProb = self.generator_age.get_jmIgnoreFoeProb() + \
                          self.generator_stress.get_jmIgnoreForProb()
        if 0.0 <= jmIgnoreFoeProb <= 1.0:
            return jmIgnoreFoeProb
        else:
            return default_jmIgnoreFoeProb
    
    # @brief
    # This value is used in conjunction with jmIgnoreFoeProb. Only vehicles with a speed 
    # below or equal to the given value may be ignored.
    def get_jmIgnoreFoeSpeed(self)->float:
        jmIgnoreFoeSpeed = 0.0
        IgnoreSpeed = 30.0
        # union:
        jmIgnoreFoeSpeed = self.generator_age.get_jmIgnoreFoeSpeed() + \
                           self.generator_stress.get_jmIgnoreFoeSpeed()
        
        condition = { 0: "Normal", 1: "Fast"}[distrs.Bernoulli(0.2)().item()]
        if condition == "Normal":
            return default_jmIgnoreFoeSpeed
        else:
            return IgnoreSpeed * (1.0 + jmIgnoreFoeSpeed)
            
    # @brief
    # The vehicle's impatience (willingness to obstruct others)
    def get_impatience(self)->float:
        impatience = 0.0
        # union:
        impatience = ( self.generator_age.get_impatience() + 
                       self.generator_stress.get_impatience()) / 2
        if 0.0 <= impatience <= 1.0:
            return impatience
        else:
            return default_impatience

    # Pending solution (probably will be dropped)
    def get_jmIgnoreKeepClearTime(self)->float:
        # default = -1.0
        return -1.0
    
    def get_jmDriveAfterRedTime(self)->float:
        # default = -1.0
        return -1.0
    
    def get_jmDriveAfterYellowTime(self)->float:
        # default = -1.0
        return -1.0
    
    # not implemented in vType
    def get_jmSigmaMinor(self)->float:
        pass
    
    def get_jmTimegapMinor(self)->float:
        pass
    
    # Don't know what to do with them
    def get_laneChangeModel(self)->str:
        pass

    def get_latAlignment(self)->str:
        pass

    def get_carFollowingModel(self)->str:
        pass
