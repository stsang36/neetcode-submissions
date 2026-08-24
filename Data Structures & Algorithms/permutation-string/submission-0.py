class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freqS1 = [0] * 26

        for c in s1:
            index = ord(c) - ord("a")
            freqS1[index] += 1
        
        window = deque()


        i = 0
        freqS2 = [0] * 26
        n = len(s1)

        while i < len(s2):
            window.append(s2[i])
            index = ord(s2[i]) - ord("a")
            freqS2[index] += 1

            if n < len(window):
                c = window.popleft()
                index = ord(c) - ord("a")
                freqS2[index] -= 1
            
            
            if n == len(window): 
                if freqS2 == freqS1:
                    return True
            i+=1

        return False
            

            




        
        