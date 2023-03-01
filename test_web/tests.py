a= 9223372036854771712
b= 0
while True:
    a /= 1024
    b+=1
    if a % 1024 == a:
        break
    print(f"{a},{b}")