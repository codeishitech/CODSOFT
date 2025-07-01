#creating class with functions performing the operations of a basic calculator:
class Calculator:
    def __init__(self):
        self.a=int(input("Enter the first value: "))
        self.b=int(input("Enter the second value: "))
        self.opr=input("Enter the required operation (+,-,*,/): ")
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error! Division by zero is not allowed."

calc=Calculator()
if calc.opr=="+":
    print("The sum is: ",calc.add())
elif calc.opr=="-":
    print("The difference is: ",calc.sub())
elif calc.opr=="*":
    print("The product is: ",calc.mul())
elif calc.opr=="/":
    print("The quotient is: ",calc.div())
else:
    print("Invalid operation. Please enter a valid operation.")
print("Thank you for using the calculator!")