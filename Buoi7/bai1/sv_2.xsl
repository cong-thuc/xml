<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>

<xsl:template match="/">
<html>
<head>
    <title>Danh sách sinh viên</title>
 
    <style>
    body { font-family: Arial, sans-serif; margin: 30px; }
    table { 
        border-collapse: collapse; 
        width: 80%; 
        margin: 0 auto 30px auto; /* căn giữa */
        background-color: #8eb0ceff;   /* nền xanh nhạt */
    }
   th, td { 
    border: 1px solid #bde2a3ff; 
    padding: 6px 10px; 
    text-align: left; 
    background-color: #8eb0ceff;   /* nền xanh nhạt */
}
th { background-color: #a2f2f1ff; } /* vẫn giữ thẻ th khác màu nhạt */

    h2 { color: #cf86bcff; margin-top: 40px; text-align: center; }
    </style>
    
</head>
<body>

<h2>1. Danh sách sinh viên (Mã &amp; Họ tên)</h2>
<table>
  <tr><th>Mã SV</th><th>Họ tên</th></tr>
  <xsl:apply-templates select="school/student" mode="list1"/>
</table>

<h2>2. Danh sách sinh viên sắp xếp theo điểm giảm dần</h2>
<table>
  <tr><th>Mã SV</th><th>Họ tên</th><th>Điểm</th></tr>
  <xsl:for-each select="school/student">
    <xsl:sort select="grade" data-type="number" order="descending"/>
    <tr>
      <td><xsl:value-of select="id"/></td>
      <td><xsl:value-of select="name"/></td>
      <td><xsl:value-of select="grade"/></td>
    </tr>
  </xsl:for-each>
</table>

<h2>3. Danh sách sinh viên sắp xếp theo tháng sinh</h2>
<table>
  <tr><th>STT</th><th>Họ tên</th><th>Ngày sinh</th></tr>
  <xsl:for-each select="school/student">
    <xsl:sort select="substring(date,6,2)" order="ascending"/>
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="name"/></td>
      <td><xsl:value-of select="date"/></td>
    </tr>
  </xsl:for-each>
</table>

<h2>4. Các khóa học có sinh viên học</h2>
<table>
  <tr><th>Khóa học</th></tr>
  <xsl:for-each select="school/course">
    <xsl:variable name="courseId" select="id"/>
    <xsl:if test="/school/enrollment[courseRef=$courseId]">
      <tr><td><xsl:value-of select="name"/></td></tr>
    </xsl:if>
  </xsl:for-each>
</table>



<h2>5. Sinh viên học khóa "Hóa học 201"</h2>
<table>
  <tr><th>STT</th><th>Họ tên</th></tr>
  <xsl:variable name="courseTarget" select="/school/course[name='Hóa học 201']/id"/>
  <xsl:for-each select="/school/enrollment[courseRef=$courseTarget]">
    <xsl:variable name="studentId" select="studentRef"/>
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="/school/student[id=$studentId]/name"/></td>
    </tr>
  </xsl:for-each>
</table>

<h2>6. Sinh viên sinh năm 1997</h2>
<table>
  <tr><th>Mã SV</th><th>Họ tên</th><th>Năm sinh</th></tr>
  <xsl:for-each select="/school/student[starts-with(date, '1997')]">
    <tr>
      <td><xsl:value-of select="id"/></td>
      <td><xsl:value-of select="name"/></td>
      <td><xsl:value-of select="substring(date,1,4)"/></td>
    </tr>
  </xsl:for-each>
</table>

<h2>7. Sinh viên họ “Trần”</h2>
<table>
  <tr><th>STT</th><th>Họ tên</th></tr>
  <xsl:for-each select="/school/student[starts-with(name,'Trần')]">
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="name"/></td>
    </tr>
  </xsl:for-each>
</table>

</body>
</html>
</xsl:template>


<xsl:template match="student" mode="list1">
  <tr>
    <td><xsl:value-of select="id"/></td>
    <td><xsl:value-of select="name"/></td>
  </tr>
</xsl:template>

</xsl:stylesheet>
