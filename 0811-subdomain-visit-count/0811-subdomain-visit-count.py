from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        
        for info in cpdomains:
            count, domain = info.split(" ")
            count = int(count)
            subdomains = domain.split(".")
            
            for i in range(len(subdomains)):
                d[".".join(subdomains[i:])] += count
                
        ret = []
        
        for key, value in d.items():
            ret.append(str(value) + " " + key)
        
        return ret