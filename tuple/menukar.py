t1 = (5, 3, 1, 0)
t2 = (10, 20)
print("Sebelum di tukar")
print(t1)
print(t2)

print("Sesudah di tukar")
t1, t2 = t2, t1
print(t1)
print(t2)