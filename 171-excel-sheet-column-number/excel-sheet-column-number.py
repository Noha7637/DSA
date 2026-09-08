class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dictionary = dict()
        alphabets_list = [chr(i) for i in range(65, 91)]
        number_list = [i for i in range(1, 27)]
        for key, value in zip(alphabets_list, number_list):
            dictionary[key] = value
        list1 = list(columnTitle)
        add = 0
        x = len(list1)
        for i in range(len(list1)):
            j = i+1
            add += (26**(x-j))*dictionary[list1[i]] 
        return add


            
