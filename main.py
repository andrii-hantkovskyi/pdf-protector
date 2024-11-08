from secrets import token_urlsafe

from pypdf import constants, PdfWriter, PdfReader

out = PdfWriter()
file = PdfReader("input.pdf")

num = len(file.pages)
  
for idx in range(num):
    page = file.pages[idx] 
    out.add_page(page)
  
password = token_urlsafe(16)

out.encrypt(user_password='', owner_password=password, permissions_flag=constants.UserAccessPermissions.PRINT)

with open("output.pdf", "wb") as f:
    out.write(f)
