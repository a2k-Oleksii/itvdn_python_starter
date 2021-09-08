a = {1, 2, 2, 2, 3, 4}
print(a)
a.pop()
print(a)
b = {1, 2, 3, 4, 5, 9, 10, 44}

b.discard(3)
print(b)

c = {1, 2, 5, 6, 4, 3}
c.add(6)
print(c)

print(a.union(b))
print(a.intersection(b))
print(a)


e = {1, 2, 3, 4}
f = {3, 4}

print(e.difference(f))
print(f.difference(e))

print(3 in e)


new_tuples = (1, 2, 3, 4, 3, 5, 5, 5)
print(new_tuples)

aa = (1, 2)
x, y = aa
print(x, y)
x, y = y, x
print(x, y)
print("________________________")
aaa = [(1, 2), (3, 4), (5, 6)]
for firs, second in aaa:
    print(firs, second)
