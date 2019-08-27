def function1():
    VAR1 = "My! name@ is Abhishek"
    TRIMMEDVAR = VAR1.split(" ")
    SPLITTEDVAR= [x.strip("!, @") for x in TRIMMEDVAR] 
    print (SPLITTEDVAR)

class myclass():
    def method1 (self):
        function1()

if __name__ == "__main__":
    s1=myclass()
    s1.method1()