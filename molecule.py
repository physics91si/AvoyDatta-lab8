# Physics 91SI
# Spring 2017
# Lab 8

import numpy as np
from particle import Particle

class Molecule:

	def __init__(self, position1, position2, mass1, mass2,sprConstant, equiLength):
		self.p1 = Particle(position1, mass1)
		self.p2 = Particle(position2, mass2)

		self.k = sprConstant
		self.LO = equiLength
		
		self.p1.pos = position1
		self.p2.pos = position2

		self.p1.m = mass1
		self.p2.m = mass2

	def get_displ(self):
		dr = self.p1.pos - self.p2.pos
		return dr

	def get_force(self):
		dr = self.get_displ()
		drMag = np.linalg.norm(dr)
		forceMag = (drMag - self.LO) * self.k
		return forceMag * (dr / drMag) 