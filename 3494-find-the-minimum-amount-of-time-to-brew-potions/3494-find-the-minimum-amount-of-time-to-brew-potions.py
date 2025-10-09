class Solution:
    def minTime(self, skill, mana):
        n, m = len(skill), len(mana)
        # prefix sum of skills: SK[i] = sum_{t=0..i} skill[t]
        SK = [0] * n
        s = 0
        for i in range(n):
            s += skill[i]
            SK[i] = s

        # S is S[j-1] (start time of previous potion on wizard 0)
        S = 0
        for j in range(1, m):
            mj = mana[j]
            mjm1 = mana[j - 1]
            max_lb = -10**18  # large negative initial
            prev_sk = 0  # SK[i-1], SK[-1] considered 0

            # compute max over i of ( SK[i]*mana[j-1] - SK[i-1]*mana[j] )
            for i in range(n):
                si = SK[i]
                if i == 0:
                    lb = si * mjm1
                else:
                    lb = si * mjm1 - prev_sk * mj
                if lb > max_lb:
                    max_lb = lb
                prev_sk = si

            S += max_lb

        # makespan = start time of last potion on wizard0 + total time for last potion on all wizards
        return S + SK[-1] * mana[-1]
