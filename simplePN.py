import numpy as np
import random as rnd
def isfirable(M,T):
        for idx,i in enumerate(-1*T):
            if i == 1 :
                if M[idx] < 1:
                    return False
        return True
                    
class PetriNet:
    def __init__(self,W):
        self.W = np.array(W,dtype=int)
        self.transitions_n = len(W[0]) 
        self.places_n = len(W) 

    def transition(self,t):
        return self.W[:,t]


    def enabled(self,M):
        res = np.zeros(self.transitions_n,dtype=int)

        for j in range(self.transitions_n):
                # print(self.W[i,j])
                # print(self.W)

            if isfirable(M,self.transition(j)):
                res[j] = 1
        return res
    def fire_all(self,M,T):
        return (M+np.dot(self.W,T))

    def rnd_transition(self,M):
        ts = []
        for i,t in enumerate(self.enabled(M)):
            if int(t) == 1:
                ts.append(i)
        # print(ts)
        return rnd.choice(ts)
    def simulate (self,i,M=[]):
        ts = np.zeros(self.transitions_n,dtype=int)
        if M ==[]:
            M = np.zeros(self.places_n,dtype=int)
        for i in range(i):
            t = self.rnd_transition(M)
            ts[t]+=1
            M = self.fire_one(M,t)   
        return M,ts
        
    def fire_one(self,M,t):
        T = np.zeros(self.transitions_n,dtype=int)
        T [t] = 1
        # print(T)
        # print(M)
        if isfirable(M,self.W[:,t]):
            # print("firable")
            return self.fire_all(M,T)
        else: return M