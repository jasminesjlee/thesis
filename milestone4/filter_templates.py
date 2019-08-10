#!/usr/bin/env python
if __name__=='__main__':
    with open("/Users/leezsun/PycharmProjects/thesis/milestone4/templates.txt") as f:
        out = open("/Users/leezsun/PycharmProjects/thesis/milestone4/filtered_templates.txt", 'w')
        for line in f:
            if "[w1]" in line and "[w2]" in line:
                out.write(line)
