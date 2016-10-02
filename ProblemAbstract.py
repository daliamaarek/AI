from abc import ABCMeta, abstractmethod, abstractproperty

class ProblemAbstract:
	__metaclass__= ABCMeta

	@abstractproperty
	def operators(self, operators): pass

	@abstractproperty
	def initialState(self, initial_state): pass
		
	@abstractproperty
	def pathCost(self, path_cost): pass

	def __init__(self, operators, initial_state, goal_test, path_cost): pass

	@abstractmethod
	def goalTest(self): pass