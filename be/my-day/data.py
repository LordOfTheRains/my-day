people = [
    {
        "id": 1,
        "name": "Rain Li",
        "obligations": [
            {
                "id": 1,
                "obligation_type": "Event",
                "name": "party",
                "description": "some party",
            },
            {
                "id": 2,
                "obligation_type": "Event",
                "name": "study group",
                "description": "ha right",
            },
            {
                "id": 2,
                "obligation_type": "Chore",
                "name": "eating",
                "duration": 2,
                "description": "nom nom",
            },
        ],
    },
    {
        "id": 2,
        "name": "Rain Bot",
        "obligations": [
            {
                "id": 2,
                "name": "study group",
                "obligation_type": "Event",
                "description": "ha right",
            },
            {
                "id": 1,
                "obligation_type": "Chore",
                "name": "laundry",
                "description": "washy washy",
                "duration": 1,
            },
        ],
    },
]

events = [
    {"id": 1, "name": "party", "description": "some party", "participants": [1, 2]},
    {"id": 2, "name": "study group", "description": "ha right", "participants": [1]},
]

chores = [
    {
        "id": 1,
        "name": "laundry",
        "description": "washy washy",
        "duration": 1,
        "participants": [2],
    },
    {
        "id": 2,
        "name": "eating",
        "description": "nom nom",
        "duration": 2,
        "participants": [1],
    },
]
