def function1():
    VAR1="My name! is Abhishek"
    SPLITTEDVAR=VAR1.split(" ")
    TRIMMEDVAR=[x.strip("!") for x in SPLITTEDVAR]
    print (TRIMMEDVAR)

def function2():
    VAR1 = ["Mon", "Tue", "Wed"]
    for i,d in enumerate(VAR1):
        print (str(i) + " " + "day of the week is" + " " + str(d))

class myclass():
    def method1(self):
        function1()
        function2()

if __name__=="__main__":
    s1=myclass()
    s1.method1()