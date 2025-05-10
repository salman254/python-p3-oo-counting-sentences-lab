#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            # Print message instead of raising an exception to match test expectation
            print("The value must be a string.")

    def is_sentence(self):
        # Check if the value ends with a period
        return self._value.endswith(".")

    def is_question(self):
        # Check if the value ends with a question mark
        return self._value.endswith("?")

    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self._value.endswith("!")

    def count_sentences(self):
        # Replace question marks and exclamations with periods for easier splitting
        cleaned = self._value.replace("?", ".").replace("!", ".")
        # Split on periods and remove empty strings
        sentences = [s.strip() for s in cleaned.split(".") if s.strip()]
        return len(sentences)
