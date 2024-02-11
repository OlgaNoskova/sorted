def sorted_file(*files):
    file_dict = {}
    for file in files:
        with open(file, encoding='UTF-8') as f:
            lines = f.readlines()
            file_dict[file] = len(lines)
    num_lines = list(file_dict.items())
    num_lines.sort(key=lambda a: a[1])
    for i in range(len(num_lines)):
        with open(str(num_lines[i][0]), encoding='UTF-8') as f:
            s = f.read()
        with open('sorted.txt', 'a', encoding='UTF-8') as file:
            file.write(s)
            file.write('\n')


sorted_file("1.txt", "2.txt", "3.txt")