import random

def main():
    sentence1 = make_sentence(1, 'past')
    sentence2 = make_sentence(1, 'present')
    sentence3 = make_sentence(1, 'future')
    sentence4 = make_sentence(2, 'past')
    sentence5 = make_sentence(2, 'present')
    sentence6 = make_sentence(3, 'future')

    print(f'{sentence1}')
    print(f'{sentence2}')
    print(f'{sentence3}')
    print(f'{sentence4}')
    print(f'{sentence5}')
    print(f'{sentence6}')

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositonal_phrase = get_prepositonal_phrase(quantity)
    adjective = get_adjective()

    sentence = f"{determiner} {adjective} {noun} {verb} {prepositonal_phrase}".capitalize()
    return sentence

def get_prepositonal_phrase(quantity):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition = get_prepositon()
    adjective = get_adjective()

    prepositonal_phrase = f"{preposition} {determiner} {adjective} {noun}"
    return prepositonal_phrase


def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]

    determiner = random.choice(determiners)
    return determiner

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == 'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'prensent' and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb

def get_prepositon():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
    return preposition

def get_adjective():
    adjectives = ["great", "old", "big", "happy", "beautiful", "small", "sad", "young"]

    adjective = random.choice(adjectives)
    return adjective
main()