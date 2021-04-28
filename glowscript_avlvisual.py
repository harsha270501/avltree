# GlowScript 3.1 VPython

from vpython import *

bg_color = vec(0.8941, 0.9765, 0.9608)
arr_color = vec(0.4313, 0.7686, 0.7607)
node_color = vec(0.0510, 0.4510, 0.4667)

inp_str = ""
win = undefined


def bind_fn(obj):
    global inp_str, win
    inp_str = obj.text
    win.delete()


def get_input(prompt_text=""):
    global inp_str, win
    inp_str = ""
    win = winput(prompt=prompt_text, type='string', bind=bind_fn)


def wait_for_input():
    global inp_str
    while inp_str == "":
        rate(100)

class node:

    def __init__(self):
        self.element = 0
        self.leftchild = undefined
        self.rightchild = undefined
        self.parent = undefined
        self.currobj = undefined  # sphere obj
        self.arrparent = undefined  # arrow obj
        self.textobj = undefined  # label obj
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
            self.pointer.pos = curnode.currobj.pos
            if e < curnode.element:
                if curnode.leftchild == undefined:
                    sleep(1)
                    self.pointer.color = color.green
                    return curnode
                else:
                    return self.findInsert(e, curnode.leftchild)
            else:

                if curnode.rightchild == undefined:
                    sleep(1)
                    self.pointer.color = color.green
                    return curnode
                else:
                    return self.findInsert(e, curnode.rightchild)

    # function to find the position where the given element has to be deleted

    def findDelete(self, e, curnode):
        sleep(1)
        if curnode != undefined:

            self.pointer.pos = curnode.currobj.pos
            if e < curnode.element:
                return self.findDelete(e, curnode.leftchild)

            elif e == curnode.element:
                sleep(1)
                self.pointer.color = color.green
                return curnode
            else:
               return self.findDelete(e, curnode.rightchild)
        return undefined

    # checks if the height is balanced

    def balanceCheck(self, w):
        if w != undefined:
            lh = self.findHeightIter(w.leftchild)
            rh = self.findHeightIter(w.rightchild)
            h = lh-rh
            if h < -1 or h > 1:
                return w
            else:
                return self.balanceCheck(w.parent)
        return undefined

    # restructuring after delete - done recursively

    def restructureDel(self, u):
        if u != undefined:
            p1 = u.parent
            self.trinode_restructure(u)
            if p1 != undefined:
                self.restructureDel(p1)

    # restructure to balance tree

    def trinode_restructure(self, u):
        z = self.balanceCheck(u)

        if z != undefined:
            print("Imbalance at: ", z.element)

            q = [z]
            self.del_Pos_Before_Restructure(q)

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

            h1 = self.findHeight(y.leftchild)
            h2 = self.findHeight(y.rightchild)
            if h1 > h2:
                x = y.leftchild
            else:
                x = y.rightchild

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
                    if(t2 != undefined):
                        t2.parent = z
                else:
                    t2 = y.leftchild
                    y.leftchild = z
                    z.rightchild = t2
                    if(t2 != undefined):
                        t2.parent = z
                if p != undefined:
                    if z == p.leftchild:
                        p.leftchild = y
                    else:
                        p.rightchild = y
                else:
                    self.root = y
                y.parent = p
                z.parent = y
                q = [y]
                self.new_Pos_After_Restructure(q)
            elif b == x:
                p = z.parent
                t1 = x.leftchild
                t2 = x.rightchild
                if y == z.leftchild and x == y.rightchild:
                    z.leftchild = t2
                    if(t2 != undefined):
                        t2.parent = z
                    if(t1 != undefined):
                        t1.parent = y
                    y.rightchild = t1
                    x.leftchild = y
                    x.rightchild = z
                else:
                    z.rightchild = t1
                    if(t1 != undefined):
                        t1.parent = z
                    y.leftchild = t2
                    if(t2 != undefined):
                        t2.parent = y
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
                q = [x]
                self.new_Pos_After_Restructure(q)

        else:
            if ((int(u.currobj.pos.x) in self.posnode) and (u.element != self.posnode[str(int(u.currobj.pos.x))].element)):
                self.clashHandle(u)
                self.posnode[str(int(u.currobj.pos.x))] = u
            else:
                self.posnode[str(int(u.currobj.pos.x))] = u

    def del_Pos_Before_Restructure(self, q):
        q1 = []
        if(len(q) > 0):
            for i in q:
                if ((int(i.currobj.pos.x) in self.posnode) and (i.element == self.posnode[str(int(i.currobj.pos.x))].element)):
                    del self.posnode[str(int(i.currobj.pos.x))]
                if(i.currobj != undefined):
                    i.currobj.visible = False
                    #o=i.currobj
                    #i.currobj=undefined
                    #del o

                if(i.arrparent != undefined):
                    i.arrparent.visible = False
                    #o=i.arrparent
                    #i.arrparent=undefined
                    #del o

                if(i.textobj != undefined):
                    i.textobj.visible = False
                    #o=i.textobj
                    #i.textobj=undefined
                    #del o

                w = self.getChildren(i)
                for j in w:
                    q1.append(j)
            self.del_Pos_Before_Restructure(q1)

    def new_Pos_After_Restructure(self, q):
        q1 = []
        if(len(q) > 0):
            for u in q:
                v = u.parent
                if v == undefined:
                    vect = vector(0, 0, 0)
                    s = sphere(pos=vect, radius=0.25, color=node_color)
                    ln = label(pos=vect, text=str(u.element),
                               color=color.white, opacity=0, height=18, box=False)
                    u.currobj = s
                    u.textobj = ln
                else:
                    if u == v.rightchild:
                        vx = int(v.currobj.pos.x) + 1
                        vy = int(v.currobj.pos.y) - 1
                        vect = vector(vx, vy, 0)
                        s = sphere(pos=vect, radius=0.25, color=node_color)
                        ln = label(pos=vect, text=str(u.element), color=color.white, height=18,
                                   opacity=0, box=False)
                        a = arrow(
                            pos=v.currobj.pos,
                            axis=vect - v.currobj.pos,
                            shaftwidth=u.arrShaftWidth,
                            headwidth=u.arrHeadWidth,
                            headlength=u.arrHeadLength,
                            color=arr_color,
                        )
                        u.currobj = s
                        u.arrparent = a
                        u.textobj = ln
                    else:
                        vx = int(v.currobj.pos.x) - 1
                        vy = int(v.currobj.pos.y) - 1
                        vect = vector(vx, vy, 0)
                        s = sphere(pos=vect, radius=0.25, color=node_color)
                        ln = label(pos=vect, text=str(u.element), color=color.white, height=18,
                                   opacity=0, box=False)
                        a = arrow(
                            pos=v.currobj.pos,
                            axis=vect - v.currobj.pos,
                            shaftwidth=u.arrShaftWidth,
                            headwidth=u.arrHeadWidth,
                            headlength=u.arrHeadLength,
                            color=arr_color,
                        )
                        u.currobj = s
                        u.arrparent = a
                        u.textobj = ln

                if str(int(u.currobj.pos.x)) in self.posnode:
                    self.clashHandle(u)
                    self.posnode[str(int(u.currobj.pos.x))] = u
                else:
                    self.posnode[str(int(u.currobj.pos.x))] = u

                scene.visible = True
                w = self.getChildren(u)
                for j in w:
                    q1.append(j)
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
            s = sphere(pos=vect, radius=0.25, color=node_color)
            ln = label(pos=vect, text=str(e), color=color.white, height=18,
                       opacity=0, box=False)
            u.currobj = s
            u.textobj = ln
        else:
            if u == v.rightchild:
                vx = int(v.currobj.pos.x) + 1
                vy = int(v.currobj.pos.y) - 1
                vect = vector(vx, vy, 0)
                s = sphere(pos=vect, radius=0.25, color=node_color)
                ln = label(pos=vect, text=str(e), color=color.white, height=18,
                           opacity=0, box=False)
                a = arrow(
                    pos=v.currobj.pos,
                    axis=vect - v.currobj.pos,
                    shaftwidth=u.arrShaftWidth,
                    headwidth=u.arrHeadWidth,
                    headlength=u.arrHeadLength,
                    color=arr_color,
                )
                u.currobj = s
                u.arrparent = a
                u.textobj = ln
            else:
                vx = int(v.currobj.pos.x) - 1
                vy = int(v.currobj.pos.y) - 1
                vect = vector(vx, vy, 0)
                s = sphere(pos=vect, radius=0.25, color=node_color)
                ln = label(pos=vect, text=str(e), color=color.white, height=18,
                           opacity=0, box=False)
                a = arrow(
                    pos=v.currobj.pos,
                    axis=vect - v.currobj.pos,
                    shaftwidth=u.arrShaftWidth,
                    headwidth=u.arrHeadWidth,
                    headlength=u.arrHeadLength,
                    color=arr_color,
                )
                u.currobj = s
                u.arrparent = a
                u.textobj = ln
        #self.pointer.pos=u.currobj.pos
        # if int(u.currobj.pos.x) in self.posnode.keys():
        #     self.clashHandle(u)
        #     self.posnode[int(u.currobj.pos.x)] = u

        # else:
        #     self.posnode[int(u.currobj.pos.x)] = u
        self.pointer.pos = u.currobj.pos
        sleep(1)
        self.pointer.color = color.cyan
        scene.visible = True

        self.trinode_restructure(u)
        self.pointer.pos = u.currobj.pos
        return

    # BST insertion - visualisation
    def insertVisual(self, e):
        #rate(1)
        u = self.insertElementAVL(e)

    # function to handle clashes
    def searchvis(self, k, n):
        sleep(1)
        self.pointer.pos = n.currobj.pos
        if n.element == k:
            sleep(1)
            self.pointer.color = color.green
            return
        else:
            if k > n.element and n.rightchild != undefined:
                self.searchvis(k, n.rightchild)
            if k < n.element and n.leftchild != undefined:
                self.searchvis(k, n.leftchild)

    def preordervis(self, n):
        sleep(1)
        self.pointer.pos = n.currobj.pos
        print(n.element, end=", ")
        if n.leftchild != undefined:
            self.preordervis(n.leftchild)

        if n.rightchild != undefined:
            self.preordervis(n.rightchild)
        return

    def postordervis(self, n):
        if n.leftchild != undefined:
            self.postordervis(n.leftchild)

        if n.rightchild != undefined:
            self.postordervis(n.rightchild)

        sleep(1)
        self.pointer.pos = n.currobj.pos
        print(n.element, end=", ")
        return

    def inordervis(self, n):
        if n.leftchild != undefined:
            self.inordervis(n.leftchild)
        sleep(1)
        self.pointer.pos = n.currobj.pos
        print(n.element, end=", ")
        if n.rightchild != undefined:
            self.inordervis(n.rightchild)
        return

    def levelordervis(self, n):
        q = []
        q.append(n)
        while(len(q) != 0):
            x = q.pop(0)
            sleep(1)
            print(x.element, end=", ")
            self.pointer.pos = x.currobj.pos
            if x.leftchild != undefined:
                q.append(x.leftchild)
            if x.rightchild != undefined:
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

        cx = 0
        if(node.element < self.root.element):
            cx = -1
        else:
            cx = 1

        for i in nodepos:
            if((cx == -1 and i <= node.currobj.pos.x) or (cx == 1 and i >= node.currobj.pos.x)):
                if((self.posnode[str(i)] != self.root) and ((i != node.currobj.pos.x) or ((cx == -1 and node.parent != undefined and node.parent.rightchild != node) or (cx == 1 and node.parent != undefined and node.parent.leftchild != node)))):
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

        if((cx == -1 and node.parent != undefined and node.parent.rightchild == node) or (cx == 1 and node.parent != undefined and node.parent.leftchild == node)):
            node.currobj.pos.x += cx
            node.arrparent.pos = node.parent.currobj.pos
            node.arrparent.axis = node.currobj.pos - node.parent.currobj.pos
            node.textobj.pos = node.currobj.pos

        for j in changed_posnode:
            self.posnode[j] = changed_posnode[j]

        if(flag == 1):
            self.pointer.pos = node.currobj.pos

#    def clashInorderTraverse(self, currnode, cx):
#        if cx == -1:                        #LPR Left subtree extension
#            if currnode != undefined:
#                if currnode.leftchild != undefined:22
#                    self.clashInorderTraverse(currnode.leftchild, cx)
#
#                del self.posnode[currnode.currobj.pos.x]
#                currnode.currobj.pos += vector(cx, 0, 0)
#                currnode.arrparent.pos = currnode.currobj.pos
#                currnode.arrparent.axis = currnode.currobj.pos - currnode.parent.currobj.pos
#                currnode.textobj.pos = currnode.currobj.pos
#                self.posnode[currnode.currobj.pos.x] = currnode
#
#                if currnode.rightchild != undefined:
#                    self.clashInorderTraverse(currnode.rightchild, cx)
#
#        else:                                #RPL Right subtree extension
#            if currnode != undefined:
#                if currnode.rightchild != undefined:
#                    self.clashInorderTraverse(currnode.rightchild, cx)
#
#                del self.posnode[currnode.currobj.pos.x]
#                currnode.currobj.pos += vector(cx, 0, 0)
#                currnode.arrparent.pos = currnode.currobj.pos
#                currnode.arrparent.axis = currnode.currobj.pos - currnode.parent.currobj.pos
#                currnode.textobj.pos = currnode.currobj.pos
#                self.posnode[currnode.currobj.pos.x] = currnode
#
#                if currnode.leftchild != undefined:
#                    self.clashInorderTraverse(currnode.leftchild, cx)
#

    def inorderTraverse(self, v):
        if v != undefined:
            if v.leftchild != undefined:
                self.inorderTraverse(v.leftchild)

            print(v.element, end=" ")

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
        #sleep(1)
        print("Deleting element ", e)
        self.pointer.pos = vector(0, 0, 0)
        self.pointer.color = color.red
        l = t.leftchild
        r = t.rightchild
        p = t.parent
        child = 0
        if l != undefined:
            child += 1
        if r != undefined:
            child += 1
        if self.isExternal(t):
            print("Deleting external node")
            if p == undefined:
                self.root = undefined

            else:
                if t == p.leftchild:
                    p.leftchild = undefined
                else:
                    p.rightchild = undefined
            x = int(t.currobj.pos.x)
            t.currobj.visible = False
            if(t.arrparent != undefined):
                t.arrparent.visible = False
            t.textobj.visible = False
            del self.posnode[str(x)]
            self.restructureDel(t.parent)

            del t
        elif child == 1:
            if(l != undefined):
                tempele = l.element
            else:
                tempele = r.element
            print("Deleting node with 1 child")

            self.removeElement(tempele)

            t.element = tempele
            t.textobj.text = str(tempele)
        else:
            temp = self.returnNextInorder(t.rightchild)
            tempele = temp.element
            print("Deleting node with 2 children")

            self.removeElement(tempele)

            t.element = tempele
            t.textobj.text = str(tempele)
        return

    def repositionAfterDel(self):

        nodepos = []
        for i in self.posnode:
            nodepos.append(int(i))

        nodepos.sort()
        for i in range(1, len(nodepos)):
            if(nodepos[i]-nodepos[i-1] != 1):
                if(nodepos[i-1] < 0):
                    for j in range(i-1, -1, -1):
                        o = self.posnode[str(nodepos[j])]
                        del self.posnode[str(int(o.currobj.pos.x))]
                        o.currobj.pos.x = int(o.currobj.pos.x)+1
                        if(o.parent != undefined):
                            o.arrparent.pos = o.parent.currobj.pos
                            o.arrparent.axis = o.currobj.pos - o.parent.currobj.pos
                        o.textobj.pos = o.currobj.pos
                        self.posnode[str(int(o.currobj.pos.x))] = o
                        if(o.rightchild != undefined):
                            rc = o.rightchild
                            rc.arrparent.pos = o.currobj.pos
                            rc.arrparent.axis = rc.currobj.pos - o.currobj.pos
                            o.rightchild = rc

                elif(nodepos[i] > 0):
                    for j in range(i, len(nodepos)):
                        o = self.posnode[str(nodepos[j])]
                        del self.posnode[str(int(o.currobj.pos.x))]
                        o.currobj.pos.x = int(o.currobj.pos.x)-1
                        if(o.parent != undefined):
                            o.arrparent.pos = o.parent.currobj.pos
                            o.arrparent.axis = o.currobj.pos - o.parent.currobj.pos
                        o.textobj.pos = o.currobj.pos
                        self.posnode[str(int(o.currobj.pos.x))] = o
                        if(o.leftchild != undefined):
                            lc = o.leftchild
                            lc.arrparent.pos = o.currobj.pos
                            lc.arrparent.axis = lc.currobj.pos - o.currobj.pos
                            o.leftchild = lc
                break

    # AVL- delete element

    def removeElementAVL(self, e):
        t = self.findElement(e, self.root)
        if(t != undefined):
            self.removeElement(e)
            self.repositionAfterDel()
            return 1
        else:
            return 0

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
        if l == 0:
            return

        mid = l // 2

        lr = items[:mid]
        rr = items[mid + 1:]
        u = items[mid]
        if l > 1:
            lchild = self.createTree(lr)
            rchild = self.createTree(rr)
            u.leftchild = lchild
            u.rightchild = rchild
            if lchild != undefined or rchild != undefined:
                y = u.currobj.pos.y
                if lchild != undefined:
                    lchild.parent = u
                    if lchild.currobj.pos.y > y:
                        y = lchild.currobj.pos.y

                if rchild != undefined:
                    rchild.parent = u
                    if rchild.currobj.pos.y > y:
                        y = rchild.currobj.pos.y
                j = 0
                u.currobj.pos.y = y
                u.textobj.pos.y = y
                while(j < 2):
                    sleep(1)
                    u.currobj.pos.y += 1
                    u.textobj.pos.y += 1
                    j += 1

                if lchild != undefined:
                    lchild.currobj.pos.y = y
                    lchild.textobj.pos.y = y
                    lchild.arrparent = arrow(pos=u.currobj.pos,
                                             axis=lchild.currobj.pos - u.currobj.pos, shaftwidth=u.arrShaftWidth,
                                             headwidth=u.arrHeadWidth,
                                             headlength=u.arrHeadLength,
                                             color=arr_color)
                if rchild != undefined:
                    rchild.currobj.pos.y = y
                    rchild.textobj.pos.y = y
                    rchild.arrparent = arrow(pos=u.currobj.pos,
                                             axis=rchild.currobj.pos - u.currobj.pos, shaftwidth=u.arrShaftWidth,
                                             headwidth=u.arrHeadWidth,
                                             headlength=u.arrHeadLength,
                                             color=arr_color)
        else:

            u.leftchild = undefined
            u.rightchild = undefined
        self.root = u
        return u

    def isExternal(self, curnode):
        if curnode.leftchild == undefined and curnode.rightchild == undefined:
            return True
        else:
            return False

    def getChildren(self, curnode):
        children = []

        if curnode.leftchild != undefined:
            children.append(curnode.leftchild)

        if curnode.rightchild != undefined:
            children.append(curnode.rightchild)
        return children

    def preorderTraverse(self, v):
        curnode = v

        print(curnode.element, end=" ")

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

        print(curnode.element, end=" ")

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

    def preOrderHideTraverse(self, curnode):
        if(curnode != undefined):
            curnode.textobj.visible = False
            curnode.currobj.visible = False
            if curnode.arrparent != undefined:
                curnode.arrparent.visible = False
            if curnode.leftchild != undefined:
                self.preOrderHideTraverse(curnode.leftchild)
            if curnode.rightchild != undefined:
                self.preOrderHideTraverse(curnode.rightchild)
        return


bst1 = BinarySearchTree()
bst2 = BinarySearchTree()
bst2.pointer = ring(pos=vector(0, 0, 0), axis=vector(
    0, 0, 1), radius=0.26, color=color.purple, thickness=0.1)
bst2.pointer.visible = False


def testmain(op):

    if(op.index == 1):
        op.index = 0
        print('Visualising - Create AVL tree')
        bst1.preOrderHideTraverse(bst1.root)
        if(bst2.root != undefined):
            bst2.preOrderHideTraverse(bst2.root)
        get_input("Enter elements to build an AVL tree: ")
        wait_for_input()
        l = list(map(int, inp_str.split(' ')))
        x = len(l)//2
        x *= -1
        l.sort()
        objlist = []
        y = x
        for i in l:
            sleep(1)
            n = node()
            n.element = i
            s = sphere(pos=vector(x, y, 0), radius=0.25, color=node_color)
            ln = label(pos=vector(x, y, 0), text=str(i), color=color.white,
                       opacity=0, box=False)
            n.currobj = s
            n.textobj = ln
#            print(x,i)
            x += 1

            objlist.append(n)

        bst1.createTree(objlist)
#        scene.waitfor('click')

    elif(op.index == 2):
        op.index = 0
        bst1.preOrderHideTraverse(bst1.root)
        if(bst2.root != undefined):
            bst2.pointer.visible = True
        print('\nVisualising - Insertion')
        bst2.pointer.pos = vector(0, 0, 0)
        bst2.pointer.color = color.red
        get_input('Enter element to be inserted: ')
        wait_for_input()
        i = int(inp_str)
        bst2.insertVisual(i)
    elif(op.index == 3):
        op.index = 0
        print('Visualising - Searching')
        if(bst2.root == undefined):
            print("Tree does not exist.")
        else:
            bst2.pointer.pos = vector(0, 0, 0)
            bst2.pointer.color = color.red
            get_input('Enter element to be searched: ')
            wait_for_input()
            i = int(inp_str)
            bst2.searchvis(i, bst2.root)
            if(bst2.pointer.color == color.red):
                print("Element", i, "does not exist in tree.")
            else:
                print("Element found.")
    elif(op.index == 4):
        op.index = 0
        print('Visualising - Deletion')
        get_input('Enter element to be deleted: ')
        wait_for_input()
        i = int(inp_str)
        if(bst2.root == undefined):
            print("Tree does not exist.")
        else:
            bst2.pointer.pos = vector(0, 0, 0)
            bst2.pointer.color = color.red
            cond = bst2.removeElementAVL(i)
            if(cond == 1):
                print("Element", i, "deleted.")
            else:
                print("Element does not exist.")

    elif(op.index == 5):
        op.index = 0
        print('Visualising - Preorder Traversal')
        if(bst2.root == undefined):
            print("Tree does not exist.")
        else:
            bst2.pointer.pos = vector(0, 0, 0)
            bst2.pointer.color = color.yellow
            bst2.preordervis(bst2.root)
    elif(op.index == 6):
        op.index = 0
        print('Visualising - Postorder Traversal')
        if(bst2.root == undefined):
            print("Tree does not exist.")
        else:
            bst2.pointer.pos = vector(0, 0, 0)
            bst2.pointer.color = color.yellow
            bst2.postordervis(bst2.root)
    elif(op.index == 7):
        op.index = 0
        print('Visualising - Inorder Traversal')
        if(bst2.root == undefined):
            print("Tree does not exist.")
        else:
            bst2.pointer.pos = vector(0, 0, 0)
            bst2.pointer.color = color.yellow
            bst2.inordervis(bst2.root)
    elif(op.index == 8):
        op.index = 0
        print('Visualising - Level Order Traversal')
        if(bst2.root == undefined):
            print("Tree does not exist.")
        else:
            bst2.pointer.pos = vector(0, 0, 0)
            bst2.pointer.color = color.yellow
            bst2.levelordervis(bst2.root)

#       scene.waitfor('click')

#        ch = input('Do you want to continue?(y/n): ')
    sleep(1)
    print()
#    bst2.pointer.visible = True


if __name__ == '__main__':
    scene.background = bg_color
    #    1.Insertion 2. Searching 3.Deletion 4.Preorder 5.Postorder 6.Inorder 7.LevelOrder
    menu(choices=['Select Option', 'Create AVL Tree', 'Insert', 'Search', 'Delete', 'Preorder Traversal',
                  'Postorder Traversal', 'Inorder Traversal', 'Level Order Traversal'], bind=testmain)
    scene.append_to_caption('\n\n')
