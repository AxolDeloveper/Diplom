import random


class Domain:
    def __init__(self):
        self.__max_length = 8
        self.res = self.__generate_domain(50)

    def __generate_domain(self, lenght: int):
        nums = '0123456789'
        words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        special_symbols = '_*()$#№@'

        super_str = ''.join(nums + words + special_symbols)

        res = []
        for key in range(lenght):
            res.append(
                random.choice(super_str)
            )

        return ''.join(res)

    def __str__(self):
        return self.res

if __name__ == '__main__':
    test = Domain()