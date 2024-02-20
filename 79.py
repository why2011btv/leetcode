class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_safe(x, y, board, word, word_index, visited):
            return (0 <= x < len(board)) and (0 <= y < len(board[0])) and not visited[x][y] and board[x][y] == word[word_index]

        def search_word(board, word, x, y, word_index, visited):
            #print(x, y, word_index)
            #if (0 <= x < len(board)) and (0 <= y < len(board[0])):
            #    print(board[x][y])
            #else:
            #    print("out of bounds")

            if word_index == len(word):
                return True
            
            rows = [0, 0, -1, 1]
            cols = [-1, 1, 0, 0] # exploration order: left, right, up, down
            
            if is_safe(x, y, board, word, word_index, visited):
                visited[x][y] = True
                
                for k in range(4):
                    if search_word(board, word, x + rows[k], y + cols[k], word_index + 1, visited):
                        return True
                
                visited[x][y] = False  # Backtrack
            
            return False

        def word_search(board, word):
            if not board or not word:
                return False
            
            rows, cols = len(board), len(board[0])
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == word[0] and search_word(board, word, i, j, 0, visited):
                        return True
            
            return False

        return(word_search(board, word))


# https://chat.openai.com/share/fa954947-621d-45bc-bb29-4aa997d67ab2

# [["A","B","C","E"],
#  ["X","F","C","S"],
#  ["A","D","E","E"]]

# "ABCCED"

# Exploration order:
# A -> left of A -> right of A (B) -> left of B -> right of B (C) -> left of C -> right of C -> above C -> below C (C) -> left of C (F) -> right of C (S) -> above C (C) -> below C (E) -> 
# left of E (D) -> left of D (A), word_index == len(word), return True
