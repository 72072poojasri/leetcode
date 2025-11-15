class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pos0 = [i for i,ch in enumerate(s) if ch == '0']
        ans = 0
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1
        if not pos0:
            return ans
        B = int(n**0.5) + 1
        m = len(pos0)
        for z in range(1, B + 1):
            if z > m:
                break
            for start in range(0, m - z + 1):
                a = pos0[start]
                b = pos0[start + z - 1]
                prev = pos0[start - 1] if start - 1 >= 0 else -1
                nxt = pos0[start + z] if start + z < m else n
                Lg = a - prev - 1
                Rg = nxt - b - 1
                base_len = b - a + 1
                need = z * z + z - base_len
                if need <= 0:
                    ans += (Lg + 1) * (Rg + 1)
                    continue
                if need > Lg + Rg:
                    continue
                total = (Lg + 1) * (Rg + 1)
                t = need - 1
                x = t if t < Lg else Lg
                if x < 0:
                    bad = 0
                else:
                    full_u = x if t - Rg >= x else (t - Rg if t - Rg >= 0 else -1)
                    if full_u >= 0:
                        cnt_full = (full_u + 1) * (Rg + 1)
                    else:
                        cnt_full = 0
                    rem_start = full_u + 1
                    if rem_start <= x:
                        mcount = x - rem_start + 1
                        first = t - rem_start + 1
                        last = t - x + 1
                        cnt_rem = mcount * (first + last) // 2
                    else:
                        cnt_rem = 0
                    bad = cnt_full + cnt_rem
                ans += total - bad
        return ans