name=input("Enter your name please ")
age=int(input("Enter your age? {} ".format(name)))
if age>18 and age<=30:#or  if 18<= age <31:

    print("Enjoy your holidays..{} ".format(name))
else:
    print("Sorry you can't go on holidays yet {} ".format(name))