def mye(level):
    if level <1:
        raise Exception("Invalid level!")
    print("hello")

try:
    mye(2)

except Exception as err:
    print(1,err)
else:
    print(2)

