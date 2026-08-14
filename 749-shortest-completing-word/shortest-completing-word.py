class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        target_counts = [0] * 26
        for char in licensePlate:
            if char.isalpha():
                target_counts[ord(char.lower()) - ord('a')] += 1
                
        shortest_word = None
        
        for word in words:
            word_counts = [0] * 26
            for char in word:
                word_counts[ord(char) - ord('a')] += 1
                
            is_valid = True
            for i in range(26):
                if word_counts[i] < target_counts[i]:
                    is_valid = False
                    break
            
            if is_valid:
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
                    
        return shortest_word
