import json


def main() -> None:
    with open('./Materialien/books.json') as book_file:
        data = json.load(book_file)

        print(data[0])


if __name__ == '__main__':
    main()
