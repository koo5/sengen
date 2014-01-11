#!/usr/bin/env python2
#-*- coding: utf-8 -*-

dictionary = open("wordlist.txt").read().split()
print "dictionary:", dictionary

def ok(s):
#	print "is", s, "ok?"
	words = sentence.split()
	for word in words:
		if word not in dictionary:
			return False
	return True

for line in open("sentences.csv", "r").readlines():
	line = line.split("\t")[2]
	sentence = line[:-2]
	if ok(sentence):
		print line
