from typing import List 
class Solution:
    def isMatch(self, s, p):
        sn, pn = len(s), len(p)
        si = pi = 0
        save_si, save_pi = None, None
        while si < sn:
            if pi < pn and (p[pi] == '?' or p[pi] == s[si]):
                si += 1
                pi += 1
            elif pi < pn and p[pi] == '*':
                # Meet "*", save si and pi, searching for next character
                save_si, save_pi = si + 1, pi
                pi += 1
            elif save_pi is not None:
                # Dead end, restore si and pi, carry on.
                si, pi = save_si, save_pi
            else:
                return False
        # Check trailing "*"
        return p[pi:].count("*") == pn - pi