#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
from tkinter import scrolledtext
import random

# Define responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What do you need help with?"],
    "options": ["What information do you need about the college?",
                "How can I assist you with information about the college?"],
    "courses": "We offer a wide range of courses including CSE,CAI,ECE,EEE,ME,CE and more",
    "facilities": "Our college provides state-of-the-art facilities including libraries, labs, and sports amenities.",
    "location": "Our college is located at Yerrakota,Yemmiganur.",
    "contact": "You can contact the college at 123456789 or via email at sjcetsjcet@gmail.com.",
    "farewell": ["Thank you for reaching out! Have a great day!", "Goodbye! If you have any more questions, feel free to ask."]
}

# Define chatbot logic
def get_response(message):
    message = message.lower()
    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])
    elif "course" in message:
        return responses["courses"]
    elif any(word in message for word in ["facility", "facilities"]):
        return responses["facilities"]
    elif any(word in message for word in ["location", "where"]):
        return responses["location"]
    elif any(word in message for word in ["contact", "phone", "email"]):
        return responses["contact"]
    elif any(word in message for word in ["thank", "bye"]):
        return random.choice(responses["farewell"])
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

# Define GUI
def send():
    message = entry.get()
    if message.strip() != "":
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        response = get_response(message)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Bot: " + response + "\n")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)

# Create GUI
root = tk.Tk()
root.title("College Chatbot")
root.geometry("400x400")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
chat_box.config(state=tk.DISABLED)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send)
send_button.pack()

root.mainloop()


# In[ ]:


import nltk
from nltk.tokenize import word_tokenize

# Initialize NLTK
nltk.download('punkt')

# Sample software installation function
def install_software(software_name, operating_system):
    # Implement installation logic here
    print(f"Installing {software_name} on {operating_system}...")

def process_input(user_input):
    # Tokenize user input
    tokens = word_tokenize(user_input)
    
    # Simple intent recognition
    if 'install' in tokens and 'software' in tokens:
        # Extract software name
        software_name = tokens[tokens.index('software') + 1]
        
        # Extract operating system (if mentioned)
        operating_system = 'Windows'  # Default to Windows
        if 'on' in tokens:
            os_index = tokens.index('on')
            if os_index + 1 < len(tokens):
                operating_system = tokens[os_index + 1]
        
        # Call install function
        install_software(software_name, operating_system)
    else:
        print("Sorry, I didn't understand that.")

def main():
    print("Welcome to Software Installation Bot!")
    print("You can ask me to install software.")
    print("Example: 'Can you install VLC on Windows?'")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        process_input(user_input)

if __name__ == "__main__":
    main()


# In[2]:


import nltk
nltk.download()


# In[ ]:


pip install nltk


# In[ ]:


import os

def play_song(song_name):
    # Replace 'songs_folder' with the directory where your songs are stored
    songs_folder = "C:/Users/Public/Gskd/AAI/Songs"
    
    # Check if the song exists in the songs folder
    if os.path.exists(os.path.join(songs_folder, song_name)):
        # Assuming you have a media player installed that can play mp3 files
        os.system(f"start {os.path.join(songs_folder, song_name)}")
    else:
        print(f"Sorry, {song_name} not found in the songs folder.")

def main():
    while True:
        command = input("What song would you like to play? (Type 'quit' to exit): ")
        if command.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            play_song(command)

if __name__ == "__main__":
    main()


# In[10]:


from pytube import YouTube

def download_youtube_audio(youtube_url, output_path=""):
    try:
        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if output_path:
            audio_stream.download(output_path=output_path)
        else:
            audio_stream.download()
        print("Audio downloaded successfully.")
    except Exception as e:
        print("Error downloading audio:", e)

def main():
    youtube_url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output directory (leave blank for current directory): ")
    download_youtube_audio(youtube_url, output_path)

if __name__ == "__main__":
    main()


# In[ ]:


import requests
import os

def download_image(image_url, output_dir="."):
    try:
        # Send a GET request to the image URL
        response = requests.get(image_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Get the filename from the URL
            filename = os.path.basename(image_url)
            
            # Save the image file
            image_file = os.path.join(output_dir, filename)
            with open(image_file, "wb") as f:
                f.write(response.content)
            
            print("Image downloaded successfully.")
            return image_file
        else:
            print("Failed to retrieve image URL:", response.status_code)
            return None
    except Exception as e:
        print("Error downloading image:", e)
        return None

def main():
    image_url = input("Enter the URL of the image: ")
    output_dir = input("Enter the output directory to save the image (leave blank for current directory): ")
    if not output_dir:
        output_dir = "."
    download_image(image_url, output_dir)

if __name__ == "__main__":
    main()


# In[1]:


import requests

def download_webpage(url, output_file="webpage.html"):
    try:
        # Send a GET request to the webpage URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the HTML content to a file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(response.text)
            
            print("Webpage downloaded successfully.")
            return output_file
        else:
            print("Failed to retrieve webpage URL:", response.status_code)
            return None
    except Exception as e:
        print("Error downloading webpage:", e)
        return None

def main():
    webpage_url = input("Enter the URL of the webpage: ")
    output_file = input("Enter the output filename to save the webpage (leave blank for 'webpage.html'): ")
    if not output_file:
        output_file = "webpage.html"
    download_webpage(webpage_url, output_file)

if __name__ == "__main__":
    main()


# In[6]:


import os
import requests

def download_webpage(url, output_file):
    try:
        # Send a GET request to the webpage URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the HTML content to the specified output file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(response.text)
            
            print("Webpage downloaded successfully.")
            return output_file
        else:
            print("Failed to retrieve webpage URL:", response.status_code)
            return None
    except Exception as e:
        print("Error downloading webpage:", e)
        return None

def main():
    webpage_url = input("Enter the URL of the webpage: ")
    output_folder = "C:/Users/Public/Gskd/AAI/Songs/"
    
    output_file = os.path.join(output_folder, "webpage.html")
    download_webpage(webpage_url, output_file)

if __name__ == "__main__":
    main()


# In[11]:


import os
import requests

def download_webpage(url, output_dir=".", filename="webpage.html"):
    try:
        # Send a GET request to the webpage URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the HTML content to a file
            output_path = os.path.join(output_dir, filename)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            
            print("Webpage downloaded successfully.")
            return output_path
        else:
            print("Failed to retrieve webpage URL:", response.status_code)
            return None
    except Exception as e:
        print("Error downloading webpage:", e)
        return None

def main():
    webpage_url = input("Enter the URL of the webpage: ")
    output_dir = "C:/Users/Public/Gskd/AAI/Songs/"
    if not output_dir:
        output_dir = "."
    filename = input("Enter the filename to save the webpage (leave blank for 'webpage.html'): ")
    if not filename:
        filename = "webpage.html"
    download_webpage(webpage_url, output_dir, filename)

if __name__ == "__main__":
    main()


# In[ ]:


from moviepy.editor import *

def convert_mp4_to_mp3(input_file, output_file):
    try:
        # Load the MP4 file
        video_clip = VideoFileClip(input_file)
        
        # Extract the audio from the video clip
        audio_clip = video_clip.audio
        
        # Save the audio clip as an MP3 file
        audio_clip.write_audiofile(output_file)
        
        print("Conversion successful.")
    except Exception as e:
        print("Error converting MP4 to MP3:", e)

def main():
    input_file = input("Enter the path to the input MP4 file: ")
    output_file = input("Enter the path to save the output MP3 file: ")
    convert_mp4_to_mp3(input_file, output_file)

if __name__ == "__main__":
    main()


# In[3]:


import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

def convert_to_mp3(input_file, output_file):
    try:
        video_clip = VideoFileClip(input_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_file)
        audio_clip.close()
        video_clip.close()
        print("Conversion completed successfully.")
    except Exception as e:
        print("Error converting file:", e)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def convert_file():
    input_file = entry.get()
    if not input_file:
        print("Please select a file to convert.")
        return
    output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if output_file:
        convert_to_mp3(input_file, output_file)

# Create the main window
root = tk.Tk()
root.title("MP4 to MP3 Converter")

# Create widgets
label = tk.Label(root, text="Select an MP4 file:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

convert_button = tk.Button(root, text="Convert to MP3", command=convert_file)
convert_button.pack()

# Run the main event loop
root.mainloop()


# In[ ]:




