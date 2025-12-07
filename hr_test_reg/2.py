# 测试创建同名值权限
import winreg
from colorama import init, Fore, Style

from utils import record_result

init(autoreset=True)
import os

CASEINDEX = int(os.path.basename(__file__).split('.')[0])


def testcase(hive, subkey, value_name, value, value_type=winreg.REG_SZ):
    try:
        with winreg.OpenKey(hive, subkey, 0, winreg.KEY_SET_VALUE) as key:
            if value_name is None or value_name == "":
                winreg.SetValue(key, '', value_type, value)
            else:
                winreg.SetValueEx(key, value_name, 0, value_type, value)
        print(f"{Fore.BLUE}Registry value set '{value_name}' to '{value}'.{Style.RESET_ALL}")
        return True
    except PermissionError:
        print(f"{Fore.RED}Permission denied to create registry key '{subkey}'.{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"{Fore.RED}Failed to create registry key '{subkey}': {e}{Style.RESET_ALL}")
        exit(-1)


if __name__ == '__main__':
    res = testcase(winreg.HKEY_CLASSES_ROOT, r"test", "name1", "name1 is value")
    record_result(CASEINDEX - 1, res)
