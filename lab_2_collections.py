import random

# 1. create a list of random number of dicts (from 2 to 10)
# dictionary's random numbers of keys should be a letter,
# dictionary's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

dicts_count = random.randint(2, 10)
dict_len = random.randint(2, 10)
iter_i = 0
dict_list = []
keys_str = "abcdefghijklmnopqrstuvwxyz"
while iter_i < dicts_count:
    m_dict = {}
    iter_j = 0
    while iter_j < dict_len:
        d_key = keys_str[random.randint(0, len(keys_str) - 1)]
        d_value = random.randint(0, 100)
        m_dict[d_key] = d_value
        iter_j += 1
    dict_list.append(m_dict.copy())
    m_dict.clear()
    iter_i += 1
print('number of dictionaries: ', dicts_count)
print('number of a pairs in a dictionary', dict_len)
print('input: ', dict_list)

#
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# creating combined dictionary with will contain all keys from the dictionaries in input list
# as a value it will keep a list of 3 items
# 1st item is a current max value for corresponding key
# 2nd item is a number of a dictionary with that max value
# 3rd True in case if the key can be found in a few dictionaries, False if is unique
#
combined_dic = {}
i_d = 0
while i_d < len(dict_list):
    for i_key, i_value in dict_list[i_d].items():
        if i_key in combined_dic:
            if i_value > combined_dic[i_key][0]:
                combined_dic[i_key] = [i_value, i_d, True]
            else:
                combined_dic[i_key][2] = True
        else:
            combined_dic[i_key] = [i_value, i_d, False]
    i_d += 1

# creating result dictionary
# for each pair key value of combined dictionary produce a new entry in result dictionary
# if a key is unique value[2] == False : copy key and value to result
# else add to a key number of a default dictionary were the max value found
# and copy combined key with the value to the result dic
result_dic = {}
for cd_key, cd_value in combined_dic.items():
    if cd_value[2]:
        r_key = cd_key + '_' + str(cd_value[1] + 1)
        result_dic[r_key] = cd_value[0]
    else:
        result_dic[cd_key] = cd_value[0]

print('result:', result_dic)
