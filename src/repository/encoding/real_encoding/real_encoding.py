from src.domain.encoding import EncodingInterface


class RealEncoding(EncodingInterface):

    def decode(self,ind):
        return ind