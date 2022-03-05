ans = int(input("Guess a number from 1 to 10 :"))

if ans == 1:
  print("I chose 7")
else:
  print("I chose " + str(ans - 1))
print("You chose "+str(ans))
