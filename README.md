# Academic paper recommendation

In this project I build an Academic paper recommendation system. It will be focussed on Theoretical linguistics and Computational 
linguistics papers, but it is extendable to other fields. All papers used to build the system are [open source](http://www.oajse.com/subjects/linguistics.html). 
The recommendation system will not recommend papers that are the most similar to the papers the user already read, but will 
rather recommend papers that have some overlap but are sufficiently distinct for the researcher to extend her/his horizon, 
getting inspiration and insights from related yet distinct fields, and from opposing views, building bridges between different areas of research. It's all
about multi disciplinarity!

## Desing:

### The data
Open source research articles form the following fields:
* Theoretical linguistics
* Computational linguistics

### Design
* Scraping the data. Most papers are in pdf format, which will require [previous transformation](https://pythontips.com/2016/02/25/ocr-on-pdf-files-using-python/). Between 500 and 1000 papers will
be used. Potential problem: papers in theoretical linguistics tend to be much longer (30-50 pages) than papers in Computational
linguistics (10-20 pages).
* Topic modeling: [vectorizing](https://github.com/facebookresearch/fastText) the texts to be able to classify them according 
to topic. Preferrably, identification of several topics per paper. Each paper will correspond to one document.
* Document similarity: calculate distance between different documents. 
* Threshold: decide on a similarity threshold to recommend sufficiently distinct papers.
