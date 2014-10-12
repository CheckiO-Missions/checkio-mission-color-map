"""
CheckiOReferee is a base referee for checking you code.
    arguments:
        tests -- the dict contains tests in the specific structure.
            You can find an example in tests.py.
        cover_code -- is a wrapper for the user function and additional operations before give data
            in the user function. You can use some predefined codes from checkio.referee.cover_codes
        checker -- is replacement for the default checking of an user function result. If given, then
            instead simple "==" will be using the checker function which return tuple with result
            (false or true) and some additional info (some message).
            You can use some predefined codes from checkio.referee.checkers
        add_allowed_modules -- additional module which will be allowed for your task.
        add_close_builtins -- some closed builtin words, as example, if you want, you can close "eval"
        remove_allowed_modules -- close standard library modules, as example "math"

checkio.referee.checkers
    checkers.float_comparison -- Checking function fabric for check result with float numbers.
        Syntax: checkers.float_comparison(digits) -- where "digits" is a quantity of significant
            digits after coma.

checkio.referee.cover_codes
    cover_codes.unwrap_args -- Your "input" from test can be given as a list. if you want unwrap this
        before user function calling, then using this function. For example: if your test's input
        is [2, 2] and you use this cover_code, then user function will be called as checkio(2, 2)
    cover_codes.unwrap_kwargs -- the same as unwrap_kwargs, but unwrap dict.

"""

from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

cover = """def cover(f, data):
    return f(tuple(tuple(row) for row in data))
"""

NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))

COLORS = (1, 2, 3, 4)

ERROR_NOT_FOUND = "Didn't find a color for the country {}"
ERROR_WRONG_COLOR = "I don't know about the color {}"


def checker(region, user_result):
    if not isinstance(user_result, (tuple, list)):
        return False, "The result must be a tuple or a list"
    country_set = set()
    for i, row in enumerate(region):
        for j, cell in enumerate(row):
            country_set.add(cell)
            neighbours = []
            if j < len(row) - 1:
                neighbours.append(region[i][j + 1])
            if i < len(region) - 1:
                neighbours.append(region[i + 1][j])
            try:
                cell_color = user_result[cell]
            except IndexError:
                return False, ERROR_NOT_FOUND.format(cell)
            if cell_color not in COLORS:
                return False, ERROR_WRONG_COLOR.format(cell_color)
            for n in neighbours:
                try:
                    n_color = user_result[n]
                except IndexError:
                    return False, ERROR_NOT_FOUND.format(n)
                if cell != n and cell_color == n_color:
                    return False, "Same color neighbours."
    if len(country_set) != len(user_result):
        return False, "Excess colors in the result"
    return True, "Gratz!"


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,
            'python-3': cover
        },
        checker=checker,
        function_name="color_map"
    ).on_ready)
