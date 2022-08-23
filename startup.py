import os


def add_to_startup(file_path):
    cmd = '''reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "AotuConnect" /t REG_SZ /d "%s" /f''' % file_path
    os.system(cmd)


def delete_from_startup():
    cmd = '''reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "AotuConnect" /f'''
    os.system(cmd)
