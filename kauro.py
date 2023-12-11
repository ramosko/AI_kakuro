import copy
class KakuroSolver:
    def __init__(self, puzzel):
        self.puzzel = puzzel
        self.towDPosibilityArray = self.make2DPosibilityArray(puzzel)
        self.initializePosibilityArray()
        

    def isBlock(self, row, col):
        return self.puzzel[row][col] == "x"
    
    def isEmpty(self, row, col):
        return self.puzzel[row][col] == "-"
    
    def isBlockNumber(self, row, col):
        if(not self.isBlock(row, col) and not self.isEmpty(row, col) and not type(self.puzzel[row][col]) == int):
            return True
        return False
    
    def findEmpty(self):
        for row in range(len(self.puzzel)):
            for col in range(len(self.puzzel)):
                if self.isEmpty(row, col):
                    return row, col
        return None, None
    
    def findLeftBlockNumber(self, row, col):
        for i in range(col, -1, -1):
            if self.isBlockNumber(row, i):
                return row,  i
        return None, None
    
    def findRightBlockNumber(self, row, col):
        i , j = self.findLeftBlockNumber(row, col)
        for k in range(j + 1, len(self.puzzel)):
            if self.isBlockNumber(row, k):
                return row, k
        return None, None
    
    def findUpBlockNumber(self, row, col):
        for i in range(row, -1, -1):
            if self.isBlockNumber(i, col):
                return i, col
        return None, None
    
    def findDownBlockNumber(self, row, col):
        i, j = self.findUpBlockNumber(row, col)
        for k in range(i + 1, len(self.puzzel)):
            if self.isBlockNumber(k, col):
                return k, col
        return None, None
    
    
    def UsedInRow(self, row, col ,num):
        i , j = self.findLeftBlockNumber(row, col)
        ii , jj = self.findRightBlockNumber(row, col)

        if ii == None:
            ii = row
            jj = len(self.puzzel)

        for c in range(j + 1, jj):
            if self.puzzel[row][c] == num:
                return True
        return False
    
    def UsedInCol(self, row, col, num):
        i , j = self.findUpBlockNumber(row, col)
        ii , jj = self.findDownBlockNumber(row, col)
        if ii == None:
            ii = len(self.puzzel)
            jj = col
        for r in range(i + 1, ii):
            if self.puzzel[r][col] == num:
                return True
        return False
    
    def sumOfRow(self, row, col):
        sum = 0
        i , j = self.findLeftBlockNumber(row, col)
        ii , jj = self.findRightBlockNumber(row, col)
        if ii == None:
            ii = row
            jj = len(self.puzzel)
        for c in range(j + 1, jj):
            if(type(self.puzzel[row][c]) == int):
                sum += int(self.puzzel[row][c])
        return sum

    def sumOfCol(self, row, col):
        sum = 0
        i , j = self.findUpBlockNumber(row, col)
        ii , jj = self.findDownBlockNumber(row, col)
        if jj == None:
            ii = len(self.puzzel)
            jj = col

        for r in range(i + 1, ii):
            if(type(self.puzzel[r][col]) == int):
                sum += int(self.puzzel[r][col])
        return sum

    
    def numberOfRow(self, row, col):
        i , j = self.findLeftBlockNumber(row , col)
        return int(self.puzzel[row][j][len(self.puzzel[row][j]) - 2]) * 10 + int(self.puzzel[row][j][len(self.puzzel[row][j]) - 1])

    
    def numberOfCol(self,row, col):
        i , j = self.findUpBlockNumber(row, col)
        return int(self.puzzel[i][col][0]) * 10 + int(self.puzzel[i][col][1])
    
    def isFullRow(self, row, col):
        i , j = self.findLeftBlockNumber(row, col)
        ii , jj = self.findRightBlockNumber(row, col)
        if ii == None:
            ii = row
            jj = len(self.puzzel)

        for c in range(j + 1, jj):
            if self.isEmpty(row, c):
                return False
        return True
    
    def isFullCol(self,row, col):
        i , j = self.findUpBlockNumber(row, col)
        ii , jj = self.findDownBlockNumber(row, col)
        if ii == None:
            ii = len(self.puzzel)
            jj = col
        for r in range(i + 1, ii):
            if self.isEmpty(r, col):
                return False
        return True
    
    def isSafe(self, row, col, num):
        self.puzzel[row][col] = num
        if(self.isFullRow(row, col) and self.numberOfRow(row, col) != self.sumOfRow(row, col)):
            self.puzzel[row][col] = "-"
            return False
        if(self.isFullCol(row, col) and self.numberOfCol(row, col) != self.sumOfCol(row, col)):
            self.puzzel[row][col] = "-"
            return False
        self.puzzel[row][col] = "-"
        if(self.UsedInRow(row, col, num) or self.UsedInCol(row, col, num)):
            return False
        return True
    

    def solve(self):
        row, col = self.findEmpty()
        if row == None:
            return True
        for num in range(1, 10):
            if self.isSafe(row, col, num):
                self.puzzel[row][col] = num
                if self.solve():
                    return True
                self.puzzel[row][col] = "-"
        return False
    

    def Print(self):
        if(self.solve()):
            for i in range(len(self.puzzel)):
                for j in range(len(self.puzzel)):
                    print(self.puzzel[i][j], end=" ")
                print()
        else:
            print("No solution exists")

                                #//////////////////////////////////////Pro Version////////////////////////////////////////////////////////
    def make2DPosibilityArray(self, puzzel):
        size = len(puzzel)
        two_dimensional_array = [[[1,2,3,4,5,6,7,8,9] for _ in range(size)] for _ in range(size)]
        return  two_dimensional_array
    
    def removeNumPosibilityFromRow(self, row, col, num):
        i , j = self.findLeftBlockNumber(row, col)
        ii , jj = self.findRightBlockNumber(row, col)
        if ii == None:
            ii = row
            jj = len(self.puzzel)
        for c in range(j + 1, jj):
            if num in self.towDPosibilityArray[row][c]:
                self.towDPosibilityArray[row][c].remove(num)
    
    def removeNumPosibilityFromCol(self, row, col, num):
        i , j = self.findUpBlockNumber(row, col)
        ii , jj = self.findDownBlockNumber(row, col)
        if ii == None:
            ii = len(self.puzzel)
            jj = col
        for r in range(i + 1, ii):
            if num in self.towDPosibilityArray[r][col]:
                self.towDPosibilityArray[r][col].remove(num)

    def addNumPosibilityToRow(self, row, col, num):
        i , j = self.findLeftBlockNumber(row, col)
        ii , jj = self.findRightBlockNumber(row, col)
        if ii == None:
            ii = row
            jj = len(self.puzzel)
        for c in range(j + 1, jj):
            if num not in self.towDPosibilityArray[row][c]:
                self.towDPosibilityArray[row][c].append(num)
    
    def addNumPosibilityToCol(self, row, col, num):
        i , j = self.findUpBlockNumber(row, col)
        ii , jj = self.findDownBlockNumber(row, col)
        if ii == None:
            ii = len(self.puzzel)
            jj = col
        for r in range(i + 1, ii):
            if num not in self.towDPosibilityArray[r][col]:
                self.towDPosibilityArray[r][col].append(num)
    
    def isRowZeroPosibilities(self, row, col):
        i , j = self.findLeftBlockNumber(row, col)
        ii , jj = self.findRightBlockNumber(row, col)
        if ii == None:
            ii = row
            jj = len(self.puzzel)
        for c in range(j + 1, jj):
            if len(self.towDPosibilityArray[row][c]) == 0:
                return True
        return False

    
    def isColZeroPosibilities(self, row, col):
        i , j = self.findUpBlockNumber(row, col)
        ii , jj = self.findDownBlockNumber(row, col)
        if ii == None:
            ii = len(self.puzzel)
            jj = col
        for r in range(i + 1, ii):
            if len(self.towDPosibilityArray[r][col]) == 0:
                return True
        return False
    
    def removeBiggerNumPosibilityInRow(self, row, col):
        i , j = self.findLeftBlockNumber(row, col)
        ii , jj = self.findRightBlockNumber(row, col)
        if ii == None:
            ii = row
            jj = len(self.puzzel)
        kk = self.numberOfRow(row, col) - self.sumOfRow(row, col)
        for c in range(j + 1, jj):
            for k in range(10):
                if k in self.towDPosibilityArray[row][c] and k > kk:
                    self.towDPosibilityArray[row][c].remove(k)

    def removeBiggerNumPosibilityInCol(self, row, col):
        i , j = self.findUpBlockNumber(row, col)
        ii , jj = self.findDownBlockNumber(row, col)
        if ii == None:
            ii = len(self.puzzel)
            jj = col
        kk = self.numberOfCol(row, col) - self.sumOfCol(row, col)
        for r in range(i + 1, ii):
            for k in range(10):
                if k in self.towDPosibilityArray[r][col] and k > kk:
                    self.towDPosibilityArray[r][col].remove(k)
    
    def addBiggerNumPosibilityInRow(self, row, col):
        i , j = self.findLeftBlockNumber(row, col)
        ii , jj = self.findRightBlockNumber(row, col)
        if ii == None:
            ii = row
            jj = len(self.puzzel)
        kk = self.numberOfRow(row, col) - self.sumOfRow(row, col)
        for c in range(j + 1, jj):
            for k in range(10):
                if k not in self.towDPosibilityArray[row][c] and k > kk:
                    self.towDPosibilityArray[row][c].append(k)

    def addBiggerNumPosibilityInCol(self, row, col):
        i , j = self.findUpBlockNumber(row, col)
        ii , jj = self.findDownBlockNumber(row, col)
        if ii == None:
            ii = len(self.puzzel)
            jj = col
        kk = self.numberOfCol(row, col) - self.sumOfCol(row, col)
        for r in range(i + 1, ii):
            for k in range(10):
                if k not in self.towDPosibilityArray[r][col] and k > kk:
                    self.towDPosibilityArray[r][col].append(k)

    def upDate2DPosibilityArray(self, row, col):
        self.towDPosibilityArray[row][col] = [1,2,3,4,5,6,7,8,9]
        k = self.numberOfRow(row, col) - self.sumOfRow(row, col)
        kk = self.numberOfCol(row,col) - self.sumOfCol(row, col)
        for i in range(1, 10):
            if(self.UsedInRow(row, col, i) or self.UsedInCol(row, col, i)):
                self.towDPosibilityArray[row][col].remove(i)
            if((i > k or i > kk) and i in self.towDPosibilityArray[row][col]):
                self.towDPosibilityArray[row][col].remove(i)
    
    def proIsSafe(self, row, col, num):
        self.puzzel[row][col] = num

        self.removeNumPosibilityFromRow(row, col, num)
        if self.isRowZeroPosibilities(row, col) and not self.isFullRow:
            self.puzzel[row][col] = "-"
            self.upDate2DPosibilityArray(row,col)
            return False
        
        self.removeNumPosibilityFromCol(row, col, num)
        if self.isColZeroPosibilities(row, col) and not self.isFullCol:
            self.puzzel[row][col] = "-"
            self.upDate2DPosibilityArray(row,col)
            return False
        
        self.removeBiggerNumPosibilityInRow(row, col)
        if self.isRowZeroPosibilities(row, col) and not self.isFullRow:
            self.puzzel[row][col] = "-"
            self.upDate2DPosibilityArray(row,col)
            return False
        
        self.removeBiggerNumPosibilityInCol(row, col)
        if self.isColZeroPosibilities(row, col) and not self.isFullCol:
            self.puzzel[row][col] = "-"
            self.upDate2DPosibilityArray(row,col)
            return False
        
        if self.isFullRow(row, col) and self.numberOfRow(row, col) != self.sumOfRow(row, col):
            self.puzzel[row][col] = "-"
            self.upDate2DPosibilityArray(row,col)
            return False
        
        if self.isFullCol(row, col) and self.numberOfCol(row, col) != self.sumOfCol(row, col):
            self.puzzel[row][col] = "-"
            self.upDate2DPosibilityArray(row,col)
            return False
        
        self.puzzel[row][col] = "-"
        return True
    
    def initializePosibilityArray(self):
        for i in range(len(self.puzzel)):
            for j in range(len(self.puzzel)):
                if self.isEmpty(i, j):
                    for k in range(1, 10):
                        if(k in self.towDPosibilityArray[i][j] and k > self.numberOfRow(i, j)):
                            self.towDPosibilityArray[i][j].remove(k)

                        if(k in self.towDPosibilityArray[i][j] and k > self.numberOfCol(i, j)):
                            self.towDPosibilityArray[i][j].remove(k)
    

    def findMinPosibility(self):
        min = 10
        row = None
        col = None
        for i in range(len(self.puzzel)):
            for j in range(len(self.puzzel)):
                if self.isEmpty(i, j) and len(self.towDPosibilityArray[i][j]) < min:
                    min = len(self.towDPosibilityArray[i][j])
                    row = i
                    col = j
        if(row != None and col != None):
            if len(self.towDPosibilityArray[row][col]) == 0:
                return None, None
        return row, col
        
    def proSolve(self):
        row, col = self.findMinPosibility()
        if row == None:
            return True
        self.upDate2DPosibilityArray(row, col)
        copy2DPosibilityArray = copy.deepcopy(self.towDPosibilityArray)
        for i in range(1, 10):
            if i in self.towDPosibilityArray[row][col]:
                if self.proIsSafe(row, col, i):
                    self.puzzel[row][col] = i
                    if self.proSolve():
                        return True
                    self.puzzel[row][col] = "-"
                    self.towDPosibilityArray = copy2DPosibilityArray 
        return False
    
    def proPrint(self):
        
        if(self.proSolve()):
            for i in range(len(self.puzzel)):
                for j in range(len(self.puzzel)):
                    print(self.puzzel[i][j], end=" ")
                print()
        else:
            print("No solution exists")
    





SamplePuzzel1 = [["x", "05/", "19/", "x"],
                ["/13", "-", "-", "04/"],
                ["/12", "-", "-", "-"],
                ["x", "/03", "-", "-"]]



solver1 = KakuroSolver(SamplePuzzel1)
solver1.Print()
solver1.proPrint()