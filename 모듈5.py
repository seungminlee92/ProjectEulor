def submul(n):
    i=0
    l=[]
    while i<=n:
        i+=1
        if n%i == 0:
            l.append(i)
        else:
            continue

    return l

def mul(n):
    i,t=1,1
    while i<=n:
        t*=i
        i+=1

    return t

total=mul(10)
total_list=list(range(1,11))
target=1
target_list=total_list

print(total)
print(total_list)

div=1

for i in total_list:
    while div<=i:
        if total%div==0 & i in total_list:
            total_list.remove(div)
        i+=1
print(total_list)