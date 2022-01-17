#How to create the deck of cards
#How to shuffle the deck
#Getting player names and strategies from console
#Dealing the cards to the players
#Calculating total cards value for each player
#Check for winner using various strategies


    #Check the player_score
        #If player_score < 17, set PLAYER_STATUS = HIT 
        #If player_score >= 17 and <= 21, PLAYER_STATUS = STICK
        #Else set PLAYER_STATUS = BURST
    
    #Check each players status and act on it
        #If PLAYER_STATUS = HIT, add to hit players and hand another card
        #If PLAYER_STATUS = STICK, add to sticked players
        #If PLAYER_STATUS = Burst, add to bursted players

    #Check Set<STICK> 
        #If >= 1, GAME_STATUS = Ended
        #else check Set<Burst>
            #if == 3, GAME_STATUS = Ended
            #else GAME_STATUS = In_motion

#Assign Cards, Assign status, check status, assignCardsDue