class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        player1 = 0
        player2 = 0
        while True:
            if x == 0:
                return "Bob"
                break
            else:
                player1+=75
                x-=1
                while y!=0:
                    player1+=10
                    y-=1
                    if player1 == 115:
                        break
                else:
                    return "Bob"
            if x == 0:
                return "Alice"
            else:
                player2+=75
                x-=1
                while y!=0:
                    player2+=10
                    y-=1
                    if player2 == 115:
                        break
                else:
                    return "Alice"
            player1 = 0
            player2 = 0
    
            
            
            

                


        