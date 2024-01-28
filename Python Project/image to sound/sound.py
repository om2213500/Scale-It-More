from PIL import Image
import pytesseract
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image_path = 'img_1.jpg'  
img = Image.open(image_path)


text = pytesseract.image_to_string(img)

tts = gTTS(text, lang='en')  # 'en' represents English; change as needed


output_audio_file = 'output_audio.mp3'
tts.save(output_audio_file)

# Play the audio (optional)
os.system("mpg321 " + output_audio_file)  


