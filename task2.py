'''
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}
'''
from typing import Dict


def dictionary_generation(**kwargs) -> Dict:
    dictionary = {}

    for key, value in kwargs.items():
        try:
            dictionary[value] = key
        except:
            dictionary[str(value)] = key
    return dictionary


# start

print(dictionary_generation(res1=1, res2=2, res3=3,
                            res4=[4], res5=[5.0],
                            res6=(6.0,)))

# stop
