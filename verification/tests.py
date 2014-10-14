"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [

    ],
    "Extra": [

    ],
    "Random": [

    ]
}

BASIC = [
    [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 2],
    ],
    [
        [0, 0, 2, 3],
        [0, 1, 2, 3],
        [0, 1, 1, 3],
        [0, 0, 0, 0],
    ],
    [
        [1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 1, 0, 4, 3, 1],
        [1, 1, 1, 3, 3, 3],
        [1, 1, 1, 1, 3, 5],
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 6, 0, 8, 10, 0, 1, 0],
        [0, 1, 0, 5, 0, 7, 9, 0, 1, 0],
        [0, 1, 0, 0, 4, 0, 0, 0, 1, 0],
        [0, 1, 0, 3, 0, 2, 2, 0, 1, 0],
        [0, 1, 0, 3, 0, 2, 11, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
]

EXTRA = [
    [[0]],
    [[0 for _ in range(10)] for __ in range(10)],
    [[i * 5 + j for j in range(5)]for i in range(5)],
    [
        [11, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 4, 4, 4, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [5, 5, 1, 2, 1, 6, 6, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 3, 3, 0, 8, 0],
        [0, 0, 10, 10, 9, 0, 8, 0],
        [0, 0, 0, 10, 9, 9, 8, 0],
    ],
    [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [0, 1, 2, 3, 4, 5, 6, 7],
        [0, 1, 2, 3, 4, 5, 6, 7],
    ],

]

from random import randint, random, choice


def generate_map(rows=None, cols=None, p=0.1):
    if rows is None:
        rows = randint(3, 10)
    if cols is None:
        cols = randint(3, 10)
    region = [[-1 for _ in range(cols)] for _ in range(rows)]
    unchecked = set((i, j) for i in range(rows) for j in range(cols))
    country = 0
    current = None
    while unchecked:
        if not current:
            current = unchecked.pop()
        else:
            unchecked.remove(current)
        x, y = current
        region[x][y] = country
        neighbors = [(x + dx, y + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
                     if 0 <= x + dx < rows and 0 <= y + dy < cols and region[x + dx][y + dy] == -1]
        if not neighbors or random() < p:
            current = None
            country += 1
        else:
            current = choice(neighbors)
    # for row in region:
    #     print([str(i).zfill(2) for i in row])
    return region

for test in BASIC:
    TESTS["Basics"].append({"input": test, "answer": test})

for test in EXTRA:
    TESTS["Extra"].append({"input": test, "answer": test})

for dummy in range(5):
    test = generate_map()
    TESTS["Random"].append({"input": test, "answer": test})