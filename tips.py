from win11toast import toast


def tip():
    icon = {
        'src': r'C:\Users\11924\PycharmProjects\RequestsConnect\深圳技术大学校徽.ico',
        'placement': 'appLogoOverride'
    }
    toast('SZTU自动联网', '连接成功', icon=icon, duration='short')
