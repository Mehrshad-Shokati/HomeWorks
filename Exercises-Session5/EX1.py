class Fraction:
    def  __init__(self, N , D):
        self.numerator = N
        self.denominator = D


    def show(self):
        print(self.numerator, "/", self.denominator)



    def sum(self, f2):
        result = Fraction(None, None)
        result.numerator = self.numerator * f2.denominator + f2.numerator * self.denominator
        result.denominator = self.denominator * f2.denominator
        return result


    def sub(self, f2):
        result = Fraction(None, None)
        result.numerator = self.numerator * f2.denominator - f2.numerator * self.denominator
        result.denominator = self.denominator * f2.denominator
        return result


    def div(self, f2):
        result = Fraction(None, None)
        result.numerator = self.numerator * f2.denominator
        result.denominator = self.denominator * f2.numerator
        return result

    def mul(self, f2):
        result = Fraction(None, None)
        result.numerator = self.numerator * f2.numerator
        result.denominator = self.denominator * f2.denominator
        return result 


fraction1 = Fraction(3, 4)
print("\nFraction 1: ")
fraction1.show()

fraction2 = Fraction(5, 7)
print("\nFraction 2: ")
fraction2.show()

sum = fraction2.sum(fraction1)
print("\n Sum: ")
sum.show()

sub = fraction2.sub(fraction1)
print("\n Subtraction: ")
sub.show()

mul = fraction2.mul(fraction1)
print("\n Multiplication: ")
mul.show()


division = fraction2.div(fraction1)
print("\n Division : ")
division.show()