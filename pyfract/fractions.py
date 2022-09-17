class Fraction:
    """
        A fraction represents a number in the a/b form. Takes a fraction-like formatted string and returns a fraction object.
    """

    def __init__(self, fract: str):
        if type(fract) == str:
            try:
                self._numerator = int(fract.replace(" ", "").split("/")[0])
                self._denominator = int(fract.replace(" ", "").split("/")[1])
                self._fraction = self.simplify(fract)
            except ValueError:
                raise ValueError("Invalid numerator or denominator values. Numerator and denominator must be integers")
            except IndexError:
                raise ValueError("Interger or floating point numbers should be entered as int or float")
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

    def updateFraction(self):
        self._fraction = self.simplify(f"{self._numerator}/{self._denominator}")

    def add(self, *args, apply=True):
        """
            Adds to the fraction the ints, floats or fractions given as arguments. Takes apply argument to check whether to persist changes or not.
        """
        if apply:
            for value in args:
                if type(value) == int:
                    num_to_add = value*self._denominator
                    self._numerator += num_to_add
                    self.updateFraction()
                if type(value) == Fraction:
                    self._numerator = self._numerator * value._denominator + value._numerator * self._denominator
                    self._denominator = self._denominator * value._denominator
                    self.updateFraction()
                else:
                    raise ValueError("Invalid term. Term should be either int or Fraction")
            return self._fraction
        else:
            temp = Fraction(f"{self._numerator}/{self._denominator}")
            for value in args:
                if type(value) == int:
                    num_to_add = value*temp._denominator
                    temp._numerator += num_to_add
                    temp.updateFraction()
                if type(value) == Fraction:
                    temp._numerator = temp._numerator * value._denominator + value._numerator * temp._denominator
                    temp._denominator = temp._denominator * value._denominator
                    temp.updateFraction()
                else:
                    raise ValueError("Invalid term. Term should be either int or Fraction")
            return temp._fraction

    def substract(self, *args, apply=True):
        """
            Adds to the fraction the ints, floats or fractions given as arguments. Takes apply argument to check whether to persist changes or not.
        """
        if apply:
            for value in args:
                if type(value) == int:
                    num_to_add = value*self._denominator
                    self._numerator -= num_to_add
                    self.updateFraction()
                if type(value) == Fraction:
                    self._numerator = self._numerator * value._denominator - value._numerator * self._denominator
                    self._denominator = self._denominator * value._denominator
                    self.updateFraction()
                else:
                    raise ValueError("Invalid term. Term should be either int or Fraction")
            return self._fraction
        else:
            temp = Fraction(f"{self._numerator}/{self._denominator}")
            for value in args:
                if type(value) == int:
                    num_to_add = value*temp._denominator
                    temp._numerator -= num_to_add
                    temp.updateFraction()
                if type(value) == Fraction:
                    temp._numerator = temp._numerator * value._denominator - value._numerator * temp._denominator
                    temp._denominator = temp._denominator * value._denominator
                    temp.updateFraction()
                else:
                    raise ValueError("Invalid term. Term should be either int or Fraction")
            return temp._fraction

    def multiply(self, *args, apply=True):
        """
            Multiplies the fraction by the ints, floats or fractions given as arguments. Takes apply argument to check whether to persist changes or not.
        """
        if apply:
            for value in args:
                if type(value) == int or type(value) == float:
                    self._numerator = self._numerator * value
                    self.updateFraction()
                elif type(value) == Fraction:
                    self._numerator = self._numerator * value._numerator
                    self._denominator = self._denominator * value._denominator
                    self.updateFraction()
                else:
                    raise ValueError("Invalid factor. Factor should be either int, float or Fraction")
            return self._fraction
        else:
            temp = Fraction(f"{self._numerator}/{self._denominator}")
            for value in args:
                if type(value) == int or type(value) == float:
                    temp._numerator = temp._numerator * value
                    temp.updateFraction()
                elif type(value) == Fraction:
                    temp._numerator = temp._numerator * value._numerator
                    temp._denominator = temp._denominator * value._denominator
                    temp.updateFraction()
                else:
                    raise ValueError("Invalid factor. Factor should be either int, float or Fraction")
            return temp._fraction

    def divide(self, *args, apply=True):
        """
            Divides the fraction by the ints, floats or fractions given as arguments. Takes apply argument to check whether to persist changes or not.
        """
        if apply:
            for value in args:
                if type(value) == int or type(value) == float:
                    self._denominator = self._denominator * value
                    self.updateFraction()
                elif type(value) == Fraction:
                    self._numerator = self._numerator * value._denominator
                    self._denominator = self._denominator * value._numerator
                    self.updateFraction()
                else:
                    raise ValueError("Invalid factor. Factor should be either int, float or Fraction")
            return self._fraction
        else:
            temp = Fraction(f"{self._numerator}/{self._denominator}")
            for value in args:
                if type(value) == int or type(value) == float:
                    temp._denominator = temp._denominator * value
                    temp.updateFraction()
                elif type(value) == Fraction:
                    temp._numerator = temp._numerator * value._denominator
                    temp._denominator = temp._denominator * value._numerator
                    temp.updateFraction()
                else:
                    raise ValueError("Invalid factor. Factor should be either int, float or Fraction")
            return temp._fraction