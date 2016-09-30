from abc import ABCMeta, abstractmethod, abstractproperty


class State():
	__metaclass__= ABCMeta
	
	@abstractproperty
	def row(self): pass

	@abstractproperty
	def column(self): pass

	@abstractproperty
	def direction(self): pass

	@abstractproperty
	def matrix(self): pass #Or Bitmask 

	