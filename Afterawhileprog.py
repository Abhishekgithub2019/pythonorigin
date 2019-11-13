def function1():
    print ("Hello World")

def function2():
    STR1 = ["Mon", "Tue"]
    for i,d in enumerate (STR1):
        print (str(i) + " " + "day of the week is" + " " + str(d))

def function3():
    STR1 = ("Abhishek IS FINICKY!")
    SPLIT1 = STR1.split(" ")
    TRIM1 = [x.strip ("!") for x in SPLIT1]
    print (TRIM1)

class myclass():
    def method1(self):
        function1()
        function2()
        function3()   

if __name__ == "__main__":
    s1=myclass()
    s1.method1()