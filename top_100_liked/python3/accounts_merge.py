import re
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        result = []
        name_count = defaultdict(lambda: 0)
        distinct_email = set()
        email_parent = {}
        name_parent = {}
        name_rank   = {}
        for acc in accounts:
            name = acc[0] + str(name_count[acc[0]])
            name_count[acc[0]] += 1
            name_parent[name] = name
            name_rank[name] = 0
            for i in range(1, len(acc)):
                distinct_email.add(acc[i])
                if(acc[i] in email_parent):
                    self.union(email_parent[acc[i]], name, name_parent, name_rank)
                else:
                    email_parent[acc[i]] = name
        name_emails = defaultdict(lambda: [])
        for emails in list(distinct_email):
            name_emails[self.find(email_parent[emails], name_parent)].append(emails)
            
        pattern = "[0-9]"
        for k in name_emails.keys():
            name_emails[k].sort()
            result.append([re.sub(pattern, "", k)] + name_emails[k])
        return result
        
    def union(self, n1, n2, parent, rank):
        p1 = self.find(n1, parent)
        p2 = self.find(n2, parent)
        if(rank[p1] > rank[p2]):
            parent[p2] = parent[p1]
        elif(rank[p2] > rank[p1]):
            parent[p1] = parent[p2]
        else:
            parent[p2] = parent[p1]
            rank[p1] += 1
            
    ### path compression
    def find(self, n, parent):
        while(parent[n] != n):
            parent[n] = parent[parent[n]]
            n = parent[n]
        return n
        
                
