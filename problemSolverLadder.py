def print_visited(visited):
    text = ""
    for x in range(26):
        if visited[x] != 0:
            text += "({}, {}) ".format(x, visited[x])
    return text

adyacencies = {}
ROLL_1 = 0
ROLL_2 = 1
ROLL_3 = 2
ROLL_4 = 3
ROLL_5 = 4
ROLL_6 = 5
#Build the board
for i in range(26):
    ads = [i+1,i+2,i+3,i+4,i+5,i+6]
    adyacencies[i] = ads

#Special cases
#Ladder from 1 -> 18
adyacencies[0][ROLL_1] = 18
#Ladder from 8 -> 18
adyacencies[2][ROLL_6] = 18
adyacencies[3][ROLL_5] = 18
adyacencies[4][ROLL_4] = 18
adyacencies[5][ROLL_3] = 18
adyacencies[6][ROLL_2] = 18
adyacencies[7][ROLL_1] = 18
#Snake from 22 -> 20
adyacencies[21][ROLL_1] = 20
adyacencies[20][ROLL_2] = 20
adyacencies[19][ROLL_3] = 20
adyacencies[18][ROLL_4] = 20
adyacencies[17][ROLL_5] = 20
adyacencies[16][ROLL_6] = 20
#Snake from 24 -> 2
adyacencies[23][ROLL_1] = 2
adyacencies[22][ROLL_2] = 2
adyacencies[21][ROLL_3] = 2
adyacencies[20][ROLL_4] = 2
adyacencies[19][ROLL_5] = 2
adyacencies[18][ROLL_6] = 2
#Snake from 15 -> 7
for i in range(9,15):
    adyacencies[i][5-(i-9)] = 7

#BFS until we find the first goal state
queue = [0]
visited = [0 for x in range(26)]
while len(queue) != 0:
    node = queue.pop(0)
    print(node)
    for ady in adyacencies[node]:
        if ady == 26:
            print("Steps: ", visited[node] + 1)
            queue.clear()
            break
        if visited[ady] == 0:
            visited[ady] = visited[node] + 1
            queue.append(ady)
    print(print_visited(visited))
