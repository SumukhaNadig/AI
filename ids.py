#Ids on graph 
# Author Praguna Manvi
graph={0:[1,2,4],1:[3,5],2:[6],4:[7],3:[9],5:[10,11]}
def dfs(src,target,limit):
     global graph
     if src==target:
         return True
     if limit <= 0: return False   
     try:
         for x in graph[src]:
             if dfs(x,target,limit-1): return True             
     except KeyError:
         return False

def iddfs(src,target,depth):
    for limit in range(0,depth+1):
        if dfs(src,target,limit):
            return True
    return False


print(iddfs(0,11,3))
