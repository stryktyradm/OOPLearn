class DigitRetrive:
    def __call__(self, number):
        try:
            return int(number)
        except:
            return None


dg = DigitRetrive()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))
