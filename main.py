if __name__ == "__main__":
    '''star pattern algorithms'''

    def basic_pattern_algo(rows: int) -> None:
        '''
        *
        **
        ***
        '''
        for stars in range(1, rows):
            print("*"*stars)

    basic_pattern_algo(10)
