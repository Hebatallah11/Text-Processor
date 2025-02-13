

from collections import Counter
import re

class Stack:
    def __init__(self):
        self.items = []  
    
    def push(self, item):
        self.items.append(item)  
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  
        return None
    
    def is_empty(self):
        return len(self.items) == 0   

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  
        return None
    
    def is_empty(self):
        return len(self.items) == 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node   
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def traverse(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

class TextProcessor:
    def __init__(self, text):
        self.text = text 
        self.char_array = list(text) 
        self.words = text.split()   
        self.unique_words = set(self.words)   
        self.char_stack = Stack()  
        self.word_queue = Queue()   
        self.word_list = LinkedList()  
        
        # Initialize data structures
        self._initialize_structures() 
    
    def _initialize_structures(self):
        # Fill stack with characters
        for char in self.text:
            self.char_stack.push(char)
        
        # Fill queue with words
        for word in self.words:
            self.word_queue.enqueue(word)
            self.word_list.insert(word)
    
    def get_char_frequencies(self):
        return dict(Counter(self.char_array))
    
    def get_word_frequencies(self):
        return dict(Counter(self.words))
    
    def get_reversed_string(self):
        reversed_chars = []
        temp_stack = Stack()
        
        # Create a copy of the stack to preserve original
        while not self.char_stack.is_empty():
            char = self.char_stack.pop()
            reversed_chars.append(char)
            temp_stack.push(char)
        
        # Restore original stack
        while not temp_stack.is_empty():
            self.char_stack.push(temp_stack.pop())
            
        return ''.join(reversed_chars)
    
    def get_fifo_words(self):
        words_order = []
        temp_queue = Queue()
        
        # Create a copy of the queue to preserve original
        while not self.word_queue.is_empty():
            word = self.word_queue.dequeue()
            words_order.append(word)
            temp_queue.enqueue(word)
        
        # Restore original queue
        while not temp_queue.is_empty():
            self.word_queue.enqueue(temp_queue.dequeue())
            
        return words_order
    
    def get_linked_list_words(self):
        return self.word_list.traverse()

    def search_word(self, search_term: str, case_sensitive: bool = False):
        #Search for a word and return its positions
        positions = []
        words = self.text.split()
        
        for i, word in enumerate(words):
            if case_sensitive:
                if search_term == word:
                    positions.append((i, word))
            else:
                if search_term.lower() == word.lower():
                    positions.append((i, word))
        
        return positions

    def replace_word(self, search_term: str, replacement: str, case_sensitive: bool = False):
        #Replace all occurrences of a word and return the new text
        if case_sensitive:
            pattern = r'\b' + re.escape(search_term) + r'\b'  
            new_text = re.sub(pattern, replacement, self.text)
        else:
            pattern = r'\b' + re.escape(search_term) + r'\b'
            new_text = re.sub(pattern, replacement, self.text, flags=re.IGNORECASE)
        
        return new_text
    
    def get_sentence_count(self):
        #Count the number of sentences in the text
        # Simple sentence detection (ends with ., !, or ?)
        sentences = re.split(r'[.!?]+', self.text)
        # Filter out empty strings
        return len([s for s in sentences if s.strip()])

    def get_average_word_length(self):
        #Calculate the average word length
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return round(total_length / len(self.words), 2)
    
    def analyze_text(self):
        #Perform all text analysis and return results
        return {
            'char_frequencies': self.get_char_frequencies(),
            'word_frequencies': self.get_word_frequencies(),
            'reversed_string': self.get_reversed_string(),
            'fifo_words': self.get_fifo_words(),
            'linked_list_words': self.get_linked_list_words(),
            'total_words': len(self.words),
            'unique_words': len(self.unique_words),
            'sentence_count': self.get_sentence_count(),
            'avg_word_length': self.get_average_word_length()
        }

def display_menu():
    print("\n=== Text Processor Menu ===")
    print("1. Show character frequencies")
    print("2. Show word frequencies")
    print("3. Show reversed text")
    print("4. Show FIFO word order")
    print("5. Show linked list word order")
    print("6. Search for a word")
    print("7. Replace a word")
    print("8. Show text statistics")
    print("9. Process new text")
    print("0. Exit")
    return input("Choose an option (0-9): ")

def main():
    processor = None
    
    while True:
        if processor is None:
            text = input("Please enter your text to analyze: ")
            processor = TextProcessor(text)
        
        choice = display_menu()
        
        if choice == '0':
            print("Goodbye!")
            break
            
        elif choice == '1':
            char_freq = processor.get_char_frequencies()
            print("\n=== Character Frequencies ===")
            for char, freq in char_freq.items():
                char_display = "SPACE" if char.isspace() else char
                print(f"'{char_display}': {freq}")
                
        elif choice == '2':
            word_freq = processor.get_word_frequencies()
            print("\n=== Word Frequencies ===")
            for word, freq in word_freq.items():
                print(f"'{word}': {freq}")
                
        elif choice == '3':
            print("\n=== Reversed String ===")
            print(processor.get_reversed_string())
            
        elif choice == '4':
            print("\n=== Words in FIFO Order ===")
            print(" ".join(processor.get_fifo_words()))
            
        elif choice == '5':
            print("\n=== Words in Linked List Order ===")
            print(" ".join(processor.get_linked_list_words()))
            
        elif choice == '6':
            search_term = input("Enter word to search: ")
            case_sensitive = input("Case sensitive? (y/n): ").lower() == 'y'
            results = processor.search_word(search_term, case_sensitive)
            if results:
                print(f"\nFound '{search_term}' at positions: ")
                for pos, word in results:
                    print(f"Position {pos}: '{word}'")
            else:
                print(f"\nWord '{search_term}' not found.")
                
        elif choice == '7':
            search_term = input("Enter word to replace: ")
            replacement = input("Enter replacement word: ")
            case_sensitive = input("Case sensitive? (y/n): ").lower() == 'y'
            new_text = processor.replace_word(search_term, replacement, case_sensitive)
            print("\n=== Modified Text ===")
            print(new_text)
            
        elif choice == '8':
            results = processor.analyze_text()
            print("\n=== Text Statistics ===")
            print(f"Total words: {results['total_words']}")
            print(f"Unique words: {results['unique_words']}")
            print(f"Sentences: {results['sentence_count']}")
            print(f"Average word length: {results['avg_word_length']} characters")
            
        elif choice == '9':
            processor = None
            continue
            
        else:
            print("Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()