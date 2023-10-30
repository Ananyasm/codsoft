#CALCULATOR


def cal(n1,n2,op):
    if op=='+':
        res=n1+n2
    elif op=='-':
        res=n1-n2
    elif op=='*':
        res=n1*n2
    elif op=='/':
        res=n1/n2
    elif op=='^':
        res=n1**n2
    else:
        print("Invalid operator")  
        exit()     
    return res


print("SIMPLE CALCULATOR:")
no1=int(input("Enter First Number:"))
no2=int(input("Enter Second Number:"))
print("Enter ONE OPERATOR(+,-,*./,^)-")
oper=input()
re=cal(no1,no2,oper)
print("The result of",no1,oper,no2,'=',re)

