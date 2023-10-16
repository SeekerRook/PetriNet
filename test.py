import petrinet as pn
# a = pn.Place('A')
# b = pn.Place('B')
# t = pn.Transition("T",[a],[b])
# p = pn.PetriNet([a,b,t])
# a.settokens(2)
# print(a)
# print(b)
# print(t)
# t.fire()
# print(a)
# print(b)
# print(t)
# print(p)
# t.fire()
# print(p)
import tools
st = """
---
title: "diagram"
---
flowchart
	name(("P1")) ---> 1["T2"]
	1 -->|"2"| 804668(("P2"))
	1 --> 771969(("P3"))

"""
print(tools.frommermaid(st))


p = pn.PetriNet().from_mermaid(st)
# p.from_mermaid(st)

print(p)

a = p.get("P1")
print(a)
a.settokens(6)
input(p)
while(True):
    p.fire()
    input(p)
