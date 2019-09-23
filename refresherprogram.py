def function1():
    VAR1="My name! is Singh$"
    VAR2= VAR1.split(" ")
    VAR3=[x.strip("!, $") for x in VAR2]
    print (VAR3)

def function2():
    VAR4={"Mon", "Tue"}
    for i,d in enumerate(VAR4):
        print ("First day is" + " " + d)


class myclass():
    def method1(self):
        function1()
        function2()


if __name__=="__main__":
    s1=myclass()
    s1.method1()