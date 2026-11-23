import doctest


def year_word(n: int) -> str:
    """Повертає правильну форму слова "рік" для числа n.

    >>> year_word(1)
    'рік'

    >>> year_word(2)
    'роки'

    >>> year_word(3)
    'роки'

    >>> year_word(4)
    'роки'

    >>> year_word(5)
    'років'

    >>> year_word(10)
    'років'

    >>> year_word(11)
    'років'

    >>> year_word(12)
    'років'

    >>> year_word(13)
    'років'

    >>> year_word(14)
    'років'

    >>> year_word(15)
    'років'

    >>> year_word(20)
    'років'

    >>> year_word(21)
    'рік'

    >>> year_word(22)
    'роки'

    >>> year_word(23)
    'роки'

    >>> year_word(24)
    'роки'

    >>> year_word(25)
    'років'

    >>> year_word(31)
    'рік'

    >>> year_word(32)
    'роки'

    >>> year_word(41)
    'рік'

    >>> year_word(52)
    'роки'

    >>> year_word(101)
    'рік'

    >>> year_word(102)
    'роки'

    >>> year_word(111)
    'років'

    >>> year_word(112)
    'років'

    >>> year_word(113)
    'років'

    >>> year_word(114)
    'років'

    >>> year_word(121)
    'рік'

    >>> year_word(122)
    'роки'

    >>> year_word(125)
    'років'
    """
    if (n % 10) in [2, 3, 4] and (n % 100) not in [12, 13, 14]:
        return "роки"
    elif (n % 10) == 1:
        if (n % 100) != 11:
            return "рік"
        else:
            return "років"
    else:
        return "років"


def age_chat(age: int) -> None:
    """Виводить повідомлення залежно від віку користувача.

    >>> age_chat(0)
    Я думав, що Вам 1 рік

    >>> age_chat(1)
    Я думав, що Вам 2 роки

    >>> age_chat(4)
    Я думав, що Вам 5 років

    >>> age_chat(5)
    Я думав, що Вам 6 років

    >>> age_chat(20)
    Я думав, що Вам 21 рік

    >>> age_chat(21)
    Я думав, що Вам 22 роки

    >>> age_chat(22)
    Я думав, що Вам 23 роки

    >>> age_chat(23)
    Я думав, що Вам 24 роки

    >>> age_chat(24)
    Я думав, що Вам 25 років

    >>> age_chat(109)
    Я думав, що Вам 110 років

    >>> age_chat(110)
    Я думав, що Вам 111 років

    >>> age_chat(111)
    Я думав, що Вам 112 років

    >>> age_chat(119)
    Я думав, що Вам 120 років

    >>> age_chat(120)
    Я думав, що Вам 121 рік

    >>> age_chat(121)
    Я думав, що Вам 122 роки

    >>> age_chat(122)
    Я думав, що Вам 123 роки

    >>> age_chat(123)
    Я думав, що Вам 124 роки

    >>> age_chat(124)
    Я думав, що Вам 125 років

    >>> age_chat(139)
    Я думав, що Вам 140 років

    >>> age_chat(140)
    Я думав, що Вам 141 рік

    >>> age_chat(-1)
    Ви ще не народилися

    >>> age_chat(-100)
    Ви ще не народилися

    >>> age_chat(141)
    Стільки не живуть...

    >>> age_chat(155)
    Стільки не живуть...
    """
    form_of_word = year_word(age + 1)

    if 0 <= age <= 140:
        print(f"Я думав, що Вам {age + 1} {form_of_word}")
    elif age < 0:
        print("Ви ще не народилися")
    else:
        print("Стільки не живуть...")


doctest.testmod()

age_in: int
age_in = int(input("Введіть Ваш вік: "))

age_chat(age_in)
