def function1():
    VAR1 = "My! name@ is Abhishek"
    TRIMMEDVAR = VAR1.split(" ")
    SPLITTEDVAR= [x.strip("!, @") for x in TRIMMEDVAR] 
    print (SPLITTEDVAR)

def function2():
    DAYS = ["Mon", "TUE"]
    for i,d in enumerate (DAYS):
        print (str(i) + " " + "Day of the week is" + " " + str(d))
        
class myclass():
    def method1 (self):
        function1()
    def method2(self):
        function2()


if __name__ == "__main__":
    s1=myclass()
    s1.method1()
    s1.method2()