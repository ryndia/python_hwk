def find_path(maze, path=[(0, 0)]):
    count = 0
    point = path[-1]
    if point[0] >= len(maze) or point[0] < 0 or point[1] < 0 or point[1] >= len(maze[0]):
        path.pop()
        return None
    elif maze[point[0]][point[1]] == '*':
        return path
    else:
        if maze[point[0]][point[1]] != "o":
            if maze[point[0]][point[1]] == ">":
                newp = (point[0], point[1] + 1)
            elif maze[point[0]][point[1]] == "^":
                newp = (point[0] - 1, point[1])
            elif maze[point[0]][point[1]] == "<":
                newp = (point[0], point[1] - 1)
            elif maze[point[0]][point[1]] == "v":
                newp = (point[0] + 1, point[1])

            if newp not in path:
                path.append(newp)
                return find_path(maze, path)
            else:
                path.pop()
                return None
        else:
            choice = ["v", "<", ">", "^"]
            for c in choice:
                if c == ">":
                    newp = (point[0], point[1] + 1)
                elif c == "^":
                    newp = (point[0] - 1, point[1])
                elif c == "<":
                    newp = (point[0], point[1] - 1)
                elif c == "v":
                    newp = (point[0] + 1, point[1])

                if newp not in path:
                    path.append(newp)
                    temp = find_path(maze, path)
                    if temp is None:
                        count = count + 1
                        path.pop()
                        if count == 4:
                            return None
                    else:
                        return temp


l = [["o", ">", ">", "v"], [">", "v", "<", "v"], ["^", ">", ">", "*"]]
for x in l:
    print(x)
print(find_path(l))
