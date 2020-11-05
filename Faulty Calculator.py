
# Faulty Calculator

n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=(input("what you want?"+"/,*,+,-,%"))

if n1==45 and n2==3 and n3=="*":
    print("555")
elif n1==56 and n2==9 and n3=="+":
    print("77")
elif n1 == 56 and n2 ==6 and n3 == "/":
    print("4")
elif n3=="*":
    mul=n1*n2
    print(mul)
elif n3=="+":
    sum=n1+n2
    print(sum)
elif n3=="/":
    div=n1/n2
    print(div)
elif n3=="-":
    sub=n1=n2
    print(sub)
elif n3=="%":
    mod=n1%n2
    print(mod)
else:
    print("plece cheke value")
