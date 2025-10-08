import pytest

def run_tests():
    exit_code = pytest.main(["test_working.py"])
    print(f"pytest exit code: {exit_code}")

if __name__ == "__main__":
    run_tests()
