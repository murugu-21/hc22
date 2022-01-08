import os
import sys
import solver
import scorer

for filename in os.listdir("input"):
    fi = open(os.path.join("input", filename))
    sys.stdin = fi
    fo = open(os.path.join('output', filename), "w+")
    sys.stdout = fo
    solver.solve()
    fo.close()
    fi.close()
    
maxi = int(open("score").read())
cur = scorer.score()

if cur > maxi:
    open("score", "w").write(str(cur))
    import shutil
    shutil.copytree("output", "submissions/{}".format(str(cur)))