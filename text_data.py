import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

# Function to fetch and return article text
def fetch_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_content = soup.find_all('p')
    
    article_text = ""
    for paragraph in article_content:
        article_text += paragraph.get_text() + "\n"
    
    return article_text

# Function to display the text in the GUI and save it to a file
def display_and_save_article():
    url = url_entry.get()
    article_text = fetch_article_text(url)
    
    # Display text in the GUI
    text_area.delete(1.0, tk.END)  # Clear previous text
    text_area.insert(tk.INSERT, article_text)
    
    # Save text to a file
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if save_path:  # Check if a file path was provided
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(article_text)
        print(f"Article text saved to {save_path}")

# Create the main window
window = tk.Tk()
window.title("Article Text Viewer")

# Create an entry widget for the URL
url_label = tk.Label(window, text="Enter URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)

# Create a button to fetch, display, and save the article
fetch_button = tk.Button(window, text="Fetch and Save Article", command=display_and_save_article)
fetch_button.pack(pady=5)

# Create a scrolled text widget to display the article
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=20)
text_area.pack(padx=10, pady=10)

# Run the application
window.mainloop()
