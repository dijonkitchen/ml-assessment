from itertools import permutations
import time


def play_countdown(letters: str, words = None) -> str:
    """
    Plays the game of countdown with the given letters.
    """
    # Brute force: Time complexity: O(letters! * words), Space complexity: O(letters!)
    # Generate all permutations of possible words given letters. Time complexity: O(letters!), Space complexity: O(letters!)

    # Search wordlist for each possible word. Time: O(letters! * words)

    # If actual word
        # Save to new list. Space: O(letters!)

    # Loop through each actual word for longest word. Space: O(letters!)

    # Return longest word


    # Optimized: Time complexity: O(letters!), Space complexity: O(letters! + words)
    # Set longest word to empty string. Space: O(1)

    # Generate all permutations of possible words given letters. Time complexity: O(letters!), Space complexity: O(letters!)

    # Generate a dictionary based on wordlist if it doesn't exist. Time: O(words), Space: O(words)

    # Search for each possible word. Time: O(letters!)

    # If actual word and length is greater than longest word,
        # If same length as letters, return early
        # Else, save as longest word

    # Return longest word

    longest = ""

    possible_words = []

    for i in range(1, len(letters) + 1):
        possible_words += [''.join(p) for p in permutations(letters, i)]

    if not words:
        words = create_dictionary('algorithms/words_alpha.txt')

    for possible_word in possible_words:
        if words.get(possible_word) and (len(possible_word) > len(longest)):
            if len(possible_word) == len(letters):
                return possible_word

            longest = possible_word

    return longest

def create_dictionary(file_path: str) -> dict[str, True]:
    with open(file_path, 'r') as file:
        data = file.readlines()

    words = {}
    for line in data:
        word = line.strip()
        words[word] = True

    return words


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
