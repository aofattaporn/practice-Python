x = [2, 3, 11, 24, 13, 14, 16]
print(x[2 : 7 : 2]) # start stop step
print(x)

# List comprehension
data = []
# for x in range(0, 21, 2):
#     data.append(x)
#     print(data)
data = [x for x in range(0, 21, 2)]
print(data)

celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = [ (9/5*x +32) for x in celsius]
print(fahrenheit)

 