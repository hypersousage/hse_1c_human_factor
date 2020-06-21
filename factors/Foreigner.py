import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

class FactorForeigner:
    def __init__(self, is_foreigner: bool):
        self.is_foreigner = is_foreigner

    def get_decel(self) -> float:
        raise NotImplementedError

    def get_sigma(self) -> float:
        if self.is_foreigner:
            return 0.5 + distrs.Normal(0.05, 0.05)().item()
        else:
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

