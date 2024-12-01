with open("message.txt", "r") as f:
    text = f.readlines()

target = "ludvigkanintehittadennatext"

def solve(puzzle):
    a = len(puzzle[0]) 
    b = len(puzzle)
    size = (a, b)
    for i in range(b):
        for j in range(a):
            try:
                if puzzle[i][j] == target[0]:
                    placed_temp = [i, j]
                    solve_internal(puzzle, placed_temp, size, 1)
            except IndexError:
                print("Done")

def solve_internal(puzzle, placed, size, targetPos):
    for i in range(3):
        for j in range(3):
            point = [placed[0] + i - 2, placed[1] + j - 2]
            if [i, j] == [2,2]:
                continue
            if point[0] < 2 or point[1] < 2:
                continue
            if point[0] >= size[0] or point[1] >= size[1]:
                continue           
            if text[point[0]][point[1]] == target[targetPos]:
                print(point, text[point[0]][point[1]])
                targetPos += 1
                solve_internal(puzzle, point, size, targetPos)
        


solve(text)