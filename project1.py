# Exercise 24
# (a) find all words in text6 that end in -ise
import nltk
from nltk.book import *
print([w for w in text6 if w.endswith("ise")])
# (b) find all words in text6 that contain "z", including at the beginning of words
print([w for w in text6 if "z" in w or "Z" in w])
# (c) find all words in text6 that contain "pt" including at the beginning of words
print([w for w in text6 if "pt" in w or "Pt" in w])
# (d) find all words in text6 that begin with a titlecase letter
print([w for w in text6 if w.istitle()])

# Exercise 25
# create a list
sent = ["she", "sells", "sea", "shells", "by", "the", "sea", "shore"]
# if a word in sent begins with "sh", print it
print([w for w in sent if w. startswith("sh")])

# print all words from sent that are longer than 4 characters
print([w for w in sent if len(w)>4])