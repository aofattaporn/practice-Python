"""
Dictionary มีการเก็บเป็นคู่อันดับ
keys กัย value (kay-value pair)
keys : value
keys ทำงานคล้ายกับ index
have a meaning full
"""
fruits = { "apple" : 10, \
           "banana" : 25,\
           "mangoteen": 30}
print(fruits)

print(fruits["apple"])
print(fruits.keys())
print(fruits.values())
print(fruits.items())

for (k,v) in fruits.items():
    print(k, ":", v)

res = fruits.get("Durian")
print(res)

fruits["orange"] = 400
print(fruits)
fruits.pop("banana")
print(fruits)