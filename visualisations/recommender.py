import flask
import numpy as np
import pandas as pd
from copy import deepcopy
import json

# Initialize the app
app = flask.Flask(__name__)

@app.route("/")
def viz_page():
    with open("index.html", 'r') as viz_file:
        return viz_file.read()

#with open('all_recommendations.csv') as f:



@app.route("/recommend", methods=["POST"])
def recommend():
    data = flask.request.json
    x = data["paper"]
    df = pd.read_csv('all_recommendations.csv', index_col = 'paper')
# # the paper has to come from the index.html
    r = df.loc[x]

    recommended_papers = pd.DataFrame(columns = ['topic0', 'topic1', 'topic2']).append(r)

    out_json = recommended_papers.to_json(orient='split')  

    return out_json
    #return out_csv

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(port=5002,debug=True)
