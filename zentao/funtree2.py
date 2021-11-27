from openpyxl import load_workbook

wb = load_workbook('functree2.xlsx')
sheet = wb.active
# a1 = sheet['a1'].value
# print(a1)
# print(sheet.cell(4,3).value)

i = 2
j = 1

to_copy = ""


def findrow(all_row, all_col):
    for col in range(1, all_col + 1):
        to_copy = ""

        for row in range(1, all_row + 1):
            cell = sheet.cell(row, col)
            print(cell.value)
            # print(cell)
            if cell.value is not None:
                to_copy = cell.value
                # print(to_copy,"if")
                to_copy = cell.value

            else:
                cell.value = to_copy
                # print(to_copy,"else")


findrow(28, 6)
wb.save('functree3.xlsx')
wb.close()
