import gspread

sa = gspread.service_account(filename='timesheet-385217-1e290f31c340.json')
sh = sa.open("trackingStudy")

wks = sh.worksheet("Sheet1")

wks.update('A1','subject')