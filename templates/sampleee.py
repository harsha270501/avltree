GlowScript 3.1 VPython
#!/usr/bin/python
# -*- coding: utf-8 -*-
# WIth clash handling
# GlowScript 3.0 VPython

from vpython import *



class node:

    def __init__(self):
        self.element = 0
        self.leftchild = undefined
        self.rightchild = undefined
        self.parent = undefined
        self.currobj = undefined  # sphere obj
        self.arrparent = undefined  # arrow obj
        self.textobj = undefined  # label obj
        self.freq = 0  # freq
        self.arrShaftWidth = 0.15
        self.arrHeadWidth = 2 * self.arrShaftWidth
        self.arrHeadLength = 3 * self.arrShaftWidth


class BinarySearchTree:

    def __init__(self):
        self.sz = 0
        self.root = undefined
        self.ht = 0
        self.posnode = {}  # pos-node dictionary
        self.fcn = 0
        self.pointer = undefined
    # function to find the position where the new element has to be inserted
    def findElement(self, e, curnode):
        
        if curnode != undefined:
            if e < curnode.element:
                return self.findElement(e, curnode.leftchild)
            elif e == curnode.element:
                return curnode
            else:
                return self.findElement(e, curnode.rightchild)
        return undefined

    def findInsert(self, e, curnode):
        sleep(1)
        if curnode != undefined:
            self.pointer.pos=curnode.currobj.pos
            if e < curnode.element:
                if curnode.leftchild == undefined:
                    sleep(1)
                    self.pointer.color=color.yellow
                    return curnode
                else:
                    return self.findInsert(e, curnode.leftchild)
            else:

                if curnode.rightchild == undefined:
                    sleep(1)
                    self.pointer.color=color.yellow
                    return curnode
                else:
                    return self.findInsert(e, curnode.rightchild)

    # function to find the position where the given element has to be deleted

    def findDelete(self, e, curnode):
        if curnode != undefined:
            sleep(1)
            self.pointer.pos=self.pointer.pos=curnode.currobj.pos
            # print(curnode.element)

            if e < curnode.element:
                return self.findDelete(e, curnode.leftchild)
            elif e == curnode.element:
                sleep(1)
                self.pointer.color=color.yellow
                return curnode
            else:
                return self.findDelete(e, curnode.rightchild)

    # checks if the height is balanced

    def balanceCheck(self, w):
        if w != undefined:
            h = self.findHeightIter(w.leftchild) \
                - self.findHeightIter(w.rightchild)

         #   print(w.element,h)

            if h < -1 or h > 1:
                return w
            else:
                return self.balanceCheck(w.parent)
        return undefined

    # restructuring after delete - done recursively

    def restructureDel(self, u):

        if u != undefined:
            p1 = u.parent
        if u == undefined:
            p1 = undefined
        self.trinode_restructure(u)
        if p1 != undefined:
            self.restructureDel(p1)

    # restructure to balance tree

    def trinode_restructure(self, u):
        z = self.balanceCheck(u)
        
        if z != undefined:
            print("Imbalance at: ",z.element)
            print(self.posnode)
            q=[z]
            self.del_Pos_Before_Restructure(q)
            #print(self.posnode)
            if z.leftchild == undefined:
                h1 = 0
            else:
                h1 = self.findHeight(z.leftchild)
            if z.rightchild == undefined:
                h2 = 0
            else:
                h2 = self.findHeight(z.rightchild)
            if h1 > h2:
                y = z.leftchild
            else:
                y = z.rightchild

            # print(z.element,z.leftchild.element,z.rightchild.element,z.parent.element)

            h1 = self.findHeight(y.leftchild)
            h2 = self.findHeight(y.rightchild)

            # print(y.element,y.leftchild.element,y.rightchild.element,y.parent.element)

            if h1 > h2:
                x = y.leftchild
            else:
                x = y.rightchild

            # print(x.element,x.leftchild.element,x.rightchild.element,x.parent.element)

            sl = []
            sl.append(x.element)
            sl.append(y.element)
            sl.append(z.element)
            sl.sort()
            if sl[1] == x.element:
                b = x
            elif sl[1] == y.element:
                b = y
            elif sl[1] == z.element:
                b = z
            if b == y:
                p = z.parent
                if y == y.parent.leftchild:
                    t2 = y.rightchild
                    y.rightchild = z
                    z.leftchild = t2
                    if(t2!=undefined):
                        t2.parent=z
                else:
                    t2 = y.leftchild
                    y.leftchild = z
                    z.rightchild = t2
                    if(t2!=undefined):
                        t2.parent=z
                if p != undefined:
                    if z == p.leftchild:
                        p.leftchild = y
                    else:
                        p.rightchild = y
                else:
                    self.root = y
                y.parent = p
                z.parent = y
                q=[y]
                print(z.element,y.element,x.element)
                self.new_Pos_After_Restructure(q)
                print(z.element,y.element,x.element)
            elif b == x:
                p = z.parent
                t1 = x.leftchild
                t2 = x.rightchild
                if y == z.leftchild and x == y.rightchild:
                    z.leftchild = t2
                    if(t2!=undefined):
                        t2.parent=z
                    if(t1!=undefined):
                        t1.parent=y
                    y.rightchild = t1
                    x.leftchild = y
                    x.rightchild = z
                else:
                    z.rightchild = t1
                    if(t1!=undefined):
                        t1.parent=z
                    y.leftchild = t2
                    if(t2!=undefined):
                        t2.parent=y
                    x.leftchild = z
                    x.rightchild = y
                if p != undefined:
                    if z == p.leftchild:
                        p.leftchild = x
                    else:
                        p.rightchild = x
                else:
                    self.root = x
                x.parent = p
                y.parent = x
                z.parent = x
                q=[x]
                print(z.element,y.element,x.element)
                self.new_Pos_After_Restructure(q)
                print(z.element,y.element,x.element)
    
    def del_Pos_Before_Restructure(self,q):
        q1=[]
        if(len(q)>0):
            for i in q:
                if i
                del self.posnode[str(int(i.currobj.pos.x))]
                if(i.currobj!=undefined):
                    i.currobj.visible=False
                    #o=i.currobj
                    #i.currobj=undefined
                    #del o

                if(i.arrparent!=undefined):
                    i.arrparent.visible=False
                    #o=i.arrparent
                    #i.arrparent=undefined
                    #del o

                if(i.textobj!=undefined):
                    i.textobj.visible=False
                    #o=i.textobj
                    #i.textobj=undefined
                    #del o

                w=self.getChildren(i)
                for j in w:
                    q1.append(j)
            self.del_Pos_Before_Restructure(q1)

    def new_Pos_After_Restructure(self,q):
        q1=[]
        if(len(q)>0):
            for u in q:
                v=u.parent
                if v == undefined:
                    vect = vector(0, 0, 0)
                    s = sphere(pos=vect, radius=0.25, color=color.green)
                    ln = label(pos=vect, text=str(u.element), color=color.white,opacity=0, height=18, box=False)
                    u.currobj = s
                    u.textobj = ln
                else:
                    if u == v.rightchild:
                        vx = int(v.currobj.pos.x) + 1
                        vy = int(v.currobj.pos.y) - 1
                        vect = vector(vx, vy, 0)
                        s = sphere(pos=vect, radius=0.25, color=color.green)
                        ln = label(pos=vect, text=str(u.element), color=color.white, height=18,
                                opacity=0, box=False)
                        a = arrow(
                            pos=v.currobj.pos,
                            axis=vect - v.currobj.pos,
                            shaftwidth=u.arrShaftWidth,
                            headwidth=u.arrHeadWidth,
                            headlength=u.arrHeadLength,
                            color=color.red,
                            )
                        u.currobj = s
                        u.arrparent = a
                        u.textobj = ln
                    else:
                        vx = int(v.currobj.pos.x) - 1
                        vy = int(v.currobj.pos.y) - 1
                        vect = vector(vx, vy, 0)
                        s = sphere(pos=vect, radius=0.25, color=color.green)
                        ln = label(pos=vect, text=str(u.element), color=color.white, height=18,
                                opacity=0, box=False)
                        a = arrow(
                            pos=v.currobj.pos,
                            axis=vect - v.currobj.pos,
                            shaftwidth=u.arrShaftWidth,
                            headwidth=u.arrHeadWidth,
                            headlength=u.arrHeadLength,
                            color=color.red,
                            )
                        u.currobj = s
                        u.arrparent = a
                        u.textobj = ln
                
                dummylist=[]
                for i in self.posnode:
                    if i!=undefined:
                        dummylist.append(int(i))
                    
                if int(u.currobj.pos.x) in dummylist:
                    #print("clash")
                    self.clashHandle(u)
                    self.posnode[str(int(u.currobj.pos.x))] = u
                else:
                    self.posnode[str(int(u.currobj.pos.x))] = u
                
                scene.visible = True
                w=self.getChildren(u)
                for i in w:
                    q1.append(i)
            self.new_Pos_After_Restructure(q1)

    # Basic BST insertion

    def insertElement(self, e):
        v = self.root
        u = node()
        u.element = e

        if self.root == undefined:
            self.root = u
        else:
            v = self.findInsert(e, self.root)

            print(v.element)

            if e < v.element:
                v.leftchild = u
            else:

                v.rightchild = u
        u.parent = v
        return u

    # ADT - insertion in AVL
    def insertElementAVL(self, e):
        
        u = self.insertElement(e)
        v = u.parent
        if v == undefined:
            vect = vector(0, 0, 0)
            s = sphere(pos=vect, radius=0.25, color=color.green)
            ln = label(pos=vect, text=str(e), color=color.white, height=18,
                       opacity=0, box=False)
            u.currobj = s
            u.textobj = ln
        else:
            if u == v.rightchild:
                vx = int(v.currobj.pos.x) + 1
                vy = int(v.currobj.pos.y) - 1
                vect = vector(vx, vy, 0)
                s = sphere(pos=vect, radius=0.25, color=color.green)
                ln = label(pos=vect, text=str(e), color=color.white, height=18, 
                           opacity=0, box=False)
                a = arrow(
                    pos=v.currobj.pos,
                    axis=vect - v.currobj.pos,
                    shaftwidth=u.arrShaftWidth,
                    headwidth=u.arrHeadWidth,
                    headlength=u.arrHeadLength,
                    color=color.red,
                    )
                u.currobj = s
                u.arrparent = a
                u.textobj = ln
            else:
                vx = int(v.currobj.pos.x) - 1
                vy = int(v.currobj.pos.y) - 1
                vect = vector(vx, vy, 0)
                s = sphere(pos=vect, radius=0.25, color=color.green)
                ln = label(pos=vect, text=str(e), color=color.white, height=18,
                           opacity=0, box=False)
                a = arrow(
                    pos=v.currobj.pos,
                    axis=vect - v.currobj.pos,
                    shaftwidth=u.arrShaftWidth,
                    headwidth=u.arrHeadWidth,
                    headlength=u.arrHeadLength,
                    color=color.red,
                    )
                u.currobj = s
                u.arrparent = a
                u.textobj = ln
        self.pointer.pos=u.currobj.pos
        dummylist=[]
        for i in self.posnode:
            if i!=undefined:
                dummylist.append(int(i))
        print(int(u.currobj.pos.x),dummylist)
        print(int(u.currobj.pos.x) in dummylist)            
        if int(u.currobj.pos.x) in dummylist:
            
            self.clashHandle(u)
            self.posnode[str(int(u.currobj.pos.x))] = u

        else:
            self.posnode[str(int(u.currobj.pos.x))] = u
        self.pointer.pos=u.currobj.pos
        sleep(1)
        self.pointer.color=color.cyan
        scene.visible = True
        
        self.trinode_restructure(u)
        dummylist=[]
        for i in self.posnode:
            if i!=undefined:
                dummylist.append(int(i))
        for i in dummylist:
                print(i," ",self.posnode[str(i)].element)
        self.pointer.pos=u.currobj.pos
        return

    # BST insertion - visualisation
    def insertVisual(self, e):
        #rate(1)
        u = self.insertElementAVL(e)
        
    # function to handle clashes
    def searchvis(self,k,n):
        sleep(1)
        self.pointer.pos=n.currobj.pos
        #print(n.element)
        #print(n.element==k)
        if n.element==k:
            sleep(1)
            self.pointer.color=color.yellow
            #print("is it getting reflected?")
            return 
        else:
            if k>n.element and n.rightchild!=undefined:
                self.searchvis(k,n.rightchild)
            if k<n.element and n.leftchild!=undefined:
                self.searchvis(k,n.leftchild)
    def preordervis(self,n):
        sleep(1)
        self.pointer.pos=n.currobj.pos

        if n.leftchild!=undefined:
            self.preordervis(n.leftchild)

        if n.rightchild!=undefined:
            self.preordervis(n.rightchild)
        return 
    
    def postordervis(self,n):
        if n.leftchild!=undefined:
            self.postordervis(n.leftchild)

        if n.rightchild!=undefined:
            self.postordervis(n.rightchild)
        
        sleep(1)
        self.pointer.pos=n.currobj.pos
        return
    
    def inordervis(self,n):
        if n.leftchild!=undefined:
            self.inordervis(n.leftchild)
        sleep(1)
        self.pointer.pos=n.currobj.pos

        if n.rightchild!=undefined:
            self.inordervis(n.rightchild)
        return
        
    
    def levelordervis(self,n):
        q=[]
        q.append(n)
        while(len(q)!=0):
            x=q.pop(0)
            sleep(1)
            print(x.element)
            self.pointer.pos=x.currobj.pos
            if x.leftchild!=undefined:
                q.append(x.leftchild)
            if x.rightchild!=undefined:
                q.append(x.rightchild)
        return
        
            
                
    def clashHandle(self, node):
        flag = 0
        if(self.pointer.pos == node.currobj.pos):
            flag = 1
        nodepos = []
        changed_posnode = {}
        for i in self.posnode:
            nodepos.append(int(i))
        
        print("Clash",nodepos)
        cx = 0
        if(node.element<self.root.element):
            cx = -1
        else:
            cx = 1

        for i in nodepos:
            if((cx == -1 and i <= node.currobj.pos.x) or (cx == 1 and i >= node.currobj.pos.x)):
                if((self.posnode[str(i)] != self.root) and ((i!=node.currobj.pos.x) or ((cx == -1 and node.parent.rightchild != node) or (cx == 1 and node.parent.leftchild != node)))):
                    temp = self.posnode[str(i)]
                    del self.posnode[str(i)]

                    temp.currobj.pos.x += cx
                    temp.arrparent.pos = temp.parent.currobj.pos
                    temp.arrparent.axis = temp.currobj.pos - \
                        temp.parent.currobj.pos
                    temp.textobj.pos = temp.currobj.pos
                    if(temp.leftchild != undefined):
                        temp.leftchild.arrparent.pos = temp.currobj.pos
                        temp.leftchild.arrparent.axis = temp.leftchild.currobj.pos - \
                            temp.currobj.pos

                    if(temp.rightchild != undefined):
                        temp.rightchild.arrparent.pos = temp.currobj.pos
                        temp.rightchild.arrparent.axis = temp.rightchild.currobj.pos - \
                            temp.currobj.pos

                    changed_posnode[str(i+cx)] = temp

        if((cx == -1 and node.parent.rightchild==node) or (cx == 1 and node.parent.leftchild==node)):
            node.currobj.pos.x += cx
            node.arrparent.pos = node.parent.currobj.pos
            node.arrparent.axis = node.currobj.pos - node.parent.currobj.pos
            node.textobj.pos = node.currobj.pos
        
        for j in changed_posnode:
            self.posnode[j] = changed_posnode[j]

        if(flag == 1):
            self.pointer.pos = node.currobj.pos



    def inorderTraverse(self, v):
        if v != undefined:
            if v.leftchild != undefined:
                self.inorderTraverse(v.leftchild)

            print(v.element,end=" ")

            if v.rightchild != undefined:
                self.inorderTraverse(v.rightchild)

    # inorder successor

    def returnNextInorder(self, v):
        if v.leftchild == undefined:
            return v
        else:
            return self.returnNextInorder(v.leftchild)
        return

    # BST - delete element

    def removeElement(self, e):
        t = self.findDelete(e, self.root)
        
        print("Deleting ele",e)
        self.pointer.pos = vector(0,0,0)
        self.pointer.color=color.red
        l = t.leftchild
        r = t.rightchild
        p = t.parent
        child = 0
        if l != undefined:
            child += 1
        if r != undefined:
            child += 1
        if self.isExternal(t):
            if p == undefined:
                self.root = undefined
                
            else:
                if t == p.leftchild:
                    p.leftchild = undefined
                else:
                    p.rightchild = undefined
            x=int(t.currobj.pos.x)
            del self.posnode[x]
            t.currobj.visible=False
            t.arrparent.visible=False
            t.textobj.visible=False
            del t
        elif child == 1:
            if(l!=undefined):
                tempele=l.element
            else:
                tempele=r.element
            print("Case 1 children")
            print("tempele",tempele)

            self.removeElement(tempele)
            
            t.element = tempele
            t.textobj.text=str(tempele)
        else:
            temp = self.returnNextInorder(t.rightchild)
            tempele = temp.element
            print("Case 2 children")
            print("tempele",tempele)

            self.removeElement(tempele)
            
            t.element = tempele
            t.textobj.text=str(tempele)
        return


    # AVL- delete element

    def removeElementAVL(self, e):
        t = self.findDelete(e, self.root)
        self.removeElement(e)

        # print("Immediate after delete")
        # self.inorderTraverse(self.root)
        # print()

        w = t

        self.restructureDel(w)

        return

    # AVL - adt create

    def adtCreate(self, items):
        l = len(items)
        if l == 0:
            return

        mid = l // 2

        lr = items[:mid]
        rr = items[mid + 1:]
        u = node()
        u.element = items[mid]

        # print(mid,u.element)

        if l > 1:
            lchild = self.adtCreate(lr)
            rchild = self.adtCreate(rr)
            u.leftchild = lchild
            u.rightchild = rchild
            if lchild != undefined:
                lchild.parent = u
            if rchild != undefined:
                rchild.parent = u
        else:
            u.leftchild = undefined
            u.rightchild = undefined
        self.root = u
        return u

    # AVL - visualise create tree

    def createTree(self, items):
        l = len(items)
        #print("length of items= ",l)
        if l == 0:
            return

        mid = l // 2

        lr = items[:mid]
        rr = items[mid + 1:]
        u = items[mid]

        # print("element:",u.element,end="-")

        if l > 1:
            #print("call is happening")
            lchild = self.createTree(lr)
            rchild = self.createTree(rr)
            u.leftchild = lchild
            u.rightchild = rchild
            if lchild != undefined or rchild != undefined:
                y = u.currobj.pos.y
                if lchild != undefined:

                    # print("left:",lchild.element,end=",")

                    lchild.parent = u
                    if lchild.currobj.pos.y > y:
                        y = lchild.currobj.pos.y

                if rchild != undefined:

                    # print("right:",rchild.element)

#                     print ()
                    rchild.parent = u
                    if rchild.currobj.pos.y > y:
                        y = rchild.currobj.pos.y
                j = 0
                u.currobj.pos.y = y
                u.textobj.pos.y = y
                while(j<2):
                    sleep(1)
                    u.currobj.pos.y += 1
                    u.textobj.pos.y += 1
                    j+=1
                    
                if lchild != undefined:
                    lchild.currobj.pos.y = y
                    lchild.textobj.pos.y = y
                    lchild.arrparent = arrow(pos=u.currobj.pos,
                            axis=lchild.currobj.pos - u.currobj.pos, shaftwidth=u.arrShaftWidth,
                    headwidth=u.arrHeadWidth,
                    headlength=u.arrHeadLength,
                            color=color.red)
                if rchild != undefined:
                    rchild.currobj.pos.y = y
                    rchild.textobj.pos.y = y
                    rchild.arrparent = arrow(pos=u.currobj.pos,
                            axis=rchild.currobj.pos - u.currobj.pos, shaftwidth=u.arrShaftWidth,
                    headwidth=u.arrHeadWidth,
                    headlength=u.arrHeadLength,
                            color=color.red)
        else:

            u.leftchild = undefined
            u.rightchild = undefined
        #print ('Changed position',u.element,' ',u.currobj.pos.x,' ',u.currobj.pos.y)
        self.root = u
        return u

    def isExternal(self, curnode):
        if curnode.leftchild == undefined and curnode.rightchild == undefined:
            return True
        else:
            return False

    def getChildren(self, curnode):
        children = []
        print(curnode.element)
        if curnode.leftchild != undefined:
            children.append(curnode.leftchild)

        if curnode.rightchild != undefined:
            children.append(curnode.rightchild)
        return children

    def preorderTraverse(self, v):
        curnode = v

        print(curnode.element,end=" ")

        if curnode.leftchild != undefined:
            self.preorderTraverse(curnode.leftchild)
        if curnode.rightchild != undefined:
            self.preorderTraverse(curnode.rightchild)
        return

    def postorderTraverse(self, v):
        curnode = v
        if curnode.leftchild != undefined:
            self.postorderTraverse(curnode.leftchild)
        if curnode.rightchild != undefined:
            self.postorderTraverse(curnode.rightchild)

        print(curnode.element,end=" ")

        return

    def findDepthIter(self, v):
        if v == self.root:
            return 0
        else:
            return 1 + self.findDepthIter(v.parent)

    def findDepth(self, v):
        return self.findDepthIter(self.findElement(v.element,
                                  self.root))

    def findHeightIter(self, v):
        if v == undefined:
            return 0
        if v != undefined:
            if self.isExternal(v):
                return 1
            else:
                h = 0
                if v.leftchild != undefined:
                    h = max(h, self.findHeightIter(v.leftchild))
                if v.rightchild != undefined:
                    h = max(h, self.findHeightIter(v.rightchild))
                return 1 + h

    def findHeight(self, v):
        if v == undefined:
            return 0

        u = self.findElement(v.element, self.root)
        if u == undefined:
            return 0
        if u != undefined:
            return self.findHeightIter(u)

    def printTree(self, v):
        return

    def preOrderHideTraverse(self, curnode):
        curnode.textobj.visible = False
        curnode.currobj.visible=False
        if curnode.arrparent!=undefined:
            curnode.arrparent.visible=False
        if curnode.leftchild != undefined:
            self.preOrderHideTraverse(curnode.leftchild)
        if curnode.rightchild != undefined:
            self.preOrderHideTraverse(curnode.rightchild)
        return

def testmain():
    ch = 'y'
    
    """bstadt = BinarySearchTree()
    bstadt.pointer.visible = False
    scene.visible = False
    print('ADT Demo: ')
    while ch == 'y':
        print('1.Creation 2.Insertion 3.Deletion')
        op = int(input())
        if op == 1:
            l = list(map(int, input().strip().split()))
            l.sort()
            bstadt.adtCreate(l)
            print("Inorder traversal: ",end=" ")

            bstadt.inorderTraverse(bstadt.root)
            print ()

            print("Preorder traversal: ",end=" ")

            bstadt.preorderTraverse(bstadt.root)
            print ()
        elif op == 2:
            i = int(input('Enter element to be inserted: '))
            bstadt.insertElementAVL(i)

            print("Inorder traversal: ",end=" ")

            bstadt.inorderTraverse(bstadt.root)
            print ()

            print("Preorder traversal: ",end=" ")

            bstadt.preorderTraverse(bstadt.root)
            print ()
        elif op == 3:
            i = int(input('Enter element to be deleted: '))
            bstadt.deleteElementAVL(i)

            print("Inorder traversal: ",end=" ")

            bstadt.inorderTraverse(bstadt.root)
            print ()

            print("Preorder traversal: ",end=" ")

            bstadt.preorderTraverse(bstadt.root)
            print ()
        else:
            print('Invalid option')
        ch = input('Do you want to continue?(y/n): ')
"""
    print('Visualisation - Create AVL tree')
#       scene.visible = False
#     scene = canvas()
    bst1 = BinarySearchTree()
#     bst1.pointer.visible = False
#     bst1.pointer = ring(pos=vector(0,0,0),axis=vector(0,0,1),radius=0.26,color=color.purple,thickness=0.1)
    l = list(map(int, input().split(' ')))
    x = len(l)
    x *= -1
    l.sort()
    objlist = []
    y = x
    for i in l:
        sleep(1)
        n = node()
        n.element = i
        s = sphere(pos=vector(x, y, 0), radius=0.25, color=color.green)
        ln = label(pos=vector(x, y, 0), text=str(i), color=color.white, 
                   opacity=0, box=False)
        n.currobj = s
        n.textobj = ln
        x += 2

        #print(x)
        objlist.append(n)
        #print("length of objlist: ",len(objlist))
        
    bst1.createTree(objlist)
    scene.waitfor('click')
    bst1.preOrderHideTraverse(bst1.root)

    bst2 = BinarySearchTree()
    bst2.pointer = ring(pos=vector(0,0,0),axis=vector(0,0,1),radius=0.26,color=color.purple,thickness=0.1)
    ch = input('Do you want to continue?(y/n): ')
#     scene = canvas()
    
    
#    
    
    
    while ch == 'y':
        rate(1)
        op=int(input("Enter option : 1.Insertion 2. Searching 3.Deletion 4.Preorder 5.Postorder 6.Inorder 7.LevelOrder"))
        if(op==1):
            print('Visualisation - BST tree insertion')
            bst2.pointer.pos = vector(0,0,0)
            bst2.pointer.color=color.red
            i = int(input('Enter element to be inserted: '))
            bst2.insertVisual(i)
        elif(op==2):
            print('Visualisation - BST tree Searching')
            if(bst2.root==undefined):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.red
                i = int(input('Enter element to be searched: '))
                
                if(bst2.pointer.color==color.red):
                    print("Element",i,"does not exist in tree")
                else:
                    print("Element found")
        elif(op==3):
            print('Visualisation - BST tree Deletion')
            i = int(input('Enter element to be deleted: '))
            if(bst2.root==undefined):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.red
                bst2.searchvis(i,bst2.root)
                bst2.removeElementAVL(i)
                if(bst2.pointer.color==color.red):
                    print("Element",i,"does not exist in tree")
                else:
                    print("Element deleted")
            
        elif(op==4):
            print('Visualisation - Preorder')
            if(bst2.root==undefined):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.yellow
                bst2.preordervis(bst2.root)
        elif(op==5):
            print('Visualisation - Postorder')
            if(bst2.root==undefined):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.yellow
                bst2.postordervis(bst2.root)
        elif(op==6):
            print('Visualisation - Inorder')
            if(bst2.root==undefined):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.yellow
                bst2.inordervis(bst2.root)
        elif(op==7):
            print('Visualisation - Levelorder')
            if(bst2.root==undefined):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.yellow
                bst2.levelordervis(bst2.root)
        else:
            print("Invalid option")

#       scene.waitfor('click')
        ch = input('Do you want to continue?(y/n): ')


def main():
    testmain()


if __name__ == '__main__':
    main()
