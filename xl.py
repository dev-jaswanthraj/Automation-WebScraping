from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter




class XlDataBase():
    __user_fields = ["FullName", "UserName", "Password"]
    __total_user = 2
    __workbook_created = False
    __worksheet_created = False
    def __init__(self) -> None:
        if not XlDataBase.__workbook_created:
            self.wb = Workbook()
            self.__workbook_created = True
        else:
            self.wb = load_workbook("userdata.xlsx")

    def set_worksheet(self):
        if not XlDataBase.__worksheet_created:
            self.ws = self.wb.active
            self.ws.title = "User Detail"
            self.ws.append(XlDataBase.__user_fields)
            self.wb.save("userdata.xlsx")

    def set_data(self, fullname:str, password:str):
        self.username = "User"+str(XlDataBase.__total_user-1)
        self.ws['A'+str(XlDataBase.__total_user-1)] = fullname
        self.ws['B'+str(XlDataBase.__total_user-1)] = self.username
        self.ws['C'+str(XlDataBase.__total_user-1)] = password
        self.wb.save("userdata.xlsx")
        XlDataBase.__total_user += 1
        return self.username






# # wb = Workbook()
# wb = load_workbook("User Database.xlsx")
# worksheet = wb.active

# for row in range(1, 14):

#     for col in range(1, 3):

#         char = get_column_letter(col)

#         print(worksheet[char + str(row)].value, end = " | ")
    
#     print()








# # worksheet.title = "User Details"
# # worksheet.append(['Name', 'Password'])

# # wb.save("User Database.xlsx")
