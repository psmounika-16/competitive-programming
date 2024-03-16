# leetcode platform codes
# 1. //150
class Solution:
    def evalRPN(self,tokens: List[str])->int:
        stack=[]
        res=0
        for element in tokens:
            match(element):
                case '+':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    res=op1+op2
                    stack.append(str(res))
                case '-':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                res=op1-op2
                stack.append(str(res))
            case '*':
                op2=int(stack.pop())
                op1=int(stack.pop())
                res=op1*op2
                stack.append(str(res))
            case '/':
                op2=int(stack.pop())
                op1=int(stack.pop())
                res=int(op1/op2)
                stack.append(str(res))
            case_:
                stack.append(element)
        return int(stack.pop())


# program 2  // 155  //min no find // sourcetree   scm source control management  git //git,github account,sourcetree
import sys
class MinStack:
    def __init__(self):
        self.stack = []
        self.min=sys.maxsize
    def push(self,x: int) -> None:
        self.min=min(self.min,x)
        self.stack.append([x,self.min])
    def pop(self) ->None:
        self.stack.pop()
        if (self.stack):
            self.min=self.stack[-1][1]
        else:
            self.min=sys.maxsize
    def top(self) ->int:
        return self.stack[-1][0]
    def getMin(self) ->int:
        return self.stack[-1][1]
    
#// corrected code below
#-------------------------
    class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float('inf')

    def push(self, val: int) -> None:
        if val < self.min_value:
            self.min_value = val
        self.stack.append((val, self.min_value))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            if self.stack:
                self.min_value = self.stack[-1][1]
            else:
                self.min_value = float('inf')

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_value

        
 # 3. // 232 //implement queue using stack
 class MyQueue:
    def __init__(self):
        self.push_stack=[]
        self.pop_stack=[]
    def push(self,x: int) -> None:
        self.push_stack.append(x)
    def pop(self) ->int:
        if self.empty(): return
        if len(self.pop_stack):
            return self.pop_stack.pop()
        else:
            while len(self.push_stack)>0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()
    def peek(self) ->int:
        if self.empty():return
        if len(self.pop_stack):
            return self.pop_stack[-1]
        else:
            while len(self.push_stack)>0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1
    def empty(self) ->bool:
        return len(self.push_stack)==0 and len(self.pop_stack)==0
        
# 4.//331 //verify preorder serilization of a binary tree


class Solution:
    def isValidSerialization(self,preorder: str) ->bool:
        lst=[node for node  in preorder.split(',')]
        stack=[]
        if (len(lst)<3):
            if (len(lst)==1 and lst[0]=='#'):
                return True
            else:
                return False
        else:
            j=0
            for node in lst:
                if (node != '#'):
                    stack.append(node)
                else:
                    if (len(lst)==0):
                        if (len(lst)==j+1):
                            return True
                        else:
                            return False
                    else:
                        stack.pop()
                j+=1


##corrected code
##-----------------
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slots = 1

        for node in nodes:
            slots -= 1  # Consume one slot for the current node
            if slots < 0:  # Check if there's not enough slots
                return False

            if node != '#':  # If current node is not null, add two slots
                slots += 2

        return slots == 0  # Check if all slots are used up
#--------------------------------------


#5.//654
#-----------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return
        else:
            ma=max(nums)
            index=nums.index(ma)
            root=TreeNode(ma)
            root.left=self.constructMaximumBinaryTree(nums[0:index])
            root.right=self.constructMaximumBinaryTree(nums[index+1:])
        return root
#=====================================
#6. // 739
#---------------------------
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i,temperature in enumerate(temperatures):
            while stack and temperature >temperatures[stack[-1]]:
                index=stack.pop()
                ans[index]=i-index
            stack.append(i)
        return ans
#======================================
#7. //1441     **
#----------------------
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        i=1
        index=0
        while n>0 and index >len(target):
            if target[index]==i:
                res.append("Push")
                index+=1
            else:
                res.append("Push")
                res.append("Pop")
            n-=1
            i+=1
        return res
#==================================
#8. ///1996
#------------------
class Solution
    def
        count=0
        properties=sorted(properties,key=lamda x: (-x[0],x[1]))
        maxDefence=properties[0][1]
        for i in properties:
            if i[1]<maxDefence :
                count+=1
            maxDefence=max(i[1],maxDefence)
        return count
#===============================================
# 
