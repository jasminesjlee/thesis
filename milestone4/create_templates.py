#!/usr/bin/env python
if __name__=='__main__':
    with open("templates.txt") as f:
        out3 = open("template_grep_3.txt")
        out4 = open("template_grep_4.txt")
        out5 = open("template_grep_5.txt")
        lemmas = open("all_lemma.txt").readlines()
        out_new_3 = open("new_templates_3.txt", 'w')
        out_new_4 = open("new_templates_4.txt", 'w')
        out_new_5 = open("new_templates_5.txt", 'w')
        for f, out_new in zip([out3, out4, out5], [out_new_3, out_new_4,
                                                   out_new_5]):
            for line in f:
                for lemma_line in lemmas:
                    if len(lemma_line.split('\t')) == 4:
                        w1, w2, w3, _ = lemma_line.split('\t')
                        new_line = line.replace("${w2}", w2).replace("${w1}", w1)
                        out_new.write(new_line)

                        new_line = line.replace("${w2}", w3).replace("${w1}", w2)
                        out_new.write(new_line)
