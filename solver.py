def solve():
    n = int(input())
    likes = set()
    dislikes = set()
    for i in range(n):
        likes.update(set(input().split()[1::]))
        dislikes.update(set(input().split()[1::]))
        likes - dislikes
    print(str(len(likes)) + " " + " ".join([ing for ing in list(likes)]))