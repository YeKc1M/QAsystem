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
            l=calculateLogical(maxSim[0], question)
            ids=l[0]
            logicalSims=l[1]
            id=maxSim[0]
            content=''
            if(logicalSims[0][1]>0.7):
                id=ids[logicalSims[0][0]]
                print(id)
                content=qp.getResult(id)
            else:
                content=qp.getResult(id)
            reply={'type':'text'}
            reply['content']=content
            results.append(reply)
            quickReply={'type':'QuickReply','buttons':[{'title':'Yes','value':'Yes'},{'title':'No','value':'No'}],
            'content':'Is it helpful?'}
            results.append(quickReply)
        else:
            print('return 3')
            reply={'type':'QuickReply','buttons':[]}
            content=''
            for i in range(0,3):
                button={'title':'Q'+str(i+1),'value':qp.names[sims[i][0]]}
                reply['buttons'].append(button)
                content+=('Q'+str(i+1)+': '+qp.names[sims[i][0]]+'\n')
            content=content[:-1]
            reply['content']=content
            results.append(reply)
        print(results)
        return jsonify(results)
    return render_template('index.html')

if __name__=='__main__':
    # testModelling()
    app.run(debug=True)