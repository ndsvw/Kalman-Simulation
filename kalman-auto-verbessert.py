#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
from copy import deepcopy
from random import gauss

def my_round(x, i):
  if x == 0:
    return "0"
  else:
    return str(round(x,i))
    

def matrixToTex(index, x1, u, P1, z, K, x2, P2):
  print(str(index) + " & $\\begin{pmatrix}")

  print(my_round(u[0],1) + "\\" + "\\")
  print(my_round(u[1],1))
  
  print("\end{pmatrix}$ & $\\begin{pmatrix}")
  x1 = x1.tolist()
  for i in range(len(x1)):
    zeile = x1[i]
    s = ""
    for j in range(len(zeile)):
      if j < len(zeile)-1:
        s += my_round(zeile[j],1) + " & "
      else:
        s += my_round(zeile[j],1)
    if i < len(x1)-1:
      s += "\\\\"
    print(s)
  print("\end{pmatrix}$ & $\\begin{pmatrix}")
  P1 = P1.tolist()
  for i in range(len(P1)):
    zeile = P1[i]
    s = ""
    for j in range(len(zeile)):
      if j < len(zeile)-1:
        s += my_round(zeile[j],4) + " & "
      else:
        s += my_round(zeile[j],4)
    if i < len(x1)-1:
      s += "\\\\"
    print(s)
  print("\end{pmatrix}$ & $\\begin{pmatrix}")

  print(my_round(z[0],1) + "\\" + "\\")
  print(my_round(z[1],1))

  print("\end{pmatrix}$ & $\\begin{pmatrix}")
  K = K.tolist()
  for i in range(len(K)):
    zeile = K[i]
    s = ""
    for j in range(len(zeile)):
      if j < len(zeile)-1:
        s += my_round(zeile[j],4) + " & "
      else:
        s += my_round(zeile[j],4)
    if i < len(x1)-1:
      s += "\\\\"
    print(s)
  print("\end{pmatrix}$ & $\\begin{pmatrix}")
  x2 = x2.tolist()
  for i in range(len(x2)):
    zeile = x2[i]
    s = ""
    for j in range(len(zeile)):
      if j < len(zeile)-1:
        s += my_round(zeile[j],1) + " & "
      else:
        s += my_round(zeile[j],1)
    if i < len(x1)-1:
      s += "\\\\"
    print(s)
  print("\end{pmatrix}$ & $\\begin{pmatrix}")
  P2 = P2.tolist()
  for i in range(len(P2)):
    zeile = P2[i]
    s = ""
    for j in range(len(zeile)):
      if j < len(zeile)-1:
        s += my_round(zeile[j],4) + " & "
      else:
        s += my_round(zeile[j],4)
    if i < len(x1)-1:
      s += "\\\\"
    print(s)
  print("\end{pmatrix}$\\\\")


class Log:
  x = []
  P = []
  K = []
log = Log()

#gemessene Geschwindigkeit
u = [(89.7, 53.9), (88.2, 54.4), (88.1, 54.3), (86.5, 55.5), (85.8, 58.4), (84.7, 64.7), (82.1, 70.4), (77.1, 78.4), (73.6, 81.7), (69.6, 85.9), (67.7, 86.4), (72.7, 82.6), (76.1, 79.2), (77.9, 71.4), (76.0, 62.4), (80.0, 51.2), (80.7, 42.5), (79.4, 32.8), (81.7, 25.7), (80.4, 20.2), (80.5, 18.2), (80.2, 20.8), (81.7, 22.5)]

deltaT = 1/float(3.6)


#Koordinaten (GPS) (Abweichungen sind sogar normalverteilt)

###
### Berechnung normalverteilter Werte für y:
STANDARDABWEICHUNG = 5.2
pos_x, pos_y = 0, 0
verlauf_x, verlauf_y = [], []
gauss_x, gauss_y = [], []
for t in u:
  pos_x = pos_x + deltaT * t[0]
  pos_y = pos_y + deltaT * t[1]
  verlauf_x.append(pos_x)
  verlauf_y.append(pos_y)
  gauss_x.append(gauss(pos_x, STANDARDABWEICHUNG))
  gauss_y.append(gauss(pos_y, STANDARDABWEICHUNG))

# y = []
# for i in range(len(gauss_x)):
#   y.append((gauss_x[i], gauss_y[i]))
# print(y)

# GPS-Messwerte:
#y = [(23.68293541291074, 14.839576864778971), (54.420390848061, 36.60816065373174), (75.15504596177817, 47.54551357854399), (101.83021651190946, 62.263496783741346), (119.01733708583718, 74.29687300486532), (143.76091699412473, 93.53380938980047), (169.5312609513003, 116.43251102760969), (195.8531399041626, 136.0485241257699), (209.18426343692073, 159.82997141662355), (233.5610666610375, 169.6320220640272), (245.02106529087115, 204.6132238078705), (265.7957064340591, 229.91366908487043), (284.08130826950173, 257.65926452391733), (303.29277560336755, 269.30653324294406), (335.3944725314843, 283.14226908844955), (362.57040836194886, 310.43664150220684), (367.8816363218172, 310.74852623289615), (393.7199387176737, 330.77448509829446), (410.64093950177073, 327.381714997638), (439.67988671856, 333.65335374313185), (468.3609671284073, 346.0445210380948), (488.79460468072597, 348.204346630893), (515.9616824110924, 354.19731449345704)]
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

  # Zur Erzeugung einer Latex-Tabelle
  # if i in [0,1,2,11,12,21,22]:
  #   matrixToTex(i+1, x_tmp, u[i], P_tmp, y[i], K, x, P)
  
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

def test():
  plt.xlabel('Position x')
  plt.ylabel('Position y')
  a, = plt.plot([e[0] for e in log.x], [e[2] for e in log.x], label='Kalman-Filter', color='#000000')
  b, = plt.plot([e[0] for e in y], [e[1] for e in y], label='Messung', marker=".", color='#999999', linewidth='0.5')
  plt.legend(handles=[a,b])
  plt.scatter(300,300, color='#FFFFFF')
  plt.show()

gain()
main()
test()
