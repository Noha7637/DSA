class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        i = 0
        arr = []
        temp1=0
        temp2=0
        while i < len(command):
            if i<len(command)-1:
                temp1 = command[i]+ command[i+1]
            if i<len(command)-3:
                temp2 = command[i]+ command[i+1] + command[i+2] + command[i+3]
            if command[i]=="G":
                arr.append("G")
                i = i+1
            if temp1=="()":
                arr.append("o")
                i = i+2
                temp1 = 0
            if temp2=="(al)":
                arr.append("al")
                i = i + 4
                temp2 = 0
        new_string="".join(arr)
        return new_string
                   


            
                
            