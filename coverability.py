import simplePN as PN
infty = 100000000000
ω = -42
def next(M,p):
    Mold = [i for i in M]
    ps = []
    for idx,i in enumerate(M):
        if i == ω:
            Mold[idx] = infty
        
    for idx,t in enumerate(p.enabled(Mold)):
        if t == 1:
            ps.append(p.fire_one(Mold,idx))
    for mtmp in ps:
        for idx,i in enumerate(mtmp):
            if i >= infty/2:
                mtmp[idx] = -42
    return ps

def greaterthan(M1,M2):
    for i,j in zip(M1,M2):
        if i < j :
            if i == ω or j == ω:
                continue
            return False
    return True

def format(M1,M2):
    res = []
    for i , j in zip(M1,M2):
        if i > j or j == ω:
            res.append (ω)
        else:
            res.append(i)
    return res



def coverability_tree(M,pn,path = []):
    M = list(M)
    print("     "*len(path),M)

    if M in path  :
        return 
    else: 

        for Mi in next(M,pn):
            for Mj in path:
                if  greaterthan(Mi,Mj):
                    Mi = (format(Mi,Mj))                    
            coverability_tree(Mi,pn,path+[M])
            



    


