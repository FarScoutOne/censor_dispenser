# Must be able to refer to a specific word by its location in the text.
# Must be able to replace words with concealer using same number of characters.
# Must keep punctuation intact.
#   Keep in mind that punctuation can be before, after, or in middle of word.

# GENERAL WORKFLOW 
# Use word_finder to find each instance of word
# Replace each instance with the concealer
# Replace punctuation
# For multiple word terms, compare returned index positions of previous word with current word. If the index positions are consecutive, replace words with concealer.

# These are the emails that need to be censored The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
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

    # if len(word_positions) < 1:
    #     return word_positions.append('')


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
# Conceals the word by replacing each character with the concealer.
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

#Iterate through first list and compare with each element in other lists looking for consecutiveness
def consecutive_values_check(list_of_lists):
    num_of_lists = len(list_of_lists)
    consecutive_values = []
    other_lists = list_of_lists[1:]

    if len(list_of_lists) == 1:
        return list_of_lists

    for value1 in list_of_lists[0]:
        counter = 1
        consecutive = True

        for list in other_lists: # Iterate through remaining lists
            if not consecutive: break

            for i in range(len(list)): # Compare value from first list with each value in current list
                value2 = list[i]
                #print("*********************************************************")
                #print("First List Value: " + str(value1))
                #print("Compare with: " + str(value2))
                #print("Is " + str(value2) + " consecutive with " + str(value1) + "?")
                #print("Does " + str((value1 + counter)) + " = " + str(value2) + "?")
                if value2 > value1 + counter:
                    consecutive = False
                    #print("There is no consecutiveness for this value.")
                    break
                elif value2 == value1 + counter:
                    #print("Yes. We have consecutiveness so far.")
                    counter += 1
                    break
                elif i == len(list) - 1:
                    consecutive = False
                    #print("There is no consecutiveness for this value.")
                    break
                #else:
                    #print("Not yet.")

        if consecutive:
            #print("CONSECUTIVE MATCH: " + str(value1))
            consecutive_values.append(value1)

    return consecutive_values

#print(consecutive_values_check([[1, 2, 18],[3, 7, 8, 19, 22], [4]]))




def launcher(text, proprietary_terms, negative_terms, concealer):
    text_as_list = text_to_list(text)
    censored_terms = proprietary_terms + negative_terms

    for term in censored_terms:
        term = term.split()
        num_of_words = len(term)

        # Create a list for each word in the term composed of its locations within the text
        word_instances = ['' for x in range(len(term))]
        #print(word_instances)

        index = 0
        while index < len(word_instances):
            word_instances[index] = word_finder(text_as_list, term[index])
            index += 1

        #print(word_instances)

        #if len(word_instances[0]) == 0: break # Only continue if there are any instance of the term

        # Check for consecutive values if term in case term is multi-word
        word_instances = consecutive_values_check(word_instances)

        if len(word_instances) > 0:
            if (type(word_instances[0])  != list):
                temp_list = []
                temp_list.append(word_instances)
                word_instances = temp_list

            word_instances = word_instances[0]

            if len(word_instances) > 0:

                counter = 0
                for word in term:  # For each word in the term
                    #print(term)
                    #print(word_instances)
                    for instance in word_instances:  # For each instance of that word
                        #print(instance + counter)
                        punctuation_map = punctuation_mapper(text_as_list[instance + counter])  # Get punctuation map of the word within the text
                        #print(punctuation_map)

                        coverup = conceal(text_as_list[instance + counter], punctuation_map, concealer)

                        text_as_list[instance + counter] = coverup

                    counter += 1



    print(' '.join(text_as_list))


launcher(email_four, proprietary_terms, negative_words, "*")
