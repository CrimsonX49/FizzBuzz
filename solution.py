result = []

for i in range(26):
    result.append(i)
print(result) 

for i in result.copy():
    if i % 3 == 0 and i % 5 == 0:
        result.remove(i)
        result.insert(i, "FizzBuzz")
    elif i % 5 == 0:
        result.remove(i)
        result.insert(i, "Buzz")
    elif i % 3 == 0:
        result.remove(i)
        result.insert(i, "Fizz")
        
print(result) 

