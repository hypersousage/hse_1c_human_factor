import pyro
import pyro.distributions as distrs
from Age import HumanFactorAge
from Stress import HumanFactorStress
# ... other factor classes

pyro.set_rng_seed(100)

class HumanFactorCommon:
    # Default SUMO values:
    default_accel = 2.9  # m/s^2
    default_decel = 7.5  # m/s^2
    default_sigma = 0.5  # (sigma in [0, 1])
    default_minGap = 2.5  # m 
    default_emergencyDecel = 9  # m/s^2
    default_maxSpeed = 180  # km/h
    default_actionStepLength = 1  # chosen by myself
    default_jmCrossingGap = 10  # m
    
    def __init__(self, age: int, sex: int, has_higher_education: bool, stress: float, social_deviation: int, 
                 experience: float, personality: int, is_foreigner: bool, kids_on_board: bool):
        self.age = age
        self.sex = sex

        # Extended:
        # self.has_education = has_higher_education
        # self.stress = stress
        # self.socila_deviation = social_deviation
        # self.experience = experience
        # self.personality = personality
        # self.is_foreigner = is_foreigner
        # self.has_kids = kids_on_board
        
        # Optional
        self.generator_age = HumanFactorAge(age)
        self.generator_stress = HumanFactorStress(stress)
        # other factor generators

    def get_accel(self, absolute_val=False)->float:
        accel = 0
        # our shitty code
        
        accel = self.generator_age.get_accel() + \
                self.generator_stress.get_accel()
        
        # our shitty code
        if absolute_val:
            return self.default_accel * (1.0 + accel)
        else:
            return accel
    
    def get_decel(self, absolute_val=False)->float:
        decel = 0
        # our shitty code
        
        decel = self.generator_age.get_decel() + \
                self.generator_stress.get_decel()
        
        # our shitty code
        if absolute_val:
            return self.default_decel * (1.0 + decel)
        else:
            return decel
    
    def get_apparentDecel(self, absolute_val=False)->float:
        apparentDecel = 0
        # our shitty code
        if absolute_val:
            return self.default_apparentDecel * (1.0 + apparentDecel)
        else:
            return apparentDecel
    
    def get_emergencyDecel(self, absolute_val=False)->float:
        emergencyDecel = 0
        # our code
        if absolute_val:
            return self.default_emergencyDecel * (1.0 + emergencyDecel)
        else:
            return emergencyDecel
    
    def get_sigma(self, absolute_val=False)->float:
        sigma = 0
        # our code
        if absolute_val:
            return self.default_sigma * (1.0 + sigma)
        else:
            return sigma
    
    def get_minGap(self, absolute_val=False)->float:
        minGap = 0
        # our code
        if absolute_val:
            return self.default_minGap * (1.0 + minGap)
        else:
            return minGap
    
    def get_maxSpeed(self, absolute_val=False)->float:
        maxSpeed = 0
        # our code
        if absolute_val:
            return self.default_maxSpeed * (1.0 + maxSpeed)
        else:
            return maxSpeed
    
    def get_speedFactor(self, absolute_val=False)->float:
        speedFactor = 0
        # our code
        if absolute_val:
            return self.default_speedFactor * (1.0 + speedFactor)
        else:
            return speedFactor
    
    # аналогично ниже
    def get_speedDev(self, absolute_val=False)->float:
        pass
    
    def get_actionStepLength(self, absolute_val=False)->float:
        pass
    
    def get_jmCrossingGap(self, absolute_val=False)->float:
        pass
    
    def get_jmIgnoreKeepClearTime(self, absolute_val=False)->float:  # время ожидания, по истечении которого водитель выедет на перекресток, даже если это может образовать пробку;
        pass
    
    def get_jmDriveAfterRedTime(self, absolute_val=False)->float:  # время ожидания, по истечении которого водитель проедет на красный свет;
        pass
    
    def get_jmDriveAfterYellowTime(self, absolute_val=False)->float:  # время ожидания, по истечении которого водитель проедет на желтый свет;
        pass
    
    def get_jmDriveRedSpeed(self, absolute_val=False)->float:  # при проезде на красный из-за jmDriveAfterRedTime водитель снизит скорость, и она не будет выше времени ожидания, по истечении которого водитель проедет на красный;
        pass
    
    def get_jmIgnoreFoeProb(self, absolute_val=False)->float:  # вероятность игнорирования машин, у которых на данный момент есть приоритет в движении;
        pass
    
    def get_jmIgnoreFoeSpeed(self, absolute_val=False)->float:  # идет вместе с jmIgnoreFoeProb, только машин со скоростью не выше этой будут игнорировать;
        pass
    
    def get_jmSigmaMinor(self, absolute_val=False)->float:  # скорость въезда водителя на перекресток;
        pass
    
    def get_jmTimegapMinor(self, absolute_val=False)->float:  # минимальный промежуток между проездом машин с бОльшим приоритетом;
        pass
    
    def get_impatience(self, absolute_val=False)->float:  # степень желания препятствовать машинамам с бОльшим приоритетом.
        pass
