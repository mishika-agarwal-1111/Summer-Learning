a=input("enter a string")
def reverse(s):
    res=""
    for i in range(len(s)-1,-1,-1):
        res=res+s[i]
    return res
print(reverse(a))
