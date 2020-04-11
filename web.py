from flask import Flask, request, render_template, jsonify
from flask.helpers import url_for

from Modelling import calculateAllNames, calculateLogical
from QuestionParser import QuestionParser

app=Flask(__name__)
qp=QuestionParser()

def testModelling():
    print('test')
    sims=calculateAllNames('explore knowledge sources step 1')
    print(sorted(enumerate(sims), key=lambda x: x[1], reverse=True)[0])

@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        question=request.form['question']
        print(question)
        sims=calculateAllNames(question)
        maxSim=sims[0]
        print(str(maxSim[0])+' '+str(maxSim[1]))
        results=[]
        if(maxSim[1]>0.6):
            print('calculate logical')
        else:
            print('return 3')
            reply={'type':'QuickReply','buttons':[]}
            for i in range(0,3):
                button={'title':'Q'+str(i+1),'value':qp.names[sims[i][0]]}
                reply['buttons'].append(button)
            results.append(reply)
        print(results)
        return jsonify(result=question+' back')
    return render_template('index.html')

if __name__=='__main__':
    # testModelling()
    app.run(debug=True)