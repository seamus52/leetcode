# a better implementation would use dict of dict
# a simpler implementation would be no delete and every other function 
# turned into 1-liner
class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.db = {}
        self.id = {}
        for name in names:
            self.id[name] = 0
            self.db[name] = [] 
        
    def insertRow(self, name: str, row: List[str]) -> None:
        self.id[name] += 1
        self.db[name].append((self.id[name] , row))
        
        

    def deleteRow(self, name: str, rowId: int) -> None:
        idx_to_delete = -1
        for i, row in enumerate(self.db[name]):
            if row[0] == rowId:
                idx_to_delete = i
                break
        self.db[name].pop(idx_to_delete)
        
    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        idx = -1
        for i, row in enumerate(self.db[name]):
            if row[0] == rowId:
                idx = i
                break
        return self.db[name][idx][1][columnId - 1]
        
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)
