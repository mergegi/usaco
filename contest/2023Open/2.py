#import sys
#sys.stdin = open('2.in')

# read input
T = int(input().strip())

# solve for one case
def solve(nouns, tvs, itvs, conj, C, P, N):
    max_wc = 0
    counts = [0] * 4

    for c_t1 in range(len(itvs) + 1):
        c_t2 = min((len(nouns) - c_t1) // 2, len(tvs))
        while c_t2 >= 0:
            # how many conj words we can use?
            c_con = min((c_t1 + c_t2) // 2, len(conj))
            if c_t1 + c_t2 - c_con <= P:
                break
            c_t2 -= 1
        
        if c_t2 < 0:
            continue
        c_n = 0
        if c_t2 > 0:
            c_n = min(len(nouns) - c_t1 - 2 * c_t2, C)
        c_w = c_t1 * 2 + c_t2 * 3 + c_n + c_con
        if c_w > max_wc:
            max_wc = c_w
            count = [c_t1, c_t2, c_con, c_n]

    print(max_wc)
    if max_wc > 0:
        c_t1, c_t2, c_con, c_n = count
        sentences = []
        # construct t1 sentence 
        for i in range(c_t1):
            s = nouns.pop() + ' ' + itvs.pop()
            sentences.append(s)
        # construct t2 sentence
        for i in range(c_t2):
            s = nouns.pop() + ' ' + tvs.pop() + ' ' + nouns.pop()
            sentences.append(s)
        
        # if c_t2 > 0, add all extra nouns to the last t2 sentence\
        if c_t2 > 0:
            for i in range(c_n):
                sentences[-1] = sentences[-1] + ', ' + nouns.pop()
        
        # construct compound sentence
        com_sentences = []
        for i in range(c_con):
            comp_s = sentences.pop() + ' ' + conj.pop() + ' ' + sentences.pop() 
            com_sentences.append(comp_s)

        all_sentences = sentences + com_sentences

        result = '. '.join(all_sentences)
        result += '.'
        print(result)
    else:
        print()
 

for _ in range(T):
    N, C, P = [int(e) for e in input().strip().split()]
    nouns = []
    tvs = []
    itvs = []
    conj = []

    for i in range(N):
        w, t = input().strip().split()
        if t[0] == 'n':
            nouns.append(w)
        elif t[0] == 'i':
            itvs.append(w)
        elif t[0] == 't':
            tvs.append(w)
        else:
            conj.append(w)

    solve(nouns, tvs, itvs, conj, C, P, N)
# find out max words count

# construct all sentence

# print result