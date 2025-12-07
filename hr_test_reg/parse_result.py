# 解析result.bin文件，输出测试结果
import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

RESULT_FILE_PATH = "hr_test_reg/result.bin"


def parse_results_detailed():
    """解析result.bin文件并按行输出结果 - 带Test前缀版本"""
    try:
        if not os.path.exists(RESULT_FILE_PATH):
            print(f"{Fore.RED}Error: result.bin file not found!{Style.RESET_ALL}")
            return False

        with open(RESULT_FILE_PATH, "rb") as f:
            results = f.read()

        if not results:
            print(f"{Fore.YELLOW}Warning: result.bin is empty!{Style.RESET_ALL}")
            return False

        print(f"\n{Fore.CYAN}=============== TEST RESULTS (DETAILED) ==============={Style.RESET_ALL}")
        print(f"{Fore.CYAN}Total tests: {len(results)}{Style.RESET_ALL}\n")

        success_count = 0
        for i, result_byte in enumerate(results):
            test_number = i + 1
            if result_byte == ord('1'):
                print(f"Test {test_number:2d}: {Fore.GREEN}√{Style.RESET_ALL}")
                success_count += 1
            elif result_byte == ord('0'):
                print(f"Test {test_number:2d}: {Fore.RED}×{Style.RESET_ALL}")
            else:
                print(f"Test {test_number:2d}: {Fore.YELLOW}?{Style.RESET_ALL}")

        print(f"\n{Fore.CYAN}=============== SUMMARY ==============={Style.RESET_ALL}")
        print(f"Successful tests: {Fore.GREEN}{success_count}{Style.RESET_ALL}")
        print(f"Failed tests: {Fore.RED}{len(results) - success_count}{Style.RESET_ALL}")
        print(f"Success rate: {Fore.CYAN}{success_count / len(results) * 100:.1f}%{Style.RESET_ALL}")

        return True

    except IOError as e:
        print(f"{Fore.RED}Error reading result file: {e}{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")
        return False


def parse_results_simple():
    """解析result.bin文件并按行输出结果 - 简洁版本"""
    try:
        if not os.path.exists(RESULT_FILE_PATH):
            print(f"{Fore.RED}Error: result.bin file not found!{Style.RESET_ALL}")
            return False

        with open(RESULT_FILE_PATH, "rb") as f:
            results = f.read()

        if not results:
            print(f"{Fore.YELLOW}Warning: result.bin is empty!{Style.RESET_ALL}")
            return False

        print(f"\n{Fore.CYAN}=============== TEST RESULTS ==============={Style.RESET_ALL}")
        print(f"{Fore.CYAN}Total tests: {len(results)}{Style.RESET_ALL}\n")

        success_count = 0
        for i, result_byte in enumerate(results):
            if result_byte == ord('1'):
                print(f"{Fore.GREEN}√{Style.RESET_ALL}")
                success_count += 1
            elif result_byte == ord('0'):
                print(f"{Fore.RED}×{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}?{Style.RESET_ALL}")

        print(f"\n{Fore.CYAN}=============== SUMMARY ==============={Style.RESET_ALL}")
        print(f"Successful tests: {Fore.GREEN}{success_count}{Style.RESET_ALL}")
        print(f"Failed tests: {Fore.RED}{len(results) - success_count}{Style.RESET_ALL}")
        print(f"Success rate: {Fore.CYAN}{success_count / len(results) * 100:.1f}%{Style.RESET_ALL}")

        return True

    except IOError as e:
        print(f"{Fore.RED}Error reading result file: {e}{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")
        return False


if __name__ == '__main__':
    parse_results_detailed()
    parse_results_simple()
