from py2neo import Graph, Node, Relationship

class QuestionParser:
    def __init__(self):
        self.graph=Graph(host='localhost',user='neo4j',password='password')
        self.labels=[]
        self.names=[]
        results=self.graph.run('match(n) return id(n) as id,n.name as name')
        while(results.forward()):
            result=results.next()
            self.labels.append(result['id'])
            self.names.append(result['name'])
        print(self.labels)
        print(self.names)
        print(len(self.labels))


if __name__=='__main__':
    qp=QuestionParser()
    # results=qp.graph.run('match(n) return id(n) as id,n.name as name') # Cursor
    # while(results.forward()):
    #     result=results.next()
    #     print(str(result['id'])+' '+result['name'])