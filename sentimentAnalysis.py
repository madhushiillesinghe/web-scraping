from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
from textblob.wordnet import Synset

# import nltk;
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')

# Part-of-speech Tagging
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print(wiki.tags)

# Noun Phrase Extraction
print(wiki.noun_phrases)

# Sentiment Analysis
testimonial = TextBlob("bad is better than good")
print(testimonial.sentiment)
print("polarity",testimonial.sentiment.polarity)



# Tokenization¶
zen = TextBlob(
    "Beautiful is better than ugly. "
    "Explicit is better than implicit. "
    "Simple is better than complex."
)
print(zen.words)
print(zen.sentences)

for sentence in zen.sentences:
    print("loop",sentence.sentiment)


# Words Inflection and Lemmatization
sentence = TextBlob("Use 4 spaces per indentation level.")
print(sentence.words)
print(sentence.words[2].singularize())
print(sentence.words[-1].pluralize())


# Words can be lemmatized by calling the lemmatize method.
w = Word("octopi")
print(w.lemmatize())
w = Word("went")
print(w.lemmatize("v"))

# WordNet Integration
word = Word("octopus")
print(word.synsets)
print(Word("hack").get_synsets(pos=VERB))
print(Word("octopus").definitions)
octopus = Synset("octopus.n.02")
shrimp = Synset("shrimp.n.03")
print(octopus.path_similarity(shrimp))

# WordLists
animals = TextBlob("cat dog octopus")
print(animals.words)
print(animals.words.pluralize())


# Spelling Correction
b = TextBlob("I havv goood speling!")
print(b.correct())
w = Word("falibility")
print(w.spellcheck())

# Get Word and Noun Phrase Frequencies
monty = TextBlob("We are no longer the Knights who say Ni. "

                    "We are now the Knights who say Ekki ekki ekki PTANG.")

print(monty.word_counts['ekki'])

# second way for get thye count
print(monty.words.count('ekki'))
print(monty.words.count('ekki', case_sensitive=True))
print(wiki.noun_phrases.count('python'))

# Parsing
# Use the parse() method to parse the text.
b = TextBlob("And now for something completely different.")
print(b.parse())

# TextBlobs Are Like Python Strings!
print(zen[0:19])
print(zen.upper())
print(zen.find("Simple"))


apple_blob = TextBlob("apples")
banana_blob = TextBlob("bananas")
print(apple_blob < banana_blob)
print(apple_blob == "apples")


# You can concatenate and interpolate TextBlobs and strings.
print(apple_blob + " and " + banana_blob)
print("{0} and {1}".format(apple_blob, banana_blob))

# n-grams
blob = TextBlob("Now is better than never.")
print(blob.ngrams(n=3))

# Get Start and End Indices of Sentences
for s in zen.sentences:
    print(s)
    print("---- Starts at index {}, Ends at index {}".format(s.start, s.end))

