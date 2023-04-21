import string
from random import shuffle, randint
from secrets import choice, randbelow


def standart_password_generator(password_length: int = 8, password_count: int = 1, add_uppercase: bool = True,
                                add_numbers: bool = False, add_symbols: bool = False,
                                add_specific_symbols: bool = False,
                                remove_duplicates: bool = False):
    symbols = '%$#@!?&'
    specific_symbols = '()*+./:;=>?@[\]^`{|}~'
    output_password = []
    output_password_list = []

    for i in range(password_count):
        for j in range(password_length):
            output_password.append(choice(string.ascii_lowercase))

        if add_uppercase:
            for k in range(password_length // randint(2, 3)):
                output_password[randbelow(password_length - 1)] = choice(string.ascii_uppercase)

        if add_numbers:
            for k in range(password_length // randint(3, 5)):
                output_password[randbelow(password_length - 1)] = choice(string.digits)

        if add_symbols:
            for k in range(password_length // randint(3, 5)):
                output_password[randbelow(password_length - 1)] = choice(symbols)

        if add_specific_symbols:
            for k in range(password_length // randint(5, 8)):
                output_password[randbelow(password_length - 1)] = choice(specific_symbols)

        if remove_duplicates:
            k = 0
            while k != password_length - 2:
                if output_password.count(output_password[k]) > 1:
                    rchar = choice(string.ascii_letters)
                    if (rchar.lower() not in output_password) and (rchar.upper() not in output_password):
                        ind = output_password.index(output_password[k])
                        output_password.remove(output_password[k])
                        output_password.insert(ind, rchar)
                    else:
                        continue
                k += 1

        shuffle(output_password)
        output_password_list.append(''.join(output_password))
        output_password.clear()

    return output_password_list


def XKCD_password_generator(password_length: int, password_count: int,
                            word_list: str):

    with open('dicts\\' + word_list, encoding='utf-8') as file:
        lines = file.readlines()

    output_password = []
    output_password_list = []

    for i in range(password_count):
        for j in range(password_length):
            output_password.append(choice(lines).strip())

        output_password_list.append(str('_'.join(output_password)))
        output_password.clear()

    return output_password_list

