class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1]))
        arr = list(sorted_count.values())[::-1]
        total_count = 0
        for i in range(len(arr)):
            if i<8:
                total_count += arr[i]
            elif i<16:
                total_count += 2*arr[i]
            elif i<24:
                total_count += 3*arr[i]
            elif i<26:
                total_count += 4*arr[i]
        return total_count


                