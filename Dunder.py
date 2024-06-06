## any methods that are preceeded and followed by __
# eg __init__,__str__,__call__,__repr__,__iter__

class student:
    num_of_std=0
    def __init__(self,fname,lname,fee=20000):
        self.fname=fname
        self.lname=lname
        self.email=fname+lname+'@abc.com'
        self.fee=fee
        student.num_of_std+=1

    def full_name(self):
        return f'{self.fname} {self.lname}'

    def __repr__(self):
        return f'student("{self.fname}","{self.lname}")'

    def __str__(self):
        return f'{self.full_name()} {self.email}'

    def __add__(self,another):
        return f'total fee {self.fee+another.fee}'

    def __len__(self):
        return len(self.full_name())
        

std1=student('Anmol','chalise',3000)
std2=student('Arima','meheta',30000)

print(std1)

print(repr(std1))
print(str(std1))

print(std1+std2)

print(f'length of student name is {len(std1)}')

print(std1.__dict__)
##same as using
# print(std1.__repr__)
# print(std1.__str__)