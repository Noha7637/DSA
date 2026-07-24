class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        arr = []
        for sentence in sentences:
            arr.append(len(sentence.split()))
        return max(arr)

        