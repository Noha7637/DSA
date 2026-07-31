class Solution:
    def minimumPushes(self, word: str) -> int:
        count =  Counter(word)
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1]))
        arr = []
        for i in sorted_count.keys():
                arr.append(i)
        arr2 = arr[::-1]
        mycounter = 0
        for i in range(len(word)):
            if word[i] in arr2[0:8]:
                mycounter +=1
            elif word[i] in arr2[8:16]:
                mycounter +=2
            elif word[i] in arr2[16:24]:
                mycounter +=3
            elif word[i] in arr2[24:26]:
                mycounter +=4
        return mycounter
        