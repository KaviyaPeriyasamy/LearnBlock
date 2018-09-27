from __future__ import print_function
import numpy
import time


def slow_down(lbot, duration=0.15, decAdv=-2, decRot=-0.02):
	lbot.adv = lbot.adv + decAdv
	if lbot.adv<0:
		lbot.adv=0

	sR = numpy.sign(lbot.rot)
	lbot.rot = lbot.rot + decRot*sR
	if sR!=numpy.sign(lbot.rot):
		lbot.rot=0
	
	lbot.setRobotSpeed(lbot.adv, lbot.rot)

	if duration!=0:
		time.sleep(duration)
