from abc import ABCMeta, abstractmethod, abstractproperty

class NodeAbstract:
 
	__metaclass__= ABCMeta

	#properties
	@abstractproperty
	def state(self): pass
	
	@abstractproperty
	def parent(self): pass

	@abstractproperty
	def operators(self):pass

	@abstractproperty
	def depth(self): pass
	
	@abstractproperty
	def cost(self): pass

	#methods 
	@abstractmethod
	def expand(self, operators): pass  