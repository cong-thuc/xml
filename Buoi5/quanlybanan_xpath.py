from lxml import etree

# Đọc file XML
tree = etree.parse("quanlybanan.xml")
root = tree.getroot()

# 1. Lấy tất cả bàn
bans = tree.xpath("/QUANLY/BANS/BAN")
print("1. Tất cả bàn:")
for ban in bans:
    print(etree.tostring(ban, pretty_print=True).decode())

# 2. Lấy tất cả nhân viên
nvs = tree.xpath("/QUANLY/NHANVIENS/NHANVIEN")
print("\n2. Tất cả nhân viên:")
for nv in nvs:
    print(etree.tostring(nv, pretty_print=True).decode())

# 3. Lấy tất cả tên món
ten_mon = tree.xpath("/QUANLY/MONS/MON/TENMON")
print("\n3. Tất cả tên món:")
for mon in ten_mon:
    print(mon.text)

# 4. Tên nhân viên NV02
nv02 = tree.xpath('/QUANLY/NHANVIENS/NHANVIEN[MANV="NV02"]/TENV')
print("\n4. Tên NV02:", [n.text for n in nv02])

# 5. Tên và SDT nhân viên NV03
nv03 = tree.xpath('/QUANLY/NHANVIENS/NHANVIEN[MANV="NV03"]')
print("\n5. Tên & SDT NV03:")
for nv in nv03:
    ten = nv.find("TENV").text
    sdt = nv.find("SDT").text
    print(f"{ten} - {sdt}")

# 6. Tên món giá > 50k
mon_gt50k = tree.xpath("/QUANLY/MONS/MON[number(GIA)>50000]/TENMON")
print("\n6. Tên món giá > 50k:")
for mon in mon_gt50k:
    print(mon.text)

# 7. Số bàn của HD03
soban_hd03 = tree.xpath('/QUANLY/HOADONS/HOADON[SOHD="HD03"]/SOBAN')
print("\n7. Số bàn HD03:", [s.text for s in soban_hd03])

# 8. Tên món mã M02
ten_m02 = tree.xpath('/QUANLY/MONS/MON[MAMON="M02"]/TENMON')
print("\n8. Tên món M02:", [m.text for m in ten_m02])

# 9. Ngày lập HD03
ngay_hd03 = tree.xpath('/QUANLY/HOADONS/HOADON[SOHD="HD03"]/NGAYLAP')
print("\n9. Ngày lập HD03:", [d.text for d in ngay_hd03])

# 10. Mã món trong HD01
mamon_hd01 = tree.xpath('/QUANLY/HOADONS/HOADON[SOHD="HD01"]/CTHDS/CTHD/MAMON')
print("\n10. Mã món HD01:", [m.text for m in mamon_hd01])

# 11. Tên món trong HD01
ten_mon_hd01 = tree.xpath('/QUANLY/MONS/MON[MAMON=/QUANLY/HOADONS/HOADON[SOHD="HD01"]/CTHDS/CTHD/MAMON]/TENMON')
print("\n11. Tên món HD01:", [m.text for m in ten_mon_hd01])

# 12. Tên NV lập HD02
ten_nv_hd02 = tree.xpath('/QUANLY/NHANVIENS/NHANVIEN[MANV=/QUANLY/HOADONS/HOADON[SOHD="HD02"]/MANV]/TENV')
print("\n12. Tên NV lập HD02:", [n.text for n in ten_nv_hd02])

# 13. Đếm số bàn
count_ban = tree.xpath("count(/QUANLY/BANS/BAN)")
print("\n13. Tổng số bàn:", int(count_ban))

# 14. Đếm số hóa đơn lập bởi NV01
count_hd_nv01 = tree.xpath('count(/QUANLY/HOADONS/HOADON[MANV="NV01"])')
print("\n14. Số HD lập bởi NV01:", int(count_hd_nv01))

# 15. Tên tất cả món trong HD bàn số 2
ten_mon_b2 = tree.xpath('/QUANLY/MONS/MON[MAMON=/QUANLY/HOADONS/HOADON[SOBAN="2"]/CTHDS/CTHD/MAMON]/TENMON')
print("\n15. Tên món bàn số 2:", [m.text for m in ten_mon_b2])

# 16. Nhân viên lập HD bàn số 3
nv_b3 = tree.xpath('/QUANLY/NHANVIENS/NHANVIEN[MANV=/QUANLY/HOADONS/HOADON[SOBAN="3"]/MANV]')
print("\n16. NV lập HD bàn số 3:")
for n in nv_b3:
    print(n.find("TENV").text)

# 17. Hóa đơn do NV nữ lập
hd_nu = tree.xpath('/QUANLY/HOADONS/HOADON[MANV=/QUANLY/NHANVIENS/NHANVIEN[GIOITINH="NU"]/MANV]')
print("\n17. HD do NV nữ lập:")
for h in hd_nu:
    sohd = h.find("SOHD").text
    print(sohd)

# 18. Nhân viên phục vụ bàn số 1
nv_b1 = tree.xpath('/QUANLY/NHANVIENS/NHANVIEN[MANV=/QUANLY/HOADONS/HOADON[SOBAN="1"]/MANV]')
print("\n18. NV phục vụ bàn số 1:")
for n in nv_b1:
    print(n.find("TENV").text)

# 19. Món gọi >1 lần
mon_nhieu = tree.xpath('/QUANLY/MONS/MON[MAMON=/QUANLY/HOADONS/HOADON/CTHDS/CTHD[number(SOLUONG)>1]/MAMON]/TENMON')
print("\n19. Món gọi >1 lần:")
for m in mon_nhieu:
    print(m.text)

# 20. Tên bàn + ngày lập HD02
ngay_hd02 = tree.xpath('/QUANLY/HOADONS/HOADON[SOHD="HD02"]/NGAYLAP')
ten_ban_hd02 = tree.xpath('/QUANLY/BANS/BAN[SOBAN=/QUANLY/HOADONS/HOADON[SOHD="HD02"]/SOBAN]/TENBAN')
print("\n20. Ngày lập HD02:", [d.text for d in ngay_hd02])
print("Tên bàn HD02:", [b.text for b in ten_ban_hd02])
