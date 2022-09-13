class Fraction:
    """
        A fraction represents a number in the a/b form. Takes a fraction-like formatted string and returns a fraction object.
    """

    def __init__(self, fract: str):
        if type(fract) == str:
            try:
                self._numerator = int(fract.replace(" ", "").split("/")[0])
                self._denominator = int(fract.replace(" ", "").split("/")[0])
                self._fraction = self.simplify(fract)
            except ValueError:
                raise ValueError("Invalid numerator or denominator values. Numerator and denominator must be integers")
        else:
            raise ValueError("Fraction must be delivered as a string")
    
    def __str__(self):
        return self._fraction

    def __int__(self):
        try:
            return int(self._fraction)
        except ValueError:
            raise ValueError("Fraction hasn't got any integer representation")

    def __float__(self):
        return float(eval(self._fraction))

    def __bool__(self):
        if float(eval(self._fraction)) >= 0:
            return True
        else:
            return False

    def simplify(self, fraction: str):
        fraction = fraction.replace(" ", "").split("/")
        if len(fraction) == 2:
            try:
                num = int(fraction[0])
                den = int(fraction[1])

                i = 2
                while i <= abs(min(num, den)):
                    if num % i == 0 and den % i == 0:
                        num = int(num/i)
                        den = int(den/i)
                        i = 2
                    else: 
                        i+=1
                if den == 1:
                    return str(num)
                else:
                    return(f"{num}/{den}")

            except ValueError:
                raise ValueError("Invalid numerator or denominator values. Numerator and denominator must be integers")
        else:
            raise ValueError("Invalid format")