def get_num_words(text):
    word_list = text.split() # Splits the entire novel into a list of individual words
    return len(word_list) # Returns the length of the new split list 

def get_character_count(text):
    count_dict = {}
    word_list = text.split() # Splits the entire novel into a list of individual words
    for word in word_list:
        for character in word:
            lowercase_character = str.lower(character)
            if lowercase_character in count_dict:
                count_dict[lowercase_character] += 1
            else:
                count_dict[lowercase_character] = 1
    return count_dict

def get_sorted_dict(text):
    count_dict = {} # Creates an empty dictionary that we will fill up with characters and their counts
    report_list = []
    word_list = text.split() # Splits the entire novel into a list of individual words
    for word in word_list: # Iterate over each word in the text
        for character in word: # Iterate over each character in each word
            lowercase_character = str.lower(character) # Create a new variable that changes an uppercase letter to lowercase
            if lowercase_character in count_dict: # If the character is already in our dictionary,
                count_dict[lowercase_character] += 1 # Add a count to the key/value pair
            else: # If not,
                count_dict[lowercase_character] = 1 # Add a new key/value pair and start the count at one since it's the first occurrence
    list_of_count_dicts = [{"character": key, "count": value} for key, value in count_dict.items()] # Creates a list of dictionaries for each key-value pair
    list_of_count_dicts.sort(reverse=True, key=lambda x: x["count"]) # Sort our list of dictionaries by highest first (reverse=True) with a lambda function that sets the key equal to the "count" value in each dictionary
    for entry in list_of_count_dicts: # Iterate over the sorted list
        if entry["character"].isalpha(): # If the list entry is alphabetical,
            report_list.append(f"{entry['character']}: {entry['count']}") # Append the entry using this format
        # If the entry isn't alphabetical, nothing happens
    return report_list