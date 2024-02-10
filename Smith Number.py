def Prime(n,c):
    if c<=n:
        if n%c==0:
            return 1+Prime(n,c+1)
        else:
            return Prime(n,c+1)
    else:
        return 0
def digit_sum(n):
    if n>0:
        return (n%10)+digit_sum(n//10)
    else:
        return 0
def Smith(n,c):
    if c<=n//2:
        if Prime(c,1)==2 and n%c==0:
            return digit_sum(c)+Smith(n,c+1)
        else:
            return Smith(n,c+1)
    else:
        return 0
n=int(input("Enter any number:"))
if Prime(n,1)!=2 and Smith(n,2)==digit_sum(n):
    print("Smith Number.")
else:
    print("Not")
    