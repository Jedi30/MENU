class employee:
       def __init__(self,name,empid,position, is_on_probation) :
              
        self.name= name 
        self.empid = empid
        self.position = position
        self.is_on_probation = is_on_probation

        def Hi(self):
          print("Hello" + self.name)

employee1 = employee("Chris Mariano", 20242703, "Junior Python Developer", True)  

print(employee1.name)
print(employee1.empid)
print(employee1.position)
print(employee1.is_on_probation)
    


          