expert system=knowledge+rules=decisions
NLP works with the human language.
Tokenization 
pos tagging
NER(Name Entity Recognition)
Sentiment analysis (read comment positive or negative)
Machine translation
Text summarization

NLU(Natural language Understanding)
"book a flight to Yangon tmw"

NLG(Natural Language Generation)
Generating language from data to information

Natural Language Interaction(NLI)
Understanding the user's input and producing an appropriate response.

NLP->Process language
NLU->Understand language
NLG->Generate Language
NLI->Interact using language


Three Day#

1.Shallow Parsing
2.Deep Parsing
3.Statistical approach

focus on one thing not the overall
1.Shallow Parsing
1.make the sentence into words (Tokenization)
2.(determine words like nouns,verb,....)
3.find important entites->NER
4.Remove unneccessary words->Stopword Removal (eample. remove the pro nouns)
5.Identify phrases->Chunking
6.Analyze word forms->Morphological analysis
7.Reduce words to their base forms->Stemming
8.find word meanings and relationships->WordNet

Shallow parsing tells us "What are the imp words and phrases in this senetence?" ( use one of 8 ways)



2.Deep Parsing
grammatical structure & meaning reslationships within a sentence
1.Syntactic Parsing->builds a completee syntax structure/Three
2.TextRank->extracts important sentences/words
3.LexRank->identifies importatnt sentences using graph-based ranking
4.GPT Transformers->understands and generates human-like language

"How are the words connected , and what does the sentence mean?"


3.Statistical approach 
uses mathematics,probatilities,and  machine learning to learn patterns from  text data.

Markov Models->predicts the next state/word based on previous states
Bag of Words=>represent text using word frequencies.( the word that shows up how many times)
N-grams=>represent sequences of words(kyunt taw => 2 grams)
TF-IDF->measure the importance of words
TF-IDF Transformers->convert text into numerical features
SVM-> classify text into categories
Centroid-based Classification->classify text based on similariy to calss centers
K-mean
converst languuae into numbers and uses math/Statistical methods to find patterns, classify, or group text.


SP->What words and phrase are here
DP->how are they connected
S NLP-> How can computers learn from text



MOrpheme

cats->cat(main meaning)+s(plural)


free MOrpheme (happy, play)
bound morpheme( es, ed,...)

find some POS tags 

parsing has three types , Chunking is in the Shallow parsing


Stemming Alogrithm
Porter Stemmer (english)
Snowball Stemmer (multilang)
Lancaster Stemmer

Stemming is fast ,
rule-based,produce invalid words

lemmatization is slow, 
uses linguistic information,
valid dictionary form, 
computationally involved



Day2#
summy->summarization and summa->keyword extration
summy->importance sentence & summa->importance words/phrases


summarize 10 lines into 1 line called "Extraction"









