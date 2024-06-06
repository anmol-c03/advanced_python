# so to tackle above error we want setter 
class student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    @property  #added portion
    def email(self):
        return f'{self.fname}{self.lname}@gmail.com'
        
    @property    #added portion
    def fullname(self):
        if self.fname==None or self.lname==None:
            return f'Name deleted successfully'
        return self.fname+self.lname

    @fullname.setter
    def fullname(self,name):
        self.fname,self.lname=name.split(' ')

    @fullname.deleter
    def fullname(self):
        self.fname=None
        self.lname=None
        print('Delete Name!')
        
std1=student('Anmol','chalise')
std2=student('Amol','meheta')
#------------------------------------------------------------------------------------------
std1.fullname='Manoj Khanal'
print(std1.fname)
print(std1.email)
print(std1.fullname)     
#------------------------------------------------------------------------------------------

print('\n')
del std1.fullname
print(std1.fname)
print(std1.email)
print(std1.fullname)  
#------------------------------------------------------------------------------------------
#so if we want to access method as an attribute , use @property decoraror
# and if we want to assign method a value as an attribute ,create setter for that property class