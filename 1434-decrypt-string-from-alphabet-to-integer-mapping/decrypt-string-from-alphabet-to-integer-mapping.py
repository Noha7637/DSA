class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        for i in range(len(s)):
            if i < len(s)-2 and s[i+2]=="#":
                temp = s[i] + s[i+1]
                if temp == "10":
                    arr.append("j")
                elif temp == "11":
                    arr.append("k")
                elif temp == "12":
                    arr.append("l")
                elif temp == "13":
                    arr.append("m")
                elif temp == "14":
                    arr.append("n")
                elif temp == "15":
                    arr.append("o")
                elif temp == "16":
                    arr.append("p")
                elif temp == "17":
                    arr.append("q")
                elif temp == "18":
                    arr.append("r")
                elif temp == "19":
                    arr.append("s")
                elif temp == "20":
                    arr.append("t")
                elif temp == "21":
                    arr.append("u")
                elif temp == "22":
                    arr.append("v")
                elif temp == "23":
                    arr.append("w")
                elif temp == "24":
                    arr.append("x")
                elif temp == "25":
                    arr.append("y")
                elif temp == "26":
                    arr.append("z")
            elif s[i] != "#":
                if i < len(s)-1 and s[i+1]=="#":
                         pass
                else:
                    if s[i] == "1":
                        arr.append("a")
                    elif s[i] == "2":
                        arr.append("b")
                    elif s[i] == "3":
                        arr.append("c")
                    elif s[i] == "4":
                        arr.append("d")
                    elif s[i] == "5":
                        arr.append("e")
                    elif s[i] == "6":
                        arr.append("f")
                    elif s[i] == "7":
                        arr.append("g")
                    elif s[i] == "8":
                        arr.append("h")
                    elif s[i] == "9":
                        arr.append("i")
        new_string = "".join(arr)
        return new_string
        
                    
                      



                
        