class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransomList = []
        magazineList = []
        for _ in range(len(ransomNote)):
            ransomList.append(ransomNote[_])
        for _ in range(len(magazine)):
            magazineList.append(len(magazine))
        ransomList.sort()
        magazineList.sort()
        
        while ransomList:
            if ransomList[0] in magazineList:
                magazineList.remove(ransomList[0])
                ransomList.pop(0)
            else:
                return False
        return True
            
        
        
    
testcase = Solution()
ransomNote = "aa"
magazine = "aab"
print(testcase.canConstruct(ransomNote, magazine))