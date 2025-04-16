import sys
from stats import get_num_words, get_sorted_dict

def get_book_text(filepath): # Takes filepath provided in sys.argv[1] as input
    with open(filepath) as f:  # Opens the file path, sets it to f
        file_contents = f.read() # Read the file (our book)
    return file_contents # Return the entire text of the read book

def main():
    if len(sys.argv) < 2: # If a filepath is not provided, ie the sys.argv is less than two arugments
        print("Usage: python3 main.py <path_to_book>") # Show instructions on how to use the function
        sys.exit(1) # Exit program with a status code of 1
    else:
        text = get_book_text(sys.argv[1]) # Set text equal to the entire book supplied in the filepath provided in the second part of the input
        word_count = get_num_words(text) # Splits the entire book text string into individual word strings
        sorted_report = get_sorted_dict(text) # Returns a sorted list of alphabetical characters and their count in the book
        print("============ BOOKBOT ============") # Begin report format
        print(f"Analyzing book found at {sys.argv[1]}...") 
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words") 
        print("--------- Character Count -------")
        for line in sorted_report: # For each item in our list, 
            print(line) # Print the key/value pair.  This helps with readability vs printing the list alone

main()