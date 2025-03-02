# Image Steganography in Python
<h2>Overview</h2>
This project implements an Image Steganography tool in Python, allowing users to securely hide and retrieve messages within images using Least Significant Bit (LSB) encoding. The tool provides passcode protection to ensure that only authorized users can decode the hidden message. This project demonstrates image manipulation, secure communication, and data protection techniques using OpenCV and NumPy.

<h2>Features</h2>
✅ Encrypt and Decrypt Messages – Hide and retrieve secret messages inside images.
✅ Passcode Protection – Ensures only authorized access to hidden messages.
✅ Lossless Encoding – The message is hidden without noticeable changes to the image.
✅ Cross-Platform Compatibility – Works on Windows, macOS, and Linux.
✅ Real-Time Status Updates – Displays encoding & decoding progress in the terminal.

<h2>Technology Used </h2>
Programming Language: Python

<h2>Libraries</h2>:

OpenCV (cv2) – For image processing
NumPy – For efficient pixel manipulation
Sys – For handling command-line execution
Platform Compatibility: Windows, macOS, Linux

<h2>Development Environment</h2>: PyCharm, VS Code, Jupyter Notebook

<h2>Installation</h2>
Clone the repository:
git clone https://github.com/YourGitHubUsername/Python-Image-Steganography.git
Install the required dependencies:
pip install opencv-python numpy
Run the script:
python steganography.py
Usage
Encrypt a Message:
Update test_choice = "1" in the script.
Set the correct image path, message, and passcode in the script.
Run the script to hide the message inside the image.
Decrypt a Message:
Update test_choice = "2" in the script.
Set the encoded image path and the correct passcode in the script.
Run the script to retrieve the hidden message.
Example
Decoded Message: Hidden message!
Contributing
Contributions are welcome! Fork the repository and submit a pull request with well-documented changes.

License
This project is open-source and available under the MIT License.

Contact
📌 Name: Shaik Allabakash
📌 Email: shaikallu0000@gmail.com
