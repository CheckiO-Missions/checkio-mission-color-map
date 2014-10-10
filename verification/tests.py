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
        {
            "input": [6, 3],
            "answer": 9,
            "explanation": "6+3=?"
        },
        {
            "input": [6, 7],
            "answer": 13,
            "explanation": "6+7=?"
        }
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

for test in BASIC:
    TESTS["Basics"].append({"input": test, "answer": test})