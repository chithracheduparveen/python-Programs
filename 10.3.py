try:
     num=int(input("Enter a number:"))
     result=10/num
except valueerror:
     print("Error:invalid input!please enter a valid number")
except zerodivisionerror:
     print("Error:division by zero!")
else:
     print("Result:",result)
