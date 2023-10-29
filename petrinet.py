from tools import frommermaid

class Component:
    """
    base class for PN Components (Places, Transitions, Arcs)
    """   
    def __init__(self,ID,ntype=None,pn=None):
        self.ID = ID
        self.ntype = ntype
        self.PN = pn
    def setpn(self,pn):
        self.PN = pn

class Arc(Component):
    """
    Implements Arcs 
    """
    def __init__(self,ID,inID,outID,weight=1):
        Component.__init__(self,ID,ntype="Arc",pn=None)
        self.inID = inID
        self.outID = outID
        self.weight = weight
    def remove(self,p):
        p.removeTokens(self.weight)
    def add(self,p):
        p.addTokens(self.weight)
    def trigger(self):
        if self.inID in self.PN.Places:
            self.remove(self.PN.Places[self.inID])
        elif self.outID in self.PN.Places:
            self.add(self.PN.Places[self.outID])
    def isready(self):
        if self.inID in self.PN.Places:
           source = self.PN.Places[self.inID]
           return (source.getTokens() >= self.weight)

class Place(Component):
    """
    Implements Places. #TODO implement list of tokens instead of counter.
    """
    def __init__(self,ID,tokens=0):
        Component.__init__(self,ID,ntype="Place",pn=None)
        # self.tokens = []
        self.tokens = tokens
        self.default_token = '.'
    def addToken(self,token):
        # self.tokens.append(token)
        self.tokens+=1
    def addTokens(self,i):
        
        # for _ in range (int(i)): 
            # self.addToken(self.default_token)
        self.tokens+=i
    def removeTokens(self,i):
            # self.tokens = self.tokens[:i]
            self.tokens -= i
    def getTokens(self):
        # return len(self.tokens)
        return self.tokens

class Transition(Component):
    """
    Implements Transitions 
    """
    def __init__(self,ID):
        Component.__init__(self,ID,ntype="Transition",pn=None)
        self.IN = []
        self.OUT = []
    def isFirable(self):
        res = True
        for i in self.IN:
            res = res and self.PN.Arcs[i].isready()
        return res
    def add_in(self,ID):
        self.IN.append(ID)
    def add_out(self,ID):
        self.OUT.append(ID)
    def fire(self):
        if self.isFirable():
            for i in self.IN + self.OUT:
                self.PN.Arcs[i].trigger()
    
class PetriNet:
    """
    The Base PN Class. Can be overriten for other type of PNs (ColorPN, StochasticPN, CPNs) 
    """
    def __init__(self,Components):
        self.Places = {}
        self.Transitions = {}
        self.Arcs = {}
        for component in Components:
            self.add(component)
            component.setpn(self)
        self.fill_trans()
    def add(self,component):
        if component.ntype == "Place":
            self._add(component,self.Places)
        elif component.ntype == "Transition":
            self._add(component,self.Transitions)
        elif component.ntype == "Arc":
            self._add(component,self.Arcs)

        else: raise TypeError (f"Unknown Type {component.ntype}")
    def _add(self,c,l):
        if c.ID not in self.Places | self.Transitions | self.Arcs:
                l[c.ID] = c
        else: raise KeyError("Duplicate IDs not allowed")
    def fill_trans(self):
        for a in self.Arcs:
            if self.Arcs[a].inID in self.Transitions:
                self.Transitions[self.Arcs[a].inID].add_out(a)
            if self.Arcs[a].outID in self.Transitions:
                self.Transitions[self.Arcs[a].outID].add_in(a)
    def fire(self):
        for t in [i for i in list(self.Transitions.values()) if i.isFirable()]: #simultaneous firing
            
            t.fire()
    def render(self):
        print("Rendering ...")
        import base64
        from PIL import Image
        import matplotlib.pyplot as plt
        graph = self.tomermaid()

        graphbytes = graph.encode("utf8")
        base64_bytes = base64.b64encode(graphbytes)
        base64_string = base64_bytes.decode("ascii")
       
        import requests
        from io import BytesIO

        response = requests.get("https://mermaid.ink/img/" + base64_string)
        img = Image.open(BytesIO(response.content))
        img.save("out.jpg")
        print("Done")
        # Image(url="https://mermaid.ink/img/" + base64_string).save('out.jpg')
    @classmethod
    def from_mermaid(cls,s,mode='byID'):

        items = []
        pl,tr,ar = frommermaid(s,mode)
 
        for p in pl:
            try:
                items.append(Place(p,int(pl[p])))
            except :
                items.append(Place(p))
        for t in tr:
            items.append(Transition(t))
        for id,a in enumerate(ar):
            items.append(Arc(f"A{id}",a[0],a[1],a[2]))

        return cls(items)
    
    def tomermaid(self):
        res = """
flowchart
"""
        for i in self.Places:
            res += f"{i}((\"{self.Places[i].getTokens()}\"))\n"
        for i in self.Transitions:
        
            res += f"{i}[\" \"]\n"
        for i in self.Arcs:
        
            res += f"{self.Arcs[i].inID} --> |\"{self.Arcs[i].weight}\"| {self.Arcs[i].outID}\n"
        return res
    def __repr__(self) -> str:
        # return f"""
        # Places = {[f'{i}[{self.Places[i].getTokens()}]' for i in self.Places]}
        # Transitions = {[f'{i} {self.Transitions[i].IN}->{self.Transitions[i].OUT}' for i in self.Transitions]}
        # Arcs = {[f'{i} : {self.Arcs[i].inID} -{self.Arcs[i].weight}-> {self.Arcs[i].outID}' for i in self.Arcs]}
        # """
        return self.tomermaid()