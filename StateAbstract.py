from abc import ABCMeta, abstractmethod, abstractproperty


class State():
	__metaclass__= ABCMeta

	@abstractproperty
	def cell(self): pass

	@abstractproperty
	def direction(self): pass

	@abstractproperty
	def matrix(self): pass #Or Bitmask 

	