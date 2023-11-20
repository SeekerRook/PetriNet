
import simplePN as spn
import numpy as np

pn_raw = np.array([[1,-1,-1,0,1],[0,1,0,-1,0],[0,0,1,0,-1]])
pn = spn.PetriNet(pn_raw)

state = [0,0,0]
s ,ts = pn.simulate(10)
print(s,ts)
print(pn.fire_all([0,0,0],ts))



pn = PN.PetriNet(np.array([[-1,0,1],[1,-1,-1],[1,-1,0]]))  
states = [[1,0,0]]
prev = []

print(coverability_tree([1,0,0],pn))
