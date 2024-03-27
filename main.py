# myNum = input() # takes input

# listOfNums = list     (map(int, myNum)) # converts to list

# firstNum = listOfNums [0] # gets the index of first value from the list 
# lastNum = listOfNums [-1] # gets the index of last value from the list 

# print(firstNum + lastNum) # prints the sum of first and last value

num = int(input())
last = num % 10
first = 0

while num:
  temp = num % 10
  if num == temp:
    first = num
  num = num // 10
print(first + last)