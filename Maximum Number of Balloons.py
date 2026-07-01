class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_freq = Counter(text)

        return min(char_freq['b'], char_freq['a'], 
                    char_freq['l']//2, char_freq['o']//2,
                    char_freq['n'])
