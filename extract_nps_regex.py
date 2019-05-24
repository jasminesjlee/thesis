#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

def writematch(match,branch):
    words = match.split(" ")
    if branch=="1":
        return words[2][:-1]+" "+words[4][:-1]+" "+words[7][:-1]+'\t'+branch
    else:
        return words[1][:-1]+" "+words[3][:-1]+" "+words[5][:-1]+'\t'+branch

extracted_nps = open("extracted_nps.txt","w")
dir = "/home1/l/leesunj/TreeBank3_np_v1.0/parsed/mrg/wsj"
folder_names = [x[0] for x in os.walk(dir)][1:]
left_match_set = set()
right_match_set = set()
for folder in folder_names:
    for filename in os.listdir(folder):
        with open(folder+"/"+filename) as f:
            lines = f.read()
            lines = re.sub('\s+', ' ', lines)
            matchesL1=re.findall(r'\(NML \(N\w* \w*\) \(N\w* \w*\) \) \(N\w* \w*\)', lines)
            matchesL2=re.findall(r'\(JJP \(J\w* \w*\) \(N\w* \w*\) \) \(N\w* \w*\)',lines)
            matchesR1=re.findall(r'\(JJ\w* \w*\) \(N\w* \w*\) \(N\w* \w*\)',lines)
            matchesR2=re.findall(r'\(N\w* \w*\) \(N\w* \w*\) \(N\w* \w*\)',lines)
            
            
        for i, matches_set in enumerate([matchesL1, matchesL2, matchesR1,matchesR2]):
            for match in matches_set:
                words = match.split(" ")
                if i < 2:
                    left_match_set.add(writematch(match, "1"))
                else:
                    right_match_set.add(writematch(match, "0"))


            

left_match_set = sorted(list(left_match_set))
right_match_set = sorted(list(right_match_set))
for curr_dir in [left_match_set, right_match_set]:
    for l in curr_dir:
        extracted_nps.write(l+'\n')
extracted_nps.close()

