def count_words(text):
    """Function to count words in the given text."""
    try:
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")
        
        words = text.split()
        return len(words)

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    try:
        user_input = input("Enter a sentence or paragraph: ")
        word_count = count_words(user_input)

        if word_count is not None:
            print(f"Word Count: {word_count}")
    
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")