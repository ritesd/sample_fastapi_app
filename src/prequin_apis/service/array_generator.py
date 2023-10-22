import random

def sentence_to_random_array(input_sentence: str) -> list:
    # Tokenize the input sentence into words
    words = input_sentence.split()
    
    # Initialize a 500-dimensional array with random float values
    random_array = [random.uniform(0, 1) for _ in range(500)]
    
    # Map words to indices in the array and add their values
    for word in words:
        # Use a hash function or any method to map the word to an index in the array
        # Here, we're using a simple hash function that sums the ASCII values of the characters in the word
        index = sum(ord(char) for char in word) % 500
        
        # Add the value to the array at the calculated index
        random_array[index] += 1.0
    
    return random_array