def test_fun(arg1: str) -> str:
    arg1
    return "Ok"


def main() -> None:
    print(test_fun("My arg"))


if __name__ == "__main__":
    main()
