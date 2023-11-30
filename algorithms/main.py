import time
from itertools import permutations


def create_dictionary(file_path: str) -> dict[str, True]:
    with open(file_path, 'r', encoding="utf-8") as file:
        data = file.readlines()

    words = {}
    for line in data:
        word = line.strip()
        words[word] = True

    return words


def play_countdown(letters: str, words=None) -> str:
    """
    Plays the game of countdown with the given letters.
    """
    # Brute force: Time complexity: O(letters! * words), Space complexity: O(letters!)
    # Generate all permutations of possible words given letters. Time complexity: O(letters!), Space complexity: O(letters!)

    # Search wordlist for each possible word. Time: O(letters! * words)

    # If actual word
    #   Save to new list. Space: O(letters!)

    # Loop through each actual word for longest word. Space: O(letters!)

    # Return longest word


    # Better1: Time complexity: O(letters!), Space complexity: O(letters! + words)
    # Set longest word to empty string. Space: O(1)

    # Generate all permutations of possible words given letters. Time complexity: O(letters!), Space complexity: O(letters!)

    # Generate a dictionary based on wordlist if it doesn't exist. Time: O(words), Space: O(words)

    # Search for each possible word. Time: O(letters!)

    # If actual word and length is greater than longest word,
    #   If same length as letters, return early
    #   Else, save as longest word

    # Return longest word


    # Better2: Time complexity: O(letters!), Space complexity: O(words) if not cached, O(1) if cached
    # Generate a dictionary based on wordlist if it doesn't exist. Time: O(words), Space: O(words)

    # Generate permutations of possible words given letters from most to least. Time complexity: O(letters!), Space complexity: O(1)
    #   Search for each possible word. Time: O(letters!)

    #   If actual word and length is greater than longest word,
    #       If word found, return word

    # Return empty string since none found
    if not words:
        words = create_dictionary('algorithms/words_alpha.txt')

    for i in range(len(letters), 0, -1):
        for perm in permutations(letters, i):
            possible_word = ''.join(perm)

            if words.get(possible_word):
                return possible_word

    return ""


if __name__ == "__main__":
    tic = time.perf_counter()

    words = create_dictionary('algorithms/words_alpha.txt')

    assert len(play_countdown("sretpmocc", words)) == 8
    assert len(play_countdown("ndaelryra", words)) == 7
    assert len(play_countdown("terhbswoa", words)) == 9
    assert len(play_countdown("iouytsdne", words)) == 8
    assert len(play_countdown("lcaethbir", words)) == 8
    assert len(play_countdown("afgolbnui", words)) == 7
    assert len(play_countdown("xriapeset", words)) == 8
    assert len(play_countdown("sjwuylnie", words)) == 8
    assert len(play_countdown("potgmearh", words)) == 9
    assert len(play_countdown("aqqqqqqqq", words)) == 2
    assert len(play_countdown("nnnnnnnnn", words)) == 1

    toc = time.perf_counter()

    print("All tests passed in {} seconds!".format(toc - tic))
