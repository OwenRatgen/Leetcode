class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = {}
        ls = []

        for ele in arr:
            if res.get(ele) == None:
                res[ele] = 1
            else:
                res[ele] = res.get(ele) + 1
        
        for val in res.values():
            if val in ls:
                return False
            else:
                ls.append(val)

        return True
        