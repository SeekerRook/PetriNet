from tools import dictionarize,frommermaid
class PetriNet:

    def __init__(self,items=[]):

        self.places = []
        self.transitions = []
        for i in items:
            if i.ntype == "Place":
                self.places.append(i)
            if i.ntype == "Transition":
                self.transitions.append(i)

    def __repr__(self) -> str:
        res = "places:\n"
        for p in self.places:
            res += f"{p}\n"
        res += "transitions:\n"
        for t in self.transitions:
            res += f"{t}\n"
        return res
    @classmethod
    def from_mermaid(cls,s,mode='byName'):

        items = []
        pl,tr,ar = frommermaid(s,mode)
        nd = {}
        for p in pl:
            P = Place(p)
            # print(P)
            items.append(P)
            nd[p] = P
        for t in tr:

            T = Transition(t)
            # print(T)

            items.append(T)
            nd[t] = T
        for a in ar:
            # print(nd)
            # print(a[0],a[1],a[2])
            nd[a[0]].add_outputs([(nd[a[1]],a[2])])
        return cls(items)
    
    def get(self,ID):
        for i in self.places + self.transitions:
            if(ID == i.ID):
                return i
    def fire(self):
        for i in self.transitions:
            i.fire()

class Node:
    def __myinit__(self,ID,inputs,outputs,ntype=None):
        inputs = inputs
        outputs = outputs
        self.inputs = inputs
        self.outputs = outputs
        self.ID = ID
        self.ntype=ntype
        self.lb = '{'
        self.rb = '}'
        self.extra=""

        for node,weight in inputs.items():
            node.outputs[self] = weight
        for node,weight in outputs.items():
            node.inputs[self] = weight

    def __init__(self,ID,inputs=[],outputs=[],ntype=None):
        inputs = dictionarize(inputs)
        outputs = dictionarize(outputs)
        self.__myinit__(ID,inputs,outputs,ntype)    

    def add_outputs(self,outputs):
        outputs = dictionarize(outputs)
        self.outputs.update(outputs)
        for node,weight in outputs.items():
            node.inputs[self] = weight
    def add_inputs(self,inputs):   
        inputs = dictionarize(inputs)
        self.inputs.update(inputs)

        for node,weight in inputs.items():
            node.outputs[self] = weight

    def __repr__(self) -> str:
        
        return f"{self.lb} {self.ID}, {self.ntype}, {[f'{i.ID}:{w}' for i,w in self.inputs.items()]} -> {[f'{i.ID}:{w}' for i,w in self.outputs.items()]} {self.extra} {self.rb}"


class Place(Node):
    def __init__(self,ID,inputs=[],outputs=[],tokens=0,):

        Node.__init__(self,ID,inputs,outputs,ntype="Place")
        self.tokens = tokens
        self.lb = '('
        self.rb = ')'
    def addtokens(self,i):
        self.tokens += i
    def settokens(self,i):
        self.tokens = i
    def __repr__(self) -> str:
        self.extra = f"tokens : {self.tokens}"
        return Node.__repr__(self)

class Transition(Node):
    def __init__(self,ID,inputs=[],outputs=[]):
        Node.__init__(self,ID,inputs,outputs,ntype="Transition")
        self.lb = '['
        self.rb = ']'
    def isfirable(self):
        for i,w in self.inputs.items():
            if i.tokens < w:
                return False
        return True

    def fire(self):
        if self.isfirable():
            for i,w in self.inputs.items():
                i.tokens -= w
            for i,w in self.outputs.items():
                i.tokens += w    

