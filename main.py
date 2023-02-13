from random import randint
import time
import functools
import pwinput


def timer(func):  # декоратор таймер
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} заняло {runtime:.4f} секунд")
        return result

    return _wrapper


def alph_gen() -> list:  # генератор алфавита для паролей
    alph = []
    for i in range(65, 91):
        alph.append(chr(i)) # Заглавные английские

    for i in range(1072, 1104):
        alph.append(chr(i)) # Прописные русские
    print(len(alph))
    return alph


def passw_gen(alph) -> str:  # генератор пароля при помощи алфавита и с изменением символов
    passw = [0, 0, 0, 0]
    passwrd = []
    passwT = []

    for i in range(4):
        passw[i] = randint(0, len(alph) - 1)
    for i in passw:
        passwT += alph[i]
    print("Password is ", passwT)
    if True:
        passw[0] = (passw[1] + 1) % len(alph)
        passw[1] = passw[2] - 1 if passw[2] - 1 >= 0 else len(alph) - 1
        passw[2] = round((passw[2] + passw[1]) / 2) - 1 if round((passw[2] + passw[1]) / 2) - 1 >= 0 else len(alph) - 1
        passw[3] = passw[0] - 1 if passw[0] - 1 >= 0 else len(alph) - 1
    for i in passw:
        passwrd += alph[i]
    passwrd = "".join(passwrd)
    print("Another password is ", passwrd)
    return passwrd


@timer
def pass_brut(alph, passw) -> str:  # прямой перебор паролей
    mbPassw = []
    for i in range(4):
        mbPassw.append(alph[0])

    char = [0, 0, 0, 0]
    width = len(alph)
    while mbPassw != list(passw):
        char[0] += 1
        if char[0] == width:
            char[1] += 1
            char[0] = 0
            if char[1] == width:
                char[2] += 1
                char[1] = 0
                if char[2] == width:
                    char[3] += 1
                    char[2] = 0

        for i in range(4):
            mbPassw[i] = alph[char[i]]
        print(mbPassw)
    return str(mbPassw)


def main():
    alph = alph_gen()
    passw = passw_gen(alph)
    bruted = pass_brut(alph, passw)
    print("Начальный пароль", passw)
    print("Брутед пароль", bruted)

    password = pwinput.pwinput()  # работает при запуске через консоль
    print(password)

    if password == passw:
        print("Login confirm")
    else:
        print("Denied")


if __name__ == "__main__":
    main()
