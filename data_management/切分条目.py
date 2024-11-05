import json


def read_original_file():
    file_path = "../post_ocr/清代诗文集汇编总目录.txt"
    with open(file_path, "r", encoding='utf-8-sig') as original_file:
        data = original_file.readlines()
    # print(data)
    return data


def delete_ce(lst):
    after_del_list = [i for i in lst if not (i.startswith("第") and i.endswith("册\n"))]
    return after_del_list


def transfer_to_dict(lst):
    entry = {}
    index = 1
    key_list = []
    for i in range(len(lst)):
        if "卷" in lst[i] and ("本" in lst[i-1] or "年" in lst[i-1]):
            if key_list:  # 如果已经有一个条目，先把上一个条目存入字典
                entry[index] = key_list
                index += 1
            key_list = [lst[i]]  # 初始化新条目
        else:
            key_list.append(lst[i])
    if key_list:
        entry[index] = key_list
    return entry


def save_dict_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    original_list = read_original_file()
    new_list = delete_ce(original_list)
    entry_dict = transfer_to_dict(new_list)
    # print(entry_dict)
    save_dict_to_json(entry_dict, "relay_file/条目切分后.json")


if __name__ == "__main__":
    main()
