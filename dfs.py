# -*- coding: utf-8 -*-

GOLE_SIZE = 2
path_count = 0

def dfs(x, y):
    global path_count

    if x == GOLE_SIZE and y == GOLE_SIZE:
        path_count += 1
        return

    if y < GOLE_SIZE:
        dfs(x, y+1)

    if x < GOLE_SIZE:
        dfs(x+1, y)

if __name__ == '__main__':
    dfs(0, 0)
    print('最短経路のpathの数：' + str(path_count))