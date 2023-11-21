from PN import PetriNet
def Id(t):
    return t

class token:
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return f"t|{self.value}|"

class ColouredPetriNet(PetriNet):

    def __init__(self,W):
        PetriNet.__init__(self,W)

    def isfirable(self,M,T):
        for idx,i in enumerate(T):
            print(i)
            if i != 0 and i!= None:
                s,f = i
                if s > 0 :
                    if f(M[idx])  is not None:
                       return False
        return True
    
if __name__ == "__main__":
    import numpy as np
    a = np.array([(-1,Id),(1,Id)])
    cpn = ColouredPetriNet(a)
    print(cpn.W)
    cpn.isfirable([1,0],cpn.W[:,0])
