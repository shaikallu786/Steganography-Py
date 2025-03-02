import cv2
import numpy as np
from PIL import Image, ImageTk
import sys

try:
    from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
except ImportError:
    print("Error: Tkinter module is not installed. Please install it using 'sudo apt-get install python3-tk' or 'pip install tk'.")
    sys.exit(1)

# Function to encrypt and encode the message into an image
def encode_message(image_path, message, passcode, output_path):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Cannot open image!")
        return
    
    message = passcode + message + "@@@"  # Include passcode and end marker
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    
    data_index = 0
    binary_length = len(binary_message)
    rows, cols, _ = img.shape
    
    for row in range(rows):
        for col in range(cols):
            pixel = img[row, col]
            for channel in range(3):
                if data_index < binary_length:
                    pixel[channel] = pixel[channel] & 254 | int(binary_message[data_index])
                    data_index += 1
    
    cv2.imwrite(output_path, img)
    messagebox.showinfo("Success", "Message encrypted and hidden successfully!")

# Function to decrypt and retrieve the message from an image
def decode_message(image_path, passcode):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Cannot open image!")
        return ""
    
    binary_message = ""
    rows, cols, _ = img.shape
    
    for row in range(rows):
        for col in range(cols):
            pixel = img[row, col]
            for channel in range(3):
                binary_message += str(pixel[channel] & 1)
    
    message = "".join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    message = message.split("@@@")[0]
    
    if message.startswith(passcode):
        return message[len(passcode):]
    else:
        messagebox.showerror("Error", "Incorrect passcode!")
        return ""

# GUI Application
class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography")
        self.root.geometry("500x450")
        
        self.image_path = ""
        
        Label(root, text="Secure Image Steganography", font=("Arial", 16)).pack(pady=10)
        
        self.load_btn = Button(root, text="Select Image", command=self.load_image)
        self.load_btn.pack(pady=5)
        
        self.image_label = Label(root)
        self.image_label.pack(pady=5)
        
        self.message_entry = Entry(root, width=50)
        self.message_entry.pack(pady=5)
        self.passcode_entry = Entry(root, width=50, show='*')
        self.passcode_entry.pack(pady=5)
        
        self.encode_btn = Button(root, text="Encrypt & Hide Message", command=self.encode)
        self.encode_btn.pack(pady=5)
        
        self.decode_btn = Button(root, text="Decrypt Message", command=self.decode)
        self.decode_btn.pack(pady=5)
        
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            img = Image.open(file_path)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
    
    def encode(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please load an image first!")
            return
        message = self.message_entry.get()
        passcode = self.passcode_entry.get()
        if not message or not passcode:
            messagebox.showwarning("Warning", "Please enter a message and passcode!")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if output_path:
            encode_message(self.image_path, message, passcode, output_path)
    
    def decode(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please load an image first!")
            return
        passcode = self.passcode_entry.get()
        if not passcode:
            messagebox.showwarning("Warning", "Please enter the passcode!")
            return
        decoded_message = decode_message(self.image_path, passcode)
        if decoded_message:
            messagebox.showinfo("Decoded Message", decoded_message)

if __name__ == "__main__":
    root = Tk()
    app = SteganographyApp(root)
    root.mainloop()
