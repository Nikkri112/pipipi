#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import random
import os

class crab:
    
    def __init__(self):
        self.nick = "crab"
        self.n = n-1
        self.m = m-1
        l =[1,m]
        self.y = random.randint(1, (n-1))
        if self.y > 1 and self.y<n:
            self.x = random.choice(l)
        elif self.y == n or self.y ==1:
            self.x = random.randint(1,m)
        
    def action(self):
        if self.y > 1 and self.y<n:
            k == randint(1,2)
            if k == 1:
                self.up
            else:
                self.down
        if self.x > 1 and self.x<n:
            k == randint(1,2)
            if k == 1:
                self.right
            else:
                self.left
        if self.y == n and self.x == 1:
            k == randint(1,2)
            if k == 1:
                self.right
            else:
                self.up
                
        if self.y == n and self.x == m:
            k == randint(1,2)
            if k == 1:
                self.left
            else:
                self.up
                
        if self.y == 1 and self.x == m:
            k == randint(1,2)
            if k == 1:
                self.left
            else:
                self.down
                
        if self.y == 1 and self.x == 1:
            k == randint(1,2)
            if k == 1:
                self.right
            else:
                self.down
                
        return(self.x,self.y)
    
    def up(self):
        self.y-=1
        return(self.x,self.y)
    
    def down(self):
        self.y+=1
        return(self.x,self.y)
    
    def left(self):
        self.x-=1
        return(self.x,self.y)
    
    def right(self):
        self.x+=1
        return(self.x,self.y)
    
class Player:
    
    def __init__(self):
        self.n = n
        self.m = m
        self.nick = input("Введите ник ")
        self.attack = int(input("Введите урон "))
        self.hp = int(input("Введите хп "))
        self.y = random.randint(1,n-1)
        self.x = random.randint(1,m-1)
        
    def action(self):
        print(self.nick,",выберите действие ")
        print("1 - вверх 2 - вниз 3 - влево 4 - вправо; любое другое - скип")
        k = int(input())
        if k == 1:
            self.up()
        elif k == 2:
            self.down()
        elif k == 3:
            self.left()
        elif k == 4:
            self.right()
        self.cheker()
        return(self.x,self.y)
    
    def up(self):
        self.y-=1
        return(self.x,self.y)
    
    def down(self):
        self.y+=1
        return(self.x,self.y)
    
    def left(self):
        self.x-=1
        return(self.x,self.y)
    
    def right(self):
        self.x+=1
        return(self.x,self.y)
    
    def cheker(self):
        if self.x<0:
            self.x = self.x + 1
            self.action()
        if self.x > m-1:
            self.x = self.x - 1
            self.action()
        if self.y<0:
            self.y = self.y + 1
            self.action()
        if self.y > n-1:
            self.y = self.y - 1
            self.action()
        return(self.x,self.y)

def polevivod(n,m):   
    s = ""
    for i in range(0,n):
        for j in range(0,m):
            if i == B.y and j == B.x and i == A.y and j == A.x:
                s = s+(B.nick+A.nick) 
            elif i == A.y and j == A.x:
                s = s + A.nick
            elif i == B.y and j == B.x:
                s = s + B.nick
            elif i == crab.y and j == crab.x:
                s = s + crab.nick
            else:
                s = s+" - "  
        s = s+'\n'
    print(s)
def vivodstat():
    print(A.nick," ХП -", A.hp, " DMG- ", A.attack, B.nick," ХП -", B.hp, " DMG- ", B.attack,)

clear = lambda: os.system('cls')
n = int(input("Введите высоту поля "))
m = int(input("Введите ширину поля "))
A = Player()
B = Player()
crab = crab()

while A.hp >0 and B.hp > 0:
    clear()
    polevivod(n,m)
    vivodstat()
    A.action()
    A.cheker()
    if (A.x+1 == B.x and A.y+1 == B.y) or (A.x-1 == B.x and A.y-1 == B.y) or (A.x == B.x and A.y+1 == B.y) or (A.x == B.x and A.y-1 == B.y) or (A.x+1 == B.x and A.y-1 == B.y) or (A.x-1 == B.x and A.y+1 == B.y) or (A.x-1 == B.x and A.y == B.y) or (A.x+1 == B.x and A.y == B.y):
        B.hp = B.hp - A.attack
    clear()
    polevivod(n,m)
    vivodstat()
    B.action()
    B.cheker()
    if (B.x == A.x and B.y+1 == A.y) or (B.x == A.x and B.y-1 == A.y) or (B.x-1 == A.x and B.y == A.y) or (B.x+1 == A.x and B.y == A.y):
        A.hp = A.hp - B.attack
    if (crab.x == A.x and crab.y+1 == A.y) or (crab.x == A.x and crab.y-1 == A.y) or (crab.x-1 == A.x and crab.y == A.y) or (crab.x+1 == A.x and crab.y == A.y):
        A.hp = A.hp - crab.attack

if A.hp <= 0:
    print(B.nick, "победил")
    input()
if B.hp <= 0:
    print(A.nick, "победил")
    input()


# # 

# In[49]:


class soda:
    def __init__(self):
    self.syrop = input("Введите ыф")
    
    def showmydrink(self):
        if self.syrop == "Барбарис":
            print("Барабарисовая газуха")
        else:
            print("Простая газировка")

n = input("Введите сироп")            
sodasa = soda()
sodas


# In[ ]:





# In[ ]:




