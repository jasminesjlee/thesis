#!/usr/bin/env python
if __name__=='__main__':
    with open("templates.txt") as f:
        out3 = open("filtered_templates_3.txt_3", 'w')
        out4 = open("filtered_templates_4.txt", 'w')
        out5 = open("filtered_templates_5.txt", 'w')
        pos3 = open("template_position_3.txt", 'w')
        pos4 = open("template_position_4.txt", 'w')
        pos5 = open("template_position_5.txt", 'w')
        for line in f:
            words = line.split()
            if "[w1]" in line and "[w2]" in line:
                w2_pos = [idx for idx, word in enumerate(words) if word == "[w2]"][0]
                w1_pos = [idx for idx, word in enumerate(words) if word == "[w1]"][0]
                if len(line.split()) == 3:
                    out3.write(line)
                    pos3.write(str(w2_pos)+'\t'+str(w1_pos)+'\n')
                elif len(line.split()) == 4:
                    out4.write(line)
                    pos4.write(str(w2_pos)+'\t'+str(w1_pos)+'\n')
                else:
                    out5.write(line)
                    pos5.write(str(w2_pos)+'\t'+str(w1_pos)+'\n')
