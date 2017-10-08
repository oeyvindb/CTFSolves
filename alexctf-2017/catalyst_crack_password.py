from struct import pack

password = ""

password += pack('<I', (6833993 + 0x55EB052A) & 0xffffffff)
password += pack('<I', (1732044087 + 0x0EF76C39)& 0xffffffff)
password += pack('<I', (2068121063 + 0xCC1E2D64)& 0xffffffff)
password += pack('<I', (1889579618 + 0xC7B6C6F5)& 0xffffffff)
password += pack('<I', (869606716 + 0x26941BFA)& 0xffffffff)
password += pack('<I', (1364883061 + 0x260CF0F3)& 0xffffffff)
password += pack('<I', (1500347741 + 0x10D4CAEF)& 0xffffffff)
password += pack('<I', (2094174281 + 0x0C666E824)& 0xffffffff)
password += pack('<I', (1508322742 + 0x0FC89459C)& 0xffffffff)
password += pack('<I', (1179934733 + 0x2413073A)& 0xffffffff)

print "The password consist of %d characters" % len(password) 
print password