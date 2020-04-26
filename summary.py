print("----------------------------")
print("#Summary Program")
print("Type 'exit' to end program")
print("----------------------------")

# ตัวแปรไว้เก็บาค่า
sumdata = 0
count = 1

while True:
    data = input(f"Enter number {count} :")
    # ตรวจว่าผู้ใช้ป้อน 'exit'
    if data == "exit":
        break
    # หาผลรวม
    sumdata += int(data)
    count = count+1

print(f"Sum value is {sumdata}")
