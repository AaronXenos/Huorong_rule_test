# 测试创建同名项权限
import winreg
from colorama import init, Fore, Style

from utils import record_result

init(autoreset=True)
import os

CASEINDEX = int(os.path.basename(__file__).split('.')[0])


def testcase(hive, key_path):
    try:
        with winreg.CreateKeyEx(hive, key_path, access=winreg.KEY_CREATE_SUB_KEY) as _:
            pass
        print(f"{Fore.BLUE}Registry key created '{key_path}'.{Style.RESET_ALL}")
        return True
    except PermissionError:
        print(f"{Fore.RED}Permission denied to create registry key '{key_path}'.{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"{Fore.RED}Failed to create registry key '{key_path}': {e}{Style.RESET_ALL}")
        exit(-1)


if __name__ == '__main__':
    res = testcase(winreg.HKEY_CLASSES_ROOT, r"test\name1")
    record_result(CASEINDEX - 1, res)
