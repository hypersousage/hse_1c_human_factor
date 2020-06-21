import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

class FactorSocialDeviation:
    def __init__(self, is_crazy: int):
        self.is_crazy = is_crazy

    def get_decel(self) -> float:
        raise NotImplementedError

    def get_sigma(self) -> float:
        if self.is_crazy == 1:
            return 0.5 + distrs.Normal(0.25, 0.25)().item()
        if self.is_crazy == 2:
            return max(0, distrs.Exponential(0.25)().item() / 10)
        return 0.5

    def get_minGap(self):
        raise NotImplementedError

    def get_maxSpeed(self):
        raise NotImplementedError

    def get_collisionMinGapFactor(self):
        raise NotImplementedError

    def get_speedFactor(self) -> float:
        raise NotImplementedError

    def get_actionStepLength(self) -> float:
        raise NotImplementedError

    def get_jmIgnoreFoeProb(self):
        raise NotImplementedError

    def get_jmSigmaMinor(self):
        raise NotImplementedError
