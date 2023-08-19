import re

input_str = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
print('original string:', input_str)
#normalizing string form letter case point
#list of possible separators which should be followed with upper case
list_of_separators = {'.', '. ', '?', '? ', '!', '! ', "\n\t", "\n\t "}
normalized_str = input_str.capitalize()
new_sentence = ''
for sep in list_of_separators:
    normalized_str_list = normalized_str.split(sep)
    for index, s_str in enumerate(normalized_str_list):
        normalized_str_list[index] = s_str[0].upper() + s_str[1:]
        if sep == '.':
            str_words = s_str.split(' ')
            if index == 0:
                new_sentence = str(str_words[len(str_words) - 1]).capitalize()
            else:
                new_sentence += ' ' + str_words[len(str_words) - 1]
    normalized_str = sep.join(normalized_str_list)
normalized_str += new_sentence.replace('\n', '').rstrip() + '.'
print('normalized string:', normalized_str)

# correcting misspelling of "iz"
pattern = re.compile(r"(?:^|[^a-z“])iz(?![a-z“])", re.I)
normalized_str_list = normalized_str.split(' ')
for index, s_str in enumerate(normalized_str_list):
    if s_str.lower() == 'iz':
        normalized_str_list[index] = s_str[0] + 's'
    else:
        match = pattern.search(s_str)
        if match:
            print(s_str)
            start, end = match.span()
            print(match.span())
            i_str = start
            while i_str < end - 1:
                if s_str[i_str].lower() == 'i' and s_str[i_str + 1].lower() == 'z':
                    normalized_str_list[index]  = s_str[:i_str + 1] + 's' + s_str[(i_str + 2):]
                i_str += 1
str_without_misspelling = ' '.join(normalized_str_list)

print('string with corrected misspelling:', str_without_misspelling)
# count the number of whitespaces.
str_without_whitespaces = re.sub('[ \n\t]', '', input_str)
print('number of whitespaces: ', len(input_str) - len(str_without_whitespaces))

