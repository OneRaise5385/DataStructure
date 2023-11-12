def solve_n_queens(n):
    result = []
    board = [['.'] * n for _ in range(n)]
    
    def is_safe(row, col):
        # 检查列上是否有冲突
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # 检查左上对角线是否有冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 检查右上对角线是否有冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True
    
    def backtrack(row):
        if row == n:
            # 找到一个解决方案
            solution = [''.join(row) for row in board]
            result.append(solution)
            return

        for col in range(n):
            if is_safe(row, col):
                # 在当前位置放置皇后
                board[row][col] = 'Q'
                # 继续尝试下一行
                backtrack(row + 1)
                # 撤销当前位置的皇后，回溯到上一步
                board[row][col] = '.'

    backtrack(0)
    return result

# 测试
solutions = solve_n_queens(8)
for solution in solutions:
    for row in solution:
        print(row)
    print()
