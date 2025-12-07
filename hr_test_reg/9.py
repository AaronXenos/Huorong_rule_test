# 测试枚举值
import winreg
from colorama import init, Fore, Style

from utils import record_result

init(autoreset=True)
import os

CASEINDEX = int(os.path.basename(__file__).split('.')[0])


def testcase(hive, key_path):
    try:
        with winreg.OpenKey(hive, key_path, 0, winreg.KEY_QUERY_VALUE) as key:
            print(f"{Fore.BLUE}Enumerating values of '{key_path}':{Style.RESET_ALL}")
            i = 0
            while True:
                try:
                    value_info = winreg.EnumValue(key, i)
                    value_name = value_info[0]
                    value_data = value_info[1]
                    value_type = value_info[2]
                    print(f"  - {value_name}: {value_data} (Type: {value_type})")
                    i += 1
                except WindowsError as e:
                    if e.winerror == 259:  # No more items
                        break
                    else:
                        print(f"{Fore.RED}Error enumerating values: {e}{Style.RESET_ALL}")
                        exit(-1)
        return True
    except PermissionError:
        print(f"{Fore.RED}Permission denied to enumerate values of '{key_path}'.{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"{Fore.RED}Failed to enumerate values of '{key_path}': {e}{Style.RESET_ALL}")
        exit(-1)


if __name__ == '__main__':
    res = testcase(winreg.HKEY_CLASSES_ROOT, r"test\name1")
    record_result(CASEINDEX - 1, res)
