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


for test in BASIC:
    TESTS["Basics"].append({"input": test, "answer": test})

for test in EXTRA:
    TESTS["Extra"].append({"input": test, "answer": test})