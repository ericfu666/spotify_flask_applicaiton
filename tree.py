import json

class Node:
    def __init__(self,key=None,val=None):
        self.key=key
        self.val=val
        self.left=None
        self.right=None

    
class Tree:
    def loadTree(self,tupleTree):
        if tupleTree==None:
            return None
        currentNode=Node(key=tupleTree[0][0],val=tupleTree[0][1])
        self.size+=1
        currentNode.left=self.loadTree(tupleTree[1])
        currentNode.right=self.loadTree(tupleTree[2])
        return currentNode

    def __init__(self,jsonfile=None):
    # can initialize from a jsonfile
        if jsonfile==None:
            self.size=0
            self.root=None
        else:
            file=open(jsonfile,"r")
            content=file.read()
            tupleTree=json.loads(content)
            file.close()
            self.size=0
            self.root=self.loadTree(tupleTree)

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
            self.size+=1
        else:
            self.root=Node(key,val)
            self.size+=1

    def _put(self,key,val,currentNode):
        if val<currentNode.val:
            if currentNode.left!=None:
                self._put(key,val,currentNode.left)
            else:
                currentNode.left=Node(key,val)
        else:
            if currentNode.right!=None:
                self._put(key,val,currentNode.right)
            else:
                currentNode.right=Node(key,val)

    def getRange(self,val1,val2):
    # [val1,val2)  
        if self.root:
            result=[]
            self.getRangeHelper(val1,val2,self.root,result)
            return result
        else:
            return None
    
    def getRangeHelper(self,val1,val2,currentNode,result):
    # return all the node.key where node.val belongs to [val1,val2)  
        if currentNode==None:
            return 

        if currentNode.val>val1:
            self.getRangeHelper(val1,val2,currentNode.left,result)
        if val1<=currentNode.val and currentNode.val<val2:
            result.append(currentNode.key)
        if currentNode.val<val2:
            self.getRangeHelper(val1,val2,currentNode.right,result)
    
    def getHeight(self):
    # get the height of the tree
        if self.root==None:
            return None
        else:
            return self.getHeightHelper(self.root)
    def getHeightHelper(self,currentNode):
        if currentNode.left==None and currentNode.right==None:
            return 0
        elif currentNode.left==None:
            return 1+self.getHeightHelper(currentNode.right)
        elif currentNode.right==None:
            return 1+self.getHeightHelper(currentNode.left)
        else:
            return 1+max(self.getHeightHelper(currentNode.left),self.getHeightHelper(currentNode.right))

    def saveTree(self,jsonfile):
    # save the tree into jsonfile as tuples
        tupleTree=self.convertToTuple(self.root)
        content_to_write=json.dumps(tupleTree)
        file=open(jsonfile,"w")
        file.write(content_to_write)
        file.close()

    def convertToTuple(self,currentNode):
        if currentNode==None:
            return None
        return ((currentNode.key,currentNode.val),self.convertToTuple(currentNode.left),self.convertToTuple(currentNode.right))



# tree=Tree(jsonfile="to_delete.json")
# print(tree.getRange(100,300))
# print(tree.size)
# print(tree.getRange(3,34))
# print(tree.getHeight())
# print(tree.root.left.right.left.left)
# print(tree.root.left.right.left.right.val)
# tree=Tree()
# tree.put(23,23)
# tree.put(13,13)
# tree.put(23,23)
# tree.put(7,7)
# tree.put(17,17)
# tree.put(33,33)
# tree.put(3,3)
# tree.put(9,9)
# tree.put(14,14)
# tree.put(27,27)
# tree.put(39,39)
# tree.put(2,2)
# tree.put(8,8)
# tree.put(12,12)
# tree.put(14,14)
# tree.put(38,38)
# tree.put(40,40)
# tree.put(1,1)
# tree.put(14,14)
# tree.put(38,38)
# tree.put(16,16)
# tree.put(15,15)

# tree.saveTree("to_delete.json")
