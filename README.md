# Academic paper recommendation

In this project I build an Academic paper recommendation system. It will be focussed on linguistics papers, but it is extendable to other fields, provided that the papers are freely available. All papers used to build the system are [open source](http://www.oajse.com/subjects/linguistics.html).  
The recommendation system will not recommend papers that are the most similar to the papers the user already read, but will 
rather recommend papers that have some overlap but are sufficiently distinct for the researcher to extend her/his horizon, 
getting inspiration and insights from related fields, and from opposing views, building bridges between different areas of research. It's all about inter disciplinarity!

## Desing:

### The data
Open source linguistic research articles available on [Lingbuzz](https://ling.auf.net).

### Design
* Scraping the data. Most papers are in pdf format, which will require [transformation](https://pythontips.com/2016/02/25/ocr-on-pdf-files-using-python/) to a computer-readable format. Between 500 and 1000 papers will be used.
* Topic modeling: vectorizing the texts to be able to classify them according 
to topic. Preferrably, identification of several topics per paper. Each paper corresponds to one document.
* Document similarity: calculate distance between different documents. 
* Threshold: decide on a similarity threshold to recommend sufficiently distinct papers.
