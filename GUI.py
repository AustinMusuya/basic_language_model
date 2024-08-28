import random
import tkinter as tk
from tkinter import scrolledtext
from collections import Counter

# Function to generate text and display it in the text area
def generate_text():
    word1 = word1_entry.get().strip().lower()
    word2 = word2_entry.get().strip().lower()

    if not word1 or not word2:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Please enter two words to start.")
        return

    generated_text = []

    for i in range(500):
        generated_text.append(word1)
        successors = successor_map.get((word1, word2), [""])
        word3 = random.choice(successors)
        word1 = word2
        word2 = word3
    
    # Display the generated text in the text area
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, ' '.join(generated_text))

# Prepare the bigram model
filename = './text.txt'
reader = open(filename, 'r', encoding='utf-8')
punctuation = '.;,-“’”:?—‘!()_'
successor_map = {}
window = []

for line in reader:
    for word in line.split():
        cleaned_word = word.lower().strip(punctuation)
        window.append(cleaned_word)
        if len(window) == 3:
            key = (window[0], window[1])  # Use a tuple of two words as the key
            if key in successor_map:
                successor_map[key].append(window[2])
            else:
                successor_map[key] = [window[2]]
            window.pop(0)

reader.close()

# Create the GUI
root = tk.Tk()
root.title("Bigram Text Generator")

# Create labels and entry fields for word1 and word2
word1_label = tk.Label(root, text="First Word:")
word1_label.pack(pady=5)
word1_entry = tk.Entry(root, width=20)
word1_entry.pack(pady=5)

word2_label = tk.Label(root, text="Second Word:")
word2_label.pack(pady=5)
word2_entry = tk.Entry(root, width=20)
word2_entry.pack(pady=5)

# Create a scrolled text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=250, height=30)
text_area.pack(pady=10)

# Create a button to generate text
generate_button = tk.Button(root, text="Generate Text", command=generate_text)
generate_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
