#!/usr/bin/python
# -*- coding: utf-8 -*-
# WIth clash handling
# GlowScript 3.0 VPython

from vpython import *
import copy


class node:

    def __init__(self):
        self.element = 0
        self.leftchild = None
        self.rightchild = None
        self.parent = None
        self.currobj = None  # sphere obj
        self.arrparent = None  # arrow obj
        self.textobj = None  # label obj
        self.freq = 0  # freq
        self.arrShaftWidth = 0.15
        self.arrHeadWidth = 2 * self.arrShaftWidth
        self.arrHeadLength = 3 * self.arrShaftWidth


class BinarySearchTree:

    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0
        self.posnode = {}  # pos-node dictionary
        self.fcn = 0
        self.pointer = None
    # function to find the position where the new element has to be inserted
    def findElement(self, e, curnode):
        
        if curnode != None:
            if e < curnode.element:
                return self.findElement(e, curnode.leftchild)
            elif e == curnode.element:
                return curnode
            else:
                return self.findElement(e, curnode.rightchild)
        return None

    def findInsert(self, e, curnode):
        sleep(1)
        if curnode != None:
            self.pointer.pos=curnode.currobj.pos
            if e < curnode.element:
                if curnode.leftchild == None:
                    sleep(1)
                    self.pointer.color=color.yellow
                    return curnode
                else:
                    return self.findInsert(e, curnode.leftchild)
            else:

                if curnode.rightchild == None:
                    sleep(1)
                    self.pointer.color=color.yellow
                    return curnode
                else:
                    return self.findInsert(e, curnode.rightchild)

    # function to find the position where the given element has to be deleted

    def findDelete(self, e, curnode):
        sleep(1)
        if curnode != None:

            # print(curnode.element)
            self.pointer.pos=curnode.currobj.pos
            if e < curnode.element:
                return self.findDelete(e, curnode.leftchild)

            elif e==curnode.element:
                sleep(1)
                self.pointer.color=color.yellow
                return curnode
            else:
               return self.findDelete(e, curnode.rightchild)
        return None
        
        
    # checks if the height is balanced

    def balanceCheck(self, w):
        if w != None:
            h = self.findHeightIter(w.leftchild) \
                - self.findHeightIter(w.rightchild)

         #   print(w.element,h)

            if h < -1 or h > 1:
                return w
            else:
                return self.balanceCheck(w.parent)
        return None

    # restructuring after delete - done recursively

    def restructureDel(self, u):

        if u != None:
            p1 = u.parent
        if u == None:
            p1 = None
        self.trinode_restructure(u)
        if p1 != None:
            self.restructureDel(p1)

    # restructure to balance tree

    def trinode_restructure(self, u):
        z = self.balanceCheck(u)
        
        if z != None:
            print("Imbalance at: ",z.element)
            print(self.posnode)
            q=[z]
            self.del_Pos_Before_Restructure(q)
            #print(self.posnode)
            if z.leftchild == None:
                h1 = 0
            else:
                h1 = self.findHeight(z.leftchild)
            if z.rightchild == None:
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
                    if(t2!=None):
                        t2.parent=z
                else:
                    t2 = y.leftchild
                    y.leftchild = z
                    z.rightchild = t2
                    if(t2!=None):
                        t2.parent=z
                if p != None:
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
                    if(t2!=None):
                        t2.parent=z
                    if(t1!=None):
                        t1.parent=y
                    y.rightchild = t1
                    x.leftchild = y
                    x.rightchild = z
                else:
                    z.rightchild = t1
                    if(t1!=None):
                        t1.parent=z
                    y.leftchild = t2
                    if(t2!=None):
                        t2.parent=y
                    x.leftchild = z
                    x.rightchild = y
                if p != None:
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
                del self.posnode[int(i.currobj.pos.x)]
                if(i.currobj!=None):
                    i.currobj.visible=False
                    #o=i.currobj
                    #i.currobj=None
                    #del o

                if(i.arrparent!=None):
                    i.arrparent.visible=False
                    #o=i.arrparent
                    #i.arrparent=None
                    #del o

                if(i.textobj!=None):
                    i.textobj.visible=False
                    #o=i.textobj
                    #i.textobj=None
                    #del o

                w=self.getChildren(i)
                for i in w:
                    q1.append(i)
            self.del_Pos_Before_Restructure(q1)

    def new_Pos_After_Restructure(self,q):
        q1=[]
        if(len(q)>0):
            for u in q:
                v=u.parent
                if v == None:
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
                
                if int(u.currobj.pos.x) in self.posnode.keys():
                    #print("clash")
                    self.clashHandle(self.posnode[int(u.currobj.pos.x)],u.element)
                    self.posnode[int(u.currobj.pos.x)] = u
                else:
                    self.posnode[int(u.currobj.pos.x)] = u
                
                scene.visible = True
                w=self.getChildren(u)
                for i in w:
                    q1.append(i)
            self.new_Pos_After_Restructure(q1)
    


                
    def reposition(self, x, nposnode):
        clashlist = {}

        if x.leftchild != None:
            left = x.leftchild
            v = x.currobj.pos + vector(-1, 0, 0)

            if nposnode[v.x] == None:
                left.currobj.pos = v
                left.arrow = arrow(pos=x.currobj.vector,
                                   axis=left.currobj.pos,
                                   color=color.red)
                left.textobj.pos = v
                nposnode[v.x] = left
                self.posnode[v.x] = left
            else:

                self.clashcheck(nposnode[v.x], x.leftchild.element,
                                nposnode)

        if x.rightchid != None:
            right = x.rightchild
            v = x.currobj.pos + vector(1, 0, 0)

            if nposnode[v.x] == None:
                right.currobj.pos = v
                right.arrow = arrow(pos=x.currobj.vector,
                                    axis=left.currobj.pos,
                                    color=color.red)
                right.textobj.pos = v
                nposnode[v.x] = right
                self.posnode[v.x] = right
            else:

                self.clashcheck(nposnode[v.x], x.leftchild.element,
                                nposnode)

    # Basic BST insertion

    def insertElement(self, e):
        v = self.root
        u = node()
        u.element = e

        if self.root == None:
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
        if v == None:
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
        #self.pointer.pos=u.currobj.pos
        if int(u.currobj.pos.x) in self.posnode.keys():
            self.clashHandle(self.posnode[int(u.currobj.pos.x)],u.element)
            self.posnode[int(u.currobj.pos.x)] = u

        else:
            self.posnode[int(u.currobj.pos.x)] = u
        self.pointer.pos=u.currobj.pos
        sleep(1)
        self.pointer.color=color.cyan
        scene.visible = True
        
        self.trinode_restructure(u)
        for (i,v) in self.posnode.items():
                print(i," ",v.element)
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
            if k>n.element and n.rightchild!=None:
                self.searchvis(k,n.rightchild)
            if k<n.element and n.leftchild!=None:
                self.searchvis(k,n.leftchild)
    def preordervis(self,n):
        sleep(1)
        self.pointer.pos=n.currobj.pos

        if n.leftchild!=None:
            self.preordervis(n.leftchild)

        if n.rightchild!=None:
            self.preordervis(n.rightchild)
        return 
    
    def postordervis(self,n):
        if n.leftchild!=None:
            self.postordervis(n.leftchild)

        if n.rightchild!=None:
            self.postordervis(n.rightchild)
        
        sleep(1)
        self.pointer.pos=n.currobj.pos
        return
    
    def inordervis(self,n):
        if n.leftchild!=None:
            self.inordervis(n.leftchild)
        sleep(1)
        self.pointer.pos=n.currobj.pos

        if n.rightchild!=None:
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
            if x.leftchild!=None:
                q.append(x.leftchild)
            if x.rightchild!=None:
                q.append(x.rightchild)
        return
        
            
                
    def clashHandle(self, fn, cnele):
        q = []
        if cnele > fn.element:  # extend right subtree
            q.append(fn.rightchild)
            self.clashLevelOrderTraverse(q, 1)
        else:

                                            # extend left subtree

            q.append(fn.leftchild)
            self.clashLevelOrderTraverse(q, -1)

    # level order traversal to shift the tree accordingly

    def clashLevelOrderTraverse(self, q, cx):
        self.fcn += 1
        print ('queue:', q)
        if len(q) == 0:
            return
        else:
            qc = []
            for i in range(len(q)):
#                 rate(1)
                currnode = q[i]

                if currnode != None:

                    if int(currnode.currobj.pos.x) not in self.posnode.keys():
                        return -1

                    print (
                        'B:',
                        currnode.element,
                        ' ',
                        currnode.currobj.pos.x,
                        ' ',
                        currnode.currobj.pos.y,
                        ' ',
                        currnode.currobj.pos.z,
                        )

                    #                     del self.posnode[int(currnode.currobj.pos.x)]

#                     print ('Dict: ', self.posnode.items())
                    
                    beforepos =  currnode.currobj.pos
                    
                    currnode.currobj.pos.x =int(currnode.currobj.pos.x)+int(cx)

                    currnode.arrparent.pos = currnode.parent.currobj.pos
                    currnode.arrparent.axis = currnode.currobj.pos - currnode.parent.currobj.pos

                    currnode.textobj.pos = currnode.currobj.pos
                    
#                     print("Bp:",beforepos.x,"PP:",self.pointer.pos.x)
#                     print(self.pointer.pos.x == beforepos.x)
                    
                    if int(self.pointer.pos.x) == int(beforepos.x):
                        self.pointer.pos=currnode.parent.currobj.pos
                    
                    changedx = int(currnode.currobj.pos.x)
                    if changedx in self.posnode.keys():
                        if self.posnode[changedx].currobj.pos.y > currnode.currobj.pos.y:
                            self.clashHandle(self.posnode[changedx],
                                    currnode.element)
                            return -1

                    self.posnode[changedx] = currnode
                    f=0
                    l=[]
                    for (k, v) in self.posnode.items():
                        if v == currnode and k != changedx:
                            f=1
                            break
                   
                            
                    if(f==1):
                        if k != changedx:
                            del self.posnode[k]
                            
#                     print (
#                         'A:',
#                         currnode.element,
#                         ' ',
#                         currnode.currobj.pos.x,
#                         ' ',
#                         currnode.currobj.pos.y,
#                         ' ',
#                         currnode.currobj.pos.z,
#                         )
#                     print ('Dict: ', self.posnode.items())
                    for w in self.getChildren(q[i]):
                        qc.append(w)
            q = qc
            self.clashLevelOrderTraverse(q, int(cx))

#    def clashInorderTraverse(self, currnode, cx):
#        if cx == -1:                        #LPR Left subtree extension
#            if currnode != None:
#                if currnode.leftchild != None:
#                    self.clashInorderTraverse(currnode.leftchild, cx)
#
#                del self.posnode[currnode.currobj.pos.x]
#                currnode.currobj.pos += vector(cx, 0, 0)
#                currnode.arrparent.pos = currnode.currobj.pos
#                currnode.arrparent.axis = currnode.currobj.pos - currnode.parent.currobj.pos
#                currnode.textobj.pos = currnode.currobj.pos
#                self.posnode[currnode.currobj.pos.x] = currnode
#
#                if currnode.rightchild != None:
#                    self.clashInorderTraverse(currnode.rightchild, cx)
#
#        else:                                #RPL Right subtree extension
#            if currnode != None:
#                if currnode.rightchild != None:
#                    self.clashInorderTraverse(currnode.rightchild, cx)
#
#                del self.posnode[currnode.currobj.pos.x]
#                currnode.currobj.pos += vector(cx, 0, 0)
#                currnode.arrparent.pos = currnode.currobj.pos
#                currnode.arrparent.axis = currnode.currobj.pos - currnode.parent.currobj.pos
#                currnode.textobj.pos = currnode.currobj.pos
#                self.posnode[currnode.currobj.pos.x] = currnode
#
#                if currnode.leftchild != None:
#                    self.clashInorderTraverse(currnode.leftchild, cx)
#

    def inorderTraverse(self, v):
        if v != None:
            if v.leftchild != None:
                self.inorderTraverse(v.leftchild)

            print(v.element,end=" ")

            if v.rightchild != None:
                self.inorderTraverse(v.rightchild)

    # inorder successor

    def returnNextInorder(self, v):
        if v.leftchild == None:
            return v
        else:
            return self.returnNextInorder(v.leftchild)
        return

    # BST - delete element

    def deleteElement(self, e):
        t = self.findDelete(e, self.root)
        #sleep(1)
        print("Deleting ele",e)
        self.pointer.pos = vector(0,0,0)
        self.pointer.color=color.red
        l = t.leftchild
        r = t.rightchild
        p = t.parent
        child = 0
        if l != None:
            child += 1
        if r != None:
            child += 1
        if self.isExternal(t):
            if p == None:
                self.root = None
                
            else:
                if t == p.leftchild:
                    p.leftchild = None
                else:
                    p.rightchild = None
            x=int(t.currobj.pos.x)
            del self.posnode[x]
            t.currobj.visible=False
            t.arrparent.visible=False
            t.textobj.visible=False
            del t
        elif child == 1:
            if(l!=None):
                tempele=l.element
            else:
                tempele=r.element
            print("Case 1 children")
            print("tempele",tempele)

            self.deleteElement(tempele)
            
            t.element = tempele
            t.textobj.text=str(tempele)
        else:
            temp = self.returnNextInorder(t.rightchild)
            tempele = temp.element
            print("Case 2 children")
            print("tempele",tempele)

            self.deleteElement(tempele)
            
            t.element = tempele
            t.textobj.text=str(tempele)
        return


    # AVL- delete element

    def deleteElementAVL(self, e):
        t = self.findDelete(e, self.root)
        self.deleteElement(e)

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
            if lchild != None:
                lchild.parent = u
            if rchild != None:
                rchild.parent = u
        else:
            u.leftchild = None
            u.rightchild = None
        self.root = u
        return u

    # AVL - visualise create tree

    def createTree(self, items):
        l = len(items)
        if l == 0:
            return

        mid = l // 2

        lr = items[:mid]
        rr = items[mid + 1:]
        u = items[mid]

        # print("element:",u.element,end="-")

        if l > 1:
            lchild = self.createTree(lr)
            rchild = self.createTree(rr)
            u.leftchild = lchild
            u.rightchild = rchild
            if lchild != None or rchild != None:
                y = u.currobj.pos.y
                if lchild != None:

                    # print("left:",lchild.element,end=",")

                    lchild.parent = u
                    if lchild.currobj.pos.y > y:
                        y = lchild.currobj.pos.y

                if rchild != None:

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
                    
                if lchild != None:
                    lchild.currobj.pos.y = y
                    lchild.textobj.pos.y = y
                    lchild.arrparent = arrow(pos=u.currobj.pos,
                            axis=lchild.currobj.pos - u.currobj.pos, shaftwidth=u.arrShaftWidth,
                    headwidth=u.arrHeadWidth,
                    headlength=u.arrHeadLength,
                            color=color.red)
                if rchild != None:
                    rchild.currobj.pos.y = y
                    rchild.textobj.pos.y = y
                    rchild.arrparent = arrow(pos=u.currobj.pos,
                            axis=rchild.currobj.pos - u.currobj.pos, shaftwidth=u.arrShaftWidth,
                    headwidth=u.arrHeadWidth,
                    headlength=u.arrHeadLength,
                            color=color.red)
        else:

            u.leftchild = None
            u.rightchild = None
#         print (
#             'Changed position',
#             u.element,
#             ' ',
#             u.currobj.pos.x,
#             ' ',
#             u.currobj.pos.y,
#             )
        self.root = u
        return u

    def isExternal(self, curnode):
        if curnode.leftchild == None and curnode.rightchild == None:
            return True
        else:
            return False

    def getChildren(self, curnode):
        children = []

        if curnode.leftchild != None:
            children.append(curnode.leftchild)

        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    def preorderTraverse(self, v):
        curnode = v

        print(curnode.element,end=" ")

        if curnode.leftchild != None:
            self.preorderTraverse(curnode.leftchild)
        if curnode.rightchild != None:
            self.preorderTraverse(curnode.rightchild)
        return

    def postorderTraverse(self, v):
        curnode = v
        if curnode.leftchild != None:
            self.postorderTraverse(curnode.leftchild)
        if curnode.rightchild != None:
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
        if v == None:
            return 0
        if v != None:
            if self.isExternal(v):
                return 1
            else:
                h = 0
                if v.leftchild != None:
                    h = max(h, self.findHeightIter(v.leftchild))
                if v.rightchild != None:
                    h = max(h, self.findHeightIter(v.rightchild))
                return 1 + h

    def findHeight(self, v):
        if v == None:
            return 0

        u = self.findElement(v.element, self.root)
        if u == None:
            return 0
        if u != None:
            return self.findHeightIter(u)

    def printTree(self, v):
        return

    def preOrderHideTraverse(self, curnode):
        curnode.textobj.visible = False
        curnode.currobj.visible=False
        if curnode.arrparent!=None:
            curnode.arrparent.visible=False
        if curnode.leftchild != None:
            self.preOrderHideTraverse(curnode.leftchild)
        if curnode.rightchild != None:
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
    l = list(map(int, input().strip().split()))
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

        print(x)
        objlist.append(n)
        
    bst1.createTree(objlist)
    scene.waitfor('click')
    bst1.preOrderHideTraverse(bst1.root)

    bst2 = BinarySearchTree()
    bst2.pointer = ring(pos=vector(0,0,0),axis=vector(0,0,1),radius=0.26,color=color.purple,thickness=0.1)
    ch = input('Do you want to continue?(y/n): ')
#     scene = canvas()
    
    if ch!='y':
        return
#     ch = 'y'
    
    
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
            if(bst2.root==None):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.red
                i = int(input('Enter element to be searched: '))
                bst2.searchvis(i,bst2.root)
                if(bst2.pointer.color==color.red):
                    print("Element",i,"does not exist in tree")
                else:
                    print("Element found")
        elif(op==3):
            print('Visualisation - BST tree Deletion')
            i = int(input('Enter element to be deleted: '))
            if(bst2.root==None):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.red
                bst2.deleteElementAVL(i)
                if(bst2.pointer.color==color.red):
                    print("Element",i,"does not exist in tree")
                else:
                    print("Element deleted")
            
        elif(op==4):
            print('Visualisation - Preorder')
            if(bst2.root==None):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.yellow
                bst2.preordervis(bst2.root)
        elif(op==5):
            print('Visualisation - Postorder')
            if(bst2.root==None):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.yellow
                bst2.postordervis(bst2.root)
        elif(op==6):
            print('Visualisation - Inorder')
            if(bst2.root==None):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.yellow
                bst2.inordervis(bst2.root)
        elif(op==7):
            print('Visualisation - Levelorder')
            if(bst2.root==None):
                print("Tree does not exist")
            else:
                bst2.pointer.pos = vector(0,0,0)
                bst2.pointer.color=color.yellow
                bst2.levelordervis(bst2.root)
        else:
            print("Invalid option")

#       scene.waitfor('click')

        ch = input('Do you want to continue?(y/n): ')
        sleep(1)
        bst2.pointer.visible=True

def main():
    testmain()


if __name__ == '__main__':
    main()
