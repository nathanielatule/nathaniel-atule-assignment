try:
    file = open(r"C:\Users\SEDATECH\Desktop\PYTHON FILES\student. txt.txt", "r")
    content = file.read()
    file.close()

    words = content.split()
    word_count = len(words)

    result = open("result.txt", "w")
    result.write("Number of words: " + str(word_count))
    result.close()

    print("Word Count:", word_count)
    print("Result has been written to result.txt")

except FileNotFoundError:
    print("File not found.")


