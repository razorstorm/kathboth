import markovify
import numpy as np

# Get raw text as string.
with open("ari_parsed_text.txt") as f:
    text = f.read()

# Build the model.
# text_model = markovify.Text(text)
#
# num_sentences = max(1, int(round(np.random.normal(3, 1, 1)[0], 0)))
#
# sentences = []
# print num_sentences
# for i in range(num_sentences):
#     sentences.append(text_model.make_sentence(tries=1000))
#
# sentences = " ".join(sentences)
#
# print sentences



for i in xrange(100):
    num_sentences = max(1, int(round(np.random.normal(2, 1, 1)[0], 0)))
    print num_sentences