from random import sample


def shuffle_tuple(tup):
    return tuple(sample(tup, len(tup)))


tweets_hashtags = [
    " #EndAnglophoneCrisis ",
    " #KumbaMassacre ",
    " #e112233 ",
]

nouns = shuffle_tuple(
    (
        "Armed conflict", 
        "Military action", 
        "Bloodshed", 
        "Struggle", 
        "Conflict", 
        "War", 
        "Fight", 
        "Kill", 
        "Destroy", 
        "Massacre"
    )
)
adv = shuffle_tuple(
    (
        "really", 
        "absolutely", 
        "foolishly", 
        "horibly", 
        "atrociously", 
        "awfully", 
        "detestably", 
        "disastrously", 
        "abysmally", 
        "dreadfully"
    )
)
adj = shuffle_tuple(
    (
        "not fair.", 
        "clueless.", 
        "dirty.", 
        "bad.", 
        "stupid.", 
        "unacceptable.", 
        "terrible.", 
        "nasty.", 
        "immoral.", 
        "really bad."
    )
)