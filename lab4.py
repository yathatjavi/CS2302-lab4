# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:54:07 2019

@author: Javier Soto
Professor Olac fuentes
TAs:
    -Anindita Nath
    -Maliheh Zaragaran
IA
    -Eduardo Lara
Peer Leader
    -Erick Macik
    
the puspose of this lab is to demonstrate my knowldge of implementing Binary 
search trees as provided by Professor Olac Fuentes
"""
import btree as bt

def Question1(T):
    #Compute the height of the tree
    return bt.height(T)

def Question2(T,L):
    #Extract the items in the B-tree into a sorted list.
    #Travrse the tree in the same way as the print method and append to list
    # in order
    if T.isLeaf:
        for t in T.item:
            L.append(t)
    else:
        for i in range(len(T.item)):
            Question2(T.child[i],L)
            L.append(T.item[i])
        Question2(T.child[-1],L)
        

def Question3and4(T,d):
    #used to check if d exceeds the depth of tree 
    # in seperate method to not affect the time complexity of the recursive call
   if d> (bt.height(T)):
       print('This depth is larger than the height of the tree')
       return
   MinItem= Q3Helper(T,d)
   MaxItem = Question4(T,d)
   print('The smallest item at depth', end =' ')
   print(str(d), end = " ")
   print('is ' + str(MinItem) + ', and the largest number is ', end =' ')
   print(str(MaxItem) + ('.'))
   
def Q3Helper(T,d):
     #3. Return the minimum element in the tree at a given depth d.
     #will take a btree make d recursice calls and return the smallest element 
     # at that level
    if d == 0:
        return T.item[0]
    return Q3Helper(T.child[0],d-1)

def Question4(T,d):
    #Return the maximum element in the tree at a given depth d.
    #will take a b tree make d recursive calls and returnt the largest item at 
    #that level
    if d == 0:
        return T.item[-1]
    return Question4(T.child[-1],d-1)
    
def Question5(T,d):
    #Return the number of nodes in the tree at a given depth d.
    #will take a tree make d recursive calls and return all the noedes at that 
    #level
    tot=0
    if d == 0:
        return len(T.item)
    if T.isLeaf:
        return 0
    else:
        for i in range(len(T.item)):
            tot += Question5(T.child[i],d-1)
        
        return tot + Question5(T.child[-1],d-1)
    
def Question6(T,d):
    #Print all the items in the tree at a given depth d.
    if d ==0:
        for i in range(len(T.item)):
            print(str(T.item[i]), end =" ")
    if T.isLeaf:
        return
    else:
        for i in range(len(T.item)):
            Question6(T.child[i], d-1)
        Question6(T.child[-1], d-1)
        
def Question7(T):
    #Return the number of nodes in the tree that are full.
    fullNodes =0
    if len(T.item) == T.max_items:
        return 1
    if T.isLeaf:
        return 0
    else:
        for i in range(len(T.item)):
            fullNodes =+ Question7(T.child[i])
        return fullNodes + Question7(T.child[-1])
    
def Question8(T):
#Return the number of leaves in the tree that are full.
    full =0
    if T.isLeaf:
        if len(T.item) == T.max_items:
            return 1
        else:
            return 0
    for i in range(len(T.item)):
        full += Question8(T.child[i])
    return full + Question8(T.child[-1])

def Question9(T,k):
#Given a key k, return the depth at which it is found in the tree, of -1 if k is not in the tree.
    if(k in T.item):
        return 0
    if T.isLeaf:
        return -1
    else:
        #used to find the child since we only need to follow one specific path 
        #either k is smaller or larger than itmes in currect list
        depth =   1+ Question9(T.child[bt.FindChild(T,k)],k)
        if depth >0:
            return depth
    return -1
def FillBTree():
    L = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21, 22]
    
    T = bt.BTree()    
    for i in L:
        bt.Insert(T,i)
    return T

inSize =int(input('What depth would you like to test?'))
searchee = int(input('Which item would you like to search for?'))
T = FillBTree()
T2 = FillBTree()
SorList =[]

print('Question 1:')
print('The height of this tree is ' + str(Question1(T)) + '.')
print()

print('Question 2:')
Question2(T,SorList)
print('The list created from this Tree is:')
print(*SorList , sep = ", ")
print()

print('Question 3 & 4:')
Question3and4(T,inSize)
print()

print('Question 5:')
print('there are ' + str(Question5(T,inSize)) + ' nodes at level ' + str(inSize) + '.')
print()


print('Question 6:')
print("The item(s) at depth " + str(inSize) + " is/are:" )
Question6(T,inSize)
print()
print()

print('Question 7:')
print("There are/is " + str(Question7(T)) + " full node(s) in this tree")
print()


print('Question 8:')
print('There are/is ' + str(Question8(T)) + " full  leaf node(s) in this tree" )
print()

print('Question 9:')
foundAt = Question9(T,searchee)
if foundAt<0:
    print(str(searchee) + " is not an item in this tree. ")
else:
    print(str(searchee) + " was found at depth " + str(foundAt))
#bt.PrintD(T,'')