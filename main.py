def reverse_pattern_algo(rows: int) -> None:
    for stars in reversed(range(1, rows)):
        print("*"*stars)


def basic_pattern_algo(rows: int) -> None:
    '''
    *
    **
    ***
    '''
    for stars in range(1, rows):
        print("*"*stars)


if __name__ == "__main__":
    basic_pattern_algo(10)
    reverse_pattern_algo(10)
