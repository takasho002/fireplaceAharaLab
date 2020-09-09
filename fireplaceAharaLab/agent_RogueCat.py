# agent_RogueCat.py

import random

from utils import ExceptionPlay, Candidate, executeAction, getCandidates
from agent_Standard import postAction

def printAllRogueCards():
	    
	pass

def RogueCatAI(game: Game, option=[], debugLog=False):
	while True:
		myCandidate = getCandidates(game)
		if len(myCandidate)>0:
			myChoice = random.choice(myCandidate)
			executeAction(thisgame, myChoice, debugLog=debugLog)
			postAction(player)
		else:
			return
