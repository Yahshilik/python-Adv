import logging
import time



# def birni_qosh(num):
#     return num + 1
#
# func = birni_qosh
# print(func(2))

# def tashqi():
#     print("tashqi ishladi")
#
#     def ichki():
#         print("ichki ishladi")
#
#     ichki()
#
# tashqi()
# from typing import Callable
# def salom_ber(message:str):
#     return f"salom {message}"
#
# def uppercase_decor(func: Callable) -> Callable:
#     def inner(message: str) ->str:
#         result = func(message)
#         return  result.upper()
#     return inner
#
# a = uppercase_decor(salom_ber)
# print(a("dunyo"))

# def timer_decorater(func):
#     def inner(message):
#         start = time.time()
#         r = func(message)
#         end = time.time()
#         print(f"salom ber funksiyasi {end-start} ishladi")
#         return r
#
#     return inner
#
#
# @timer_decorater
# def salom_ber(m):
#     return f"salom {m}"
#
# begin = time.time()
# print(salom_ber("dunyo"))
# end = time.time()
# print(f"salom ber funksiyasi {end-begin} ishladi")

# def decor1(func):
#     def inner():
#         x = func()
#         return x ** 2
#     return inner
#
# def decor2(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner
#
# # @decor1
# # @decor2
#
# @decor2
# @decor1
#
# def num():
#     return 10
# def num2():
#     return 10

# print(num())
# print(num2)
import  logging
logging.basicConfig(
    filename="log.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        logging.info("lkgger decor ishladi")
        a = self.func(*args,**kwargs)
        logging.info("logger tugadi")
        return a
from typing import Callable
@Logger
def split(sep="") -> Callable:
    def decorator(func: Callable):
        def inner(message: str) -> str:
            result = func(message)
            print(result)
            return result.split(sep=sep)

        return inner

def salom_ber(*args, **kwargs):
    for i in args:
        print(f"salom {i}")

    for k, v in kwargs.items():
        print(f"salom {k} - {v}")
        return "tugadi"

salom_ber("Ali", "Vali", "Gani", alisher="Usmonov")

print(salom_ber("Alisher"))