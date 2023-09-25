import re
import time


# add functions to the lab 3
# Returns the number of whitespaces in the string


def decorator_factory():
    def decorator(func):
        def wrapper(*args):
            start_time = time.time()
            func_res = func(*args)
            end_time = time.time()
            print(f'Execution time: {end_time - start_time}')
            return func_res

        return wrapper

    return decorator


@decorator_factory()
def get_number_of_whitespaces(l_input_str):
    str_without_whitespaces = re.sub('[ \n\t]', '', l_input_str)
    num_of_whitespaces: int = len(l_input_str) - len(str_without_whitespaces)
    return num_of_whitespaces


@decorator_factory()
def correct_is_misspelling(l_input_str):
    pattern = re.compile(r"(?:^|[^a-z“])iz(?![a-z“])", re.I)
    str_list = l_input_str.split(' ')
    for index, s_str in enumerate(str_list):
        match = pattern.search(s_str)
        if match:
            start, end = match.span()
            str_list[index] = (
                    s_str[:(start + 1)]
                    + 's'
                    + s_str[(start + 2):]
            )
    str_without_misspelling = ' '.join(str_list)
    return str_without_misspelling


def capitalize_first_word(l_input_str):
    none_space_index = re.search('[^ ]', l_input_str).start()
    result_str = (
            l_input_str[:none_space_index]
            + l_input_str[none_space_index].upper()
            + l_input_str[(none_space_index + 1):]
    )
    return result_str


@decorator_factory()
def normalize_str(l_input_str):
    list_of_separators = {'.', '?', '!', "\n\t"}
    l_normalized_str = l_input_str.capitalize()
    for sep in list_of_separators:
        normalized_str_list = l_normalized_str.split(sep)
        for index, s_str in enumerate(normalized_str_list):
            normalized_str_list[index] = capitalize_first_word(s_str)
        l_normalized_str = sep.join(normalized_str_list)
    return l_normalized_str


def get_last_word(l_input_str):
    str_words = l_input_str.rstrip().split(' ')
    last_word = str_words[len(str_words) - 1]
    return last_word


@decorator_factory()
def build_sentence_from_last_words(l_input_str):
    list_str = l_input_str.split('.')
    result_sentence = ''
    for index, value_str in enumerate(list_str):
        result_sentence += ' ' + get_last_word(value_str)
    result_sentence = result_sentence.lstrip().rstrip().capitalize() + '.'
    return result_sentence



INPUT_STR = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


if __name__ == '__main__':
    whitespaces_number = get_number_of_whitespaces(INPUT_STR)
    print(f'Number of whitespaces: {whitespaces_number}.')
    fixed_str = correct_is_misspelling(INPUT_STR)
    print(f'String with corrected misspelling: "{fixed_str}".')
    normalized_str = normalize_str(fixed_str)
    print(f'Normalized string: "{normalized_str}"')
    whitespaces_number2 = get_number_of_whitespaces(normalized_str)
    print(f'Number of whitespaces in normalized string. Should be same as in the input string: {whitespaces_number2}.')
    additional_sentence = build_sentence_from_last_words(normalized_str)
    print(f'Last words sentence: "{additional_sentence}"')

