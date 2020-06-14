import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

class FactorEducation:
    def __init__(self, is_higher: bool):
        self.is_higher = is_higher

    def get_decel(self) -> float:
        raise NotImplementedError

    def get_sigma(self) -> float:
        raise NotImplementedError

    def get_minGap(self):
        raise NotImplementedError

    def get_maxSpeed(self):
        raise NotImplementedError

    def get_collisionMinGapFactor(self):
        raise NotImplementedError

    def get_speedFactor(self) -> float:
        if self.is_higher:
            return min(1.1, max(1, distrs.Uniform(1, 1.1)().item())) - 1
        return 0

    def get_actionStepLength(self) -> float:
        raise NotImplementedError

    def get_jmIgnoreFoeProb(self):
        raise NotImplementedError

    def get_jmSigmaMinor(self):
        raise NotImplementedError
