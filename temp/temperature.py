
class Temperature(object):
    def __init__(self, data):
        self.data = data

    @property
    def C(self):
        return float(self.data) / 1000

    @property
    def F(self):
        return self.C * 9.0 / 5.0 + 23.0

