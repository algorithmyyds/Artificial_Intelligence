from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    # A不是同时为骑士或者无赖
    Not(And(AKnight, AKnave)),
    # A要么是骑士或者无赖
    Or(AKnight, AKnave),
    # 假如A是骑士，这句话就是真的，那么A就既是骑士，又是无赖
    Implication(AKnight, And(AKnight, AKnave)),
    # 假如A是无赖，这句话就是假的，直接取否定即可
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    # A不是同时为骑士或者无赖
    Not(And(AKnight, AKnave)),
    # A要么是骑士或者无赖
    Or(AKnight, AKnave),
    # B不是同时为骑士或者无赖
    Not(And(BKnight, BKnave)),
    # B要么是骑士或者无赖
    Or(BKnight, BKnave),
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave,Not(And(AKnave,BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    # A不是同时为骑士或者无赖
    Not(And(AKnight, AKnave)),
    # A要么是骑士或者无赖
    Or(AKnight, AKnave),
    # B不是同时为骑士或者无赖
    Not(And(BKnight, BKnave)),
    # B要么是骑士或者无赖
    Or(BKnight, BKnave),
    Implication(AKnight,And(AKnight,BKnight)),
    Implication(AKnave,Not(And(AKnave,BKnave))),
    Implication(BKnight,And(BKnight,AKnave)),
    Implication(BKnave,Not(And(BKnight,AKnave)))


)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    # TODO
    # 不是同时为骑士或者无赖
    Not(And(AKnight, AKnave)),
    # 要么是骑士或者无赖
    Or(AKnight, AKnave),
    # 不是同时为骑士或者无赖
    Not(And(BKnight, BKnave)),
    # B是骑士或者无赖
    Or(BKnight, BKnave),
    # 不是同时为骑士或者无赖
    Not(And(CKnight, CKnave)),
    # C要么是骑士或者无赖
    Or(CKnight, CKnave),
    And(
        #Or语句代表A说的话是“我是骑士”还是“我是无赖”
        Or(
        #A说的话是我是骑士
        And(
            #A是骑士，那么A说的话是真的->A就是骑士
            Implication(AKnight, AKnight),
            #A是无赖，那么A不是骑士
            Implication(AKnave, AKnave)
        ),
        #A说的话是我是无赖
        And(
            #假如A是骑士—>A说的话是真的->那么A是无赖
            Implication(AKnight, AKnave),
            #假如A是无赖—>A说的话是假的->那么A是骑士
            Implication(AKnave, Not(AKnave)),
        )
    ),
    #下面的语句代表对B,C身份的假设
    # B是骑士，B说的第一句话是真的，即A确实说的是“我是无赖”
    Implication(BKnight, And(
        #A说的是我是无赖：A是骑士->A说的话是真的->A是骑士
        Implication(AKnight, AKnave),
        #A说的是我是无赖：A是无赖->A说的话是假的->A是骑士
        Implication(AKnave, Not(AKnave))
    )),
    # B是无赖，B说的第一句话是假的，即A说的是“我是无赖”
    Implication(BKnave, Not(And(
        #在A说的话是"我是无赖"的情况下，假如A是骑士，那么A说的话是真的，那么A就是无赖
        Implication(AKnight, AKnave),
        #在A说的话是"我是无赖"的情况下，假如A是无赖，那么A说的话是假的，那么A就是骑士，
        Implication(AKnave, AKnight)
    ))),
    #假如B是骑士->则B说的第二句话是真的->C是无赖
    Implication(BKnight, CKnave),
    #假如B是骑士->则B说的第二句话是假的->C是骑士
    Implication(BKnave, Not(CKnave)),
    # 假如C是骑士->则C说的话是真的->A是骑士
    Implication(CKnight, AKnight),
    #假如C是无赖->则C说的话是假的->A是无赖
    Implication(CKnave, AKnave)
    )
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"{symbol}")


if __name__ == "__main__":
    main()