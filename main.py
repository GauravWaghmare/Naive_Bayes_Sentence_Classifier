from __future__ import print_function

import csv

from nltk.stem import *
import nltk
from nltk.stem.porter import *

import numpy as np
import scipy

from sklearn.naive_bayes import MultinomialNB

from res_map import responses

file_path = "/home/gaurav/Github/Naive_Bayes_Sentence_Classifier/data.csv"

class Proto(object):

	def __init__(self):
		self.no_ques = 0
		self.no_words = 0
		self.clf = MultinomialNB()
		self.res = responses()
		self.stems = []
		self.word_pos = dict()

	# Read the CSV file into a list of lists
	def read_data(self):
		data = []
		with open(file_path) as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in spamreader:
				data.append(row)
		# Remove the first row
		data = data[1:]
		self.no_ques = len(data)
		return data

	# Change all characters to lower case
	def lower_case(self):
		data = self.read_data()
		for element in data:
			element[0] = element[0].lower()
		return data

	# Change all sentences to tokens
	def tokenize(self):
		data = self.lower_case()
		sentences = []
		for element in data:
			sentences.append(nltk.word_tokenize(element[0]))
		return sentences

	# Change all tokens to their respective stems
	def stemify(self):
		sentences = self.tokenize()
		print("Sentences ", len(sentences))
		stemmer = PorterStemmer()
		for sentence in sentences:
			stem = [stemmer.stem(word) for word in sentence]
	    	self.stems.append(stem)

	# Construct vocabulary
	def build_voc(self):
		vocab = dict()
		sentences = self.stemify()
		vocab_size = 0
		for i in self.stems:
			for ii in i:
				vocab[ii] = 1
		vocab_size = len(vocab)
		self.no_words = vocab_size
		return vocab

	# Construct a map to store position of each word in the vocabulary
	def word_index(self):
		vocab = self.build_voc()
		vocab_arr = list(vocab.keys())
		vocab_arr.sort()
		i = 0
		for word in vocab_arr:
			self.word_pos[word] = i
	    	i += 1

	def populateX(self):
		X = np.zeros((self.no_ques, self.no_words))
		print(len(self.stems))
		print(self.no_ques)
		for i in range(self.no_ques):
			for word in self.stems[i]:
				X[i, self.word_pos[word]] += 1
		return X

	def populateY(self):
		Y = np.zeros((self.no_ques))
		data = read_data(file_path)
		for i in range(no_ques):
			Y[i] = data[i][1]
		return Y

	def train(self):
		self.word_index()
		X = self.populateX()
		Y = self.populateY()
		self.clf.fit(X, Y)

	def vector(self, string):
	    string = string.lower()
	    tokens = nltk.word_tokenize(string)
	    stems = [stemmer.stem(word) for word in tokens]
	    vec = np.zeros((1, self.no_words))
	    for stem in stems:
	        vec[0][self.word_pos[stem]] += 1
	    return vec

	def respond(self):
	    ask = raw_input()
	    vec = vector(ask)
	    no = self.clf.predict(vec)[0]
	    no = int(no)
	    print (res[no])

def __main__():
	proto = Proto()
	proto.train()
	ans = "Yes"
	while ans=="yes":
		print("Please input your query")
		proto.respond()
		print()
		print("Do you have any more queries?")
		ans = raw_input()

__main__()



