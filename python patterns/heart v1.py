num = 20 # even number, if msg is long user larger number
n = num//2
msg = "random msg"
l = len(msg)
sym = "*"
for i in range(n):
    print(" "*(n-i-1) + f"{sym} "*(i+1), end="")
    if num%2 == 0:
        for j in range(2*(n-i-1)):
            print(" ", end="")
    else:
        for j in range(2*(n-i-1)):
            print(" ", end="")
    for i in range(i+1):
        print(f"{sym} ", end="")
    print()

if num % 2 == 0:
    if l%2==0:
        print(f"{sym} "*((num-l)//2) + " ".join(msg) + f" {sym}"*((num-l)//2) )
    else:
        print(f"{sym} " *((num-l)//2) + " ".join(msg) + f" {sym}"*(((num-l)//2)+1))

else:
    if l%2:
        print(f"{sym} " *((num-l)//2) + " ".join(msg) + f" {sym}"*(((num-l)//2)+1) )
    else:
        print(f"{sym} " *((num-l)//2) + " ".join(msg) + f" {sym}"*(((num-l)//2)))


for i in range(num, 0,-1):
    print(" "*(num-i) + f"{sym} "*(i))
