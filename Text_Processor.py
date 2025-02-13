
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import messagebox
import re
from collections import Counter
from typing import List, Dict, Set

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
        self._initialize_structures()

    def _initialize_structures(self):
        for char in self.text:
            self.char_stack.push(char)
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
        while not self.char_stack.is_empty():
            char = self.char_stack.pop()
            reversed_chars.append(char)
            temp_stack.push(char)
        while not temp_stack.is_empty():
            self.char_stack.push(temp_stack.pop())
        return ''.join(reversed_chars)
   
    def get_fifo_words(self):
        words_order = []
        temp_queue = Queue()
        while not self.word_queue.is_empty():
            word = self.word_queue.dequeue()
            words_order.append(word)
            temp_queue.enqueue(word)
        while not temp_queue.is_empty():
            self.word_queue.enqueue(temp_queue.dequeue())
        return words_order
    
    def get_linked_list_words(self):
        return self.word_list.traverse()

    def search_word(self, search_term: str, case_sensitive: bool = False):
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
        if case_sensitive:
            pattern = r'\b' + re.escape(search_term) + r'\b'
            new_text = re.sub(pattern, replacement, self.text)
        else:
            pattern = r'\b' + re.escape(search_term) + r'\b'
            new_text = re.sub(pattern, replacement, self.text, flags=re.IGNORECASE)
        return new_text
    
    def get_sentence_count(self):
        sentences = re.split(r'[.!?]+', self.text)
        return len([s for s in sentences if s.strip()])

    def get_average_word_length(self):
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return round(total_length / len(self.words), 2)

class TextProcessorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Processor")
        self.processor = None
        self.setup_gui()

    def setup_gui(self):
        # Main content frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input section
        ttk.Label(main_frame, text="Enter Text:").grid(row=0, column=0, sticky=tk.W)
        self.text_input = scrolledtext.ScrolledText(main_frame, width=60, height=10)
        self.text_input.grid(row=1, column=0, columnspan=2, pady=5)

        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Analysis buttons
        ttk.Button(buttons_frame, text="Character Frequencies", 
                  command=self.show_char_frequencies).grid(row=0, column=0, padx=5)
        ttk.Button(buttons_frame, text="Word Frequencies", 
                  command=self.show_word_frequencies).grid(row=0, column=1, padx=5)
        ttk.Button(buttons_frame, text="Reverse Text", 
                  command=self.show_reversed).grid(row=0, column=2, padx=5)
        ttk.Button(buttons_frame, text="FIFO Words", 
                  command=self.show_fifo).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Linked List Words", 
                  command=self.show_linked_list).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Statistics", 
                  command=self.show_statistics).grid(row=1, column=2, padx=5, pady=5)

        # Search/Replace frame
        search_frame = ttk.LabelFrame(main_frame, text="Search and Replace", padding="5")
        search_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, padx=5)
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1, padx=5)

        ttk.Label(search_frame, text="Replace:").grid(row=0, column=2, padx=5)
        self.replace_entry = ttk.Entry(search_frame)
        self.replace_entry.grid(row=0, column=3, padx=5)

        self.case_sensitive_var = tk.BooleanVar()
        ttk.Checkbutton(search_frame, text="Case Sensitive", 
                       variable=self.case_sensitive_var).grid(row=0, column=4, padx=5)

        ttk.Button(search_frame, text="Search", 
                  command=self.search_text).grid(row=0, column=5, padx=5)
        ttk.Button(search_frame, text="Replace", 
                  command=self.replace_text).grid(row=0, column=6, padx=5)

        # Results section
        ttk.Label(main_frame, text="Results:").grid(row=4, column=0, sticky=tk.W, pady=(10,0))
        self.results_text = scrolledtext.ScrolledText(main_frame, width=60, height=10)
        self.results_text.grid(row=5, column=0, columnspan=2, pady=5)

    def process_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            self.processor = TextProcessor(text)
            return True
        else:
            messagebox.showwarning("Warning", "Please enter some text first!")
            return False

    def show_char_frequencies(self):
        if not self.process_text():
            return
        freq = self.processor.get_char_frequencies()
        result = "Character Frequencies:\n\n"
        for char, count in freq.items():
            char_display = "SPACE" if char.isspace() else char
            result += f"'{char_display}': {count}\n"
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", result)

    def show_word_frequencies(self):
        if not self.process_text():
            return
        freq = self.processor.get_word_frequencies()
        result = "Word Frequencies:\n\n"
        for word, count in freq.items():
            result += f"'{word}': {count}\n"
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", result)

    def show_reversed(self):
        if not self.process_text():
            return
        reversed_text = self.processor.get_reversed_string()
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", f"Reversed Text:\n\n{reversed_text}")

    def show_fifo(self):
        if not self.process_text():
            return
        fifo_words = self.processor.get_fifo_words()
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", f"Words in FIFO Order:\n\n{' '.join(fifo_words)}")

    def show_linked_list(self):
        if not self.process_text():
            return
        linked_list_words = self.processor.get_linked_list_words()
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", f"Words in Linked List Order:\n\n{' '.join(linked_list_words)}")

    def show_statistics(self):
        if not self.process_text():
            return
        result = "Text Statistics:\n\n"
        result += f"Total words: {len(self.processor.words)}\n"
        result += f"Unique words: {len(self.processor.unique_words)}\n"
        result += f"Sentences: {self.processor.get_sentence_count()}\n"
        result += f"Average word length: {self.processor.get_average_word_length()} characters"
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", result)

    def search_text(self):
        if not self.process_text():
            return
        search_term = self.search_entry.get().strip()
        if not search_term:
            messagebox.showwarning("Warning", "Please enter a search term!")
            return
        
        results = self.processor.search_word(search_term, self.case_sensitive_var.get())
        if results:
            result_text = f"Found '{search_term}' at positions:\n\n"
            for pos, word in results:
                result_text += f"Position {pos}: '{word}'\n"
        else:
            result_text = f"Word '{search_term}' not found."
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", result_text)

    def replace_text(self):
        if not self.process_text():
            return
        search_term = self.search_entry.get().strip()
        replacement = self.replace_entry.get().strip()
        
        if not search_term or not replacement:
            messagebox.showwarning("Warning", "Please enter both search and replacement terms!")
            return
        
        new_text = self.processor.replace_word(
            search_term, replacement, self.case_sensitive_var.get())
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", f"Modified Text:\n\n{new_text}")
        
        
def main():
    root = tk.Tk()
    app = TextProcessorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()