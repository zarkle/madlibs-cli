"""Mad Libs Game."""


def welcome():
    """Welcome message and instructions for game."""
    print('Welcome to Mad Libs! and some instructions')


def word_types(template_filepath):
    """Read template file and make a list of needed word types."""
    with open(template_filepath, 'r') as fh:
        return fh.read()


def user_input(word_types):
    """Collect user input."""
    return []


def populate_template(words):
    """Populate the template with the user input."""
    return ''


def the_end(madlib):
    """Print resulting MadLib to user and output to new file."""
    print('MadLib')
    # print to file


if __name__ == "__main__":
    welcome()
