import urllib.request
import configparser
import openpyxl
import datetime

# cf = configparser.ConfigParser();
# cf.read("D:/test.ini");
# se = cf.sections();
#
# op = cf.options(se[0]);
#
# its = cf.items(se[0]);
#
# value = cf.get(se[0],op[0]);
#
# print("key1" in cf.options("task"));

# try:
#     wb = openpyxl.load_workbook("FundInfo.xlsx");
#     ws = wb["Sheet"];
#     print(datetime.datetime.now().strftime("%Y"));
#     ws["A1"] = datetime.datetime.now().strftime("%F");
#     wb.save("FundInfo.xlsx");
# except Exception as e:
#     print(e);
#     wb = openpyxl.Workbook();
#     ws = wb.active;
#     ws.append([1,2,3]);
#     ws.append([4,5,6]);
#     wb.save("FundInfo.xlsx");

time = datetime.datetime.now();

t = time.strftime("%F");

# print(time.strftime("%S"))
print(t);