"""Mad Libs Game."""
import sys


def welcome():
    """Welcome message and instructions for game."""
    print('Welcome to Mad Libs! and some instructions')


def word_types(template_filepath):
    """Read template file and make a list of needed word types."""
    with open(template_filepath, 'r') as fh:
        prompts = []
        content = fh.read().split()
        for word in content:
            if word[0] == '{' and word[-1] == '}':
                prompts.append(word[1:-1])
        return prompts

        # return fh.read()
        # return fh.readlines()
    # try/except FileNotFoundError:
    #     print('File Not Found. Try again.')


def user_input(word_types):
    """Collect user input."""
    print('Enter the appropriate words types:\n')
    words = []
    for word_type in word_types:
        words.append(input(f'Enter a {word_type}:  '))
    return words


def populate_template(words):
    """Populate the template with the user input."""
    return ''


def the_end(madlib):
    """Print resulting MadLib to user and output to new file."""
    print('MadLib')
    # print to file


def main():
    """Main function."""
    welcome()
    prompts = word_types(sys.argv[1])
    words = user_input(prompts)


if __name__ == "__main__":
    main()
