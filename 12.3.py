class myclass:
     def __init__(self):
          self.public_attribute="I'm a public attribute"
          self._protected__attribute="I'm a protected attribute"
          self.__private_attribute="I'm a private attribute"
     def public_method(self):
          print("I'm a public method")
     def _protected_method(self):
          print("I'm a protected method")
     def __private__method(self):
          print("I'm a private method")
obj=myclass()
print(obj.public_attribute)
obj.public_method()
print(obj._protected__attribute)
obj._protected_method()
print(obj._myclass__private_attribute)
obj._myclass__private__method()
