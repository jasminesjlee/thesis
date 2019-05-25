#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str, required=True)
parser.add_argument('-o', type=str, required=True)

def majority(input, output):
	out = open(output,"w")
	with open(input) as f:
		lines = f.readlines()
		for _ in range(len(lines)):
			out.write("0\n")


def main(args):
	majority(args.i, args.o)

if __name__ == '__main__':
	args = parser.parse_args()
	main(args)
