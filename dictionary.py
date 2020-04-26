scores = {
    'jo': 10,
    'bo': 20,
    'go': 30
}
print(scores)
print(scores['bo'])

# เพิ่มสมาชิกใหม่
scores['ro'] = 40

print(scores)

# การสร้าง dictionary ว่าง
point = {}

# เพิ่มค่า
point['m_a'] = 10.2
point['m_b'] = 10.4
point['m_c'] = 10.6

print(point)

# การลูปอ่านสมาชิก
for k, v in scores.items():
    print(k, v)
