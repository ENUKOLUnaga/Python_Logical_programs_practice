def max_aqua_curtains(s,l,n):

    max_aqua=0
    for i in range(0,n,l):
        box=s[i:i+l]
        count_a=box.count('a')
        max_aqua=max(max_aqua,count_a)

    return max_aqua

s=input("form a string by using (ab):")
l=int(input())
n=len(s)

print(f"max a in {s}:{max_aqua_curtains(s,l,n)}")
