from py2neo import Graph, Node, Relationship

class QuestionParser:
    def __init__(self):
        self.graph=Graph(host='localhost',user='neo4j',password='password')
        self.names=[]
        results=self.graph.run('match(n) return id(n) as id,n.name as name').data()
        for result in results:
            self.names.append(result['name'])


if __name__=='__main__':
    qp=QuestionParser()