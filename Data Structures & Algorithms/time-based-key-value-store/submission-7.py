class TimeMap:

    def __init__(self):
        self.dictionary = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        x = self.dictionary[key]
        l, r = 0, len(x)-1
        res = 0
        if not x:
            return ""
        if x[0][1] > timestamp:
            return ""
        
        while l <= r:
            mid = (l+r)//2
            if x[mid][1] == timestamp:
                res = max(res,mid)
                return x[res][0]
            elif x[mid][1] > timestamp:
                r = mid - 1
            else:
                res = max(res,mid)
                l = mid + 1
        return x[res][0]

        

        
