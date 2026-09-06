class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr1 = [pattern[i] for i in range(len(pattern))]
        arr2 = s.split(" ")
        final1 = []
        final2 = []
        ord1set = list(dict.fromkeys(arr1))
        ord2set = list(dict.fromkeys(arr2))
        print(ord1set)
        print(ord2set)
        if len(set(arr1))!=len(set(arr2)):
            return False
        else:
            for i in range(len(arr1)):
                for j in range(len(ord1set)):
                    if arr1[i]==ord1set[j]:
                        final1.append(j)
            for i in range(len(arr2)):
                for j in range(len(ord2set)):
                    if arr2[i]==ord2set[j]:
                        final2.append(j)
            if final1 == final2:
                return True
            else:
                return False
            

