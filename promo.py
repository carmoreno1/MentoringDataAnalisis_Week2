from datetime import datetime


class Promo:
    def __init__(self, name, expires):
        if not isinstance(name, str):
            raise TypeError("name variable must be a string")
        if not isinstance(expires, datetime):
            raise TypeError("expires variable must be a date")

        self.name = name
        self.expires = expires

    def expired(self):
        return self.expires < datetime.today()
