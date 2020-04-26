# การสร้างฟังก์ชันแบบไม่มีการ return value
def hello(name):
    print(f"Hello {name}")


# ฟังก์ชันแบบมีการ return value
def area(w, h):
    total = w*h
    return total


# เรียกใช้งานฟังก์ชัน
hello("mane")

# เรียกใข้งาน area()
print("พท ทั้งหมดเท่ากับ", area(5, 6))

# ฟังก์ชั่นแบบมีค่าเริ่มต้น


def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name:{name}")
    print(f"Salary:{salary}")
    print(f"Language:{lang}")


show_info()
print()
show_info('Suksa', 2000, 'php')
