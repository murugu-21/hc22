import os
import sys
import solver
import scorer

for filename in os.listdir("input"):
    f = open(os.path.join("input", filename))
    sys.stdin = f
    fo = open(os.path.join('output', filename), "w+")
    sys.stdout = fo
    solver.solve()
    fo.close()
    f.close()
    
cur = scorer.score()
maxi = int(open("score").read())

if cur > maxi:
    open("score", "w").write(str(cur))
    import shutil
    shutil.copytree("output", "submissions/{}".format(str(cur)))