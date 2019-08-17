#!/usr/bin/env python
if __name__=='__main__':
    with open("templates.txt") as f:
        out3 = open("template_grep_3.txt")
        out4 = open("template_grep_4.txt")
        out5 = open("template_grep_5.txt")
        lemmas = open("all_lemmas.txt")
        out_new = open("new_templates.txt", 'w')
        for f in [out3, out4, out5]:
            for line in f:
                for lemma_line in lemmas:
                    w1, w2, w3, _ = lemma_line.split('\t')
                    new_line = line.replace("${w2}", w2).replace("${w1}", w1)
                    out_new.write(new_line)

                    new_line = line.replace("${w2}", w3).replace("${w1}", w2)
                    out_new.write(new_line)
