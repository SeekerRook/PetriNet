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
	758413(("2")) --> 846518["18"]
	846518 --> 445072(("0"))
	445072 --> 433923["19"]
	433923 --> 413503(("0"))
	413503 --> 419111["20"]
	419111 --> 842017(("0"))
	842017 --> 696366["17"]
	696366 --> 758413

"""
print(tools.frommermaid(st))


p = pn.PetriNet.from_mermaid(st)
# p.from_mermaid(st)

print(p)

# print(p.Arches['A1'].PN)
# p.Places['P1'].addTokens(6)

p.render()
input(p)
while(True):
	p.fire()
	p.render()
	input(p)
