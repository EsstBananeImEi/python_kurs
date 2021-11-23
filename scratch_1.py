def division(zahl1, zahl2) -> None:
    try:
        result = zahl1 / zahl2
        [print(e[o]) in []]
        return result
    except ZeroDivisionError as error:
        print(error)
    except Exception as error_2:
        print(error_2)

if __name__ == "__main__":
    division(2,3)
    print("wieter")