class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or "" in strs or len(strs) == 1 and len(strs[0]) == 1:
            return "" if "" in strs else strs[0]
        
        pre_fixes = {}
        common_letters = {}
        greatest = {}
        count = 0
        index = 0
        for i in range(0, len(strs)):
            pre_fixes[i] = []
            common_letters[i] = []
            for j in range(0, len(strs[i])):
                pre_fixes[i].append(strs[i][j])
                
                if i > 0:
                    if strs[i-1][j] == pre_fixes[i][j]:
                        common_letters[i].append(strs[i][j])
                        count += 1
                    else: 
                        greatest[i] = common_letters[i]
                        count = 0
                        index = i
                        break
        common_prefix = "".join(greatest[index])
        return common_prefix
