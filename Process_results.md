# Process and results

Content-based recommendation

## Data scraping

The structure of Lingbuzz is not consistent, which makes scraping harder:
 * depending on where the pdf is stored (in the db of the website itself, in semantics archive or in Rutgers Uni db), the link is in another place. If it 
 is in the db of lingbuzz, the pdf can be downloaded both from the article list and from the 'individual paper' page. If it is from another source, the pdf can only be downloaded from the article list.  
 Work around: scrape link to paper and link to 'individual page' from the article list, scrape meta data from 'individual page'. 
 * external papers do not have the same meta data. They only have author, title, date, keywords and number of downloads. No reference to publication status. Since we are interested in document similarity, this is not an issue.
 * extracting the author names: author names are text on hrefs to page with author information. The number of hrefs (and text) depends on the number of authors. It is hard to only extract the text from hrefs that refer to authors: there is a variable number of hrefs lower on the page.  
 Workaround: find only hrefs within <center><\center>. The first one is title, the others are authors. Other hrefs on the page are irrelevant if url to pdf is extracted from article list.


## Conversion

The papers are downloaded as pdfs. They were converted to plain text for further processing, and stored in a MongoDB. Each document in the DB has the following fields:
* author(s)
* keywords
* paper itself
* publication information
* url (maintained in order to match converted pdfs with doc)

## The linguistified tokenizer

Removes all irrelavant information from the papers. The idea is to obtain pure linguistics, with as little noise as possible.

* tokenize with Spacy tokenizer
* lemmatize
* trigrammize
* remove stopwords: these include the regular lists of English stopwords (NLTK and SKlearn), words with low frequency in the corpus (probably paper-specific vocabulary),  frequent non-relevant words, such as 'a.', 'i.e.', 'e.g.', 'john' and frequent too general words, such as 'language', 'example', 'chapter', 'section'.

For trigrammize: build phraser (Gensim) for frequent collocations:
* tokenize the whole corpus with Spacy tokenizer
* lemmatize
* remove stopwords
* create bigram phraser with parametrized thresholds
* create trigram phraser with parametrized thresholds

What could be better:
* remove all non-English words. Non-English words occur in examples and do not contribute to the topic-relevant content. They just create noise.
* remove editors. They show up as topic-relevant, while they are not. Authors on the other hand (especially in combination with year) might be relevant for topic modeling. Both editors and authors frequently chow up as a bigram or trigram, which shows that the phraser does it's job.
* remove all wrongly converted elements: several papers contain phonetic trasncriptions/mathematical symbols. These were converted to unicode, and thus not interpretable by humans. Also, these elements cerate noise anyway.


## Vectorizing

Countvectors and tfidf vectors were made for both the papers and the keywords. Presumably, keywords summarize the topics of the papers. This is usefull for evaluation of topic models: the distance between the topic vectors of two papers should be reflected by the distance between the keyword vectors.


## Topic modeling

Iterative desing: 
* make topic models
* inspect relevant words
* fine tune the tokenizer to get rid of irrelevant words that showed up as relevant
* Repeat

DBSCAN revealed to be very useful to detect the noise in the topic model, as it shows how many noise points there are in the dataset (i.e., how many papers were not assigned any topic). It also shows the topic allocation. At certain moments during the model-clean-iteration, it was clear that most papers were assigned to one and the same topic. There is topic inbalance in the data set (syntax papers are more frequent, more or less 50% of the dataset), but with subtopics there should be a relatively balanced topic space.

Final choice:
NMF on NMF: assigning all papers to four different general topics (presumably syntax, semantics, morphology and phonology, the four topics under which the papers are classified on Lingbuzz). Then assign all papers in each general topic to a more specific topic.

## Recommender

Paper recommendation based on weighted combination of topics similarity, document similarity and keyword similarity. The best weights found were:
2 * topic + 1 * document + 3 * keywords

## Visualization:

* Zoomable circle packing which represent the relations between the topics and the most relevant words for each topic.
* Dropdown menu where you can select a paper and you get three recommended papers based on the similarity with the chosen paper.
