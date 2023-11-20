from src.domain.encoding import EncodingInterface


class RealEncodingMO(EncodingInterface):

    def __init__(self, bounds: list = ...):
        super().__init__(bounds)
        self.bounds

    def decode(self,ind):
        return ind