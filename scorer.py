import os


def score(maxi: list)->list:
    j = 0
    scores = []
    for filename in os.listdir("input"):
        score = 0
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
        if score > maxi[j]:
            import shutil
            shutil.copyfile("output/{}".format(filename), "submissions/{}".format(filename[0] + " " + str(score)))
            print(filename)
            scores.append(str(score))
        else:
            scores.append(str(maxi[j]))
        j += 1
    return scores