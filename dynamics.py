#!/usr/bin/python3

# Physics 91SI
# molecule 2017
# Lab 8

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
import random
from particle import Particle 
from molecule import Molecule

# TODO: Implement this function
def init_molecule():
    m1 = 14
    m2 = 14
    x1 = random.randint(0, 1)
    y1 = random.randint(0, 1)
    x2 = random.randint(0, 1)
    y2 = random.randint(0, 1)

    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])
    k = 5
    LO = 0.5

    mol = Molecule(p1, p2, m1, m2, k, LO)

    return mol

# TODO: Implement this function
def time_step(dt, mol):
    """Sets new positions and velocities of the particles attached to mol"""

    acc1 = mol.get_force() / mol.p1.m
    acc2 = -mol.get_force() / mol.p2.m

    vPrev1 = mol.p1.vel - acc1 * dt / 2
    vPrev2 = mol.p2.vel - acc2 * dt / 2
   
    vNext1 = vPrev1 + acc1 * dt
    vNext2 = vPrev2 + acc2 * dt

    mol.p1.vel = vNext1
    mol.p2.vel = vNext2

    mol.p1.pos = mol.p1.pos + vNext1 * dt
    mol.p2.pos = mol.p2.pos + vNext2 * dt



#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    ax.clear()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=True)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = 0.1
    run_dynamics(n, dt)
