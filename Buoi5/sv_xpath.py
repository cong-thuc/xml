from lxml import etree

# Đọc file XML
tree = etree.parse("sv.xml")
root = tree.getroot()

# 1. Lấy tất cả sinh viên
students = tree.xpath("/school/student")
print("1. Tất cả sinh viên:")
for s in students:
    print(etree.tostring(s, pretty_print=True).decode())

# 2. Liệt kê tên tất cả sinh viên
names = tree.xpath("/school/student/name")
print("\n2. Tên tất cả sinh viên:")
for n in names:
    print(n.text)

# 3. Lấy tất cả id sinh viên
ids = tree.xpath("/school/student/id")
print("\n3. ID tất cả sinh viên:")
for i in ids:
    print(i.text)

# 4. Lấy ngày sinh SV01
dob_sv01 = tree.xpath("/school/student[id='SV01']/date")
print("\n4. Ngày sinh SV01:")
for d in dob_sv01:
    print(d.text)

# 5. Lấy các khóa học
courses = tree.xpath("/school/enrollment/course")
print("\n5. Các khóa học:")
for c in courses:
    print(c.text)

# 6. Thông tin sinh viên đầu tiên
first_student = tree.xpath("/school/student[1]")[0]
print("\n6. Sinh viên đầu tiên:")
print(etree.tostring(first_student, pretty_print=True).decode())

# 7. Mã sinh viên đăng ký Vatly203
sv_vatly203 = tree.xpath("/school/enrollment[course='Vatly203']/studentRef")
print("\n7. Sinh viên học Vatly203:")
for sv in sv_vatly203:
    print(sv.text)

# 8. Tên sinh viên học Toan101
sv_toan101 = tree.xpath("/school/student[id=/school/enrollment[course='Toan101']/studentRef]/name")
print("\n8. Tên sinh viên học Toan101:")
for sv in sv_toan101:
    print(sv.text)

# 9. Tên sinh viên học Vatly203
sv_vatly203_name = tree.xpath("/school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name")
print("\n9. Tên sinh viên học Vatly203:")
for sv in sv_vatly203_name:
    print(sv.text)

# 10. Tên & ngày sinh sinh năm 1997
sv_1997 = tree.xpath("/school/student[number(substring(date,1,4))=1997]")
print("\n10. Tên & ngày sinh sinh năm 1997:")
for s in sv_1997:
    name = s.find("name").text
    date = s.find("date").text
    print(f"{name} - {date}")

# 11. Tên sinh viên sinh trước 1998
sv_before1998 = tree.xpath("/school/student[number(substring(date,1,4)) < 1998]/name")
print("\n11. Sinh viên sinh trước 1998:")
for s in sv_before1998:
    print(s.text)

# 12. Đếm tổng số sinh viên
total_sv = tree.xpath("count(/school/student)")
print("\n12. Tổng số sinh viên:", int(total_sv))

# 13. Sinh viên chưa đăng ký môn nào
sv_no_course = tree.xpath("/school/student[not(id=/school/enrollment/studentRef)]")
print("\n13. Sinh viên chưa đăng ký môn nào:")
for s in sv_no_course:
    print(s.find("name").text)

# 14. <date> anh em ngay sau <name> của SV01
date_after_name = tree.xpath("/school/student[id='SV01']/name/following-sibling::date")
print("\n14. <date> sau <name> SV01:")
for d in date_after_name:
    print(d.text)

# 15. <id> anh em ngay trước <name> của SV02
id_before_name = tree.xpath("/school/student[id='SV02']/name/preceding-sibling::id")
print("\n15. <id> trước <name> SV02:")
for i in id_before_name:
    print(i.text)

# 16. Node <course> cùng enrollment với studentRef='SV03'
courses_sv03 = tree.xpath("/school/enrollment[studentRef='SV03']/course")
print("\n16. Khóa học SV03:")
for c in courses_sv03:
    print(c.text)

# 17. Sinh viên có họ Trần
sv_tran = tree.xpath("/school/student[starts-with(name,'Trần')]/name")
print("\n17. Sinh viên họ Trần:")
for s in sv_tran:
    print(s.text)

# 18. Năm sinh SV01
year_sv01 = tree.xpath("substring(/school/student[id='SV01']/date,1,4)")
print("\n18. Năm sinh SV01:", year_sv01)
