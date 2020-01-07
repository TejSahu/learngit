age=30
print('my age is '+ str(age) + ' years')
print('my age is {0} years'.format(age)) #{} field format

print('There are {0} days in {1} , {2}, {3} , {4} , {5} , {6} and {7}'
      .format(31,"Jan", "Mar" , "May","Jul","Aug", "Oct" ,"Dec"))
print("There are {0} days in Jan, Mar, May, Jul , Aug , Oct and Dec".format(31))

print("""\nNo of days in months are as follows
Jan {0}
Feb {1}
Mar {0}
Apr {2}
May {0}
Jun {2}
Jul {0}
Aug {0}
Sep {2}
Oct {0}
Nov {2}
Dec {0}.""".format(31,28,30))