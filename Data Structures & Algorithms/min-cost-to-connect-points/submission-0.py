class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edge =  []
        for i in range(n) :
            for j in range(i+1,n):
                cost = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edge.append((cost,i,j))
        
        edge.sort()

        parent = list(range(n))

        def find(x):
            while (parent[x] != x):
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        total = 0
        used = 0

        for cost , i , j in edge:
            ri , rj = find(i) , find(j)
            if ri != rj:
                parent[ri] = rj
                total += cost
                used += 1

            if used == n-1:
                break
               
        return total





            

            
             
        