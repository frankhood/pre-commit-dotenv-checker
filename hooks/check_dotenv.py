import sys
import argparse
from typing import Optional, Sequence

CRED = "\33[31m"
# CGREEN = "\33[32m"
CYELLOW = "\33[33m"
# CBLUE = "\33[34m"
# CVIOLET = "\33[35m"
# CBEIGE = "\33[36m"
CEND = '\033[0m'


def get_variables_list(filecontent, filename):
    global HAS_ERRORS
    file_variables = []
    for line in filecontent:
        if line != "\n":
            if "=" in line:
                if not line.startswith("#"):
                    variable = line.split("=")[0]
                    file_variables.append(variable)
                    try:
                        value = line.split("=")[1]
                        if value != "\n":
                            if "#" in value:
                                print(f"{CRED}[ERROR] There is a # in {variable} value from {filename}, this is an error!!{CEND}")
                                HAS_ERRORS = True
                        else:
                            print(f"{CYELLOW}[WARNING] No value assigned to {variable} in {filename}{CEND}")    
                    except IndexError:
                        print(f"{CYELLOW}[WARNING] No value assigned to {variable} in {filename}{CEND}")
    return file_variables


def main(argv: Optional[Sequence[str]] = None) -> int:
    print("ARGV => ", sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from-file", type=str, help="Choose from which file do you want to make a diff", required=True
    )
    parser.add_argument(
        "--to-file", type=str, help="Choose to which file do you want to make a diff", required=True
    )
    args = parser.parse_args(argv)
    print("ARGS => ", args)
    print("ARGS DICT => ", args.__dict__)

    FROM_ENV_FILE = args.from_file
    TO_ENV_FILE = args.to_file

    with open(FROM_ENV_FILE) as from_env_file:
        from_file_content = from_env_file.readlines()

    with open(TO_ENV_FILE) as to_env_file:
        to_file_content = to_env_file.readlines()

    HAS_ERRORS = False

    from_variables = set(get_variables_list(from_file_content, FROM_ENV_FILE))
    to_variables = set(get_variables_list(to_file_content, TO_ENV_FILE))

    if HAS_ERRORS:
        return 1

    elements_not_in_to_file = from_variables - to_variables

    HAS_DIFF_ERORRS = False
    if elements_not_in_to_file:
        HAS_DIFF_ERORRS = True
        print(f"{CRED}[ERROR] Some of the variables present in your {FROM_ENV_FILE} are not present in your {TO_ENV_FILE}. Copy and enter a value to the following variables:{CEND}")
        for idx, element in enumerate(elements_not_in_to_file, 1):
            print(f"\t{CRED}{idx}. {element}{CEND}")

    if HAS_DIFF_ERORRS:
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
