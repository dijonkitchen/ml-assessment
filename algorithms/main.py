import time


def play_countdown(letters) -> str:
    """
    Plays the game of countdown with the given letters.
    """
    pass


if __name__ == "__main__":
    tic = time.perf_counter()
    assert len(play_countdown("sretpmocc")) == 8
    assert len(play_countdown("ndaelryra")) == 7
    assert len(play_countdown("terhbswoa")) == 9
    assert len(play_countdown("iouytsdne")) == 8
    assert len(play_countdown("lcaethbir")) == 8
    assert len(play_countdown("afgolbnui")) == 7
    assert len(play_countdown("xriapeset")) == 8
    assert len(play_countdown("sjwuylnie")) == 8
    assert len(play_countdown("potgmearh")) == 9
    assert len(play_countdown("aqqqqqqqq")) == 2
    assert len(play_countdown("nnnnnnnnn")) == 1
    toc = time.perf_counter()
    print("All tests passed in {} seconds!".format(toc - tic))
