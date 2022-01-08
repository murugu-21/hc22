from scorer import score


def solve():
    n = int(input())
    score = dict()
    for i in range(n):
        likes = input().split()[1::]
        for l in likes:
            if l in score:
                score[l] += 1
            else:
                score[l] = 1
        dislikes = input().split()[1::]
        for d in dislikes:
            if d in dislikes:
                if d in score:
                    score[d] -= 1
                else:
                    score[d] = -1
    
    ans = []
    for ing in score:
        if score[ing] >= 0:
            ans.append(ing)
    print(str(len(ans)) + " " + " ".join([ing for ing in list(ans)]))