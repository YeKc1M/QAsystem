from py2neo import Graph, Node, Relationship

class QuestionParser:
    def __init__(self):
        self.graph=Graph(host='localhost',user='neo4j',password='password')
        self.names=[]
        results=self.graph.run('match(n) return id(n) as id,n.name as name').data() # list
        # print(type(results))
        for result in results:
            self.names.append(result['name'])
    def getAllNames(self):
        return self.names
    def getRelatedNodes(self, id):
        rs=self.graph.run('match(p)-[r]->(n) where id(p)='+str(id)+' return id(n) as id, case type(r) '+
        'when "Next" then p.name+" "+type(r) else p.name+" "+type(r)+" "+r.no END as name').data()
        return rs
    def getResult(self, id):
        rs=self.graph.run('match(n) where id(n)='+str(id)+' return n.context as context').data()
        s='<strong>'+rs[0]['context']+'</strong>'
        rs=self.graph.run('match(p)-[r]->(n) where id(p)='+str(id)+
        ' and type(r)<>"Next" return n.context as context order by r.no')
        for r in rs:
            s+='\n'+r['context']
        return s


if __name__=='__main__':
    qp=QuestionParser()
    # print(qp.getRelatedNodes(5))
    # print(qp.getResult(0))