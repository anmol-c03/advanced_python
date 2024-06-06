import datetime

class student:
    num_of_std=0     # each time we create an instance it should increase by 1
    extra_charge=0.02
    admission_charge=20000
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=fname+lname+'@abc.com'
        student.num_of_std+=1

    #class method .doesnot require any instance. class is passed as parameter
    @classmethod
    def admission_fee(cls):
        return student.admission_charge

    def extra_pay(self):
        return student.admissoin_charge*self.extra_charge
        
    def full_name(self):
        return f'{self.fname} {self.lname}'


class student_alt_cons(student):
    @classmethod
    def raise_admission_fee(cls):
        cls.admission_charge=30000

    # as alt cons
    @classmethod
    def from_string(cls,std_str):#its convention/practice for class method as alt cons to start with from
        fname,lname=std_str.split('-')
        return cls(fname,lname)

class std_static_mtd(student_alt_cons):
    def __init__(self):
        pass
    
    @staticmethod
    def is_holiday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

#------------------------------------------------------------------------------------------------------------------------------
#class variable
student_alt_cons.raise_admission_fee()
print(student.admission_charge)
print(student_alt_cons.admission_charge,'\n')
#------------------------------------------------------------------------------------------------------------------------------
# for from_string (class method as constructor alternative )
std_str_1='Anmol-Chalise'
alt_cons=student_alt_cons.from_string(std_str_1)
print(f'{alt_cons.fname} {alt_cons.lname}\n')

#above implementation of from_string is same as 

# str='Anmol-chalise'
# fname,lname=str.split('-')
# new_alt_cons=student_alt_cons(fname,lname)
# print(f'{new_alt_cons.fname} {new_alt_cons.lname}')

#------------------------------------------------------------------------------------------------------------------------------
#static method implementation
today_date=datetime.date(2023,5,28)

print(std_static_mtd.is_holiday(today_date))
#another way of doing this
static_mtd_1=std_static_mtd()
print(static_mtd_1.is_holiday(today_date))

