    def getHeight(self,root):
        #Write your code here
        if root == None:
            return -1
        else:
            esqu = self.getHeight(root.left) 
            dire = self.getHeight(root.right)
            if esqu > dire:
                return esqu + 1
            else:
                return dire + 1
