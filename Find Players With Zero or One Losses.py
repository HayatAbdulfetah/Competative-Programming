class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loss_count = {}
        answer = [[], []]
        
        for match in matches:
            loss_count[match[0]] = loss_count.get(match[0], 0)
            loss_count[match[1]] = loss_count.get(match[1], 0) + 1
            
        
        answer[0] = sorted([k for k, v in loss_count.items() if v == 0])
        answer[1] = sorted([k for k, v in loss_count.items() if v == 1])
        
        return answer
            
