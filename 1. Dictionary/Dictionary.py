import json
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Enter word:")

def definition(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word, data.keys())) > 0:
		word = get_close_matches(word, data.keys())[0]
		print("Did you mean", word, "Press Y for yes: ")
		res = input()
		res = res.lower()
		if res == 'y':
			if word in data:
				return data[word]
	else:
		return "Word Doesn't exist. Please check it."

print(definition(word))