class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        word_found, sol = [False], []

        m = len(board)
        n = len(board[0])


        def backtrack(r,c):
            if word_found[0]:
                return
            if len(sol) == len(word):
                word_found[0] = True
                return
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[len(sol)]:
                return

            temp = board[r][c]
            board[r][c] = '#'
            sol.append(temp)
            backtrack(r+1,c)
            backtrack(r-1,c)
            backtrack(r,c+1)
            backtrack(r,c-1)
            sol.pop()
            board[r][c] = temp

        
        for r in range(m):
            for c in range(n):
                if word_found[0] == True:
                    return True
                else:
                    if board[r][c] == word[0]:
                        backtrack(r,c)

        return word_found[0]