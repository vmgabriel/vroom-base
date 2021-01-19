"""
Module for load process
"""

# Modules
from src.first import solve as first_solve
from src.second import solve as second_solve
from src.third import solve as third_solve


def run():
    """Run App"""
    print('app to run')

    print('----------------')
    first_solve()

    print('----------------')
    second_solve()

    print('----------------')
    third_solve()
