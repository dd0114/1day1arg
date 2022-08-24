#솔직히 왜 그런지 이해가 안간다! 다시 돌아와서 보자!
#https://leetcode.com/problems/reconstruct-itinerary/

import collections
def findItinerary(tickets):
    tickets.sort()
    t_dict = collections.defaultdict(list)
    for i in tickets:
        t_dict[i[0]].append(i[1])
    ans = []
    def dfs(start):
        while t_dict[start]:
            # print("==========================")
            # print("before",t_dict)
            dfs(t_dict[start].pop(0))
            # print("after",t_dict)
            # print("==========================")
        ans.append(start)
        # print("ans???",ans)
    dfs('JFK')    
    return ans[::-1]


print(findItinerary([["JFK","ATL"],["JFK","SFO"],["ATL","SFO"],["SFO","JFK"],["SFO","ATL"]]))