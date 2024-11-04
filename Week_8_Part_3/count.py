
f = open("file.txt", "r")


lines = f.readlines()

num_lines = 0
num_words = 0
num_characters = 0


for line in lines:
    num_lines += 1  
    num_characters += len(line)  
    num_words += len(line.split())  


f.close()


print("Number of lines:", num_lines)
print("Number of words:", num_words)
print("Number of characters:", num_characters)
