#!/usr/bin/env python

# Complexity: O(n^2)
def has_unique_characters(string):
	for i in range(0, len(string)):
		for j in range(i+1, len(string)):
			if string[i] == string[j]:
				return False
	return True


def has_unique_characters_2(string):
	chars = []
	for char in string:
		if char in chars:
			return False
		chars.append(char)
	return True

# Time and space complexity: O(n)
def has_unique_characters_3(string):
	chars = set()
	for char in string:
		if char in chars:
			return False
		chars.add(char)
	return True

def has_unique_characters_4(string):
	return len(set(string)) == len(string)