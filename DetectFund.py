"""
任务目标：爬取每日基金净值，保存到本地Excel中
"""


# 配置文件类
class Config:
    def __init__(self):
        return

    # 判断是否存在一个配置文件，如果有就加载，没有就为我新建一个后退出程序
    def existConfig(self):
        return

    # 创建一个配置文件
    def newConfig(self):
        return

    # 读取配置文件中的时间，判断今日是否已经执行过程序
    def readTime(self):
        return

    # 程序运行结束前，将今日时间写入配置文件
    def writeTime(self):
        return

    # 读取配置文件中所有需要爬取的基金id，返回列表
    def readFundList(self):
        return


# 爬取功能类
class CrawlUtil:
    def __init__(self):
        return

    # 依据基金列表爬取数据，返回(基金名称，净值数据)元组组成的列表
    def getFundInfo(self):
        return


# Excel对象类
class ExcelObject:
    def __init__(self):
        return

    # 判断是否存在一个Excel，如果有就加载，没有就新建
    def existExcel(self):
        return

    # 判断加载的Excel是空的还是已经有数据的
    def judgeExcel(self):
        return

    # 向Excel中插入数据
    def insertValue(self):
        return

    # 向Excel中插入平均值公式
    def insertAvgForm(self):
        return

    # 依据某一行的字符个数去调整数据表的列宽
    def adjustColWidth(self):
        return

    # 保存Excel
    def saveExcel(self):
        return


# 打印log信息到文件
class PrintLog:
    def __init__(self):
        return
