#walrus
"""""
while True:
    height=int(input("Write your height: "))

    if height < 170:
        print("You're short ")
        break
    else:
        print("Wow so tall")
        break
"""""
#alrus isdigit()
while not (height :=input("write your height:")).isdigit() :
    print("please enter number\n")
height=int(height)

if height < 170:
    print("You're short ")
    
else:
    print("Wow so tall")
    