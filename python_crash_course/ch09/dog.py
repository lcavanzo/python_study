class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age

	
	def sit(self):
		"""Simulates a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")


	def roll_over(self):
		"""simulates rolling in response to a command"""
		print(f"{self.name} rolled over""")
