import speech_recognition as sr
import pyttsx3
import wikipedia

def speak(text):
  """Speaks the given text."""
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def listen():
  """Listens for speech and returns the recognized text."""
  r = sr.Recognizer()
  with sr.Microphone() as source:
    audio = r.listen(source)

  try:
    text = r.recognize_google(audio)
  except sr.UnknownValueError:
    text = "I couldn't understand that."

  return text

def main():
  """Runs the voice assistant."""
  while True:
    command = listen()

    if command == "exit":
      break

    elif command == "what is the time":
      current_time = datetime.datetime.now().strftime("%H:%M:%S")
      speak("The time is now " + current_time)

    elif command.startswith("what is"):

      query = command.split("what is")[1]
      summary = wikipedia.summary(query)
      speak(summary)

    else:
      speak("hey how are you ")

if __name__ == '__main__':
  main()
