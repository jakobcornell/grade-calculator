class DataError(Exception):
	pass

class Assignment:
	def __init__(self, earned, possible, name = None, weight = 1):
		if earned < 0 or possible < 0:
			raise DataError("Point values cannot be negative")
		if weight < 0:
			raise DataError("Weights cannot be negative")
		self.name = name
		self.earned = earned
		self.possible = possible
		self.weight = weight
	def score(self):
		if self.possible > 0:
			return self.earned / self.possible
		else:
			return None

class Category:
	def __init__(self, weight, name = None, weighting = False):
		if weight < 0:
			raise DataError("Weights cannot be negative")
		self.name = name
		self.weight = weight
		self.assignments = []
		self.weighting = weighting
	def score(self):
		if self.weighting:
			scores = (assn.score() for assn in self.assignments if assn.score() is not None)
			weights = list(assn.weight for assn in self.assignments if assn.score() is not None)
			total_weight = sum(weights)
			scorables = list(zip(scores, weights))
			if scorables and total_weight:
				return sum(score * weight for (score, weight) in scorables) / total_weight
			else:
				return None
		else:
			earned = sum(assignment.earned for assignment in self.assignments)
			possible = sum(assignment.possible for assignment in self.assignments)
			return earned / possible if possible > 0 else None

class Course:
	def __init__(self, name = None):
		self.name = name
		self.categories = []
	def score(self):
		# somewhat ugly comprehensions to avoid duplicate calls to Category.score
		scorables = ((cat.score(), cat.weight) for cat in self.categories)
		scorables = list(filter(lambda entry: entry[0] is not None, scorables))
		total_weight = sum(weight for (score, weight) in scorables)
		if scorables and total_weight:
			return sum(score * weight for (score, weight) in scorables) / total_weight
		else:
			return None
