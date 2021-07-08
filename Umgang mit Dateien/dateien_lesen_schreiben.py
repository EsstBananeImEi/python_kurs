# Datei Lesen

with open("../Materialien/test_file_read.txt") as testfile:
    found = []
    for counter, line in enumerate(testfile):

        # print(line.strip())
        if "most" in line.strip().lower():
            splitted_line = line.strip().split(" ")
            word_positon = [i + 1 for i, x in enumerate(splitted_line) if x.lower() == "most"][0]
            found.append({"line_number": counter+1,
                          "word_number": word_positon})

    for item in found:
        print(item)

# Datei Schreiben
with open("../Materialien/test_file_write.txt", "w") as testfile:
    testfile.write("Hallo Welt")
