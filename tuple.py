# Tuple uses (...)
number = (1, 2, 3, 4, 5)
mixed = (10, 20, [5, 4, 3], True, 'Samit')

print(number[2])
print(mixed[1])
print(mixed[2])
print(mixed[2][1])

# ลองเปลี่ยนค่าสมาชิก ซึ่งจะ error เพราะ tuple ห้ามเปลี่ยนค่า
number[2] = 10
print(number)
