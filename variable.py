a = 3
b = 4.92
c = "itgn"

print(a)
print(b)
print(c)

print(a, b, c)

x = y = z = 10
j, k = 5, 10
print(x, y, z)
print(j, k)

status = True
msg = False
print(status, msg)

# concat string
print("ราคาขายต่อชิ้น", b, "บาท")

# string interpolation
print("ราคาขายต่อชิ้น %.2f บาท" % b)
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b, a))

# format string
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")
