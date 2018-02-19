class _avl_node:
	def __init__(self, k, data):
		self._k = k
		self._data = data
		self._left = self._right = None
		self._height = 0
		self._nod_cnt = 1
		self._min = self._max = self
		self._next = self._prev = None

class avl:
	def __init__(self):
		'''initialize a empty avl tree object
		'''
		self._root = None
	
	def __repr__(self):
		A = []
		for i in self:
			A.append(i)
		return 'avl({})'.format(A)
		
	def __iter__(self):
		return self.inorder()
	
	@property
	def key_set(self):
		A = []
		for i in self:
			A.append(i[0])
		return A
		
	@property
	def key_value_set(self):
		A = []
		for i in self:
			A.append(i)
		return A
		
	def __getitem__(self, k):
		return self.getData(k)
		
	def __contains__(self, x):
		return self.member(x)
		
	def __setitem__(self, k, data):
		self.insert(k, data)
		
	def __delitem__(self, k):
		self.delete(k)
	
	def __len__(self):
		return self.getKeyCount()
	
	def __del__(self):
		self.delAll()
		del self._root
		
	def isEmpty(self):
		'''checks if the tree is empty or not
		'''
		return self._root == None
		
	def getKeyCount(self):
		'''returns the no of keys in the tree
		'''
		return self.__getNodeCount(self._root)
		
	def height(self):
		'''returns the height of the tree
		'''
		return self.__getHeight(self._root)
	
	def __getHeight(self, x):
		if x:
			return x._height
		return -1
		
	def __getNodeCount(self, x):
		if x:
			return x._nod_cnt
		return 0
		
	def __getBalance(self, x):
		return self.__getHeight(x._left) - self.__getHeight(x._right)
		
	def __updateAug(self, x):
		x._height = 1 + max(self.__getHeight(x._left), self.__getHeight(x._right))
		x._nod_cnt = 1 + self.__getNodeCount(x._left) + self.__getNodeCount(x._right)
		min_left, min_right = self.__minUtil(x._left)[0], self.__minUtil(x._right)[0]
		if x._k <= min_left and x._k <= min_right:
			x._min = x
		elif min_left <= x._k and min_left <= min_right:
			x._min = x._left._min
		else:
			x._min = x._right._min
		max_left, max_right = self.__maxUtil(x._left)[0], self.__maxUtil(x._right)[0]
		if x._k >= max_left and x._k >= max_right:
			x._max = x
		elif max_left >= x._k and max_left >= max_right:
			x._max = x._left._max
		else:
			x._max = x._right._max
		
	def __leftRotate(self, x):
		y = x._right
		z = y._left

		x._right = z
		y._left = x
		
		self.__updateAug(x)
		self.__updateAug(y)
		
		return y
				
	def __rightRotate(self, x):
		y = x._left
		z = y._right
		
		x._left = z
		y._right = x
		
		self.__updateAug(x)
		self.__updateAug(y)
		
		return y
		
	def __rebalance(self, root, t = None):
		self.__updateAug(root)
		b1 = self.__getBalance(root)
		if b1 > 1:
			#left heavy
			b2 = self.__getBalance(root._left)
			if b2 >= 0:
				#left left heavy
				return self.__rightRotate(root), t
			else:
				#left right heavy, so lets make it left left heavy
				root._left = self.__leftRotate(root._left)
				return self.__rightRotate(root), t
		elif b1 < -1:
			#right heavy
			b2 = self.__getBalance(root._right)
			if b2 <= 0:
				#right right heavy
				return self.__leftRotate(root), t
			else:
				#right left heavy, so lets make it right right heavy
				root._right = self.__rightRotate(root._right)
				return self.__leftRotate(root), t
		return root, t
		
	def __minUtil(self, x):
		return (x._min._k, x._min._data) if x and x._min else (float('inf'), None)
		
	def min(self):
		'''returns the min_key, data as tuple, if no such key then returns None
		'''
		if not self.isEmpty():
			return self.__minUtil(self._root)
			
	def __maxUtil(self, x):
		return (x._max._k, x._max._data) if x and x._max else (-float('inf'), None)
			
	def max(self):
		'''returns the max_key, data as tuple, if no such key then returns None
		'''
		if not self.isEmpty():
			return self.__maxUtil(self._root)
		
	def __extractMinUtil(self, root):
		if root._left != None:
			root._left, minn = self.__extractMinUtil(root._left)
			return self.__rebalance(root, minn)
		else:
			if root._next:
				root._next._prev = None
				root._next = None
			t = root._right
			root._right = None
			return t, root
	
	def extractMin(self):
		'''returns the min_key, data as tuple, also remove it from the tree, if no such key then returns None
		'''
		if not self.isEmpty():
			self._root, minn = self.__extractMinUtil(self._root)
			return minn._k, minn._data
	
	def __extractMaxUtil(self, root):
		if root._right != None:
			root._right, maxx = self.__extractMaxUtil(root._right)
			return self.__rebalance(root, maxx)
		else:
			if root._prev:
				root._prev._next = None
				root._prev = None
			t = root._left
			root._left = None
			return t, root
			
	def extractMax(self):
		'''returns the max_key, data as tuple, also remove it from the tree, if no such key then returns None
		'''
		if not self.isEmpty():
			self._root, maxx = self.__extractMaxUtil(self._root)
			return maxx._k, maxx._data
	
	def __insertUtil(self, k, data, root):
		if root == None:
			t = _avl_node(k, data)
			return t, t
		
		if k < root._k:
			root._left, t = self.__insertUtil(k, data, root._left)
			if not t._next:
				t._next = root
				t._prev = root._prev
				if root._prev:
					root._prev._next = t
				root._prev = t
		elif k > root._k:
			root._right, t = self.__insertUtil(k, data, root._right)
			if not t._prev:
				t._prev = root
				t._next = root._next
				if root._next:
					root._next._prev = t
				root._next = t
		else:
			root._data = data
			return root, root
			
		return self.__rebalance(root, t)
		
	def insert(self, k, data = None):
		'''insert k, data in the tree
		'''
		if isinstance(k, (int, float)):
			self._root, t = self.__insertUtil(k, data, self._root)
		else:
			raise TypeError('key can only be integers or floating point number')
		
	def __deleteUtil(self, k, root):
		if root == None:
			return None, None
		tmp = None
		if k < root._k:
			root._left, tmp = self.__deleteUtil(k, root._left)
		elif k > root._k:
			root._right, tmp = self.__deleteUtil(k, root._right)
		else:
			tmp = root._k, root._data
			p, q = root._prev, root._next
			root._next, root._prev = None, None
			if p:
				p._next = q
			if q:
				q._prev = p
			if root._left == None:
				t = root._right
				del root
				return t, tmp
			elif root._right == None:
				t = root._left
				del root
				return t, tmp
			else:
				root._left, t = self.__extractMaxUtil(root._left)
				t._right = root._right
				del root
				return t, tmp
		
		return self.__rebalance(root, tmp)
		
	def delete(self, k):
		'''deletes key k from the tree, also returns data of that key, if no such key then raises a KeyError exception
		'''
		if isinstance(k, (int, float)):
			self._root, t = self.__deleteUtil(k, self._root)
			if t:
				return t[1]
			else:
				raise KeyError('key {} does\'nt exist in the tree'.format(k))
		else:
			raise TypeError('key can only be integers or floating point number')
			
	def __getDataUtil(self, k, root):
		if root == None:
			return None
		if k < root._k:
			return self.__getDataUtil(k, root._left)
		elif k > root._k:
			return self.__getDataUtil(k, root._right)
		else:
			return root._k, root._data
		
	def getData(self, k):
		'''returns data associated with the key k in the tree, if no such key then raises a KeyError exception
		'''
		if isinstance(k, (int, float)):
			t = self.__getDataUtil(k, self._root)
			if t:
				return t[1]
			else:
				raise KeyError('key {} does\'nt exist in the tree'.format(k))
		else:
			raise TypeError('key can only be integers or floating point number')
			
	def member(self, k):
		'''checks if key k is in the tree or not
		'''
		try:
			self.getData(k)
			return True
		except KeyError:
			return False
				
	def __getFarthestKey(self, root):
		if root:
			lh = self.__getHeight(root._left)
			rh = self.__getHeight(root._right)
			if lh == -1 and rh == -1:
				return root._k, root._data
			elif lh > rh:
				return self.__getFarthestKey(root._left)
			else:
				return self.__getFarthestKey(root._right)
			
	def getFarthestKey(self):
		'''returns the farthest key from the root and its associated data, if the tree is empty returns None
		'''
		if not self.isEmpty():
			return self.__getFarthestKey(self._root)
			
	def getRootKey(self):
		'''returns the root key and its associated data, if tree is empty returns None
		'''
		if not self.isEmpty():
			return self._root._k, self._root._data
			
	def __selectUtil(self, root, rank):
		if root:
			t = self.__getNodeCount(root._left) + 1
			if rank == t:
				return root._k, root._data
			elif rank < t:
				return self.__selectUtil(root._left, rank)
			else:
				return self.__selectUtil(root._right, rank - t)
		
	def select(self, rank):
		'''selects a key having the specified rank and returns it and its associated data, it no such key then returns None
		'''
		if isinstance(rank, int):
			if not self.isEmpty():
				return self.__selectUtil(self._root, rank)
		else:
			raise TypeError('rank can only be integers')
			
	def __rankUtil(self, root, k, rank):
		if root:
			t = self.__getNodeCount(root._left) + 1
			if k == root._k:
				return rank + t
			elif k < root._k:
				return self.__rankUtil(root._left, k, rank)
			else:
				return self.__rankUtil(root._right, k, rank + t)
	
	def rank(self, k):
		'''returns the rank of the key k, if no such key then returns None
		'''
		if isinstance(k, (int, float)):
			if not self.isEmpty():
				return self.__rankUtil(self._root, k, 0)
		else:
			raise TypeError('key can only be integers or floating point number')
		
	def __preorderUtil(self, root):
		if root != None:
			yield root._k, root._data
			yield from self.__preorderUtil(root._left)
			yield from self.__preorderUtil(root._right)
				
	def preorder(self):
		'''returns a generator the yields postorder traversal of tree
		'''
		return self.__preorderUtil(self._root)
	
	def inorder(self):
		'''returns a generator the yields inorder traversal of tree
		'''
		p = self._root._min if self._root else None
		while p:
			yield p._k, p._data
			p = p._next
	
	def __postorderUtil(self, root):
		if root != None:
			yield from self.__postorderUtil(root._left)
			yield from self.__postorderUtil(root._right)
			yield root._k, root._data
			
	def postorder(self):
		'''returns a generator the yields postorder traversal of tree
		'''
		return self.__postorderUtil(self._root)
		
	def getAll(self, desc = False):
		'''returns a generator the yields inorder traversal (either desc or asc) of tree
		'''
		if desc:
			return reversed(self)
		return self
		
	def printAll(self, order = 'inorder'):
		'''print the content of tree on console
		'''
		if order.lower() == 'inorder':
			order = self.inorder
		elif order.lower() == 'preorder':
			order = self.preorder
		elif order.lower() == 'postorder':
			order = self.postorder
		else:
			raise Exception('Order not recognized, should be either inorder, preorder or postorder')
		for i in order():
				print(i)
	
	def delAll(self):
		'''empties the tree
		'''
		p = self._root._min if self._root else None
		while p:
			q = p._next
			del p
			p = q
		self._root = None
				
	def __successorUtil(self, k, root):
		if root == None:
			return False, None
		t = False, None
		if k < root._k:
			t = self.__successorUtil(k, root._left)
		elif k > root._k:
			t = self.__successorUtil(k, root._right)
		else:
			return True, root._next
		if t[1] == None and root._k > k:
			return False, root
		return t
						
	def successor(self, k):
		'''returns k1, data as tuple where k1 is the successor k, if no such key then returns None
		'''
		if isinstance(k, (int, float)):
			if not self.isEmpty():
				found, succ = self.__successorUtil(k, self._root)
				return (succ._k, succ._data) if succ else succ
		else:
			raise TypeError('key can only be integers or floating point number')
			
	def __predecessorUtil(self, k, root):
		if root == None:
			return False, None
		t = False, None
		if k < root._k:
			t = self.__predecessorUtil(k, root._left)
		elif k > root._k:
			t = self.__predecessorUtil(k, root._right)
		else:
			return True, root._prev
		if t[1] == None and root._k < k:
			return False, root
		return t
			
	def predecessor(self, k):
		'''returns k1, data as tuple where k1 is the predecessor k, if no such key then returns None
		'''
		if isinstance(k, (int, float)):
			if not self.isEmpty():
				found, pred = self.__predecessorUtil(k, self._root)
				return (pred._k, pred._data) if pred else pred
		else:
			raise TypeError('key can only be integers or floating point number')
