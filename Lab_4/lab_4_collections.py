import random


def generate_input_data(l_dict_count, l_dict_length):
    iter_i = 0
    l_dict_list = []
    keys_str = "abcdefghijklmnopqrstuvwxyz"
    while iter_i < l_dict_count:
        m_dict = {}
        iter_j = 0
        while iter_j < l_dict_length:
            d_key = keys_str[random.randint(0, len(keys_str) - 1)]
            d_value = random.randint(0, 100)
            m_dict[d_key] = d_value
            iter_j += 1
        l_dict_list.append(m_dict.copy())
        m_dict.clear()
        iter_i += 1
    return l_dict_list


def combine_dicts(l_dict_list):
    l_combined_dic = {}
    i_d = 0
    while i_d < len(l_dict_list):
        for i_key, i_value in l_dict_list[i_d].items():
            if i_key in l_combined_dic:
                if i_value > l_combined_dic[i_key][0]:
                    l_combined_dic[i_key] = [i_value, i_d, True]
                else:
                    l_combined_dic[i_key][2] = True
            else:
                l_combined_dic[i_key] = [i_value, i_d, False]
        i_d += 1
    return l_combined_dic


def formatted_dict(l_dict):
    l_combined_dict = combine_dicts(l_dict)
    result_dic = {}
    for cd_key, cd_value in l_combined_dict.items():
        if cd_value[2]:
            r_key = cd_key + '_' + str(cd_value[1] + 1)
            result_dic[r_key] = cd_value[0]
        else:
            result_dic[cd_key] = cd_value[0]
    return result_dic


min_count = 2
max_count = 10
dicts_count = random.randint(min_count, max_count)
dict_len = random.randint(min_count, max_count)
dict_list = generate_input_data(dicts_count, dict_len)
print(f'Generated data: {dict_list}. ')
result_dict = formatted_dict(dict_list)
print(f'Result dictionary: {result_dict}. ')
