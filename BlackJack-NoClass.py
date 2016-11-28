#!/usr/bin/python
import os
import random

"""
Future

1 - Add Stats W/Total Games - Need to add to ScoreBoard
2 - Need to only show the first card for dealer on initial deal
3 - Once player switch to Dealer show full hands - can send hide variable code to function with default on
4 - Create a rule function that displays the rules of the game
5 -

"""


def clear_screen():
    """
    Step 0: Write a function that can clear screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    # os.system('clear')
    pass


def shuffle_deck(tdeck):
    """
    Step 1: Shuffle the deck of cards.
    """
    random.shuffle(tdeck)
    return tdeck


def show_hands(house_player, player_hand, ii, lower_hand_value, upper_hand_value):
    """
    Step 2: Show each player hands
    """
    print ('Show %s Hands' % (house_player))
    i = 1
    while i < ii:
        print ('%s hands == %s ' % (house_player, player_hand[i]))
        i += 1
    print ('%s hand values = %d or upper %d ' % (house_player, lower_hand_value, upper_hand_value))
    pass


def get_hand_status(house_player, lower_hand_value, upper_hand_value):
    """
    Step ?:
    """
    status = "pull_or_stop"

    if lower_hand_value == 21 or upper_hand_value == 21:
        status = "winner_%s" % (house_player)
    elif lower_hand_value > 21:
        status = "busted_%s" % (house_player)
    elif upper_hand_value > 21:
        status = "busted_upper_hand_%s" % (house_player)
    elif lower_hand_value < 21:
        status = "pull_or_stop"
    else:
        print ('Error - Invalid Value - per:get_hand_status')
        status = "error"

        quit()

    return status


def discard_hand_logic(h_lower, h_upper):
    if h_upper > 21:
        h_final = h_lower
    else:
        h_final = h_upper

    return h_final


def winner_is(p_best_hand, d_best_hand):
    p_status = "ok"
    d_status = "ok"
    winner_status = "error"

    while True:

        if p_best_hand > 21:
            p_status = "busted_player"
        if d_best_hand > 21:
            d_status = "busted_dealer"

        if p_status == "busted_player" and d_status == "busted_dealer":
            winner_status = "busted"
            break

        if p_status == 'busted_player' and d_status == 'ok':
            winner_status = 'winner_dealer'
            break

        if d_status == 'busted_dealer' and p_status == 'ok':
            winner_status = "winner_player"
            break

        if p_best_hand == 21 and d_best_hand == 21:
            winner_status = "draw"
            break
        if p_best_hand == d_best_hand:
            winner_status = "winner_draw"
            break

        if p_best_hand == 21 and d_best_hand != 21:
            winner_status = "winner_player"
            break
        if d_best_hand == 21 and p_best_hand != 21:
            winner_status = "winner_dealer"
            break

        if p_best_hand > d_best_hand and p_best_hand < 22:
            winner_status = "winner_player"
            break
        else:
            winner_status = "winner_dealer"
            break

    #print ('The Game Status = %s ' % (winner_status))
    return winner_status


def score_board(p_cash, p_wins, p_losses, p_draws, p_status, d_cash, d_wins, d_losses, d_draws, d_status):
    """
    show dealer player scoreboard standings
    """

    p_rank = p_wins /  float((p_losses + p_wins) * .01)
    d_rank = d_wins /  float((d_losses + d_wins) * .01)

    print ('                                  ')
    print ('       |RANKED|WINS  |LOSSES|DRAWS  |CASH   | STATUS')
    print ('-------|------|------|------|-------|-------|---------  ')
    print ('player | %3d  | %3d  | %3d  | %3d   |%3d    |  %1s  ' % (p_rank,p_wins,p_losses,p_draws,p_cash,p_status))
    print ('dealer | %3d  | %3d  | %3d  | %3d   |%3d   |  %1s  ' % (d_rank,d_wins,d_losses,d_draws,d_cash,d_status))
    print ('                                  ')
    pass

def new_score_board(p_cash,d_cash):
    """
    show dealer player scoreboard standings
    """

    print ('                                  ')
    print ('       |RANKED|WINS  |LOSSES|DRAWS  |CASH   | STATUS')
    print ('-------|------|------|------|-------|-------|---------')
    print ('player | 0    | 0    | 0    | 0     |%3d    |  +  ' % (p_cash))
    print ('dealer | 0    | 0    | 0    | 0     |%3d   |  +  ' % (d_cash))
    print ('                                  ')
    pass



#######################################################################################################################
# Welcome To BlackJack
#######################################################################################################################

# Bank Variable

player_cash = 700
player_wins = 0
player_draws = 0
player_losses = 0
dealer_cash = 2500
dealer_wins = 0
dealer_draws = 0
dealer_losses = 0
cash_bids = 25
p_sb_status = "-"
d_sb_status = "-"

games = 0
hit_me = 0
house_player_name = ('player', 'dealer', 'auditor')
player = 0
dealer = 1

clear_screen()
print ("")
print ("                Welcome to BlackJack")
print ("")
new_score_board(player_cash,dealer_cash)
print ("")

#######################################################################################################################
# MAIN GAME
#######################################################################################################################

while True:  # Main -New Game Counter Controller
    player_status_return = "pull_or_stop"
    player_status = " "
    game_status = " "
    switch_player = 0
    switch_hand = 0
    cards = 0
    p_sb_status = "%"
    d_sb_status = "%"

    # BlackJack Deck of 52 Cards
    deck = [['A', 'D', '1'], ['2', 'D', '2'], ['3', 'D', '3'], ['4', 'D', '4'], ['5', 'D', '5'], ['6', 'D', '6'],
            ['7', 'D', '7'], ['8', 'D', '8'], ['9', 'D', '9'], ['10', 'D', '10'], ['J', 'D', '10'], ['Q', 'D', '10'],
            ['K', 'D', '10'], ['A', 'H', '1'], ['2', 'H', '2'], ['3', 'H', '3'], ['4', 'H', '4'], ['5', 'H', '5'],
            ['6', 'H', '6'], ['7', 'H', '7'], ['8', 'H', '8'], ['9', 'H', '9'], ['10', 'H', '10'], ['J', 'H', '10'],
            ['Q', 'H', '10'], ['K', 'H', '10'], ['A', 'C', '1'], ['2', 'C', '2'], ['3', 'C', '3'], ['4', 'C', '4'],
            ['5', 'C', '5'], ['6', 'C', '6'], ['7', 'C', '7'], ['8', 'C', '8'], ['9', 'C', '9'], ['10', 'C', '10'],
            ['J', 'C', '10'], ['Q', 'C', '10'], ['K', 'C', '10'], ['A', 'S', '1'], ['2', 'S', '2'], ['3', 'S', '3'],
            ['4', 'S', '4'], ['5', 'S', '5'], ['6', 'S', '6'], ['7', 'S', '7'], ['8', 'S', '8'], ['9', 'S', '9'],
            ['10', 'S', '10'], ['J', 'S', '10'], ['Q', 'S', '10'], ['K', 'S', '10']]

    # Shuffle the Deck
    shuffle_deck(deck)

    # Initialize Hand - we may can move this above the Main While Loop
    s_player_lower_hand_value = [0, 0]
    s_player_upper_hand_value = [0, 0]
    s_dealer_lower_hand_value = [0, 0]
    s_dealer_upper_hand_value = [0, 0]

    player_hand = ['0']
    dealer_hand = ['0']

    player_status = raw_input("Player's Options (N)ew Game, (Q)uit--> ").upper()

    if games > 0:
        clear_screen()

    if player_status == "Q":  # Quit Game
        break  # End Game
    elif player_status == "N":  # New Game
        print ("........")
    else:
        print ("Ahh what did you say???")
        continue  # Restart the Game

    ###################################################################################################################
    # Auto Deal Cards
    ###################################################################################################################

    ace_counter = 0
    card_pos = 0

    while card_pos < 4:  # Get 4 Initial Cards

        cards = deck[card_pos]

        card_id = cards[0].split()
        card_family = cards[1].split()
        card_value = cards[2].split()

        # print ("Dealing initial  %d of 3 cards = %s " % (card_pos,card_value))

        s_player_upper_hand_value[switch_player] = s_player_upper_hand_value[switch_player] + int(card_value[0])

        if card_id[0] == 'A':
            if ace_counter == 0:
                s_player_upper_hand_value[switch_player] = s_player_lower_hand_value[switch_player] + 11
            else:
                s_player_upper_hand_value[switch_player] = s_player_lower_hand_value[switch_player] + 1
                ace_counter = 1

        s_player_lower_hand_value[switch_player] += int(card_value[0])

        if switch_player == player:
            player_hand.append(deck[card_pos])
            switch_player = dealer
        else:
            dealer_hand.append(deck[card_pos])
            switch_player = player

        card_pos += 1

        continue  # repeat dealing the cards

    ###################################################################################################################
    # Show Initial First Hand
    ###################################################################################################################
    card_pos -= 1

    while True:  # Checking For Winner

        print ""
        # print the full hand
        print ('----------------------------------------')
        show_hands(house_player_name[player], player_hand, len(player_hand), s_player_lower_hand_value[player],
                   s_player_upper_hand_value[player])
        print ('----------------------------------------')
        show_hands(house_player_name[dealer], dealer_hand, len(dealer_hand), s_player_lower_hand_value[dealer],
                   s_player_upper_hand_value[dealer])
        print ('----------------------------------------')

        # show the player and dealer hand
        player_status = get_hand_status(house_player_name[player], s_player_lower_hand_value[player],
                                          s_player_upper_hand_value[player])

        dealer_status = get_hand_status(house_player_name[dealer], s_player_lower_hand_value[dealer],
                                          s_player_upper_hand_value[dealer])

        if switch_player == 99 or switch_player == 97 or switch_player == 96:
            # print ("switch_player = 99 close game and start a new one")
            break

        ###############################################################################################################
        # Validate Initial First Hands
        ###############################################################################################################

        while True:  # Validating Game Fist Hands

            # print "validating game_stutus =  winner - draw - busted - pull"
            if player_status == 'winner_player' and dealer_status == 'winner_dealer':
                print ('We Have a Draw')
                switch_player = 99
                break
            elif player_status == 'winner_player':
                # print ('The Player is the winner!!! ')
                switch_player = 99
                break
            elif dealer_status == 'winner_dealer':
                # print ('The Dealer is the winner!!! ')
                switch_player = 99
                break
            else:
                # print ('Continue Game starting with Player')
                game_status = 'pull_stop'
                break  # Goto Deal or No Deal

        if switch_player == 99 or switch_player == 98:
            break  # Goto The Winner Is

        count5 = 0
        ###############################################################################################################
        # Deal or No Deal
        ###############################################################################################################

        while True:  # Deal or No Deal

            if switch_player == 0:
                print ("")
                player_status = raw_input("PLAYER's Options (P)ull, (S)tay, (Q)uit --> ").upper()
            else:
                print ("")
                player_status = raw_input("DEALER's Options (P)ull, (S)tay, (Q)uit --> ").upper()

            if player_status.upper() == 'Q':  # Please review
                print ("Stopping The Game... This will cost you a cash bid of $ %d " % (cash_bids))
                switch_player = 98  # FEE Charge To Player
                break  #

            if player_status.upper() == 'S':  # Please review
                if switch_player == player:
                    switch_player = dealer
                    print ("")
                    print ('Thank You... The Dealer will challenge your score of %d - %d with %d - %d ' % (
                        s_player_lower_hand_value[player], s_player_upper_hand_value[player],
                        s_player_lower_hand_value[dealer],
                        s_player_upper_hand_value[dealer]))
                    count5 = 0
                    continue
                else:
                    switch_player = 99
                    break  # going to status scoreboard

            elif player_status == "P":
                card_pos += 1
                count5 += 1
                print ('count5 = %d ' % (count5))

            card = deck[card_pos]

            print ('player = hand # %d = Card Properties = %s ' % (card_pos, card))
            card_id = card[0].split()
            card_family = card[1].split()
            card_value = card[2].split()
            s_player_upper_hand_value[switch_player] = s_player_upper_hand_value[switch_player] + int(card_value[0])

            if card_id[0] == 'A':
                if ace_counter == 0:
                    s_player_upper_hand_value[switch_player] = s_player_lower_hand_value[switch_player] + 11
                else:
                    s_player_upper_hand_value[switch_player] = s_player_lower_hand_value[switch_player] + 1
                    ace_counter = 1

            s_player_lower_hand_value[switch_player] += int(card_value[0])
            print ('player_lower_hand_value  = %s or %s' % (
                s_player_lower_hand_value[switch_player], s_player_upper_hand_value[switch_player]))

            if s_player_upper_hand_value[switch_player] > 21:
                s_player_upper_hand_value[switch_player] = s_player_lower_hand_value[switch_player]

            if switch_player == 0:
                player_hand.append(deck[card_pos])
            else:
                dealer_hand.append(deck[card_pos])

            player_status_return = get_hand_status(house_player_name[switch_player],
                                                     s_player_lower_hand_value[switch_player],
                                                     s_player_upper_hand_value[switch_player])

            #########################################################
            # Conditionals For The Win
            #########################################################

            if player_status_return == "busted_player":  # might want to add busted_dealer
                switch_player = 99
                break

            if player_status_return == "busted_dealer":
                switch_player = 99
                break

            if player_status_return == "winner_player":
                switch_player = 99
                break

            if player_status_return == "winner_dealer":
                switch_player = 99
                break

            if player_status_return == "busted_upper_hand_player":
                switch_player = 99
                break

            if player_status_return == "busted_upper_hand_dealer":
                switch_player = 99
                break

            if player_status_return == "pull_or_stop" and count5 == 3:
                check_5card_value = discard_hand_logic(s_player_lower_hand_value[player],
                                                       s_player_upper_hand_value[player])
                if check_5card_value < 22:
                    switch_player = 97  # Player Automatically Wins with 5 cards wo bust
                    game_status = "winner_player"
                    print ("Congrats Player for being the  SUPER 5 CARD WINNER")
                    check_5card_value = 0
                break

            if player_status_return == "pull_or_stop" and count5 == 3:
                check_5card_value = discard_hand_logic(s_player_lower_hand_value[dealer],
                                                       s_player_upper_hand_value[dealer])
                if check_5card_value < 22:
                    switch_player = 96  # Dealer Automatically Wins with 5 cards wo burst
                    game_status = "winner_dealer"
                    print ("Congrats Dealer for being the SUPER 5 CARD WINNER")
                    check_5card_value = 0
                break

            if switch_player == 0:
                show_hands(house_player_name[switch_player], player_hand, len(player_hand),
                           s_player_lower_hand_value[switch_player], s_player_upper_hand_value[switch_player])
            else:
                show_hands(house_player_name[switch_player], dealer_hand, len(dealer_hand),
                           s_player_lower_hand_value[switch_player], s_player_upper_hand_value[switch_player])
            continue
        else:
            print ('Ahh I did not understand your input - Please Try Again')
            continue

            continue  # Stay with Deal or No Deal Loop - put new user to do their hand


            ###########################################################################################################
            # And The Winner Is? - switch_player = 99
            ###########################################################################################################
    games += 1
    if switch_player == 98:
        p_sb_status = "-"
        d_sb_status = "$"
        dealer_cash += cash_bids
        player_cash -= cash_bids
        player_wins = player_wins
        dealer_wins += 1
        player_losses += 1
        dealer_losses = dealer_losses
        print ('The Dealer is the winner!!! ')

    if switch_player == 99:
        clear_screen()
        print ">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<"
        print "The Game Has Ended. Here are the results"
        print ">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<"

        # Get Hand Status
        player_status = get_hand_status(house_player_name[player], s_player_lower_hand_value[player],
                                          s_player_upper_hand_value[player])
        dealer_status = get_hand_status(house_player_name[dealer], s_player_lower_hand_value[dealer],
                                          s_player_upper_hand_value[dealer])

        player_final_hand = discard_hand_logic(s_player_lower_hand_value[player], s_player_upper_hand_value[player])
        dealer_final_hand = discard_hand_logic(s_player_lower_hand_value[dealer], s_player_upper_hand_value[dealer])

        # Print Hand
        print ('----------------------------------------')
        show_hands(house_player_name[player], player_hand, len(player_hand), s_player_lower_hand_value[player],
                   s_player_upper_hand_value[player])
        print ('----------------------------------------')
        show_hands(house_player_name[dealer], dealer_hand, len(dealer_hand), s_player_lower_hand_value[dealer],
                   s_player_upper_hand_value[dealer])
        print ('----------------------------------------')

        print ""
        print ("Player's best hand = %d and Dealer's best hand = %d " % (player_final_hand, dealer_final_hand))
        print ""
        game_status = winner_is(player_final_hand, dealer_final_hand)

    if game_status == "winner_player" or switch_player == 97:
        p_sb_status = "$"
        d_sb_status = "-"
        player_cash += cash_bids
        dealer_cash -= cash_bids
        player_wins += 1
        dealer_wins = dealer_wins
        player_losses = player_losses
        dealer_losses += 1
        print ('The Player is Winner of Game # %d!!! ' % (games))
    if game_status == "winner_dealer" or switch_player == 96:
        p_sb_status = "-"
        d_sb_status = "$"
        dealer_cash += cash_bids
        player_cash -= cash_bids
        player_wins = player_wins
        dealer_wins += 1
        player_losses += 1
        dealer_losses = dealer_losses
        print ('The Dealer is Winner of Game # %d!!! ' % (games))
    if game_status == "draw":
        p_sb_status = "="
        d_sb_status = "="
        print ('We Have A Draw on Game # %d ' % (games))

    print ""
    score_board(player_cash, player_wins, player_losses, player_draws, p_sb_status, dealer_cash, dealer_wins,
                dealer_losses, dealer_draws, d_sb_status)

    print ">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<"
    print ""
    print ">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<"

print ("Session Closed - We look forward to playing you again")
