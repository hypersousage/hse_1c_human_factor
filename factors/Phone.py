import pyro
import pyro.distributions as distrs

pyro.set_rng_seed(100)

class FactorPhone:
    def __init__(self, is_using: bool):
        self.is_using = is_using

    def get_decel(self) -> float:
        if self.is_using:
            return distrs.Normal(1, 0.05)().item() - 1
        return 0

    def get_sigma(self) -> float:
        if self.is_using:
            return min(2, max(1, distrs.Normal(1.2, 0.2)().item())) - 1
        return 0

    def get_minGap(self):
        if self.is_using:
            return min(2, max(1, distrs.Pareto(1, 1)().item())) - 1
        return 0

    def get_maxSpeed(self):
        if self.is_using:
            return min(0.3, max(0, distrs.Exponential(0.8)().item())) + 0.5 - 1
        return 0

    def get_collisionMinGapFactor(self):
        if self.is_using:
            return min(2, max(1, distrs.Pareto(1, 2)().item())) - 1
        return 0

    def get_speedFactor(self) -> float:
        if self.is_using:
            return min(0.25, max(0, distrs.Exponential(0.8)().item())) + 0.7 - 1
        return 0

    def get_actionStepLength(self) -> float:
        if self.is_using:
            return min(3, max(1, distrs.Normal(1.3, 0.1)().item())) - 1
        return 0

    def get_jmIgnoreFoeProb(self):
        if self.is_using:
            return min(0.2, max(0, distrs.Normal(0.1, 0.05)().item()))
        return 0

    def get_jmSigmaMinor(self):
        if self.is_using:
            return min(1.4, max(1, distrs.Normal(1.1, 0.1)().item()))- 1
        return 0

