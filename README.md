## avl (Adelson-Velsky-Landis) tree
>In computer science, an **AVL tree** is a self-balancing binary search tree. It was the first such data structure to be invented. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take `O(log n)` time in both the average and worst cases, where n is the number of nodes in the tree prior to the operation. Insertions and deletions may require the tree to be rebalanced by one or more tree rotations.

>The AVL tree is named after its two Soviet inventors, **Georgy Adelson-Velsky** and **Evgenii Landis**, who published it in their 1962 paper **"An algorithm for the organization of information"**.

>AVL trees are often compared with red–black trees because both support the same set of operations and take O(log n) time for the basic operations. For lookup-intensive applications, AVL trees are faster than red–black trees because they are more strictly balanced. Similar to red–black trees, AVL trees are height-balanced. Both are, in general, neither weight-balanced nor μ-balanced for any `μ ≤ 1 ⁄ 2`; that is, sibling nodes can have hugely differing numbers of descendants. For more information visit https://en.wikipedia.org/wiki/AVL_tree.

##### How to use:

  *description*: **`avl()`**
  
  *Space-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree*
  
  ```python
  import avl
  
  ob = avl.avl() 
  # Now u cud add keys and values/data to the tree
  ```
  
##### insert:

  *description*: **`insert(k, data = None)`** *it **inserts k, data (by default None)** to the tree*
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  ob.insert(1001, 'apple') # or ob[1001] = 'apple'
  ob.insert(1002, 'banana')
  ob.insert(1003) # or ob[1003] = None
  ob.insert(1004, 'orange')
  ob.insert(2001, 'pen')
  ob.insert(2002, 'pencil')
  ```

##### delete:

  *description*: **`delete(k)`** *it **deletes k** from the tree, also returns **data** of that key, if no such key then raises a **KeyError** exception*
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  ob.delete(1001) # will delete and return (1001, 'apple') from the tree
  # or del ob[1001], but this will not return anything
  ```

##### getData:

  *description*: **`getData(k)`** *it returns **data** of key k, if no such key then raises a **KeyError** exception*
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.getData(1001)) # or print(ob[1001])
  # will print (1001, 'apple') on the console
  ```
  
##### member:

  *description*: **`member(k)`** *it returns **True** if the key **k** is present in the tree*
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.member(1001))
  # will print True on the console
  ```
  
##### select:

  *description*: **`select(rank)`** *it returns **(k, data) having rank (i.e; the inorder (sorted in asc order) position of the key)** as **tuple***
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.select(1))
  # will print (1001, 'apple') on the console
  ```
 
##### rank:

  *description*: **`rank(k)`** *it returns **rank (i,e; the inorder position of the key)** of **k***
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.rank(1001))
  # will print 1 on the console
  ```
  
##### getRootKey:

  *description*: **`getRootKey()`** *it returns **root's (k, data)** as **tuple***
  
  *Time-Complexity*: **`O(1)`** 
  
  ```python
  print(ob.getRootKey())
  # will print (1004, 'orange') on the console
  ```

##### getFarthestKey:

  *description*: **`getFarthestKey()`** *it returns **farthest (i.e; the key which is farthest from the root) (k, data)** as **tuple***
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.getFarthestKey())
  # will print (2002, 'pencil') on the console
  ```
  
##### min:

  *description*: **`min()`** *it returns **min (k, data)** as **tuple***
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.min())
  # will print (1001, 'apple') on the console
  ```
 
##### extractMin:

  *description*: **`extractMin()`** *it returns **min (k, data)** as **tuple**, also it removes it from the tree*
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.extractMin())
  # will print (1001, 'apple') on the console
  ```
  
##### max:

  *description*: **`max()`** *it returns **max (k, data)** as **tuple***
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.max())
  # will print (2002, 'pencil') on the console
  ```
 
##### extractMax:

  *description*: **`extractMax()`** *it returns **max (k, data)** as **tuple**, also it removes it from the tree*
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.extractMax())
  # will print (2002, 'pencil') on the console
  ```
  
##### getKeyCount:

  *description*: **`getKeyCount()`** *it returns the no of keys in the tree*
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.getKeyCount()) # or print(len(ob))
  # will print 6 on the console
  ```

##### isEmpty:

  *description*: **`isEmpty()`** *it returns **True** if the tree is empty, otherwise returns **False***
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.isEmpty())
  # will print False on the console
  ```
  
##### height:

  *description*: **`height()`** *it returns the height of the tree*
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.height())
  # will print 2 on the console
  ```
  
##### inorder:

  *description*: **`inorder()`** *it returns a **generator** that generate **inorder traversal** of the tree*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  for i in ob.inorder():
      print(i)
  # will print
  # (1001, 'apple')
  # (1002, 'banana')
  # (1003, None)
  # (1004, 'orange')
  # (2001, 'pen')
  # (2002, 'pencil')
  ```
  
##### preorder:

  *description*: **`preorder()`** *it returns a **generator** that generate **preorder traversal** of the tree*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  for i in ob.preorder():
      print(i)
  # will print
  # (1004, 'orange')
  # (1002, 'banana')
  # (1001, 'apple')
  # (1003, None)
  # (2001, 'pen')
  # (2002, 'pencil')
  ```
  
##### postorder:

  *description*: **`postorder()`** *it returns a **generator** that generate **postorder traversal** of the tree*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  for i in ob.postorder():
      print(i)
  # will print
  # (1001, 'apple')
  # (1003, None)
  # (1002, 'banana')
  # (2002, 'pencil')
  # (2001, 'pen')
  # (1004, 'orange')
  ```
  
##### printAll:

  *description*: **`printAll(order = 'inorder')`** *it prints the content of the tree in the specified order, if order not recognized it raises a error*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  ob.printAll('inorder')
  # will print
  # (1001, 'apple')
  # (1002, 'banana')
  # (1003, None)
  # (1004, 'orange')
  # (2001, 'pen')
  # (2002, 'pencil')
  ```

##### delAll:

  *description*: **`delAll()`** *it just deletes all the keys from the tree*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  ob.delAll()
  # will empty the tree
  ```
  
##### successor:

  *description*: **`successor(k)`** *it **returns k1, data** as **tuple** where **k1** is the **successor** of **k***
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.successor(1000))
  # will print
  # (1001, 'apple')
  print(ob.successor(1001))
  # will print
  # (1002, 'banana')
  ```

##### predecessor:

  *description*: **`predecessor(k)`** *it **returns k1, data** as **tuple** where **k1** is the **predecessor** of **k***
  
  *Time-Complexity*: **`O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.predecessor(2000))
  # will print
  # (1004, 'orange')
  print(ob.predecessor(1003))
  # will print
  # (1002, 'banana')
  ```

##### __iter__:

  *description*: **`__iter__`** *avl object is **iterable***
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  for i in ob:
      print(i)
  # will print
  # (1001, 'apple')
  # (1002, 'banana')
  # (1003, None)
  # (1004, 'orange')
  # (2001, 'pen')
  # (2002, 'pencil')
  ```
  
##### __repr__:

  *description*: **`__repr__`**
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob)
  # will print
  # avl([(1001, 'apple'), (1002, 'banana'), (1003, None), (1004, 'orange'), (2001, 'pen'), (2002, 'pencil')])
  ```
