v = [[] for i in range(100)] 
def addEdge(x, y): 
    v[x].append(y) 
    v[y].append(x) 

def printPath(stack): 
    for i in range(len(stack) - 1): 
        print(stack[i], end = " -> ") 
    print(stack[-1]) 
  

def DFS(vis, x, y, stack): 
    stack.append(x) 
    if (x == y): 
  
        # print the path and return on 
        # reaching the destination node 
        printPath(stack) 
        return
    vis[x] = True
  
    # A flag variable to keep track 
    # if backtracking is taking place 
    flag = 0
    if (len(v[x]) > 0): 
        for j in v[x]: 
              
            # if the node is not visited 
            if (vis[j] == False): 
                DFS(vis, j, y, stack) 
                flag = 1
  
    if (flag == 0): 
  
        # If backtracking is taking 
        # place then pop 
        del stack[-1] 
  
# A utility function to initialise 
# visited for the node and call 
# DFS function for a given vertex x. 
def DFSCall(x, y, n, stack): 
      
    # visited array 
    vis = [0 for i in range(n + 1)] 
  
    #memset(vis, false, sizeof(vis)) 
  
    # DFS function call 
    DFS(vis, x, y, stack) 

valmap = {
    1:2, 2:6, 3:4, 4:3,5:5
}
  
# Driver Code 
n = 10
stack = [] 
  
# Vertex numbers should be from 1 to 9. 
addEdge(1, 2) 
addEdge(1, 3) 
addEdge(2, 4) 
addEdge(2, 5) 
# addEdge(2, 6) 
# addEdge(3, 7) 
# addEdge(3, 8) 
# addEdge(3, 9) 
  
# Function Call 
DFSCall(1, 4, n, stack) 
print(stack)