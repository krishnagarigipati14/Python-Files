f = open("sorted_words_input.txt", "r")

string = f.read()
#print(string)
string = string.lower()
x = string.split(" ")
x.sort()

string = " ".join(x)
new_f = open("sorted_words_output.txt", "w")
new_f.write(string)

f.close()
new_f.close()