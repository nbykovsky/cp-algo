import os
import sys

import pytest
from _pytest.config import ExitCode

file_path = sys.argv[1]
file_name = os.path.basename(file_path)
is_test_file = file_name.startswith("test_")
if not is_test_file:
    file_path = file_path.replace("/main/", "/test/").replace(f"/{file_name}", f"/test_{file_name}")
output = pytest.main([file_path])
if output == ExitCode.TESTS_FAILED:
    sys.exit(1)
