
import sys


def count_characters(text):
    
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = sum(1 for char in text if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())

    return upper_count, lower_count, punctuation_count, digit_count, space_count


def main():
    
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        raise AssertionError("More than one argument is provided")

    if text is None or text == "":
        print("No text provided.")
        return
    
    upper_count, lower_count, punctuation_count, digit_count, space_count = count_characters(text)

    
    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{digit_count} digits")
    print(f"{space_count} spaces")


if __name__ == "__main__":
    main()


