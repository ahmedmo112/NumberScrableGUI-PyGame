# Number Scrabble game
# Start with choosing numbers from 1 to 9 once 
# and the player who reach sum of 15 first win
# Author: Ahmed Mohamed Hany
# Date: 25-2-2022
# Version: 1.0

#import libraries
import pygame as pg
import sys

# initializing the constructor
pg.init()

# screen resolution
res = (720,600)

player1 = [] # list of player1 number that choose
player2 = [] # list of player2 number that choose
player= 1  #set the  player to the first 
listofnum = [1,2,3,4,5,6,7,8,9,10] #list of number that still untaken



# opens up a welcome window
welcomescreen = pg.display.set_mode(res)
# opens up a game window
gamescreen = pg.display.set_mode(res)
# window caption
pg.display.set_caption('Number Scrabble')

welcomeUI = pg.image.load(f"{sys.path[0]}/assets/ui.png")
gameUI = pg.image.load(f"{sys.path[0]}/assets/gameui.png")

clock = pg.time.Clock() #will use it leater for framerate

# colors
white_color = (255,255,255)
color_light = (167, 147, 172)
title_color = (170, 0, 136)



# defining a fonts
smallfont = pg.font.SysFont('Corbel',26)
midfont = pg.font.SysFont('Corbel',35)
winnerfont = pg.font.Font(f'{sys.path[0]}/assets/Brushot-Bold.ttf',70)


#start game button 
def startButton():
    btn= pg.Rect(231.476, 311.561, 260.615, 70.514)
    return btn

#play again button
def playAgainButtons(posx,posy,text):
    btn= pg.Rect(posx, posy, 150, 50)
    pg.draw.rect(welcomescreen,(51, 0, 128), btn)#drew Rectangle to display on UI
    
    # superimposing the text onto our button
    tx =midfont.render(f"{text}" , True , white_color)
    welcomescreen.blit(tx , (posx+15,posy+12))
    
    return btn

# number buttons to choose from them 
def numButton(posx,posy,text):
    global listofnum
    #check if the number taken or not
    if text in listofnum:
        color = title_color
    else:
        color = color_light
    btn= pg.Rect(posx, posy, 40, 40)
    pg.draw.rect(welcomescreen,color, btn)#drew Rectangle to display on UI
    
    # superimposing the text onto our button
    tx =smallfont.render(f"{text}" , True , white_color)
    welcomescreen.blit(tx , (posx+15,posy+10))
    return btn 



# the chosen number that the player choose
def chosenNumber(posx,posy,text):
    btn= pg.Rect(posx, posy, 30, 30)
    pg.draw.rect(welcomescreen,title_color, btn)#drew Rectangle to display on UI
    
    # superimposing the text onto our button
    tx =smallfont.render(f"{text}" , True , white_color)
    welcomescreen.blit(tx , (posx+10,posy+7.5))
    
    return btn 
    

# check the sum of 15 
def checkthesumofthree(player):
    if len(player)==4:
        #check the list number of player if the sum of 3 is 15 or not 
        if (player[0]+player[1]+player[2]==15) or (player[0]+player[1]+player[3]==15) or (player[3]+player[1]+player[2]==15) or (player[0]+player[2]+player[3]==15):
            return True 
    elif len(player)==3:
        if player[0]+player[1]+player[2]==15:
            return True

def checkwin():  # check if the player win
    #drew
    if len(player1) ==4 and len(player2) == 4 and checkthesumofthree(player1) == checkthesumofthree(player2):
        print("draw")
        return  'draw' 
    #player 1 win
    elif checkthesumofthree(player1):
        print("player 1 wins")
        return "player1" 
    #player 2 win
    elif checkthesumofthree(player2) and len(player2)>2:
        print("player 2 wins")
        return "player2"             

def winner(thewinner):
    global playAgain,player 
    gameover = winnerfont.render(f'Winner', True , title_color)
    if thewinner == "draw":
        gameoverDraw = winnerfont.render(f'Draw', True , title_color)
        gamescreen.blit(gameoverDraw , (280,450))
        playAgain=playAgainButtons(280,525,"Play Again")
        player = 0
    elif thewinner == "player1":
        gamescreen.blit(gameover , (50,250))
        playAgain=playAgainButtons(280,525,"Play Again")
        player = 0
    elif thewinner == "player2":
        gamescreen.blit(gameover , (470,250))
        playAgain=playAgainButtons(280,525,"Play Again")
        player =0

def playerTurn():
    global player
    if player == 1:
        player1turn = midfont.render(f'Your Turn', True , white_color)
        gamescreen.blit(player1turn , (90,300))
    elif player == 2 :
        player2turn = midfont.render(f'Your Turn', True , white_color)
        gamescreen.blit(player2turn , (510,300))


# the game runner function
def game(sc):
    global player1,player2,listofnum , player
    thewinner= ''

    while True:
        #check if any event happen
        for ev in pg.event.get():
            #quit button event
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit(1)
            
            # get the mouse position on the window
            mouse = pg.mouse.get_pos() 
            if ev.type == pg.MOUSEBUTTONDOWN:
                #check what the cliked button 
                for bb in buttonslist:
                    if bb.collidepoint(mouse):
                            try:
                                index = buttonslist.index(bb) #get the button index from the list
                                listofnum.remove(index+1) # remove the button from list
                                if player==1:
                                    player1.append(index+1) #add to player 1 the chosen number
                                    if len(player1)>=3:
                                        thewinner = checkwin() 
                                    player = 2
                                else:
                                    player2.append(index+1)
                                    if len(player2)>=3:
                                        thewinner = checkwin()
                                    player = 1
                                buttonslist.remove(bb)

                            except:
                                pass           
                             
                try:
                    if playAgain.collidepoint(mouse):
                        # return the values to the initialize values
                        player= 1    
                        thewinner= ''
                        player1 =[]
                        player2 =[]
                        listofnum = [1,2,3,4,5,6,7,8,9,10]
                        buttonslist=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
                        
                except:
                    pass

                    
        # fills the screen with a color
        sc.fill((247,235,232))
        #game UI image 
        sc.blit(gameUI,(0,0))
        #check which player has turn to play
        playerTurn()        

        # postion of selected number for each player
        for eachelement in player1:  
           chosenNumber(20+(40*(player1.index(eachelement))),540,eachelement)

        for eachelement in player2:   
           chosenNumber(670-(40*(player2.index(eachelement))),540,eachelement)
           
        #clickable buttons of number to choose
        btn1 =numButton(310,180,1)
        btn2= numButton(370,180,2)
        btn3= numButton(310,240,3)
        btn4= numButton(370,240,4)
        btn5= numButton(310,300,5)
        btn6= numButton(370,300,6)
        btn7= numButton(310,360,7)
        btn8= numButton(370,360,8)
        btn9= numButton(340,420,9)
        
        buttonslist=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
        
        # the game over widgit if the game has been finshed
        winner(thewinner)
        
        #frame rate
        clock.tick(30)
        # updates the frames of the game
        pg.display.update()


# the welcome runner function
def welcome(sc):
    while True:
        #check if any event happen
        for ev in pg.event.get():
            
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit(1)

            mouse = pg.mouse.get_pos() 
            # checks if a mouse is clicked
            if ev.type == pg.MOUSEBUTTONDOWN:      
                    if playbtn.collidepoint(mouse):
                       game(gamescreen)
                    
        # fills the screen with a color
        sc.fill((247,235,232))
        sc.blit(welcomeUI,(0,0))
        playbtn = startButton()

        #frame rate
        clock.tick(30)
        # updates the frames of the game
        pg.display.update()

welcome(welcomescreen)