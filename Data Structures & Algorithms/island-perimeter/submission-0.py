class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        check = deque()
        perimeter  = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    check.append([row, col])
                    while check:
                        nx, ny = check.pop()
                        if tuple([nx, ny]) not in visited:
                            visited.add(tuple([nx, ny]))
                            connected = 0

                            if nx - 1 >= 0:
                                if grid[nx-1][ny] == 1:
                                    check.append([nx-1, ny])
                                    connected += 1

                            if ny - 1 >= 0:
                                if grid[nx][ny-1] == 1:
                                    check.append([nx, ny-1])
                                    connected += 1

                            if nx + 1 < len(grid):
                                if grid[nx+1][ny] == 1:
                                    check.append([nx+1, ny])
                                    connected += 1

                            if ny + 1 < len(grid[0]):
                                if grid[nx][ny+1] == 1:
                                    check.append([nx, ny+1])
                                    connected += 1
                            print(f"cell {nx}{ny} - perimeter {4 - connected}")
                            perimeter  += (4 - connected)

                        else:
                            continue
                    return perimeter 
            

