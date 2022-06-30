import os
import sys
import solver
import scorer

old = sys.stdout

for filename in os.listdir("input"):
    fi = open(os.path.join("input", filename))
    sys.stdin = fi
    fo = open(os.path.join('output', filename), "w+")
    sys.stdout = fo
    solver.solve()
    fo.close()
    fi.close()

# sys.stdout = old
# maxi = open("score").readline().split()
# maxi = [int(i) for i in maxi]
# cur = scorer.score(maxi)
# open("score", "w").write(" ".join(cur))