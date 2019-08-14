x=3

def function1():
    global x
    x=5
    print (x)

def function2():
    str1 = "My! name is @Abhishek"
    str2= str1.split(" ")
    trimmedlist = [x.strip("!, @") for x in str2]
    print(trimmedlist)
    
def function3():
    Days = {"Mon", "Tue"} 
    for i,d in enumerate(Days):
        print (str(i) + " " + "day of the week is" + " " +str(d))

class myclass():
    def method1(self):
        function1()
class myclass2():
    def method1(self):
        function2()    

if __name__=="__main__":
    function1()
    function3()
    s1=myclass()
    s1.method1()
    s2=myclass2()
    s2.method1()
    
