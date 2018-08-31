import datetime
nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
print(nowTime)
nowTime = datetime.datetime.now().strftime('%Y_%m_%d')  # 现在
print(nowTime)
nowTime = datetime.datetime.now().strftime('%Y%m%d')  # 现在
fileName = "d:=d:\sirmpm{0}.dmp".format(nowTime)
print(fileName)
