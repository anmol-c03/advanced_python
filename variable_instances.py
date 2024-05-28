
class student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=fname+lname+'@abc.com'

    #class method .doesnot require any instance. class is passed as parameter
    @classmethod
    def salary(cls):
        return 20000
    
    def full_name(self):
        return f'{self.fname} {self.lname}'
    
    
std1=student('Anmol','chalise')
std2=student('Aakriti','chalise')

print(std1.email)
print(student.salary())
print(std2.full_name())
