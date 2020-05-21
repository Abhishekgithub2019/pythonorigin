def function1():
    STR1 = "TATA CONSULTANCY SERVICES"
    i=0
    count = 0
    vowels = {'a', 'e', 'i'}
    STR2=STR1.lower()
    while i < len(STR2):
        if STR2[i] in vowels:
            count = count + 1
            i=i+1
    print(count)


if __name__ == "__main__":
    function1()