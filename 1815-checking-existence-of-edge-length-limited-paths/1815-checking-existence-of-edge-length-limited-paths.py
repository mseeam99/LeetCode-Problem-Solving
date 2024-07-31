class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        parents = defaultdict(lambda: None)
        sizes = defaultdict(int)
        
        def find(a):
            if a not in parents:
                parents[a] = a
                sizes[a] = 1
                return a

            root = a
            while parents[root] != root:
                root = parents[root]

            while parents[a] != a:
                nxt = parents[a]
                parents[a] = root
                a = nxt
            
            return root
        
        def union(a,b):
            roota = find(a)
            rootb = find(b)
            
            if roota == rootb:
                return
            
            if sizes[roota] > sizes[rootb]:
                sizes[roota] += sizes[rootb]
                sizes[rootb] = 0
                parents[rootb] = roota
            else:
                sizes[rootb] += sizes[roota]
                sizes[roota] = 0
                parents[roota] = rootb
        
        Q, E = len(queries), len(edgeList)
                
        edgeList.sort(key=lambda x: x[2])
        queries = sorted(((u,v,l,i) for i,(u,v,l) in enumerate(queries)), key=lambda x: x[2])
        
        res = [False] * Q
        e_idx = 0
        for p, q, l, i in queries:
            while e_idx < E and edgeList[e_idx][2] < l:
                u, v, _ = edgeList[e_idx]
                union(u, v)
                e_idx += 1
            res[i] = find(p) == find(q)
        return res