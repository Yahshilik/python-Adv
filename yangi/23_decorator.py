import logging
import math
import time

# def timer_decorator(func):
#     def inner(messege):
#         start = time.time()
#         r = func(messege)
#         end = time.time()
#         print(f"salom ber funksiyasi {end - start} ishladi")
#         return r
#     return inner
#
#
# # print(f"salom ber funksiyasi {end - start} ishladi")
# @timer_decorator
# def salom_ber(m):
#     time.sleep(2)
#     return f"salom {m}"
#
# #
# # begin = time.time()
# print(salom_ber("dunyo"))
# # end = time.time()
# # print(f"salom ber funksiyasi {end - begin} ishladi")
#
# def factotilas(num):
#     return math.factorial(num)
#
# def tashqi_func():
#     print("tashqi")
#     def ichki():
#         print("ichki")
#
#     ichki()
#
# tashqi_func()
#
# from typing import Callable
#
# def split(func: Callable) -> Callable:
#     def inner(message:str) ->str:
#         result = func(message)
#         return result.split()
#
#     return inner
#
#
# def uppercase_deco(func: Callable) -> Callable:
#     def inner(message: str) -> str:
#         result = func(message)
#         return result.upper()
#
#     return inner
#
# @split
# @uppercase_deco
# def salom_ber(message: str) -> str:
#     return f"salom {message}"
#
#
# print(salom_ber("dunyo"))

# def decor1(func):
#     def inner():
#         x = func()
#         return x ** 2
#     return inner
#
# def decor2(func):
#     def inner():
#         x = func()
#         return  x * 2
#     return inner
#
# @decor1
# @decor2
# def num():
#     return 10
# print(num())

# class Logger:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         logging.info("logger deco ishladi")
#         a = self.func(*args, **kwargs)
#         logging.info("logger deco tugadi")
#         return a
#
# @Logger
# def salom_ber(*args, **kwargs):
#     for i in args:
#         print(f"salom {i}")
#
#     for k,v in kwargs.items():
#         print(f"salom {k}  {v}")
#
#     return "tugadi"
#
# salom_ber("ali", "vali", ali="Sherov")

# def only_positive(func):

