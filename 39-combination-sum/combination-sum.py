class Solution:
    def combinationSum(self, c, t):
        ans = []

        def f(i, a, s):
            if s == t:
                ans.append(a[:])
                return

            if s > t:
                return

            for j in range(i, len(c)):
                a.append(c[j])
                f(j, a, s + c[j])
                a.pop()

        f(0, [], 0)
        return ans