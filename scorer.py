import os


def score()->int:
    score = 0
    for filename in os.listdir("input"):
        fi = open("input/{}".format(filename))
        fo = open("output/{}".format(filename))
        myPizza = list(fo.readline().split())
        myPizza = set(myPizza[1::])
        n = int(fi.readline())
        for i in range(n):
            likes = set(fi.readline().split()[1::])
            dislikes = set(fi.readline().split()[1::])
            if likes.issubset(myPizza) and dislikes.isdisjoint(myPizza):
                score += 1
        fi.close()
        fo.close()
    return score