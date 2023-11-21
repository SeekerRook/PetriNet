import numpy as np
import random as rnd
                   
class PetriNet:
    def __init__(self,W,type=object):
        self.W = np.array(W,dtype=type)
        self.transitions_n = len(W[0]) 
        self.places_n = len(W) 
        self.dtype = type

    def transition(self,t):
        """
        given transition index t gives the Transition Matrix in the form of a Matrix with -1 in input and +1 in output Places)
        """
        return self.W[:,t]

    def isfirable(M,T):
        """
        checks if Transition (in the form of a Matrix with -1 in input and +1 in output Places) is firable for marking M
        """
        pass
        #for idx,i in enumerate(-1*T):
        #    if i == 1 :
        #        if M[idx] < 1:
        #            return False
        #return True
 

    def enabled(self,M):
        """
        given marking N returns a list of firable Transitions (index)
        """
        pass
        #res = np.zeros(self.transitions_n,dtype=self.type)

        #for j in range(self.transitions_n):
        #        # print(self.W[i,j])
        #        # print(self.W)

        #    if self.isfirable(M,self.transition(j)):
        #        res[j] = 1
        #return res
    def fire_all(self,M,T):
        """
        Given an array with the number of occurences of eac transition, returns the resulting marking of the PN
        Does not preserve the path taken, nor checks if transitions can be fired.
        Can be used for testing the result of other methods. 
        """
        pass
        #return (M+np.dot(self.W,T))

    def rnd_transition(self,M):
        """
        return random enabled transition. 
        Useful for incremental simulation
        """
        ts = []
        for i,t in enumerate(self.enabled(M)):
            if int(t) == 1:
                ts.append(i)
        return rnd.choice(ts)

    def simulate (self,i,M=[]):
        """
        Returns the Marking and the Transition occurences after i firings of the PN (random)
        """
        #ts = np.zeros(self.transitions_n,dtype=self.type)
        #if M ==[]:
        #    M = np.zeros(self.places_n,dtype=self.type)
        #for i in range(i):
        #    t = self.rnd_transition(M)
        #    ts[t]+=1
        #    M = self.fire_one(M,t)   
        #return M,ts
        pass
    def fire_one(self,M,t):
        """
        returns the Marking after the firing of transition t(index)
        """
        #T = np.zeros(self.transitions_n,dtype=self.type)
        #T [t] = 1
        #if self.isfirable(M,self.W[:,t]):
        #    return self.fire_all(M,T)
        #else: return M
        pass
