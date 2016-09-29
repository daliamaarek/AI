from abc import ABCMeta, abstractmethod, abstractproperty


class Problem:
	__metaclass__= ABCMeta

	@abstractproperty
	def operators(self): pass

	@abstractproperty
	def initialState(self): pass
	
	@abstractproperty
	def goalTest(self): pass
	
	@abstractproperty
	def pathCost(self): pass
 
	