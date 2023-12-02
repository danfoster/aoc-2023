import os


def get_input_dir() -> str:
    path = os.path.abspath(__file__)
    path = f"{path}/../../../inputs/"
    return os.path.abspath(path)


def read_file(filename: str) -> str:
    with open(os.path.join(get_input_dir(), filename), "r") as file:
        return file.read()
