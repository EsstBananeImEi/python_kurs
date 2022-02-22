import os
import subprocess
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-name", "--name", type=str, default="hello")
    parser.add_argument("-env", "--enviroment", type=str, default="development")
    arguments = parser.parse_args()

    os.environ["FLASK_ENV"] = arguments.enviroment
    os.environ["FLASK_APP"] = arguments.name

    subprocess.call(["flask", "run"])
