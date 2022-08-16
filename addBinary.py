class Solution():
    def addBinary(self, a, b):
        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()
        output = []
        c = 0
        n = max(len(a), len(b))
        for _ in range(n):
            sum = 0
            if a:
                sum += int(a[0])
                a.pop(0)
            if b:
                sum += int(b[0])
                b.pop(0)
            sum += c
            if sum >= 2:
                c = 1
                sum -= 2
                output.append(str(sum))
            else:
                output.append(str(sum))
                c = 0
        if c == 1:
            output.append(str(1))
        output.reverse()
        output = ''.join(output)
        return output
        
        
        

a = "1010"
b = "1011"

testcase = Solution()
print(testcase.addBinary(a,b))