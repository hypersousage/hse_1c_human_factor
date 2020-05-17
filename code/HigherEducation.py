import pyro.distributions as distrs


class FactorHigherEducation:
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


factor = FactorHigherEducation(1)

print([func for func in dir(FactorHigherEducation) if callable(getattr(FactorHigherEducation, func))])
print(factor.__dict__)

for name, callable in factor.__dict__.items():
    print(name)


