# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         pre_fixes = {}
#         common_letters = {}
#         greatest = {}
#         # count = 0
#         index = 0
#         for i in range(0, len(strs)):
#             pre_fixes[i] = []
#             common_letters[i] = []
#             greatest[i] = strs[i]
#             print("pre_fixes[i]", pre_fixes[i], i)
#             print("commone_letters[i]", common_letters[i], i)
#             for j in range(0, len(strs[i])):
#                 pre_fixes[i].append(strs[i][j])
#                 print("pre_fixes[i].append", pre_fixes[i] )
                
#                 if i > 0:
#                     print(True)
#                     if strs[i-1][j] == pre_fixes[i][j]:
#                         print(True)
#                         common_letters[i].append(strs[i][j])
#                         # count += 1
#                         index = i
#                         greatest[i] = common_letters[i]
#                     else: 
#                         print(True)
#                         greatest[i] = common_letters[i]
#                         # count = 0
#                         index = i
#                         break
#         print(greatest)
#         if len(greatest) > 0:
#             common_prefix = "".join(greatest[index])
#         else: common_prefix = ""
#         return common_prefix
class Solustion:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i)) == 1:
                prefix += i[0]
            else: break
        return prefix