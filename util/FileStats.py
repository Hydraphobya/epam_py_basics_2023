import csv
import re

TEXT_DEF = "Text sample to test the code. Some more text here! And something about weather, politics and stuff."
SCV_FILE_PATH = "c:\\Users\\Hanna_Hlushakova\\Documents\\Cources\\Python\\Files\\"


def get_letters_stats(text: str = TEXT_DEF) -> list:
    result_list = []
    stats_dict = {}
    count_total = 0
    for letter in text:
        if re.match('[a-z]', letter, re.IGNORECASE):
            count_total += 1
            if letter.lower() in stats_dict:
                stats_dict[letter.lower()] = [stats_dict[letter.lower()][0] + 1,
                                              stats_dict[letter.lower()][1] + int(letter.isupper())]
            else:
                stats_dict[letter.lower()] = [1, int(letter.isupper())]
    for d_key, d_value in stats_dict.items():
        result_list.append({'letter': d_key,
                            'count_all': d_value[0],
                            'count_uppercase': d_value[1],
                            'percentage': round(d_value[0] / count_total, 2) * 100})
    return result_list


def get_words_count(text: str = TEXT_DEF) -> list:
    words = re.split(f'[ .\-,;:?!\t\n''"]', text.lower())
    words_dict = {}
    result_list = []
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    for key, value in words_dict.items():
        if len(key):
            result_list.append({'word': key, 'count': value})
    return result_list


def print_text_stat(input_text: str = TEXT_DEF, output_file_path: str = SCV_FILE_PATH):
    # publish text letter's statistics
    ls_fields_name = ['letter', 'count_all', 'count_uppercase', 'percentage']
    __write_scv(ls_fields_name, get_letters_stats(input_text), output_file_path + 'letters_count.csv')
    # publish text word's statistics
    ws_fields_name = ['word', 'count']
    __write_scv(ws_fields_name, get_words_count(input_text), output_file_path + 'words_count.csv', add_header=False)


def __write_scv(fieldnames: list, input_data: list, file_path: str = SCV_FILE_PATH, add_header: bool = True) -> None:
    with open(file_path, mode='w', newline='') as csv_file:
        csv_file_writer = csv.DictWriter(
            csv_file,
            fieldnames,
            delimiter='|',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )
        if add_header:
            csv_file_writer.writeheader()
        csv_file_writer.writerows(input_data)


if __name__ == "__main__":
    print_text_stat()