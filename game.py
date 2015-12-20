'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

from card import *
import player
import deck
import rule
import random
import interface

class game(object):
    '''
    constructor
    playerList, deck, rule, trumpRank, trumpSuit, currentScore, Declarer
    '''
    def __init__(self):
        self.pe = player.Player()   #east player
        self.pn = player.Player()
        self.pw = player.Player()
        self.ws = player.Player()
        self.pe.setNext(self.pn)
        self.pn.setNext(self.pw)
        self.pw.setNext(self.ps)
        self.ps.setNext(self.pe)
        
        self.deck = deck.Deck()
        self.rule = rule.Rule()
        self.inter = interface.Interface()
        self.trumpRank = '2'
        self.trumpSuit = 'NA'
        self.currScore = 0
        self.declarer = None
        
        
    ''' 
    basic functions to set and get variables
    '''
    def setTrumpSuit(self, u):
        pass
        
    def setTrumpRank(self, r):   
        pass
    
    def setDeclarer(self, d):
        pass
    
    
    
    ''' 
    main function
    '''
    
    def on(self):
        self.start()
        self.deal()
        self.end()
    
    '''
    defines the process of dealing
    '''
            
    def deal(self):
       pass
            
            

    def play(self):
        # initiation
        lastWn = self.declarer
        tmpScore = 0

        
        while not self.declarer.getHand().empty():
        # iteration
            lastWnCds = lastWn.pickCards()
            while not self.rule.isLeadingAllowed(lastWnCds):
                
                lastWnCds = lastWn.pickCards()
            otherPlayerHand = [lastWn.getNext().getHand(),lastWn.getNext().getNext().getHand(),lastWn.getNext().getNext().getNext().getHand()]
            lastWnCds = self.rule.checkLeadingCombo(lastWnCds, otherPlayerHand) #not implemented yet
            lastWnCdSet = self.rule.getCardSet(lastWnCds)
            tmpScore = self.rule.getCardSetScore() #not implemented yet
            
            
            # player 1
            p1 = lastWn.getNext()
            p1Cds = p1.pickCards([lastWnCds])
            while not self.rule.isFollowingAllowed(p1Cds): #not implemented yet
                p1Cds = p1.pickCards([lastWnCds])
            p1CdSet = self.rule.getCardSet(p1Cds)
            tmpScore += self.rule.getCardListScore()    
            if self.rule.compareCards(lastWnCdSet, p1CdSet):
                currWn = lastWn
                currWnCdSet = lastWnCdSet
            else:
                currWn = p1
                currWnCdSet = p1CdSet
            
            # player 2
            p2 = p1.getNext()
            p2Cds = p2.pickCards([lastWnCds, p1Cds])
            while not self.rule.isFollowingAllowed(p2Cds): 
                p2Cds = p2.pickCards([lastWnCds, p1Cds])
            p2CdSet = self.rule.getCardSet(p2Cds)
            tmpScore += self.rule.getCardSetScore(p2Cds)
            if not self.rule.compareCards(currWnCdSet, p2CdSet):
                currWn = p2
                currWnCdSet = p2CdSet
                
            # player 3
            p3 = p2.getNext()
            p3Cds = p3.pickCards([lastWnCds, p1Cds, p2Cds])
            while not self.rule.isFollowingAllowed(p3Cds): 
                p3Cds = p3.pickCards([lastWnCds, p1Cds, p2Cds])
            p3CdSet = self.rule.getCardSet(p3Cds)
            tmpScore += self.rule.getCardSetScore(p3Cds)
            if not self.rule.compareCards(currWnCdSet, p3CdSet):
                currWn = p3
                currWnCdSet = p3CdSet
            
            if currWn == self.declarer or currWn == self.declarer.getNext().getNext():
                self.currScore += tmpScore
            
            lastWn = currWn
        
        if currWn == self.declarer or currWn == self.declarer.getNext().getNext():
            tmpScore = self.rule.getCardListScore()
            self.currScore += tmpScore
            
                    
        
    
    '''
    set the trump rank, declarer, opponents of the next game
    
    '''
    def end(self, opnPnt):
        pass
    
     
            
            
            
    
        
    
