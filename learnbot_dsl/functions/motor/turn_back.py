from __future__ import division
import time, math

def turn_back(lbot, params=None, verbose=False):
	lbot.setRobotSpeed(lbot.adv, math.pi)
	time.sleep(1)
	lbot.setRobotSpeed(0, 0)
	if verbose:
		print('~ Learnbot has turned back')