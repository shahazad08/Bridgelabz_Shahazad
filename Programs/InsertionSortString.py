from Utilities import utilities
#from Utilities.utilities import str1


class NumericException(RuntimeError):
   def apply(self,str1):
       super().__init__()


def verify_digit(self):
    l5=[0-9]
    for i in range(len(l5)):
        if str1 in l5:
            raise NumericException("Only String allowed")

try:
    m = int(input("Enter the Nth Elements"))
    print("Enter the elements")
    str1 = [(input()) for i in range(m)]
    print(str)
    utilities.Insertion(str1)
    #raise NumericException

except NumericException:
    print("Only String Allowed")
except ValueError:
    print("Enter the Valid String")