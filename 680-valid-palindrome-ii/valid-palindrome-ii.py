class Solution:
    def validPalindrome(self, s: str) -> bool:
        slist = list(s)
        temp = ""
        ptr1 = 0
        ptr2 = len(s)-1
        if slist==slist[::-1]:
            return True
        while ptr1<=ptr2:
            if slist[ptr1] != slist[ptr2]:
                temp = slist.pop(ptr1)
                if slist==slist[::-1]:
                    return True
                else:
                    slist.insert(ptr1, temp)
                    temp = slist.pop(ptr2)
                    if slist==slist[::-1]:
                        return True
                    elif slist!=slist[::-1]:
                        return False 
                    slist.insert(ptr2, temp)
            ptr1+=1
            ptr2-=1       



            
            