<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>

<xsl:template match="/">
<html>
<head>
    <title>Quản lý bàn ăn</title>
    <style>
    body { font-family: Arial, sans-serif; margin: 30px; }
    table { 
        border-collapse: collapse; 
        width: 80%; 
        margin: 0 auto 30px auto; /* căn giữa */
        background-color: #cce7ff;   /* nền xanh nhạt */
    }
   th, td { 
    border: 1px solid #bde2a3ff; 
    padding: 6px 10px; 
    text-align: left; 
      background-color: #cce7ff;   /* nền xanh nhạt */
}
th { background-color: #a2f2f1ff; } /* vẫn giữ thẻ th khác màu nhạt */

    h2 { color: #cf86bcff; margin-top: 40px; text-align: center; }
    .result {
    background-color: #ffe4e1; /* hồng nhạt */
    padding: 10px 15px;
    border-radius: 8px;
    width: 50%;
    margin: 0 auto 20px auto; /* căn giữa */
    font-weight: bold;
    text-align: center;
    box-shadow: 1px 1px 4px #ccc;
}
</style>

</head>
<body>
<h1 style="text-align: center; color: #2a4d7a; text-shadow: 2px 2px 4px #aaa; margin-bottom: 40px;font-family: 'Arial', sans-serif;font-size: 36px;">Kết quả truy vấn bài Quản Lý Bàn Ăn</h1>

<h2>1. Danh sách tất cả các bàn</h2>
<table>
<tr><th>STT</th><th>Số bàn</th><th>Tên bàn</th></tr>
<xsl:for-each select="QUANLY/BANS/BAN">
<tr>
  <td><xsl:number/></td>
  <td><xsl:value-of select="SOBAN"/></td>
  <td><xsl:value-of select="TENBAN"/></td>
</tr>
</xsl:for-each>
</table>

<h2>2. Danh sách các nhân viên</h2>
<table>
<tr><th>STT</th><th>Mã NV</th><th>Tên NV</th><th>Giới tính</th><th>Địa chỉ</th></tr>
<xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN">
<tr>
  <td><xsl:number/></td>
  <td><xsl:value-of select="MANV"/></td>
  <td><xsl:value-of select="TENV"/></td>
  <td><xsl:value-of select="GIOITINH"/></td>
  <td><xsl:value-of select="DIACHI"/></td>
</tr>
</xsl:for-each>
</table>

<h2>3. Danh sách các món ăn</h2>
<table>
<tr><th>STT</th><th>Mã món</th><th>Tên món</th><th>Giá</th></tr>
<xsl:for-each select="QUANLY/MONS/MON">
<tr>
  <td><xsl:number/></td>
  <td><xsl:value-of select="MAMON"/></td>
  <td><xsl:value-of select="TENMON"/></td>
  <td><xsl:value-of select="GIA"/></td>
</tr>
</xsl:for-each>
</table>

<h2>4. Thông tin nhân viên NV02</h2>
<table>
<tr><th>Mã NV</th><th>Tên NV</th><th>Giới tính</th><th>Địa chỉ</th></tr>
<xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']">
<tr>
  <td><xsl:value-of select="MANV"/></td>
  <td><xsl:value-of select="TENV"/></td>
  <td><xsl:value-of select="GIOITINH"/></td>
  <td><xsl:value-of select="DIACHI"/></td>
</tr>
</xsl:for-each>
</table>

<h2>5. Danh sách món có giá &gt; 50,000</h2>
<table>
<tr><th>STT</th><th>Tên món</th><th>Giá</th></tr>
<xsl:for-each select="QUANLY/MONS/MON[GIA &gt; 50000]">
<tr>
  <td><xsl:number/></td>
  <td><xsl:value-of select="TENMON"/></td>
  <td><xsl:value-of select="GIA"/></td>
</tr>
</xsl:for-each>
</table>

<h2>6. Thông tin hóa đơn HD03</h2>
<table>
<tr><th>Tên NV</th><th>Số bàn</th><th>Ngày lập</th><th>Tổng tiền</th></tr>
<xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD03']">
<tr>
  <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=current()/MANV]/TENV"/></td>
  <td><xsl:value-of select="SOBAN"/></td>
  <td><xsl:value-of select="NGAYLAP"/></td>
  <td><xsl:value-of select="TONGTIEN"/></td>
</tr>
</xsl:for-each>
</table>

<h2>7. Tên các món trong hóa đơn HD02</h2>
<table>
<tr><th>STT</th><th>Tên món</th></tr>
<xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD02']/CTHDS/CTHD">
<tr>
  <td><xsl:number/></td>
  <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/></td>
</tr>
</xsl:for-each>
</table>

<h2>8. Tên nhân viên lập hóa đơn HD02</h2>
<p class="result">
<xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=/QUANLY/HOADONS/HOADON[SOHD='HD02']/MANV]/TENV"/>
</p>

<h2>9. Số bàn hiện có</h2>
<p class="result"><xsl:value-of select="count(QUANLY/BANS/BAN)"/></p>

<h2>10. Số hóa đơn lập bởi NV01</h2>
<p class="result"><xsl:value-of select="count(QUANLY/HOADONS/HOADON[MANV='NV01'])"/></p>

<h2>11. Các món từng bán cho bàn số 2</h2>
<table>
<tr><th>STT</th><th>Tên món</th></tr>
<xsl:for-each select="QUANLY/HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD">
<tr>
  <td><xsl:number/></td>
  <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/></td>
</tr>
</xsl:for-each>
</table>

<h2>12. Nhân viên từng lập hóa đơn cho bàn số 3</h2>
<table>
<tr><th>STT</th><th>Tên nhân viên</th></tr>
<xsl:for-each select="QUANLY/HOADONS/HOADON[SOBAN='3']">
<tr>
  <td><xsl:number/></td>
  <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=current()/MANV]/TENV"/></td>
</tr>
</xsl:for-each>
</table>

<h2>13. Chi tiết hóa đơn HD04</h2>
<table>
<tr><th>Mã món</th><th>Tên món</th><th>Đơn giá</th><th>Số lượng</th><th>Tiền</th></tr>
<xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD04']/CTHDS/CTHD">
<tr>
  <td><xsl:value-of select="MAMON"/></td>
  <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/></td>
  <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/GIA"/></td>
  <td><xsl:value-of select="SOLUONG"/></td>
  <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/GIA * SOLUONG"/></td>
</tr>
</xsl:for-each>
</table>

</body>
</html>
</xsl:template>
</xsl:stylesheet>
