RESULT_FILE_PATH = "hr_test_reg/result.bin"


def record_result(test_index, success):
    try:
        with open(RESULT_FILE_PATH, "r+b") as f:
            results = bytearray(f.read())
            if 0 <= test_index < len(results):
                results[test_index] = b'1'[0] if success else b'0'[0]
            f.seek(0)
            f.write(results)
    except IOError as e:
        print(f"Error writing to result file: {e}")
