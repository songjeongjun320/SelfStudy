class Solution():
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        make_morse = []
        for _ in range(len(words)):
            tmp = ""
            for i in range(len(words[_])):
                tmp += morse[ord(words[_][i])-97]
            if not tmp in make_morse:
                make_morse.append(tmp)
        return len(make_morse)

    
testcase = Solution()

words = ["gin","zen","gig","msg"]
print(testcase.uniqueMorseRepresentations(words))
