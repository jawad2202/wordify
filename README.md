# Wordify: A Simple Text-to-Speech Converter

#### Video Demo: [Wordify](https://www.youtube.com/watch?v=dROlFdGf4Gc)

#### Description:

Wordify is a straightforward Python project that provides a text-to-speech conversion feature. With this application, users can convert any text input into speech output. The project utilizes the `pyttsx3` library, which allows seamless text-to-speech conversion and supports various speech engines.

### How to Use Wordify

1. Download the source code.
2. Install Python 3.10 + if you haven't already.
3. Install the required libraries by running the following command in the project directory:
   ```
   pip install pytest
   ```
   ```
   pip install pyttsx3
   ```
4. Open a terminal or command prompt in the project directory.
5. Run the `project.py` file using Python:
   ```
   python project.py
   ```
6. Enter the text you want to convert to speech when prompted.
7. Choose whether you want to listen to the speech output directly or save it as an audio file.
8. If you choose to save the speech as an audio file, enter the desired name (without extension) for the output file.

### Functions and Features

Wordify provides the following functions:

1. `text_to_speech(text: str) -> None`: This function takes a string as input and converts it to speech using the pyttsx3 library. The generated speech is played out loud, allowing the user to hear the converted text.

2. `text_to_file(text: str, output_file: str) -> None`: This function takes a string as input and converts it to speech using pyttsx3. The generated speech is saved as an audio file with the given `output_file` name. This feature enables users to save the speech for later use or share it with others.

3. `speed_control(speed: int) -> None`: This function takes an integer `speed` as input and controls the speed of the generated speech. The `speed` value ranges from -10 to 10, where negative values slow down the speech, and positive values speed it up. This feature allows users to adjust the speech speed according to their preference.

### Testing

Wordify comes with a set of test functions to ensure the correctness of its core features. The test functions are defined in the `test_project.py` file. To run the tests, make sure you have `pytest` installed (you can install it via `pip install pytest`).  Then, execute the following command in the project directory:
```
pytest
```

### Conclusion

Wordify provides a simple and efficient solution for text-to-speech conversion. Whether you need to convert textual content to speech for accessibility purposes or just for fun, Wordify has you covered.

Created by- Jawad Rahman Shovon