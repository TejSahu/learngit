for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubded is {2:4}".format(i, i**2, i **3))
    #power opeartor is "**"
    #{0:2} width addition

print()
for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubded is {2:<4}".format(i, i**2, i **3))
    #left alignment for right add > symbol
    #for center use ^ symbol

print()
for i in range(1,13):
    print("No. {0:^2} squared is {1:^3} and cubded is {2:^4}".format(i, i**2, i **3))
print()
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:<62.45f}".format(22/7))

print()
for i in range(1,13):
    print("No. {} squared is {} and cubded is {:4}".format(i, i**2, i **3))
