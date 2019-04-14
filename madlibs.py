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
    #     sys.exit('File Not Found. Try again.')


def user_input(word_types):
    """Collect user input."""
    print('Enter the appropriate words types:\n')
    words = []
    for word_type in word_types:
        words.append(input(f'Enter a {word_type}:  '))
    return words


def populate_template(template_filepath, words):
    """Populate the template with the user input."""
    with open(template_filepath, 'r') as fh:
        content = fh.read()

    curr = 0
    new = ''
    for word in content.split():
        if word[0] == '{' and word[-1] == '}':
            new += f'{words[curr]} '
            curr += 1
        else:
            new += f'{word} '
    print(new)
    return new[:-1]


def the_end(madlib):
    """Print resulting MadLib to user and output to new file."""
    print(madlib)
    with open('madlib.txt', 'w') as fh:
        fh.write(madlib)


def main():
    """Main function."""
    template = sys.argv[1]
    welcome()
    prompts = word_types(template)
    words = user_input(prompts)
    new = populate_template(template, words)
    the_end(new)


if __name__ == "__main__":
    main()
