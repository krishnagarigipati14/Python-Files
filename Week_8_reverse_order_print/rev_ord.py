f = open("rev_ord_week_8_input.txt", "r")
string = f.read()
f.close()


lines = string.splitlines()

new_f = open("rev_ord_week_8_output.txt", "w")


for line in lines:
    reversed_words = " ".join(line.split()[::-1]) 
    new_f.write(reversed_words + "\n")

new_f.close()
