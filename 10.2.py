try:
     num=int(input("enter a number:"))
     result=10/num
     print("Result:",result)
except valueerror: 
          print("error:invalid input!please enter a valid number")
except zerodivisionerror:
          print("Error:Division by zero!")
