import argparse
import json
import sys
import os

if __name__ == "__main__":
    filepath = os.path.realpath(__file__)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--nachricht",
        type=str,
        default="Keine nachricht vorhanden",
        help="'Schreib eine Nachricht...'",
        required=False,
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        default=filepath,
        help="'pfad zur datei angeben'",
    )
    parser.add_argument(
        "-j",
        "--json",
        type=json.loads,
        help="{key:value}",
    )
    arguments = parser.parse_args()
    for arg in vars(arguments):
        if arg == "json":
            print(f"json: {json.dumps(getattr(arguments, arg), indent=4)}")
            continue
        print(f"{arg}: {getattr(arguments, arg)}")
