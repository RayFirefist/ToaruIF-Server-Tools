def getDeckTrinityType(userId: int) -> list:
    # TODO logic
    return [
        {"deck_trinity_type": 1, "select_deckid": 1},
        {"deck_trinity_type": 2, "select_deckid": 1},
        {"deck_trinity_type": 3, "select_deckid": 1},
        {"deck_trinity_type": 5, "select_deckid": 1},
        {"deck_trinity_type": 6, "select_deckid": 1},
    ]


def getDeckType(userId: int) -> list:
    return [
        {"deck_type": 1, "select_deckid": 4},
        {"deck_type": 2, "select_deckid": 1},
        {"deck_type": 3, "select_deckid": 2},
        {"deck_type": 4, "select_deckid": 1},
        {"deck_type": 5, "select_deckid": 1},
        {"deck_type": 7, "select_deckid": 2},
        {"deck_type": 8, "select_deckid": 1},
        {"deck_type": 14, "select_deckid": 1},
    ]


def getDeckInfo(userId: int) -> list:
    # TODO logic
    return [
        {
            "deck_type": 1,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 1,
            "deckid": 2,
            "name": "マイチーム2",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 1,
            "deckid": 3,
            "name": "マイチーム3",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 1,
            "deckid": 4,
            "name": "マイチーム4",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 1,
            "deckid": 5,
            "name": "マイチーム5",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 2,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 3,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 3,
            "deckid": 2,
            "name": "マイチーム2",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 3,
            "deckid": 3,
            "name": "マイチーム3",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 3,
            "deckid": 4,
            "name": "マイチーム4",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 3,
            "deckid": 5,
            "name": "マイチーム5",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 4,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 4,
            "deckid": 2,
            "name": "マイチーム2",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 4,
            "deckid": 3,
            "name": "マイチーム3",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 4,
            "deckid": 4,
            "name": "マイチーム4",
            "battle_card_uniqid1": 0,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 4,
            "deckid": 5,
            "name": "マイチーム5",
            "battle_card_uniqid1": 0,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 5,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 5,
            "deckid": 2,
            "name": "マイチーム2",
            "battle_card_uniqid1": 0,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 5,
            "deckid": 3,
            "name": "マイチーム3",
            "battle_card_uniqid1": 0,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 5,
            "deckid": 4,
            "name": "マイチーム4",
            "battle_card_uniqid1": 0,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 5,
            "deckid": 5,
            "name": "マイチーム5",
            "battle_card_uniqid1": 0,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 7,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 7,
            "deckid": 2,
            "name": "マイチーム2",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 7,
            "deckid": 3,
            "name": "マイチーム3",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 7,
            "deckid": 4,
            "name": "マイチーム4",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 7,
            "deckid": 5,
            "name": "マイチーム5",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 8,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 1092285002,
            "battle_card_uniqid3": 1092285003,
            "battle_card_uniqid4": 1092285004,
            "battle_card_uniqid5": 1092285005,
            "battle_card_uniqid6": 1092285006,
            "assist_card_uniqid1": 1,
            "assist_card_uniqid2": 2,
            "assist_card_uniqid3": 3,
            "assist_card_uniqid4": 4,
            "assist_card_uniqid5": 5,
            "assist_card_uniqid6": 6,
        },
        {
            "deck_type": 8,
            "deckid": 2,
            "name": "マイチーム2",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 8,
            "deckid": 3,
            "name": "マイチーム3",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 8,
            "deckid": 4,
            "name": "マイチーム4",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 8,
            "deckid": 5,
            "name": "マイチーム5",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 14,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 14,
            "deckid": 2,
            "name": "マイチーム2",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 14,
            "deckid": 3,
            "name": "マイチーム3",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 14,
            "deckid": 4,
            "name": "マイチーム4",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 14,
            "deckid": 5,
            "name": "マイチーム5",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
        {
            "deck_type": 14,
            "deckid": 6,
            "name": "マイチーム6",
            "battle_card_uniqid1": 1092285001,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        },
    ]


def getDeckTrinityInfo(userId: int) -> list:
    # TODO logic
    return [
        {
            "deck_trinity_type": 1,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 42870065002,
            "battle_card_uniqids_1st2": 42235552001,
            "battle_card_uniqids_1st3": 63196637001,
            "battle_card_uniqids_1st4": 73147184001,
            "battle_card_uniqids_1st5": 88164738011,
            "battle_card_uniqids_1st6": 73148192001,
            "assist_card_uniqids_1st1": 42188359001,
            "assist_card_uniqids_1st2": 47235038008,
            "assist_card_uniqids_1st3": 42870164001,
            "assist_card_uniqids_1st4": 42797577001,
            "assist_card_uniqids_1st5": 42803257001,
            "assist_card_uniqids_1st6": 50356187001,
            "battle_card_uniqids_2nd1": 47237800001,
            "battle_card_uniqids_2nd2": 53984420007,
            "battle_card_uniqids_2nd3": 44216227001,
            "battle_card_uniqids_2nd4": 47162567001,
            "battle_card_uniqids_2nd5": 63821267001,
            "battle_card_uniqids_2nd6": 47292203001,
            "assist_card_uniqids_2nd1": 1177382007,
            "assist_card_uniqids_2nd2": 140734861001,
            "assist_card_uniqids_2nd3": 45127022003,
            "assist_card_uniqids_2nd4": 93008009001,
            "assist_card_uniqids_2nd5": 44092565001,
            "assist_card_uniqids_2nd6": 120549806001,
            "battle_card_uniqids_3rd1": 87812814002,
            "battle_card_uniqids_3rd2": 43168669002,
            "battle_card_uniqids_3rd3": 42235554001,
            "battle_card_uniqids_3rd4": 43672997004,
            "battle_card_uniqids_3rd5": 46778733001,
            "battle_card_uniqids_3rd6": 54917198007,
            "assist_card_uniqids_3rd1": 44553319001,
            "assist_card_uniqids_3rd2": 43594453001,
            "assist_card_uniqids_3rd3": 61590806001,
            "assist_card_uniqids_3rd4": 48268107002,
            "assist_card_uniqids_3rd5": 43751917002,
            "assist_card_uniqids_3rd6": 82624210001,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
        {
            "deck_trinity_type": 2,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 46778733001,
            "battle_card_uniqids_1st2": 43105553004,
            "battle_card_uniqids_1st3": 42235938003,
            "battle_card_uniqids_1st4": 42797577002,
            "battle_card_uniqids_1st5": 43673356006,
            "battle_card_uniqids_1st6": 42550631001,
            "assist_card_uniqids_1st1": 43674062004,
            "assist_card_uniqids_1st2": 43678132001,
            "assist_card_uniqids_1st3": 1176996027,
            "assist_card_uniqids_1st4": 43105146002,
            "assist_card_uniqids_1st5": 44092565001,
            "assist_card_uniqids_1st6": 43105553005,
            "battle_card_uniqids_2nd1": 42235552001,
            "battle_card_uniqids_2nd2": 43168669002,
            "battle_card_uniqids_2nd3": 42870065002,
            "battle_card_uniqids_2nd4": 53984420007,
            "battle_card_uniqids_2nd5": 47162567001,
            "battle_card_uniqids_2nd6": 42235554001,
            "assist_card_uniqids_2nd1": 42188359001,
            "assist_card_uniqids_2nd2": 1177382007,
            "assist_card_uniqids_2nd3": 42803257001,
            "assist_card_uniqids_2nd4": 42870164001,
            "assist_card_uniqids_2nd5": 42797577001,
            "assist_card_uniqids_2nd6": 48268107002,
            "battle_card_uniqids_3rd1": 47237800001,
            "battle_card_uniqids_3rd2": 43672997004,
            "battle_card_uniqids_3rd3": 44216227001,
            "battle_card_uniqids_3rd4": 54917198007,
            "battle_card_uniqids_3rd5": 61558399007,
            "battle_card_uniqids_3rd6": 46715187001,
            "assist_card_uniqids_3rd1": 47235038008,
            "assist_card_uniqids_3rd2": 50356187001,
            "assist_card_uniqids_3rd3": 43751917002,
            "assist_card_uniqids_3rd4": 43594453001,
            "assist_card_uniqids_3rd5": 44553319001,
            "assist_card_uniqids_3rd6": 61590806001,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
        {
            "deck_trinity_type": 3,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 43672997004,
            "battle_card_uniqids_1st2": 47237800001,
            "battle_card_uniqids_1st3": 44216227001,
            "battle_card_uniqids_1st4": 46715187001,
            "battle_card_uniqids_1st5": 42870065002,
            "battle_card_uniqids_1st6": 43168669002,
            "assist_card_uniqids_1st1": 48268107002,
            "assist_card_uniqids_1st2": 47235038008,
            "assist_card_uniqids_1st3": 43751917002,
            "assist_card_uniqids_1st4": 44553319001,
            "assist_card_uniqids_1st5": 44773128003,
            "assist_card_uniqids_1st6": 42188359001,
            "battle_card_uniqids_2nd1": 42235552001,
            "battle_card_uniqids_2nd2": 42235554001,
            "battle_card_uniqids_2nd3": 43105553004,
            "battle_card_uniqids_2nd4": 47162567001,
            "battle_card_uniqids_2nd5": 42235938003,
            "battle_card_uniqids_2nd6": 46778733001,
            "assist_card_uniqids_2nd1": 43594453001,
            "assist_card_uniqids_2nd2": 42870164001,
            "assist_card_uniqids_2nd3": 45127022003,
            "assist_card_uniqids_2nd4": 42797577001,
            "assist_card_uniqids_2nd5": 42803257001,
            "assist_card_uniqids_2nd6": 43673583008,
            "battle_card_uniqids_3rd1": 42797577002,
            "battle_card_uniqids_3rd2": 43673356006,
            "battle_card_uniqids_3rd3": 42550631001,
            "battle_card_uniqids_3rd4": 42803257002,
            "battle_card_uniqids_3rd5": 1176280006,
            "battle_card_uniqids_3rd6": 42235093001,
            "assist_card_uniqids_3rd1": 43105146002,
            "assist_card_uniqids_3rd2": 1177382006,
            "assist_card_uniqids_3rd3": 43674724001,
            "assist_card_uniqids_3rd4": 45182405002,
            "assist_card_uniqids_3rd5": 1177382007,
            "assist_card_uniqids_3rd6": 43674062004,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
        {
            "deck_trinity_type": 5,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 42870065002,
            "battle_card_uniqids_1st2": 157762243003,
            "battle_card_uniqids_1st3": 42235552001,
            "battle_card_uniqids_1st4": 47237800001,
            "battle_card_uniqids_1st5": 47162567001,
            "battle_card_uniqids_1st6": 120551378001,
            "assist_card_uniqids_1st1": 42188359001,
            "assist_card_uniqids_1st2": 42870164001,
            "assist_card_uniqids_1st3": 140734861001,
            "assist_card_uniqids_1st4": 47235038008,
            "assist_card_uniqids_1st5": 120549806001,
            "assist_card_uniqids_1st6": 50356187001,
            "battle_card_uniqids_2nd1": 63196637001,
            "battle_card_uniqids_2nd2": 88164738011,
            "battle_card_uniqids_2nd3": 44216227001,
            "battle_card_uniqids_2nd4": 63821267001,
            "battle_card_uniqids_2nd5": 157932956001,
            "battle_card_uniqids_2nd6": 47292203001,
            "assist_card_uniqids_2nd1": 42797577001,
            "assist_card_uniqids_2nd2": 42803257001,
            "assist_card_uniqids_2nd3": 45127022003,
            "assist_card_uniqids_2nd4": 93008009001,
            "assist_card_uniqids_2nd5": 61590806001,
            "assist_card_uniqids_2nd6": 1177382007,
            "battle_card_uniqids_3rd1": 73147184001,
            "battle_card_uniqids_3rd2": 73148192001,
            "battle_card_uniqids_3rd3": 53984420007,
            "battle_card_uniqids_3rd4": 43672997004,
            "battle_card_uniqids_3rd5": 87812814002,
            "battle_card_uniqids_3rd6": 43168669002,
            "assist_card_uniqids_3rd1": 43594453001,
            "assist_card_uniqids_3rd2": 43751917002,
            "assist_card_uniqids_3rd3": 82624210001,
            "assist_card_uniqids_3rd4": 48268107002,
            "assist_card_uniqids_3rd5": 44553319001,
            "assist_card_uniqids_3rd6": 44092565001,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
        {
            "deck_trinity_type": 6,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 157762243003,
            "battle_card_uniqids_1st2": 73147184001,
            "battle_card_uniqids_1st3": 73148192001,
            "battle_card_uniqids_1st4": 63196637001,
            "battle_card_uniqids_1st5": 88164738011,
            "battle_card_uniqids_1st6": 120551378001,
            "assist_card_uniqids_1st1": 44092565001,
            "assist_card_uniqids_1st2": 140734861001,
            "assist_card_uniqids_1st3": 45127022003,
            "assist_card_uniqids_1st4": 120549806001,
            "assist_card_uniqids_1st5": 82624210001,
            "assist_card_uniqids_1st6": 93008009001,
            "battle_card_uniqids_2nd1": 42870065002,
            "battle_card_uniqids_2nd2": 42235552001,
            "battle_card_uniqids_2nd3": 53984420007,
            "battle_card_uniqids_2nd4": 47162567001,
            "battle_card_uniqids_2nd5": 63821267001,
            "battle_card_uniqids_2nd6": 157932956001,
            "assist_card_uniqids_2nd1": 42188359001,
            "assist_card_uniqids_2nd2": 42803257001,
            "assist_card_uniqids_2nd3": 42870164001,
            "assist_card_uniqids_2nd4": 42797577001,
            "assist_card_uniqids_2nd5": 1177382007,
            "assist_card_uniqids_2nd6": 48268107002,
            "battle_card_uniqids_3rd1": 47237800001,
            "battle_card_uniqids_3rd2": 44216227001,
            "battle_card_uniqids_3rd3": 47292203001,
            "battle_card_uniqids_3rd4": 43672997004,
            "battle_card_uniqids_3rd5": 87812814002,
            "battle_card_uniqids_3rd6": 43168669002,
            "assist_card_uniqids_3rd1": 47235038008,
            "assist_card_uniqids_3rd2": 43751917002,
            "assist_card_uniqids_3rd3": 44553319001,
            "assist_card_uniqids_3rd4": 50356187001,
            "assist_card_uniqids_3rd5": 61590806001,
            "assist_card_uniqids_3rd6": 43594453001,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
    ]

