
import os


def is_file(func):
    def check_file(file):
        if os.path.isfile(file):
            return func(file)
        else:
            print(f"Die Datei {file} existiert nicht!!")

    return check_file

@is_file
def read_file(file) -> None:
    with open(file, "r", encoding="utf8") as file:
        print(file.read())

if __name__ == "__main__":
    read_file("../../Materialien/meal.txt")
