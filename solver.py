from scorer import score

def solve():
    c, p = map(int, input().split())
    cont_skill = {}
    cont_name = {}
    available = {}
    for i in range(c):
        name, l = input().split()
        cont_name[name] = {}
        available[name] = 1
        for j in range(int(l)):
            skill, level = input().split()
            if skill not in cont_skill:
                cont_skill[skill] = {}
            level = int(level)
            if level not in cont_skill[skill]:
                cont_skill[skill][level] = []
            cont_skill[skill][level].append(name)
            cont_name[name][skill] = int(level)
    
    projects = []
    for i in range(p):
        name, n, s, d, r = input().split()
        req = []
        for j in range(int(r)):
            skill, level = input().split()
            req.append((skill, int(level)))
        projects.append([name, int(n), int(s), int(d), req])
    
    projects.sort(key = lambda x: (x[3], -x[2]), reverse=True)
    result = ""
    cnt = 0
    temp = []
    while projects:
        cur = projects.pop()
        req_skill = cur[-1]
        ans = []
        check = []
        for skill, level in req_skill:
            levels = sorted(cont_skill[skill].keys())
            flag = 0
            for cur_level in levels:
                if cur_level >= level:
                    names = cont_skill[skill][cur_level]
                    for name in names:
                        if available[name] == 1:
                            ans.append(name)
                            available[name] = 0
                            flag = 1
                            if cur_level == level:
                                check.append([name, skill])
                            break
                if flag == 1:
                    break
            if flag == 0:
                temp.append(cur)
                for name in ans:
                    available[name] = 1
                break
        if flag == 1 and len(ans) == len(req_skill):
            result += cur[0] + "\n"
            result += ' '.join(ans) + "\n"
            cnt += 1
            for name in ans:
                available[name] = 1
            for name, skill in check:
                cont_skill[skill][cont_name[name][skill]].remove(name)
                if cont_name[name][skill] + 1 not in cont_skill[skill]:
                    cont_skill[skill][cont_name[name][skill] + 1] = []
                cont_skill[skill][cont_name[name][skill] + 1].append(name)
                cont_name[name][skill] += 1
            projects = projects + temp
            temp = []
    print(cnt)
    print(result)
