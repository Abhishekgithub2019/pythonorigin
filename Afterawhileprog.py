
def function5():
    vowels = {"a","e", "i", "o", "u"}
    STR1 = "tata consultancy services"
    Count = 0
    i=0
    while i < len(STR1):
        if STR1[i] in vowels:
            Count = Count + 1
        i=i+1 
    print (Count)

def function1():
    STR1 = "KOKOMELON MEINE BRUDER!"
    SPLITTEDVAR = STR1.split(" ")
    TRIMMEDVAR = [x.strip("!") for x in SPLITTEDVAR]
    print (TRIMMEDVAR)

def function2():
    DAYS = ["Mon", "TUE"]
    DAYS.append("Wed")
    for i,d in enumerate (DAYS):
        if type(DAYS) != tuple:
            print (str(i)+ " "+ "of the week is" + str(d))
    print(DAYS)
    del DAYS[2]
    print (DAYS)

def function3():
    STR1 = bytearray ("abc", encoding="UTF-8")
    STR1[0] = 65
    if STR1.startswith (b"A"):
        print (STR1)

def function4():
    DICT1 = {1:"Abhi", 2:"Kanu",3:"Kokomelon"}
    DICT2 = {4:"Ankuri"}
    DICT1.update(DICT2)
    print (DICT1)


class myclass():
    def method1(self):
        function1()
        function2()
    def method2(self):
        function3()
        function5()

if __name__=="__main__":
    s1=myclass()
    s1.method1()
    s1.method2()
    function4()

