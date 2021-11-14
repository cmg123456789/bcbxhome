# import a
# import importlib
# # from a import _get_list
#
#
#
# result = a.get_list(30, 50)
# print(result)
#
# importlib.reload(a)
#
# a = a.showmyself('cmg', 身高 ='1米8')
# print(a)

# a = {'ip':'127.0.0.1','port':'6379'}
# print ('ip为：%s'%a['ip'])


#-------网吧欢迎语--------
# name = input('请输入您的姓名：')
# print('%s您好，欢迎您来到绿树林网咖'%name)
#
# area_list = {'大厅':10,'包间':20,'对战席':25}
# print('我们的区域每小时价格是%s'%list(area_list.items()))
# area = input('请输入你要上网的区域：')
#
# time = input('请您输入上机时长（小时）：')
#
# print('谢谢您，系统已为您安排在%s区域，上机时长%d小时，共计%d元，祝您玩的开心！'\
#       %(area,float(time),float(float(area_list[area])*float(time))))


from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.bcbxhome.com')



















