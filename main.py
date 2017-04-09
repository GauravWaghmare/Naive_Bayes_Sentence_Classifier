from __future__ import print_function

import csv

from nltk.stem import *
import nltk

import numpy as np
import scipy

from sklearn.naive_bayes import MultinomialNB

from res_map import responses

class Proto(object):

	def __init__(self):
		self.no_ques = 0
		self.no_words = 0
		self.X = np.zeros((no_ques, no_words))
		self.Y = np.zeros((no_ques))
		self.clf = MultinomialNB()
		self.res = responses()
		self.data = []
		self.sentences = []
		self.vocab = dict()

	# Read the CSV file into a list of lists
	def read_data(self, file_path):
		with open(file_path) as csvfile:
	    	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	    	for row in spamreader:
	        	self.data.append(row)
		# Remove the first row
		self.data = self.data[1:]
		self.no_ques = len(data)
		self.Y = np.zeros((no_ques))

	# Change all characters to lower case
	def lower_case(self):
		for element in self.data:
	    	element[0] = element[0].lower()

	# Change all sentences to tokens
	def tokenize(self): 
		for element in self.data:
	    	self.sentences.append(nltk.word_tokenize(element[0]))

	# Change all tokens to their respective stems
	def stemify(self):
		stems = []
		from nltk.stem.porter import *
		stemmer = PorterStemmer()
		for sentence in sentences:
	    	stem = [stemmer.stem(word) for word in sentence]
	    	stems.append(stem)

	# Construct vocabulary
	def build_voc(self):
		vocab_size = 0
		for i in self.sentences:
	    	for ii in i:
	        	vocab[ii] = 1
		vocab_size = len(self.vocab)
		self.no_words = vocab_size
		self.X = np.zeros((self.no_ques, self.no_words))
		return vocab

	# Construct a map to store position of each word in the vocabulary
	def word_index(vocab):
		vocab_arr = list(vocab.keys())
		vocab_arr.sort()
		word_pos = dict()
		i = 0
		for word in vocab_arr:
	    	word_pos[word] = i
	    	i += 1
	    return word_pos

	def populateX(stems):
		for i in range(no_ques):
	    	for word in stems[i]:
	        	self.X[i, word_pos[word]] += 1

	def populateY(data):
		for i in range(no_ques):
	    	self.Y[i] = data[i][1]

	def train():
		self.clf.fit(self.X, self.Y)

	def vector(string):
	    string = string.lower()
	    tokens = nltk.word_tokenize(string)
	    stems = [stemmer.stem(word) for word in tokens]
	    vec = np.zeros((1, no_words))
	    for stem in stems:
	        vec[0][word_pos[stem]] += 1
	    return vec

	def respond():
	    ask = raw_input()
	    vec = vector(ask)
	    no = clf.predict(vec)[0]
	    no = int(no)
	    print (res[no])

	def __main__():
		respond()


