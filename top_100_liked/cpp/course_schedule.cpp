class Solution {
public:
    // dfs cycle detection
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int> > edges(numCourses);
        // all unvisited initially
        vector<int> visited(numCourses, 0);
        for(auto e : prerequisites){
            edges[e[0]].push_back(e[1]);
        }
        
        for(int i = 0; i < numCourses; i++){
            if(visited[i] == 0)
                if(dfs(i, edges, visited)) 
                    return false;
        }
        
        return true;
    }
    // return true if there is a cycle
    bool dfs(int node, vector<vector<int> >& edges, vector<int>& visited){
        visited[node] = 1;
        for(auto n : edges[node]){
            if(visited[n] == 0)
                if(dfs(n, edges, visited))
                    return true;
            if(visited[n] == 1)
                return true;
            // don't do anything if visited[n] == 2
        }
        visited[node] = 2;
        
        return false;
    }
};
