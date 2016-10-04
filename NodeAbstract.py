from abc import ABCMeta, abstractmethod, abstractproperty

class NodeAbstract:
 
	__metaclass__= ABCMeta

	#properties
	@abstractproperty
	def state(self, stateValue): pass
	
	@abstractproperty
	def parent(self, parentValue): pass

	@abstractproperty
	def operators(self, operatorsValue):pass

	@abstractproperty
	def depth(self, depthValue): pass
	
	@abstractproperty
	def cost(self, costValue): pass

	#methods 
	@abstractmethod
	def expand(self, operators): pass