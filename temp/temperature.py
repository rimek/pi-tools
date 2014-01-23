
class Temperature(object):
    def __init__(self, data=None):
        self.set_data(data)

    def set_data(self, data):
        self.data = data

    @property
    def C(self):
        return float(self.data) / 1000 if self.data else None

    @property
    def F(self):
        return self.C * 9.0 / 5.0 + 23.0 if self.data else None

