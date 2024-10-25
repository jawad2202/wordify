import pytest
from project import text_to_speech, text_to_file, speed_control

def test_text_to_speech():
    #1 Test if the function executes without any errors
    text_to_speech("This is a test.")

def test_text_to_file():
    #2 Test if the function executes without any errors
    text_to_file("This is a test.", "output.wav")

def test_speed_control():
    #3 Test if the function executes without any errors
    speed_control(2)
    speed_control(-1)