"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    
    Example: add_prefix_un("happy") returns "unhappy"
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with prefix applied.
    
    Example: make_word_groups(['en', 'close', 'joy', 'lighten']) 
    returns 'en :: enclose :: enjoy :: enlighten'
    """
    if not vocab_words:
        return ""
    prefix = vocab_words[0]
    prefixed_words = [prefix + word for word in vocab_words[1:]]
    return " :: ".join([prefix] + prefixed_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.
    
    Examples:
        remove_suffix_ness("heaviness") returns "heavy"
        remove_suffix_ness("sadness") returns "sad"
    """
    if word.endswith("ness"):
        base_word = word[:-4]  # Remove 'ness'
        # Handle case where base word ends with 'i' (like heavy -> heavi)
        if base_word.endswith("i"):
            return base_word[:-1] + "y"
        return base_word
    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.
    
    Example: 
        adjective_to_verb("It got dark as the sun set.", 2) returns "darken"
    """
    if not sentence:
        return ""
    
    # Split into words and handle punctuation
    words = sentence.split()
    
    # Handle negative indices
    if index < 0:
        index = len(words) + index
    
    # Get the adjective and remove any trailing punctuation
    adjective = words[index].strip(".,!?;:\"'")
    
    # Add 'en' to make it a verb
    return adjective + "en"
