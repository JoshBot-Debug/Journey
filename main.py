from decorator import *

@strict
def number(y: list, z: bool, x: int = 30) -> int:
    return x

print(number(y=["how","are"],z=""))