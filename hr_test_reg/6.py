# 测试读取键其他值
import winreg
from colorama import init, Fore, Style

from utils import record_result

init(autoreset=True)
import os

CASEINDEX = int(os.path.basename(__file__).split('.')[0])


def testcase(hive, key_path, value_name):
    try:
        with winreg.OpenKey(hive, key_path, 0, winreg.KEY_QUERY_VALUE) as key:
            value, value_type = winreg.QueryValueEx(key, value_name)
            print(f"{Fore.BLUE}Value '{value_name}' of '{key_path}': {value} (Type: {value_type}){Style.RESET_ALL}")
        return True
    except PermissionError:
        print(f"{Fore.RED}Permission denied to read value '{value_name}' from '{key_path}'.{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"{Fore.RED}Failed to read value '{value_name}' from '{key_path}': {e}{Style.RESET_ALL}")
        exit(-1)


if __name__ == '__main__':
    res = testcase(winreg.HKEY_CLASSES_ROOT, r"test\name1", "v2read")
    record_result(CASEINDEX - 1, res)
