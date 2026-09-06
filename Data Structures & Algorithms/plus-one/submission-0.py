class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        d = deque(digits)
        
        if not d:
            return [1]

        carry = False

        if d[-1] == 9:
            carry = True
            d[-1] = 0
        else:
            d[-1] += 1
            return list(d)


        for i in range(len(digits)-2, -1, -1):

            if d[i] == 9 and carry == True:
                d[i] = 0
            elif carry == True:
                d[i] += 1
                carry = False
                return list(d)
            else:
                break

        if carry == True:
            d.appendleft(1)
        

        return list(d)

            




        