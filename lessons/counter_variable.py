"""How many times does 'a' show up in 'banana'?"""

message: str = "banana"
idx: int = 0
a_counter: int = 0
while idx < len(message):
    if message[idx] == "a":
        a_counter += 1
    idx += 1
print(a_counter)
a_counter_str: str = str(a_counter)
print("there are " + a_counter_str + " a's!")

# practice problems
x: int = int(input("Pick a number: "))
y: int = 10
z: int = 2
x = x - 1
if x < 10:
    print("A")
else:
    if (x % z) == 0:
        print("B")
if x == (y + z):
    print("C")
else:
    print("D")
