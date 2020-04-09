from flask import Flask, request, render_template
from flask.helpers import url_for

from Modelling import cleanCorpora, calculateSimilarity, calculateAllNames

app=Flask(__name__)

def testModelling():
    print('test')
    sims=calculateAllNames('explore knowledge sources step 1')
    print(sorted(enumerate(sims), key=lambda x: x[1], reverse=True)[0])

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    # testModelling()
    app.run(debug=True)