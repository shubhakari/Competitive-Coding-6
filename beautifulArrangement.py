class Solution:
    # TC : O(k) - k is no of valid permutations
    # SC : O(n)
    def backtrack(self,idx,n,temparr):
        if len(temparr) == n:
            print(temparr)
            self.ct += 1
            return
        for i in range(1,n+1):
            if i not in temparr and (i%idx == 0 or idx%i == 0):
                temparr.append(i)
                self.backtrack(idx+1,n,temparr)
                temparr.pop()
    def countArrangement(self, n: int) -> int:
        if n == 0:
            return 0
        self.ct = 0
        self.backtrack(1,n,[])
        return self.ct