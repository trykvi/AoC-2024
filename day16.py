import heapq

def find_element(e, map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == e):
                return (x, y)
            
    return (-1, -1)

def add_tuples(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

d_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]

""" class Graph:
    graph = {}

    def __init__(self, map):
        queue = Queue()
        queue.put(find_element('S', map))
        visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
        path =
        current_dir = (0, -1)
        while(not queue.empty()):
            current_pos = queue.get()
            x = current_pos[0]
            y = current_pos[1]
            visited[y][x] = True

            if(not visited[y-1][x] and map[y-1][x] != '#'):

                queue.put((y-1, x))
     """

def dijkstra(map, startpos, endpos):
    dist = [[9999999999 for _ in range(len(map[0]))] for _ in range(len(map))]
    dist[startpos[1]][startpos[0]] = 0
    pq = [(0, startpos, (-1, 0))]
    """ for d in d_list:
        pos = add_tuples(d, startpos)
        if(map[pos[1]][pos[0]] != '#'):
            pq.put() """
    while(len(pq) > 0):
        current_dist, current_node, current_dir = heapq.heappop(pq)

        for d in d_list:
            adj_node = add_tuples(current_node, d)
            if(current_dir == d):
                adj_dist = current_dist + 1
            else:
                adj_dist = current_dist + 1001
            if(map[adj_node[1]][adj_node[0]] != '#' and dist[adj_node[1]][adj_node[0]] > adj_dist):
                dist[adj_node[1]][adj_node[0]] = adj_dist
                heapq.heappush(pq, (adj_dist, adj_node, d))

    return dist[endpos[1]][endpos[0]]

def part1(input):
    map = [list(line) for line in input.split("\n")[:-1]]
    return dijkstra(map, find_element('S', map), find_element('E', map))



    
            

def part2(input):
    map = [list(line) for line in input.split("\n")[:-1]]

print(part1(open("input16.txt", "r").read()))