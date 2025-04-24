import re
from collections import Counter
import string

def read_article(file_path):
    """
    Read the contents of the provided news article file into a string variable.
    
    Args:
        file_path (str): Path to the news article text file.
        
    Returns:
        str: Content of the news article.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def count_specific_word(text, word):
    """
    Count the number of occurrences of a specified word in the text.
    
    Args:
        text (str): The text to analyze.
        word (str): The word to count.
        
    Returns:
        int: Number of occurrences of the specified word.
    """
    # Convert text to lowercase and use regex to find word boundaries
    pattern = r'\b' + re.escape(word.lower()) + r'\b'
    matches = re.findall(pattern, text.lower())
    return len(matches)

def identify_most_common_word(text):
    """
    Identify the most common word in the text.
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        tuple: (most_common_word, count)
    """
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower().translate(translator)
    
    # Split text into words
    words = text.split()
    
    # Count occurrences of each word
    word_counts = Counter(words)
    
    # Remove common stop words if present
    stop_words = ['the', 'and', 'a', 'to', 'of', 'in', 'is', 'it', 'that', 'for', 'on', 'with', 'as', 'was', 'are']
    for word in stop_words:
        if word in word_counts:
            del word_counts[word]
    
    # Find the most common word
    most_common = word_counts.most_common(1)[0]
    return most_common

def calculate_avg_word_length(text):
    """
    Calculate the average length of words in the text.
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        float: Average word length.
    """
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower().translate(translator)
    
    # Split text into words
    words = text.split()
    
    # Calculate average word length
    if words:
        total_length = sum(len(word) for word in words)
        avg_length = total_length / len(words)
        return avg_length
    else:
        return 0

def count_paragraphs(text):
    """
    Count the number of paragraphs in the text.
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        int: Number of paragraphs.
    """
    # Split text by double newlines to identify paragraphs
    paragraphs = re.split(r'\n\s*\n', text)
    
    # Filter out empty paragraphs
    paragraphs = [p for p in paragraphs if p.strip()]
    
    return len(paragraphs)

def count_sentences(text):
    """
    Count the number of sentences in the text.
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        int: Number of sentences.
    """
    # Use regex to split text by sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)
    
    # Filter out empty sentences
    sentences = [s for s in sentences if s.strip()]
    
    return len(sentences)

def main():
    """
    Main function to run the news article analysis.
    """
    print("News Article Analysis Program")
    print("============================")
    
    # Ask for file path
    file_path = input("Enter the path to the news article file: ")
    
    # Read article content
    article_content = read_article(file_path)
    
    if article_content:
        print("\nAnalysis Results:")
        print("----------------")
        
        # Implement a loop to allow the user to select different analysis options
        while True:
            print("\nSelect an analysis option:")
            print("1. Count occurrences of a specific word")
            print("2. Identify the most common word")
            print("3. Calculate average word length")
            print("4. Count number of paragraphs")
            print("5. Count number of sentences")
            print("6. Run all analyses")
            print("7. Exit")
            
            choice = input("\nEnter your choice (1-7): ")
            
            # Count specific word
            if choice == '1':
                word_to_count = input("Enter the word to count: ")
                count = count_specific_word(article_content, word_to_count)
                print(f"\nThe word '{word_to_count}' appears {count} times in the article.")
            
            # Most common word
            elif choice == '2':
                most_common = identify_most_common_word(article_content)
                print(f"\nThe most common word is '{most_common[0]}' with {most_common[1]} occurrences.")
            
            # Average word length
            elif choice == '3':
                avg_length = calculate_avg_word_length(article_content)
                print(f"\nThe average word length is {avg_length:.2f} characters.")
            
            # Count paragraphs
            elif choice == '4':
                num_paragraphs = count_paragraphs(article_content)
                print(f"\nThe article contains {num_paragraphs} paragraphs.")
            
            # Count sentences
            elif choice == '5':
                num_sentences = count_sentences(article_content)
                print(f"\nThe article contains {num_sentences} sentences.")
            
            # Run all analyses
            elif choice == '6':
                # Ask for specific word to count
                word_to_count = input("Enter a specific word to count: ")
                
                # Perform all analyses
                count = count_specific_word(article_content, word_to_count)
                most_common = identify_most_common_word(article_content)
                avg_length = calculate_avg_word_length(article_content)
                num_paragraphs = count_paragraphs(article_content)
                num_sentences = count_sentences(article_content)
                
                # Display all results
                print(f"\nAnalysis Results for the Article:")
                print(f"1. The word '{word_to_count}' appears {count} times.")
                print(f"2. The most common word is '{most_common[0]}' with {most_common[1]} occurrences.")
                print(f"3. The average word length is {avg_length:.2f} characters.")
                print(f"4. The article contains {num_paragraphs} paragraphs.")
                print(f"5. The article contains {num_sentences} sentences.")
            
            # Exit
            elif choice == '7':
                print("\nThank you for using the News Article Analysis Program!")
                break
            
            else:
                print("\nInvalid choice. Please enter a number between 1 and 7.")
    
    else:
        print("Unable to analyze the article. Please check the file path and try again.")

if __name__ == "__main__":
    main()