# 测试读取键默认值
import winreg
from colorama import init, Fore, Style

from utils import record_result

init(autoreset=True)
import os

CASEINDEX = int(os.path.basename(__file__).split('.')[0])


def testcase(hive, key_path):
    try:
        with winreg.OpenKey(hive, key_path, 0, winreg.KEY_QUERY_VALUE) as key:
            value = winreg.QueryValue(key, "")
            print(f"{Fore.BLUE}Default value of '{key_path}': {value}{Style.RESET_ALL}")
        return True
    except PermissionError:
        print(f"{Fore.RED}Permission denied to read default value from '{key_path}'.{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"{Fore.RED}Failed to read default value from '{key_path}': {e}{Style.RESET_ALL}")
        exit(-1)


if __name__ == '__main__':
    res = testcase(winreg.HKEY_CLASSES_ROOT, r"test\name1")
    record_result(CASEINDEX - 1, res)
