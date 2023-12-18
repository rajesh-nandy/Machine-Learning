import random

class Node():
  def __init__(self, key, level):
    self.key = key
    self.forward = [None]*(level+1)


class SkList():

  def __init__(self, maxheight, P):
    self.maxheight = maxheight
    self.P = P
    self.head = Node(-1, self.maxheight)
    self.height = 0

  def random_height(self):
    height = 0
    while random.random()<self.P and height<self.maxheight:
      height += 1
    return height

  def insert(self, key):
    head = self.head
    update = [None]*(self.maxheight+1)

    for i in range(self.height, -1, -1):
      while (head.forward[i] and head.forward[i].key < key):
        head = head.forward[i]
      update[i] = head

    head = head.forward[0]

    if(head == None or head.key != key):
      rheight = self.random_height()
      if(rheight > self.height):
        for i in range(self.height + 1, rheight + 1):
          update[i] = self.head
        self.height = rheight
      
      n = Node(key, rheight)
      for i in range(rheight + 1):
        n.forward[i] = update[i].forward[i]
        update[i].forward[i] = n

      print("Inserted ", key)

  def search(self, key):
    head = self.head
    for i in range(self.height, -1, -1):
      while(head.forward[i] and head.forward[i].key < key):
        head = head.forward[i]
    head = head.forward[0]
    if(head and head.key == key):
      print("Key has been found")


  def search_range(self, a, b):
    head = self.head
    for i in range(self.height, -1, -1):
      while(head.forward[i] and head.forward[i].key < a):
        head = head.forward[i]
    while(head.forward[0] and head.forward[0].key < b):
      head = head.forward[0]
      print(head.key)


  def delete(self, key):
    update = [None] * (self.maxheight + 1)
    head = self.head
    for i in range(self.height, -1, -1):
      while(head.forward[i] and head.forward[i].key < key):
        head = head.forward[i]
      update[i] = head
    head = head.forward[0]

    if(head != None and head.key == key):
      for i in range(self.height + 1):
        if(update[i].forward[i] != head):
          break
        update[i].forward[i] = head.forward[i]

      while(self.height > 0 and self.head.forward[self.height] == None):
        self.level = -1
      print(key, " deleted")
              

  def display(self):
    head = self.head
    for h in range(self.height + 1):
      print("L", h, ":", end = " ")
      node = head.forward[h]
      while(node != None):
        print(node.key, end = " ")
        node = node.forward[h]
      
      print()

  def list_height(self):
    return(self.height + 1)




def main():
  l = SkList(3, 0.5)
  while(True):
    print("\n  1. insert an element \n\
  2. delete an element\n\
  3. search for an element\n\
  4. search for all elements in a given range [a,b]\n\
  5. print the skip list\n\
  6. print the height of the skip list\n\
  7. exit")
    i = input("Pick a action")
    if(i == '1'):
      key = int(input("Enter the key to Insert:"))
      l.insert(key)
    elif(i == '2'):
      key = int(input("Enter the key to Delete:"))
      l.delete(key)
    elif(i == '3'):
      key = int(input("Enter the key to Search:"))
      l.search(key)
    elif(i == '4'):
      a = int(input("Enter the lower bound to Search:"))
      b = int(input("Enter the upper bound to Search:"))
      l.search_range(a,b)
    elif(i == '5'):
      print("~~The SKIPLIST~~")
      l.display()
    elif(i == '6'):
      print("Height = ", l.list_height())
    elif(i == '7'):
      break
    else:
      print("try again")
main()
  