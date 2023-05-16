def append_after(filename="", search_string="", new_string=""):
    with open(filename, encoding="utf-8") as my_file:
        lines = my_file.readlines()
    with open(filename, 'a', encoding="utf-8") as my_file:
        for i, line in enumerate(lines):
            if search_string in lines:
                lines.insert(i+1, new_string, + '\n'