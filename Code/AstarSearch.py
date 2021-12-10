from heap import heap

inf = 1000000000


class AstarSearch:

    def __init__(self, edges):
        self.graph = {}
        self.ct = 0
        for edge in edges:
            self.joinEdge(edge[0], edge[1])
            self.joinEdge(edge[1], edge[0])

    def joinEdge(self, x, y):
        cnd = self.graph.get(x, 1)
        if cnd == 1:
            self.graph[x] = [y]
        else:
            self.graph[x].append(y)

    def heuristicsValue(self, x, y):
        #return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
        #return 0
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    def pathDistance(self, x, y):

        return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

    def searchPath(self, start, end):

        priority_queue = heap("min")
        par = {}
        distance = {start: 0}
        cc = 0
        fx = self.heuristicsValue(start, end)
        priority_queue.push((fx, start))
        while priority_queue.isEmpty() is False:
            v = priority_queue.pop()[1]
            cc += 1
            if v == end:
                break
            for node in self.graph.get(v, []):
                gx = distance.get(v, 0) + self.pathDistance(v, node)
                if gx < distance.get(node, inf):
                    par[node] = v
                    distance[node] = gx
                    fx = distance[node] + self.heuristicsValue(node, end)
                    priority_queue.push((fx, node))

        node = end
        ans = []
        while node != start:
            ans.append(node)
            node = par[node]
        ans.append(start)
        ans.reverse()
        self.ct += cc
        return ans
