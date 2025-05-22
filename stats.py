def get_num_words(file_contents):
             
        words = file_contents.split()        
        count = 0
        # Iterate through the list of words
        # and count the number of words
        for word in words:
            count += 1
        return count


def get_char_count(file_contents):
    """
    Function to add each character in file_contensts to a dictionary with letter as key and value as count. then return the dictionary
    :param file_contents: The contents of the file as a string.
    and return the dictionary.    
    """
    lower_file_contents = file_contents.lower()
    char_count = {}
    for char in lower_file_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_list(char_count):
    """
    Function to sort the dictionary by value and return a list of tuples
    :param char_count: The dictionary to be sorted.
    :return: A list of tuples sorted by count.
    """
    sorted_list = char_count.sort()
    

    return sorted_list


