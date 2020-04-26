# import ทั้งหมดทุกฟังก์ชันใน module /แบบที่ 1
# import number

# import มาบางฟังก์ชัน  /แบบที่ 2
# from number import factorial, fibonacci

# import ทุกฟังก์ชัน /แบบที่ 3
# from number import*

# import และ เปลี่ยนชื่อฟังก์ชัน เรียกว่า นามแฝง alias /แบบที่ 4
from number import factorial as fa, fibonacci as fi

# เรียกใช้งาน /แบบที่ 1
# print(number.factorial(5))
# print(number.fibonacci(100))

# เรียกใช้งาน /แบบที่ 2  3
# print(factorial(5))
# print(fibonacci(100))

# เรียกใช้งาน /แบบที่ 4
print(fa(5))
print(fi(100))
