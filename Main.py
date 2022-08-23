import json
import sys
from os.path import dirname, realpath
from sys import executable
from startup import *
from request_command import check_data

curpath = dirname(realpath(executable))
path = dirname(realpath(executable)) + r'\user_info.json'

print('------Menu------')
print('1. 安装')
print('2. 卸载')
print('3. 退出')
while True:
    UserInput = input('请输入(1,2,3):\n')
    if UserInput == '1':
        data = json.load(open('user_info.json'))
        print('\n深圳技术大学学生宿舍校园网')
        while True:
            data['user'] = input('请输入账号:\n').split()
            data['pwd'] = input('请输入密码:\n').split()
            json.dump(data, open(curpath + r'\user_info.json', 'w'))
            if check_data():
                break
            else:
                print('账号密码错误!')
        file_path = curpath + r'\AutoConnect.exe'
        add_to_startup(file_path)
        print('设置自启动成功\n')
        input('按任意键继续...')
        break
    elif UserInput == '2':
        delete_from_startup()
        print('删除成功')
        input('按任意键继续...')
        break
    elif UserInput == '3':
        sys.exit(0)
    else:
        print('输入错误!请重新输入')
