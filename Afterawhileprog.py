def function1():
    Days = ["Mon", "Tue"]
    Days.append("Wed")
    for i,d in enumerate(Days):
        print (str(i) + " " + "day of the week is" + " " + str(d))

def function2():
    STR1=bytearray("Tata Consultancy", encoding = "UTF-8")
    STR1[1] = 65
    STR2=str(STR1)
    STR3=STR2.upper()
    STR4 = STR3.split(" ")
    print (STR4)

class mimmyclass():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def method1(self):
        print (self.fname + " " + self.lname)




class firstclass():
    def method1(self):
        function1()
        function2()

if __name__=="__main__":
    s1=firstclass()
    s1.method1()
    s2=mimmyclass("Kanu", "mimmy")
    s2.method1()