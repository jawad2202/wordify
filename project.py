import pyttsx3

def text_to_speech(text: str) -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def text_to_file(text: str, output_file: str) -> None:
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

def speed_control(speed: int) -> None:
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + speed)
    engine.say('Speed test')
    engine.runAndWait()

def main():
    input_text = input("Enter the text you want to convert to speech: ")
    text_to_speech(input_text)
    output_file = input("Enter the name of the output file (without extension) to save the speech as an audio file (e.g., output.wav): ")
    text_to_file(input_text, output_file)

if __name__ == "__main__":
    main()