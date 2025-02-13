# Text Processor

TextProcessor is a Python utility that provides comprehensive text analysis and manipulation capabilities using various data structures like stacks, queues, and linked lists. It offers features for character and word frequency analysis, text reversal, word searching, and basic text statistics.

![Screenshot1](https://github.com/user-attachments/assets/63da7392-8344-4ae7-93d7-a9c4cb263d03)

# Features

- Character frequency analysis
- Word frequency counting
- Text reversal using stack implementation
- FIFO (First-In-First-Out) word processing using queue
- Linked list-based word storage and traversal
- Case-sensitive/insensitive word search functionality
- Word replacement with case sensitivity options
- Text statistics including:

   - Total word count
   - Unique word count
   - Sentence count
   - Average word length

 
# Installation

1. Ensure you have Python 3.x installed on your system
2. Clone this repository or download the Text_Processor.py file
3. Install required dependencies

# Class Structure

The implementation includes several key classes:

- TextProcessorGUI: Main class for the graphical user interface
- TextProcessor: Main class for text processing and analysis
- Stack: Implementation of stack data structure for character reversal
- Queue: Implementation of queue data structure for FIFO word processing
- Node: Basic node structure for linked list implementation
- LinkedList: Implementation of linked list for word storage


# Methods

Main TextProcessor Methods

- get_char_frequencies(): Returns dictionary of character frequencies
- get_word_frequencies(): Returns dictionary of word frequencies
- get_reversed_string(): Returns the text reversed using stack implementation
- get_fifo_words(): Returns list of words in FIFO order
- get_linked_list_words(): Returns list of words stored in linked list
- search_word(search_term, case_sensitive): Searches for word occurrences
- replace_word(search_term, replacement, case_sensitive): Replaces words in text
- get_sentence_count(): Returns the number of sentences
- get_average_word_length(): Returns average word length
- analyze_text(): Returns comprehensive text analysis
