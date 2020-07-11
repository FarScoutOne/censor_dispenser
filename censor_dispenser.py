# Must be able to refer to a specific word by its location in the text.
# Must be able to replace words with concealer using same number of characters.
# Must keep punctuation intact.
#   Keep in mind that punctuatio can be before, after, or in middle of word.

# Use word_finder to find each instance of word
# Replace each instance with the concealer
# Replace punctuation
# For multiple word terms, compare returned index positions of previous word with current word. If the index positions are consecutive, replace words with concealer.

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

# Break text into words, but make sure to retain new lines.
def text_to_list(text):
    text_as_list = []

    text = text.split('\n')
    for line in text:
        words = line.split()
        for word in words:
            text_as_list.append(word)
        text_as_list.append('\n')   # Keeps the new line locations intact

    return text_as_list

#print(text_to_list(email_three))

#word_list = text_to_list(email_one)

# Check word for punctuation. Returns list containing punctuation found and their positions within the word
# If no punctuation present in word, empty list
def punctuation_mapper(word):
    punctuation = ['!', '#', '(', ')', '-', ',', '.', '?', '"', "'"]
    punctuation_list = []

    for character in punctuation:
        for index in range(len(word)):
            if word[index] == character:
                punctuation_list.append(character)
                punctuation_list.append(index)

    return punctuation_list


# Returns list of index positions of word within the text
def word_finder(word_list, word):
    word_positions = []
    word_plural = word + 's'
    word_past_tense_1 = word + 'd'
    word_past_tense_2 = word + 'ed'


    for element in range(len(word_list)):
        if word_cleaner(word_list[element].lower()) == word.lower():
            word_positions.append(element)
        elif word_cleaner(word_list[element].lower()) == word_plural.lower():
            word_positions.append(element)
        elif word_cleaner(word_list[element].lower()) == word_past_tense_1.lower():
            word_positions.append(element)
        elif word_cleaner(word_list[element].lower()) == word_past_tense_2.lower():
            word_positions.append(element)


    return word_positions

#print(word_finder(word_list, "concerning"))

#print(punctuation_mapper('hello-goodbye-he"llo'))

# Returns a string after punctuation within it has been removed and all characters set to lower case.
def word_cleaner(word):
    punctuation = ['!', '#', '(', ')', '-', ',', '.', '?', '"', "'"]
    clean_word = []

    for character in word:
        #print(character)
        is_punctuation = False
        for symbol in punctuation:
            if (character == symbol):
                is_punctuation = True
                break
        if (is_punctuation != True):
            clean_word.append(character)

    clean_word = ''.join(clean_word)
    clean_word = clean_word.lower()

    return clean_word

#print(word_cleaner("Out-of-control"))

#############################################################################################################
# Conceals the word by replaceing each character with the concealer.
#############################################################################################################
def conceal(word, punctuation_map, concealer):
    blackout = []

    for i in range(len(word)):
        blackout.append(concealer)
    blackout = ''.join(blackout)

    if punctuation_map:
        index = 0
        while index < len(punctuation_map):
            blackout_after_punctuation = blackout[punctuation_map[index + 1] + 1:]

            blackout = blackout[:punctuation_map[index + 1]] + punctuation_map[index]

            blackout = blackout + blackout_after_punctuation

            index += 2




    return blackout

#print(conceal("horribly.)", [".", 8, ")", 9], "*"))

#print(conceal("algorithm", "*"))

# Provide the text and a word and conceal each occurrence of the words
# Should also include any plural or past tense versions of the word. This can be accomplished by including
# the target word + -ed, -d, or -s on the end.
# Convert text to list of words --> Map punctuation --> Clean word --> Search for word --> Conceal occurrences of word
text_list = text_to_list(email_three)

def test_launcher(text, word):
    word_count = 0

    for term in text_list:
        punctuation_in_word = punctuation_mapper(term)
        clean_word = word_cleaner(term)
        print(word_count)
        print("Word: " + term)
        print("Punctuation Map: " + str(punctuation_in_word))
        print("Clean Word: " + clean_word)
        print("Target Word: {target}".format(target=word))
        print("Cover-up: " + conceal(term, punctuation_in_word, "*"))
        print('----------------------------------------------------')
        word_count += 1

    word_positions = word_finder(text, word_cleaner(word))

    print(word_positions)

#test_launcher(text_list, "horribly")

def launcher(text, censored_terms, negative_terms, concealer):
    text_as_list = text_to_list(text)

    for term in censored_terms:
        term = term.split()

        # Create a list for each word in the term composed of its locations within the text
        word_instances = ['' for x in range(len(term))]
        index = 0
        while index < len(word_instances):
            word_instances[index] = word_finder(text_as_list, term[index])
            index += 1

        










launcher(email_three, proprietary_terms, negative_words, "*")
