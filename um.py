
def check(a,b):
    if a==b or abs(a-b)==400 or (a+b)== 400:
        return True
    else:
        return False

print(check(1600, 12))
print(check(200, 12))
print(check(200, 200))
print(check(480, 80))
print(check(3, 3))
print(check(14, 77))







