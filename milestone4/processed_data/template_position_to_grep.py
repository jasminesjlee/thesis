#!/usr/bin/env python

if __name__ == "__main__":
    template_files = ["template_position_3.txt", "template_position_4.txt", "template_position_5.txt"]
    idx = 3
    for file in template_files:
        template_grep_file = open("template_grep_"+str(idx)+".txt", "w")

        with open(file) as f:
            for line in f:
                word_slots = line.split()
                print(word_slots)
                slots = ["[a-zA-Z]+" for _ in range(idx)]
                slots[int(word_slots[0])] = "${w2}"
                slots[int(word_slots[1])] = "${w1}"
                template_grep_file.write(" ".join(slots)+'\n')

                slots = ["[a-zA-Z]+" for _ in range(idx)]
                slots[int(word_slots[0])] = "${w3}"
                slots[int(word_slots[1])] = "${w2}"
                template_grep_file.write(" ".join(slots) + '\n')
            idx += 1
