def function1():
    STR1 = bytearray ('ABC', encoding = 'UTF-8')
    STR1[1] = 97
    print (STR1)


class parentclass():
    def __init__ (self,fname,lname):
        self.fname = fname
        self.lname = lname
    def method1(self):
        print (self.fname + " " +self.lname) 

class childclass(parentclass):
    def __init__(self, fname, lname, age):
        parentclass.__init__(self, fname, lname)
        self.age = age
    def method1(self):
        print (self.fname + self.lname + self.age)


if __name__ == "__main__":
    function1()
    s1=childclass("kanu", "singh","32")
    s1.method1()