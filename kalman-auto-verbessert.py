#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
from copy import deepcopy
from random import gauss

class Log:
  x = []
  P = []
  K = []
log = Log()

#gemessene Geschwindigkeit
u = [(89.7, 53.9), (88.2, 54.4), (88.1, 54.3), (86.5, 55.5), (85.8, 58.4), (84.7, 64.7), (82.1, 70.4), (77.1, 78.4), (73.6, 81.7), (69.6, 85.9), (67.7, 86.4), (72.7, 82.6), (76.1, 79.2), (77.9, 71.4), (76.0, 62.4), (80.0, 51.2), (80.7, 42.5), (79.4, 32.8), (81.7, 25.7), (80.4, 20.2), (80.5, 18.2), (80.2, 20.8), (81.7, 22.5)]

deltaT = 1/float(3.6)

#Koordinaten (GPS) (Abweichungen sind normalverteilt):
y = [(30.184526727308665, 5.904739599382479), (48.89354230750558, 23.360419739718054), (73.13809182449934, 36.425261693221216), (96.01551936202007, 66.81245153667231), (122.69590647716281, 86.75145802718124), (152.68905761175094, 95.54687120014444), (166.48962724404112, 112.44815209868109), (190.35134360736728, 138.53272632066063), (214.37532399243042, 168.41478935536955), (226.0372062060824, 175.06952366563766), (249.06944037903227, 191.9533617772272), (265.0201747625014, 231.96550640383026), (286.13169452950854, 245.23682796277856), (312.1982624230246, 276.5117680398556), (322.9086285113537, 292.3994262916528), (352.31449099097915, 308.13442138728544), (374.14643137965885, 322.2384113027568), (402.99222039844216, 330.6566119238054), (416.9155705929058, 331.55157363052035), (447.49989113523736, 321.3459784421296), (473.16230517209794, 343.11508259887967), (488.70746536203, 348.66174819862664), (511.2407093847164, 352.35136172503496)]

A = numpy.matrix([ 
  [1,0,0,0], 
  [0,0,0,0], 
  [0,0,1,0],
  [0,0,0,0] 
])

B = numpy.matrix([
  [deltaT,0],
  [1,0],
  [0,deltaT],
  [0,1]
])

H = numpy.matrix([
  [1,0,0,0],
  [0,0,1,0]
])

x = numpy.matrix([ 
  [0], 
  [90],
  [0],
  [50]
])

P = numpy.matrix([
  [10,0,0,0],
  [0,0,0,0],
  [0,0,10,0],
  [0,0,0,0]
])

Q = numpy.matrix([
  [.4,0,0,0],
  [0,0,0,0],
  [0,0,.4,0],
  [0,0,0,0]
])

R = numpy.matrix([
  [4, 0],
  [0, 4]
])

for i in range(len(y)):
  #Kalman-Gleichungen 1 & 2:
  x = A * x + B * numpy.matrix([ [u[i][0]], [u[i][1]] ])
  P = A * P * numpy.transpose(A) + Q

  #
  x_tmp = deepcopy(x)
  P_tmp = deepcopy(P)
  #

  #Kalman-Gleichungen 3, 4 & 5
  K = P * numpy.transpose(H) * numpy.linalg.pinv(H * P * numpy.transpose(H) + R)
  x = x + K * (numpy.matrix([ [y[i][0]], [y[i][1]] ]) - H * x)
  P = (numpy.eye(len(K*H))-K*H)*P

  #
  log.x.append((x[0].A[0][0], x[1].A[0][0], x[2].A[0][0], x[3].A[0][0]))
  log.P.append((P[0].A[0][0], P[1].A[0][1], P[2].A[0][2], P[3].A[0][2]))
  log.K.append(K.tolist())
  #
  
def gain():
  plt.xlabel('k')
  plt.ylabel('Gain-Wert')
  plt.plot([e[0][0] for e in log.K], color='#000000')
  plt.show()
  
def main():
  plt.xlabel('time')

  _x, = plt.plot([e[0] for e in log.x], label='Kalman-Filter x (oben)', color='#000000')
  _y, = plt.plot([e[2] for e in log.x], label='Kalman-Filter y (unten)', color='#000000')

  _mess_x, = plt.plot([e[0] for e in y], label='Messung x (oben)', marker=".", color='#999999', linewidth='0.5')
  _mess_y, = plt.plot([e[1] for e in y], label='Messung y (unten)', marker=".", color='#999999', linewidth='0.5')

  plt.legend(handles=[_mess_x, _x, _mess_y, _y])
  plt.show()

def strecke():
  plt.xlabel('Position x')
  plt.ylabel('Position y')
  a, = plt.plot([e[0] for e in log.x], [e[2] for e in log.x], label='Kalman-Filter', color='#000000')
  b, = plt.plot([e[0] for e in y], [e[1] for e in y], label='Messung', marker=".", color='#999999', linewidth='0.5')
  plt.legend(handles=[a,b])
  plt.scatter(300,300, color='#FFFFFF')
  plt.show()

gain()
main()
strecke()
