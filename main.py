import requests
import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for num_page in range(len(reader.pages)):
            text += reader.pages[num_page].extract_text()
    return text


# Extract text from your PDF
pdf_path = input("Enter your pdf path: ")
pdf_text = extract_text_from_pdf(pdf_path)
pdf_text = "Hello MrSaad"

# Prepare the VoiceRSS API request
api_key = "Your Key"
params = {
    "key": api_key,
    "src": pdf_text,
    "hl": "en-gb",
    "v": "Harry",
    "c": "MP3",
    "f": "44khz_16bit_stereo"
}

# Send the request
response = requests.get("http://api.voicerss.org/", params=params)

# Save the audio file
audio_file_name = input("Enter name of audoi file without .mp3 extention: ")
with open(f"{audio_file_name}.mp3", "wb") as audio_file:
    audio_file.write(response.content)