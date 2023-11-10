import flask
from urllib.request import urlopen
import simplejson
from urllib.parse import quote

app = flask.Flask(__name__)

BASE_PATH='http://localhost:8983/solr/films/select?wt=json&q='

@app.route('/', methods=["GET","POST"])
def index():
    query = None
    numresults = None
    results = None

    # get the search term if entered, and attempt
    # to gather results to be displayed
    if flask.request.method == "POST":
#        query = flask.request.form["searchTerm"]
        query = quote(flask.request.form["searchTerm"])


        # return all results if no data was provided
        if query is None or query == "":
            query = "*:*"

        # query for information and return results
        connection = urlopen("{}{}".format(BASE_PATH, query))
        response = simplejson.load(connection)
        numresults = response['response']['numFound']
        results = response['response']['docs']

    return flask.render_template('index.html', query=query, numresults=numresults, results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')#,port=5000)