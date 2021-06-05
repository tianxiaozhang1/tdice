import pygame, sys, random#, math #, time
from math import sin, cos, radians, log

def running_lists():
    global running_colour_list
    global running_dice_list
    global running_player_list
    
    global p1_colour
    global p1_hi_colour

    global p1_sq_list

    global attacking_mode

    attacking_mode = False

    running_colour_list = [(0,0,0)]
    running_dice_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    running_player_list = [0,"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]

    p1_colour = None
    p1_hi_colour = None

def initial_setup():

    global px_sq
    global px_sq_num
    global px_colour
    global game_sq_list
    global game_colour_list

    global empty_sq_num
    global empty_sq_list

    global dice_for_sq
    
    global current_turn

    global playing

    empty_sq = 0
    empty_sq_list = []

    temp_list = []
    temp_key_list = []

    px_sq = [[],[],[],[],[],[],[]]
    px_sq_num = [0, 0, 0, 0, 0, 0, 0]
    px_colour = [None, None, None, None, None, None, None]

    dice_for_sq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #colour_list = [(168, 34, 38), (152, 80, 48), (198, 178, 38), (132, 168, 42), (32, 104, 100), (46, 88, 168), (108, 32, 108)]  
    colour_list = [(168, 34, 38), (152, 80, 48), (198, 178, 38), (132, 168, 42), (32, 104, 100), (46, 88, 168), (108, 32, 108), (204, 92, 32), (16, 138, 150), (100, 78, 50), (185, 90, 138), (128, 164, 146)]   
    sq_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

    current_sq = 0

    p1_turn = True

    hover_sq_list = []

    just_hovered_sq_num = 0

    game_sq_list = sq_list
    game_colour_list = colour_list

    global clicking_pair
    clicking_pair = []

    p1_colour = None
    p1_hi_colour = None

    #should be zero*****
    current_turn = 1

    dice_colour = panelcolour

    pygame.draw.rect(screen, panelcolour, pygame.Rect(35, 200, 359, 920)) 
    gamelog = []

def game_title():
    pygame.draw.rect(screen, (134, 144, 138), pygame.Rect(35, 28, 359, 120))  #(148, 120, 80)
    screen.blit(title_surface, title_rect)

def draw_squares(square1, colour1):
    for i in square1:
        x = i%6
        if x == 0:
            x = 6
        y = (i+5)//6
        x_pos = x*(sqwidth+6) + 423 - sqwidth
        y_pos = y*(sqheight+6) + 183 - sqheight
        pygame.draw.rect(screen, colour1, pygame.Rect(x_pos, y_pos, sqwidth, sqheight)) 

def draw_dice(squarenumber, numberofdice, attacking_mode = False, celebration = False, celebrating = False, celebrating_colour = None): 
    if numberofdice > 8:
        numberofdice == 8
    if attacking_mode == False:
        dice_colour = panelcolour
    else:
        dice_colour = dice_red
    if celebrating == True:
        dice_colour = celebrating_colour
    if celebration == True:
        dice_colour = verydarkgrey

    x1 = (squarenumber)%6
    if x1 == 0:
        x1 = 6
    y1 = ((squarenumber)+5)//6
    y_posd = y1*(sqheight+6) + 235 - sqheight

    if numberofdice < 5:
        x_posd = x1*(sqwidth+6) + 520 - sqwidth
        if numberofdice == 0:
            pass
        if numberofdice == 1:
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+40, 18, 18))
        if numberofdice == 2:
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+40, 18, 18))
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+20, 18, 18))
        if numberofdice == 3:
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+40, 18, 18))
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+20, 18, 18))
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd, 18, 18))
        if numberofdice == 4:
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+40, 18, 18)) 
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+20, 18, 18))
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd, 18, 18))    
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd-20, 18, 18))
    else:
        x_posd = x1*(sqwidth+6) + 510 - sqwidth
        y_posd = y1*(sqheight+6) + 235 - sqheight
        pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd+20, y_posd-20, 18, 18)) 
        pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd+20, y_posd, 18, 18))
        pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd+20, y_posd+20, 18, 18))    
        pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd+20, y_posd+40, 18, 18))
        if numberofdice == 5:
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+40, 18, 18))
        if numberofdice == 6:
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+40, 18, 18))
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+20, 18, 18))
        if numberofdice == 7:
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+40, 18, 18))
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+20, 18, 18))
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd, 18, 18))
        if numberofdice == 8:
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+40, 18, 18)) 
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+20, 18, 18))
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd, 18, 18))    
            pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd-20, 18, 18))

def hovering_new_game_button():
    if sum(active_players) > 12:
        if 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 28 <= pygame.mouse.get_pos()[1] <= 148:
            pygame.draw.rect(screen, (222, 108, 132), pygame.Rect(1766, 28, 120, 120)) 
            screen.blit(new_game_surface_1, new_game_surface_rect_1)
            screen.blit(new_game_surface_2, new_game_surface_rect_2)
        else:
            pygame.draw.rect(screen, (196, 92, 92), pygame.Rect(1766, 28, 120, 120)) 
            screen.blit(new_game_surface_1, new_game_surface_rect_1)
            screen.blit(new_game_surface_2, new_game_surface_rect_2)
    else:
        if 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 28 <= pygame.mouse.get_pos()[1] <= 148:
            pygame.draw.rect(screen, (0, 52, 96), pygame.Rect(1766, 28, 120, 120)) 
            screen.blit(new_game_surface_1, new_game_surface_rect_1)
            screen.blit(new_game_surface_2, new_game_surface_rect_2)
            
        else:
            pygame.draw.rect(screen, sapphire, pygame.Rect(1766, 28, 120, 120)) 
            screen.blit(new_game_surface_1, new_game_surface_rect_1)
            screen.blit(new_game_surface_2, new_game_surface_rect_2)
        
def hovering_pause_button(playing):
    if sum(active_players) > 12:
        if len(running_colour_list) > 1:
            if 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 942 <= pygame.mouse.get_pos()[1] <= 1062:
                if playing == True:
                    pygame.draw.rect(screen, (46, 72, 116), pygame.Rect(1766, 942, 120, 120)) 
                    screen.blit(pause_surface_1, pause_surface_rect_1)
                    screen.blit(pause_surface_2, pause_surface_rect_2)
                else:
                    pygame.draw.rect(screen, (216, 162, 88), pygame.Rect(1766, 942, 120, 120)) 
                    screen.blit(resume_surface_1, resume_surface_rect_1)
                    screen.blit(pause_surface_2, pause_surface_rect_2)
            else:
                if playing == True:
                    pygame.draw.rect(screen, (0, 62, 116), pygame.Rect(1766, 942, 120, 120)) 
                    screen.blit(pause_surface_1, pause_surface_rect_1)
                    screen.blit(pause_surface_2, pause_surface_rect_2)
                else:
                    pygame.draw.rect(screen, (218, 146, 52), pygame.Rect(1766, 942, 120, 120)) 
                    screen.blit(resume_surface_1, resume_surface_rect_1)
                    screen.blit(pause_surface_2, pause_surface_rect_2)
        else:
            pygame.draw.rect(screen, panelcolour, pygame.Rect(1766, 942, 120, 120))
    #else:
        #pygame.draw.rect(screen, midnight, pygame.Rect(1766, 942, 120, 120))

def hovering_end_turn_button():
    #print(end_turn_button)
    if sum(active_players) > 12:
        if end_turn_button == True:
            #print("End turn button hovering")
            if 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 792 <= pygame.mouse.get_pos()[1] <= 912:
                pygame.draw.rect(screen, (100, 114, 92), pygame.Rect(1766, 792, 120, 120))  #(92, 112, 88)
                screen.blit(end_turn_surface_1, end_turn_surface_rect_1)
                screen.blit(end_turn_surface_2, end_turn_surface_rect_2)
            else:
                pygame.draw.rect(screen, (78, 102, 72), pygame.Rect(1766, 792, 120, 120)) 
                screen.blit(end_turn_surface_1, end_turn_surface_rect_1)
                screen.blit(end_turn_surface_2, end_turn_surface_rect_2)
    #else:
        #pygame.draw.rect(screen, midnight, pygame.Rect(1766, 792, 120, 120))

def build_player(player_name, player_list, player_colour):
    temp_sum = 0
    px_number_of_dice = len(player_list)
    px_dice_list = []
    while px_number_of_dice > 0:
        px_dice_list.append(random.randint(1,5))
        px_number_of_dice -= 1
        
    px_dice_list.sort()
    temp_sum = sum(px_dice_list)

    if temp_sum > 15:
        #even number too many over 15
        if (temp_sum - 15) % 2 == 0: 
            px_dice_list[-1] -= (temp_sum - 15) / 2
            px_dice_list[-2] -= (temp_sum - 15) / 2
        else:                        #odd
            px_dice_list[-1] -= (temp_sum -15) / 2 + 0.5
            px_dice_list[-2] -= (temp_sum -15) / 2 - 0.5
    elif temp_sum < 15:
        #even number too many over 15
        if (15 - temp_sum) % 2 == 0: 
            px_dice_list[-1] += (15 - temp_sum) / 2
            px_dice_list[-2] += (15 - temp_sum) / 2
        else:                        #odd
            px_dice_list[-1] += (15 - temp_sum) / 2 + 0.5
            px_dice_list[-2] += (15 - temp_sum) / 2 - 0.5
    if px_dice_list[-1] > 8:
        px_dice_list[0] += px_dice_list[-1] - 8
        px_dice_list[-1] = 8

    #Removing the ones for players
    if px_dice_list[0] == 1 and len(px_dice_list) > 3:
        px_dice_list[1] += 1
        game_sq_list.append(player_list.pop(0))
        del px_dice_list[0]

    #print("Player name:")
    #print(player_name)
    #print("Fully processed")
    #print(px_dice_list)
    #print("Corresponding sq number:")
    #print(player_list)

    draw_squares(player_list, player_colour)

    #print("Dice list for player "+str(player_name))
    #print(player_list, px_dice_list)

    #for i in range(len(player_list)):
        #print("Trying to draw dice")
        #print("player_list[i]")
        #print(player_list[i])
        #print("px_dice_list[i]")
        #print(px_dice_list[i])
        #draw_dice(player_list[i], int(px_dice_list[i]))
        #print("Dice list for each player********************")
        #print(player_list[i], int(px_dice_list[i]))

    for i in player_list:
        running_player_list[i] = player_name

    while len(player_list) > 0:
        running_dice_list[player_list[0]] = int(px_dice_list[0])
        #draw_dice(player_list[0], int(px_dice_list[0]))
        del player_list[0]
        del px_dice_list[0]

    #print("Player's number ***")
    #print(player_name)

    #for i in range(len(player_list)):
    #    running_dice_list[player_list[i]] = int(px_dice_list[i])  
    
def new_game_setup():
    global new_game
    global empty_sq
    global end_turn_button

    global running_dice_list
    global running_player_list
    global running_colour_list

    global p1_colour
    global p1_hi_colour

    initial_setup()

    end_turn_button = True

    clicking_pair = []
    attacking_mode = False

    pygame.draw.rect(screen, panelcolour, pygame.Rect(426, 148, 1526, 12)) 
    gamelog = []

    title_surface = title_font.render("TDICE", True, panelcolour) #(88, 88, 88)
    title_rect = title_surface.get_rect(midleft = (36, 125))  #+16
    screen.blit(title_surface, title_rect)

    #new game button colour reset
    new_game_surface_1 = button_font.render("NEW", True, panelcolour) 
    #new_game_surface_rect_1 = new_game_surface_1.get_rect(midleft = (1768, 110))
    new_game_surface_2 = button_font.render("GAME", True, panelcolour) 
    #new_game_surface_rect_2 = new_game_surface_2.get_rect(midleft = (1768, 136))
    #screen.blit(new_game_surface_1, new_game_surface_rect_1)
    #screen.blit(new_game_surface_2, new_game_surface_rect_2)

    #pause and resume game button colour reset
    pause_surface_1 = button_font.render("PAUSE", True, panelcolour) 
    #pause_surface_rect_1 = pause_surface_1.get_rect(midleft = (1768, 1024))
    pause_surface_2 = button_font.render("GAME", True, panelcolour) 
    #pause_surface_rect_2 = pause_surface_2.get_rect(midleft = (1768, 1050))

    #end game button colour reset
    end_turn_surface_1 = button_font.render("END", True, panelcolour) 
    #end_turn_surface_rect_1 = end_turn_surface_1.get_rect(midleft = (1768, 874))
    end_turn_surface_2 = button_font.render("TURN", True, panelcolour) 
    #end_turn_surface_rect_2 = end_turn_surface_2.get_rect(midleft = (1768, 900))

    p1_sq_count=0
    
    pygame.draw.rect(screen, panelcolour, pygame.Rect(32, 156, 370, 16)) 

    active_players = [0,12,12,12,12,12,12,12]

    turn_list = [1, 2, 3, 4, 5, 6, 7]

    turn_number = 0

    current_turn = 0

    timeleftunit = 120

    pxlen = [0,0,0,0,0,0,0,0]

    px_sq_count_list = [0, 0, 0, 0, 0, 0, 0, 0]

    playing = True

    if new_game == True:

        playing = True

        current_turn = 1

        attacking_mode = False

        running_colour_list = [(172, 172, 172)]
        running_dice_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        running_player_list = [0,"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]

        pygame.draw.rect(screen, panelcolour, pygame.Rect(22, 190, 400, 920)) 
        gamelog = []

        #Reset all 36 squares
        #draw_squares(game_sq_list, panelcolour)

        for i in game_sq_list:
            draw_squares([i], panelcolour)
            #pygame.time.delay(32)

        for i in range(0,7):
            px_sq_num[i] = random.choice(player_sq_num)
            px_colour[i] = game_colour_list.pop(random.randrange(len(game_colour_list)))
            while px_sq_num[i] > 0:
                (px_sq[i]).append(game_sq_list.pop(random.randrange(len(game_sq_list))))
                px_sq_num[i] -= 1

        for i in range(0,7):
            build_player((i+1), px_sq[i], px_colour[i])
            running_colour_list.append(px_colour[i])

        empty_sq_num = [3,4,5,6]

        empty_sq = random.choice(empty_sq_num)
        if empty_sq > len(game_sq_list):
            empty_sq = len(game_sq_list)
        while empty_sq > 0:
            empty_sq_list.append(game_sq_list.pop(random.randrange(len(game_sq_list))))
            empty_sq -= 1

        for i in empty_sq_list:
            running_dice_list[i] = 0
            running_player_list[i] = "n"

        if len(game_sq_list) > 0:
            while len(game_sq_list) > 0:
                new_dice = random.randint(1,3)
                running_dice_list[game_sq_list[0]] = new_dice
                running_player_list[game_sq_list[0]] = 0
                draw_squares([game_sq_list[0]], grey)
                draw_dice(game_sq_list[0],new_dice)
                del game_sq_list[0]

        for j in range(1, 37):

            xj = j%6
            if xj == 0:
                xj = 6
            yj = (j+5)//6

            if xj == 1 or xj == 6 or yj == 1 or yj == 6:

                if running_dice_list[(yj-1)*6+xj] > 0:
                    
                    corner_blank_counter = 0

                    for (xx,yy) in ((xj,yj-1),(xj,yj+1),(xj-1,yj),(xj+1,yj)):
                        
                        if 0 < xx < 7 and 0 < yy < 7:
                            
                            if running_dice_list[(yy-1)*6+xx] == 0:
                                corner_blank_counter += 1
                                
                                if corner_blank_counter == 2:
                                
                                    running_dice_list[(yy-1)*6+xx] = 1
                                    running_player_list[(yy-1)*6+xx] = 0
                                    draw_squares([(yy-1)*6+xx], grey)
                                    draw_dice((yy-1)*6+xx, 1)    

        for i in range(1,37):
            draw_dice(i, running_dice_list[i])

        for i in range(1,8):
            pygame.draw.rect(screen, running_colour_list[i], pygame.Rect(429+197*(i-1), 28, 120, 120))  

        #end turn button
        #hover colour could be (92, 112, 88)
        pygame.draw.rect(screen, (78, 102, 72), pygame.Rect(1766, 792, 120, 120)) #main colour (78, 102, 72)

        p1_name_surface = player_name_font.render("P1", True, panelcolour) #(232, 232, 232)
        p1_name_rect = p1_name_surface.get_rect(midleft = (426, 125)) #410 for left #464 for right
        screen.blit(p1_name_surface, p1_name_rect)

        p2_name_surface = player_name_font.render("P2", True, panelcolour) 
        p2_name_rect = p2_name_surface.get_rect(midleft = (426+197*1, 125)) 
        screen.blit(p2_name_surface, p2_name_rect)

        p3_name_surface = player_name_font.render("P3", True, panelcolour) 
        p3_name_rect = p3_name_surface.get_rect(midleft = (426+197*2, 125))
        screen.blit(p3_name_surface, p3_name_rect)

        p4_name_surface = player_name_font.render("P4", True, panelcolour) 
        p4_name_rect = p4_name_surface.get_rect(midleft = (426+197*3, 125)) 
        screen.blit(p4_name_surface, p4_name_rect)

        p5_name_surface = player_name_font.render("P5", True, panelcolour) 
        p5_name_rect = p5_name_surface.get_rect(midleft = (426+197*4, 125))
        screen.blit(p5_name_surface, p5_name_rect)

        p6_name_surface = player_name_font.render("P6", True, panelcolour) 
        p6_name_rect = p6_name_surface.get_rect(midleft = (426+197*5, 125)) 
        screen.blit(p6_name_surface, p6_name_rect)

        p7_name_surface = player_name_font.render("P7", True, panelcolour) 
        p7_name_rect = p7_name_surface.get_rect(midleft = (426+197*6, 125))
        screen.blit(p7_name_surface, p7_name_rect)

        pygame.draw.rect(screen, (46, 72, 116), pygame.Rect(1766, 942, 120, 120)) #orange (218, 136, 60)
        screen.blit(pause_surface_1, pause_surface_rect_1)
        screen.blit(pause_surface_2, pause_surface_rect_2)

        screen.blit(end_turn_surface_1, end_turn_surface_rect_1)
        screen.blit(end_turn_surface_2, end_turn_surface_rect_2)

        p1_colour = running_colour_list[1]
        p1_hi_colour = hi_colour_list[colour_list.index(running_colour_list[1])]

    new_game = False

    playing = True
    #print("End of process")
    #print(px_sq)
    #print(px_colour)
    
    #p1_sq_list = px_sq[0]
    #print(p1_sq_list)
    #print("running_dice_list")
    #print(running_dice_list)
    #print("running_player_list")
    #print(running_player_list)
    #print(len(running_player_list))
    #print("running_colour_list")
    #print(running_colour_list)

    #print("Is This Normal?")
    #p1_sq_list = [i for i, x in enumerate(running_player_list) if x == 1]

    return p1_colour
    return p1_hi_colour

    return running_dice_list
    return running_player_list
    return running_colour_list

def recognize_sq():
    global hover_sq_num
    ms_x = pygame.mouse.get_pos()[0]
    ms_y = pygame.mouse.get_pos()[1]
    row1 = (ms_y - 189 + 148)// 148
    column1 = (ms_x - 429 + 218) // 218
    hover_sq_num = column1 + (row1-1) * 6
    #print(column1, row1)
    #print("Should be "+str(sqnum))
    return hover_sq_num
    
def clicking_pair_cleanup(clicking_pair):
    attacking_mode = False

    p1_1sq = clicking_pair[0]
    p1_1sq_list = []
    p1_1sq_list.append(p1_1sq)
    draw_squares(p1_1sq_list, p1_colour)
    draw_dice(p1_1sq, running_dice_list[p1_1sq])

    #if len(clicking_pair) == 0:
    #    pass
    #if len(clicking_pair) == 1:
    #    pass
    if len(clicking_pair) == 2:
        p27_1sq = clicking_pair[1]
        p27_1sq_list = []
        p27_1sq_list.append(p27_1sq)
        draw_squares(p27_1sq_list, running_colour_list[running_player_list[p27_1sq]])
        #draw_dice(p27_1sq, running_dice_list[])

def end_turn_addup(current_turn):

    end_turn_sq_list = []
    end_turn_sq_list_copy = []
    end_turn_sq_list_eliminite_8 = []
    end_turn_sq_list = [i for i, x in enumerate(running_player_list) if x == current_turn]
    end_turn_sq_list_copy = [i for i, x in enumerate(running_player_list) if x == current_turn]
    end_turn_sq_list_eliminite_8 = [i for i, x in enumerate(running_player_list) if x == current_turn]
    random_square_in_list = None

    #too crowded
    #number_of_dice_to_add = len(end_turn_sq_list)

    #test
    number_of_dice_to_add = 1

    biggest_piece_num = len(biggest_piece(end_turn_sq_list))

    if biggest_piece_num > 1:
        number_of_dice_to_add += biggest_piece_num

    #print("Square list for this user")
    #print(end_turn_sq_list_copy)
    #print("Adding")
    #print(number_of_dice_to_add)
    #print("Dice breakdown")
    #for i in end_turn_sq_list_copy:
    #    print(running_dice_list[i])

    #if number_of_dice_to_add < len(end_turn_sq_list_copy) * 8:

    #print(end_turn_sq_list)
    #print(end_turn_sq_list_copy)
    #print(end_turn_sq_list_eliminite_8)
    
    for i in end_turn_sq_list_eliminite_8:
        if running_dice_list[i] == 8:
            end_turn_sq_list_eliminite_8.remove(i)

    if len(end_turn_sq_list_eliminite_8) > 0:
        while number_of_dice_to_add > 0:
            random_square_in_list = random.choice(end_turn_sq_list_eliminite_8)
            if running_dice_list[random_square_in_list] == 8:
                end_turn_sq_list_eliminite_8.remove(random_square_in_list)
            else:
                running_dice_list[random_square_in_list] += 1
                number_of_dice_to_add -= 1
            if len(end_turn_sq_list_eliminite_8) == 0:
                number_of_dice_to_add = 0
    
    for i in running_dice_list:
        if i > 8:
            i == 8

    if sum(active_players) > 12:
        draw_squares(end_turn_sq_list_copy, running_colour_list[current_turn])
        for i in end_turn_sq_list_copy:
            draw_dice(i, running_dice_list[i])
    else:
        for i in range(1,37):
            if running_dice_list[i] > 0:
                draw_squares([i], sapphire)
            if running_dice_list[i] > 0:
                draw_dice(i, running_dice_list[i], celebration=True)

def biggest_piece(end_turn_sq_list):

    compare_1 = []
    compare_2 = []

    #while len(end_turn_sq_list) > len(compare_2):
    while len(end_turn_sq_list) > 0:

        compare_1.append(end_turn_sq_list[0])
        end_turn_sq_list.remove(end_turn_sq_list[0])
        #print(compare_1)

        for j in compare_1:
            xj = j%6
            if xj == 0:
                xj = 6
            yj = (j+5)//6
            #print("sq: "+str(j)+" compare1 xy "+str((xj, yj)))

            for i in end_turn_sq_list:
                xi = i%6
                if xi == 0:
                    xi = 6
                yi = (i+5)//6
                #print("sq: "+str(i)+" end_turn_sq_list xy "+str((xi, yi)))    

                if (xi == xj and abs(yi - yj) == 1) or (abs(xi - xj) == 1 and yi == yj):
                    #print(str(i)+" is good")
                    compare_1.append(i)
                    end_turn_sq_list.remove(i)

        if len(end_turn_sq_list) > 0:

            if len(compare_2) < 1:

                compare_2.append(end_turn_sq_list[0])
                end_turn_sq_list.remove(end_turn_sq_list[0])

                for j in compare_2:
                    xj = j%6
                    if xj == 0:
                        xj = 6
                    yj = (j+5)//6
                    #print("sq: "+str(j)+" compare2 xy "+str((xj, yj)))

                    for i in end_turn_sq_list:
                        xi = i%6
                        if xi == 0:
                            xi = 6
                        yi = (i+5)//6
                        #print("sq: "+str(i)+" end_turn_sq_list xy "+str((xi, yi)))    

                        if (xi == xj and abs(yi - yj) == 1) or (abs(xi - xj) == 1 and yi == yj):
                            #print(str(i)+" is good")
                            compare_2.append(i)
                            end_turn_sq_list.remove(i)

        if len(compare_1) > 0 and len(compare_2) > 0:
            for i in compare_1:
                xi = i%6
                if xi == 0:
                    xi = 6
                yi = (i+5)//6

                for j in compare_2:
                    xj = j%6
                    if xj == 0:
                        xj = 6
                    yj = (j+5)//6

                    if (xi == xj and abs(yi - yj) == 1) or (abs(xi - xj) == 1 and yi == yj):
                        #print(str(i)+" is good")
                        compare_2.append(i)
                        compare_1.remove(i)

        if len(compare_1) > len(compare_2):
            compare_2 = []
            for i in compare_1:
                compare_2.append(i)
            #compare_2 = compare_1
        #    compare_1 = []
        #else: 
        #    compare_1 = []
        compare_1 = []

        for j in compare_2:
            xj = j%6
            if xj == 0:
                xj = 6
            yj = (j+5)//6
            #print("sq: "+str(j)+" compare1 xy "+str((xj, yj)))

            for i in end_turn_sq_list:
                xi = i%6
                if xi == 0:
                    xi = 6
                yi = (i+5)//6
                #print("sq: "+str(i)+" end_turn_sq_list xy "+str((xi, yi)))    

                if (xi == xj and abs(yi - yj) == 1) or (abs(xi - xj) == 1 and yi == yj):
                    #print(str(i)+" is good")
                    compare_2.append(i)
                    end_turn_sq_list.remove(i)

    #biggest_piece_num = max(len(compare_1), len(compare_2))

    biggest_piece_num = len(compare_2)

    #print(biggest_piece_num)
    #print(compare_1)
    #print(end_turn_sq_list)
    #if len(compare_1) == 0:
    #    for i in 
    #print(compare_2)

    #if len(compare_2) == 0 and len(compare_1) > 0:
    #    compare_2 = compare_1

    return(compare_2) #biggest_piece_num, compare_1, 

#original AI
'''
def aigaming(player):
    global ai_round_list
    global ai_attacked_list

    ai_round_list = []
    ai_attacked_list = []
    
    #print("Starting AI again")
    #print("Player: "+str(player))
    ai_sq_list = []
    ai_dice_list = []
    ai_sq_list = [i for i, x in enumerate(running_player_list) if x == player]
    #print("The squares are: "+str(ai_sq_list))
    if len(ai_sq_list) > 0:
        for j in ai_sq_list:
            if running_dice_list[j] > 1:
                ai_dice_list.append((j, running_dice_list[j]))
        
        for i in ai_dice_list:
            xi = i[0]%6
            if xi == 0:
                xi = 6
            yi = (i[0]+5)//6

            neighbour_list = []
            for (xx,yy) in ((xi-1,yi),(xi,yi-1),(xi,yi+1),(xi+1,yi)):
                if 0 < xx < 7 and 0 < yy < 7:
                    neighbour_list.append((xx,yy))
            #print("Neighbours: "+str(neighbour_list))

            neighbour_list1 = []
            if len(neighbour_list) > 0:
                #Back to squarenumber from coordinates
                for k in neighbour_list:
                    neighbour_list1.append((k[1]-1)*6+k[0])
            #print("Neighbours: "+str(neighbour_list1))

            #print("Player:")
            #print(player)
            #print("Considering which to attack, current ai_attacked_list:")
            #print(ai_attacked_list)

            #Make sure they're an opponent/remove own squares and non_existent
            if len(neighbour_list1) > 1:
                for l in neighbour_list1:
                    if running_player_list[l] == player:
                        neighbour_list1.remove(l)
                    if running_player_list[l] == "n":
                        neighbour_list1.remove(l)
            if len(neighbour_list1) > 1:
                for m in neighbour_list1:
                    for n in ai_attacked_list:
                        if m == n:
                            print("Repeat found")
                            print("l")
                            print(m)
                            print("ai_attacked_list")
                            print(ai_attacked_list)
                            neighbour_list1.remove(m)
                    #if running_dice_list[l] == 0:
                    #    neighbour_list1.remove(l)

                for q in neighbour_list1:
                    if running_dice_list[q] == 0:
                        neighbour_list1.remove(q)
                #print("neighbour_list1, after removing self squares and non-squares")
                #print("Neighbours:")
                #print(neighbour_list1)

                if p1_sq_count < 12:
                    target_list = []
                    for m in neighbour_list1:
                        target_list.append((m, running_dice_list[m]))
                    if len(target_list) > 0:
                        target = target_list[0]
                        if len(target_list) > 1:
                            for n in target_list:
                                if n[1] < target[1]:
                                    target = n

                        if i[1] == 8 or i[1] > target[1]:
                            fighting_algorithm(i, target, player, ai_attacked_list)
                else:
                    target_list = []
                    for m in neighbour_list1:
                        if running_player_list[m] == 1 or running_player_list[m] == 0:
                            target_list.append((m, running_dice_list[m]))
                    if len(target_list) > 0:
                        target = target_list[0]
                        if len(target_list) > 1:
                            for n in target_list:
                                if n[1] < target[1]:
                                    target = n
                        if i[1] == 8 or i[1] > target[1]:
                            fighting_algorithm(i, target, player, ai_attacked_list)
        else:
            print("Nothing to attack, move on")
            
        #print(ai_round_list)                        
        return(ai_round_list)
        '''

def aigaming(player):

    ai_round_list = [] #for the processing part

    temp_running_player_list = []
    for i in running_player_list:
        temp_running_player_list.append(i)
    temp_running_dice_list = []
    for j in running_dice_list:
        temp_running_dice_list.append(j)

    updated_lists = []
    updated_lists = updating_ai_lists(player, temp_running_player_list, temp_running_dice_list)
    ai_sq_list = updated_lists[0]
    main_ai_list = updated_lists[1]
    main_sq_list = updated_lists[2]
    other_ai_sq_list = updated_lists[3]

    #rounds_left = 3
    #while rounds_left > 0:

    for i in main_ai_list:

        if i[1] > 1:

            neighbour_list = neighbour_exam(player, i, ai_sq_list, main_sq_list, temp_running_player_list, temp_running_dice_list)

            target_sq = 0

            if len(neighbour_list) > 1:
                #target_comparison(i[0], neighbour_list, other_ai_sq_list, temp_running_dice_list)
                target_sq = target_comparison(neighbour_list, other_ai_sq_list, temp_running_dice_list)
                target_sq = target_sq[0]
                print(str(i[0])+"'s target is: "+str(target_sq))
                #print(str(i)+" has targets: "+str(neighbour_list))
                pass
            elif len(neighbour_list) == 1:
                #print(str(i)+" has just one target: "+str(neighbour_list[0]))
                target_sq = neighbour_list[0][0]
                print(str(i[0])+"'s target is: "+str(target_sq))
                #print("Attack!")
                pass
            else:
                #len(neighbour_list) == 0:
                #print(str(i)+" has no target")
                pass

            if target_sq != 0:
            #print("Go fight")
                target = []
                target.append(target_sq)
                target.append(temp_running_dice_list[target_sq])

                raw_fight_result = fighting_algorithm(i, target, player, temp_running_player_list, temp_running_dice_list, ai_round_list)

                ai_round_list = raw_fight_result[0]
                fight_result = raw_fight_result[1]
                
                #Won
                if len(fight_result) == 6:
                    temp_running_player_list[fight_result[4]] = fight_result[3]
                    temp_running_dice_list[fight_result[4]] = fight_result[5]

                    ai_sq_list = []
                    ai_sq_list = [i for i, x in enumerate(temp_running_player_list) if x == player]
                    
                #Lost
                else:
                    if fight_result[2] != 1:
                        print("Failure on returned result")

                temp_running_dice_list[fight_result[1]] = fight_result[2]
            
            updated_lists = []
            updated_lists = updating_ai_lists(player, temp_running_player_list, temp_running_dice_list)
            ai_sq_list = updated_lists[0]
            main_ai_list = updated_lists[1]
            main_sq_list = updated_lists[2]
            other_ai_sq_list = updated_lists[3]

    #rounds_left -= 1
    print("Post attack updated main part: "+str(main_ai_list))

    return ai_round_list, temp_running_player_list, temp_running_dice_list

def aigaming1(player):

    temp_running_player_list = []
    for i in running_player_list:
        temp_running_player_list.append(i)
    temp_running_dice_list = []
    for j in running_dice_list:
        temp_running_dice_list.append(j)

    ai_round_list = [] #for the processing part
    
    #all player's squares
    ai_sq_list = []
    ai_sq_list = [i for i, x in enumerate(temp_running_player_list) if x == player] 

    ai_only_dice_list = [] #dice count for all current player's squares
    temp_ai_sq_list = [] #just to help get the biggest group
    for k in ai_sq_list:
        ai_only_dice_list.append(temp_running_dice_list[k])
        temp_ai_sq_list.append(k)
    
    temp_biggest_piece_group = biggest_piece(temp_ai_sq_list)

    if len(temp_biggest_piece_group) == 1:
        temp_biggest_piece_group = []
        temp_biggest_piece_group.append(ai_sq_list[ai_only_dice_list.index(max(ai_only_dice_list))])

    print("temp_biggest_piece_group")
    print(temp_biggest_piece_group)

    main_sq_list = [] #just squares
    main_ai_list = [] #both squares and their dice

    #main_dice_list = []

    for i in temp_biggest_piece_group:
        if temp_running_dice_list[i] > 1:
            main_sq_list.append(i)
            #main_dice_list.append(temp_running_dice_list[i])
            main_ai_list.append((i, temp_running_dice_list[i]))

    #print("main_sq_list")
    #print(main_sq_list)
    #print("main_dice_list")
    #print(main_dice_list)
    #print("main_ai_list")
    #print(main_ai_list)
    
    other_ai_sq_list = []
    for i in ai_sq_list:
        if i in main_sq_list:
            pass
        else:
            other_ai_sq_list.append(i)
    
    #print("The others:")
    #print(other_ai_sq_list)

    #print("temp_running_player_list")
    #print(temp_running_player_list)
    #print("temp_running_dice_list")
    #print(temp_running_dice_list)

    for i in main_ai_list:

        neighbour_list = neighbour_exam(i, ai_sq_list, temp_running_player_list, temp_running_dice_list)

        print("For "+str(i))

        print("neighbour_list right after neighbour_exam")
        print(neighbour_list)

        for j in neighbour_list:
            if temp_running_player_list[j] == player:
                neighbour_list.remove(j)
            if temp_running_dice_list[j] == 0:
                neighbour_list.remove(j)

        print("neighbour_list after additional processing")
        print(neighbour_list)

        target_sq = 0

        if len(neighbour_list) > 1:
            #target_comparison(i[0], neighbour_list, other_ai_sq_list, temp_running_dice_list)
            target_sq = target_comparison(neighbour_list, other_ai_sq_list, temp_running_dice_list)
            print(str(i[0])+"'s target is: "+str(target_sq))
            #print(str(i)+" has targets: "+str(neighbour_list))
            pass

        elif len(neighbour_list) == 1:
            #print(str(i)+" has just one target: "+str(neighbour_list[0]))
            target_sq = neighbour_list[0]
            #print(str(i[0])+"'s target is: "+str(target_sq))
            #print("Attack!")
            pass

        else:
            #len(neighbour_list) == 0:
            #print(str(i)+" has no target")
            pass

        if target_sq != 0:
            #print("Go fight")
            target = []
            target.append(target_sq)
            target.append(temp_running_dice_list[target_sq])
            #fighting_algorithm(i, target, player, temp_running_player_list, temp_running_dice_list)
            #print("Result is here: ***")
            #print()

            raw_fight_result = fighting_algorithm(i, target, player, temp_running_player_list, temp_running_dice_list, ai_round_list)

            ai_round_list = raw_fight_result[0]
            fight_result = raw_fight_result[1]
            
            #Won
            if len(fight_result) == 6:
                temp_running_player_list[fight_result[4]] = fight_result[3]
                temp_running_dice_list[fight_result[4]] = fight_result[5]

                ai_sq_list = []
                ai_sq_list = [i for i, x in enumerate(temp_running_player_list) if x == player]
                
            #Lost
            else:
                if fight_result[2] != 1:
                    print("Failure on returned result")

            temp_running_dice_list[fight_result[1]] = fight_result[2]

        #else:
            #print(str(i[0])+" can't fight")
        #

    '''
    if len(other_ai_sq_list) > 0:
        
        for i in other_ai_sq_list:
            sq_info = []
            print("Studying "+str(i))
            sq_info.append(i)
            sq_info.append(temp_running_dice_list[i])
            neighbour_list = neighbour_exam(sq_info, ai_sq_list, temp_running_player_list, temp_running_dice_list)
            print("neighbour_list")
            print(neighbour_list)

            if len(neighbour_list) > 0:
                neighbour_distance_list = []
                for j in neighbour_list:
                    others_list = []

                    ai_sq_list = []
                    ai_sq_list = [i for i, x in enumerate(temp_running_player_list) if x == player]
                    temp_ai_sq_list = []
                    for i in ai_sq_list:
                        temp_ai_sq_list.append(i)
                    temp_biggest_piece_group = biggest_piece(temp_ai_sq_list)
                    for i in temp_biggest_piece_group:
                        main_sq_list.append(i)

                    for k in main_sq_list:
                        others_list.append(k)
                    others_list.remove(i)

                    neighbour_distance_list.append(distance_comparison(j, others_list))
                    
                    print("****")
                    print("neighbour_distance_list")
                    print(neighbour_distance_list)

                    if neighbour_distance_list.count("1") == 1:
                        print("One possibility, good to attack")
                    elif neighbour_distance_list.count("1") > 1:
                        print("Multiple possibilities, need to pick")
                    else:
                        print("Can't attack")
    '''

                    #print("Neighbour's coordinates: "+str((xj, yj)))

    '''
        if len(target_list) > 0:
            target = target_list[0]
            if len(target_list) > 1:
                for n in target_list:
                    if n[1] < target[1]:
                        target = n
            if i[1] == 8 or i[1] > target[1]:
                fighting_algorithm(i, target, player, ai_attacked_list, temp_running_player_list, temp_running_dice_list) #

    #print("running_player_list")
    #print(running_player_list)
    #print(running_dice_list)
    #print("Solve this self attack thing")
    #print(ai_round_list)
    for i in ai_round_list:
        if running_player_list[i[0][1]] == running_player_list[i[1][1]]:
            print("Self attack situation")
            print(i)
            print(i[0][1])
            print(i[1][1])
            ai_round_list.remove(i)

    for i in ai_round_list:
        if running_player_list[i[1][1]] == "n":
            print("Blank attack situation")
            ai_round_list.remove(i)
        
    '''

    return ai_round_list #, temp_running_player_list, temp_running_dice_list

def updating_ai_lists(player, temp_running_player_list, temp_running_dice_list):
    ai_sq_list = []
    ai_sq_list = [i for i, x in enumerate(temp_running_player_list) if x == player] 

    ai_only_dice_list = [] #dice count for all current player's squares
    temp_ai_sq_list = [] #just to help get the biggest group
    for k in ai_sq_list:
        ai_only_dice_list.append(temp_running_dice_list[k])
        temp_ai_sq_list.append(k)

    temp_biggest_piece_group = []
    temp_biggest_piece_group = biggest_piece(temp_ai_sq_list)

    if len(temp_biggest_piece_group) == 1:
        temp_biggest_piece_group = []
        temp_biggest_piece_group.append(ai_sq_list[ai_only_dice_list.index(max(ai_only_dice_list))])

    main_sq_list = [] #just squares
    main_ai_list = [] #both squares and their dice

    for i in temp_biggest_piece_group:
        #if temp_running_dice_list[i] > 1:
        main_sq_list.append(i)
        main_ai_list.append((i, temp_running_dice_list[i]))
    
    other_ai_sq_list = []
    for i in ai_sq_list:
        if i not in main_sq_list:
        #    pass
        #else:
            other_ai_sq_list.append(i)

    for i in main_sq_list:
        xi = i%6
        if xi == 0:
            xi = 6
        yi = (i+5)//6

        for j in other_ai_sq_list:
            xj = j%6
            if xj == 0:
                xj = 6
            yj = (j+5)//6

            if (xi == xj and abs(yi - yj) == 1) or (abs(xi - xj) == 1 and yi == yj):
                #print("Previous part failed")
                main_sq_list.append(j)
                main_ai_list.append((j, temp_running_dice_list[j]))
                other_ai_sq_list.remove(j)
    
    return(ai_sq_list, main_ai_list, main_sq_list, other_ai_sq_list)

def neighbour_exam(player, i, ai_sq_list, main_sq_list, temp_running_player_list, temp_running_dice_list):

    xi = i[0]%6
    if xi == 0:
        xi = 6
    yi = (i[0]+5)//6

    neighbour_list = []
    for (xx,yy) in ((xi-1,yi), (xi,yi-1), (xi,yi+1), (xi+1,yi)):
        if 0 < xx < 7 and 0 < yy < 7:
            neighbour_list.append(((yy-1)*6+xx, temp_running_player_list[(yy-1)*6+xx], temp_running_dice_list[(yy-1)*6+xx]))
    #print(str(i[0])+"'s neighbours before processing: "+str(neighbour_list))

    #Remove non_existent squares
    for l in neighbour_list:
        if l[1] == 'n':
            neighbour_list.remove(l)
    '''
    if len(neighbour_list) > 0:
        for l in neighbour_list:
            if l[1] == 'n':
                neighbour_list.remove(l)
    '''
    if len(neighbour_list) > 0:
        for l in neighbour_list:
            if l[1] == 'n':
                neighbour_list.remove(l)
    
    #print("Blank square removal done: "+str(neighbour_list))

    #Remove own squares
    if len(neighbour_list) > 0:
        for m in neighbour_list:
            if m[1] == player:
                neighbour_list.remove(m)
    if len(neighbour_list) > 0:
        for m in neighbour_list:
            if m[1] == player:
                neighbour_list.remove(m)
    #print("Own square removal done: "+str(neighbour_list))

    #Remove opponents too strong
    if len(neighbour_list) > 0:
        for p in neighbour_list:
            if i[1] < 8:
                if p[2] >= i[1]:
                    neighbour_list.remove(p)
    if len(neighbour_list) > 0:
        for p in neighbour_list:
            if i[1] < 8:
                if p[2] >= i[1]:
                    neighbour_list.remove(p)
    #print(str(i)+" Full removal done: "+str(neighbour_list))

    return neighbour_list

'''
def neighbour_exam1(i, ai_sq_list, temp_running_player_list, temp_running_dice_list):

    xi = i[0]%6
    if xi == 0:
        xi = 6
    yi = (i[0]+5)//6

    neighbour_list = []
    for (xx,yy) in ((xi-1,yi), (xi,yi-1), (xi,yi+1), (xi+1,yi)):
        if 0 < xx < 7 and 0 < yy < 7:
            neighbour_list.append((yy-1)*6+xx)

    print(str(i[0])+"'s neighbours before processing: "+str(neighbour_list))

    #Remove non_existent squares
    #if len(neighbour_list) > 0:
    for l in neighbour_list:
        if temp_running_player_list[l] == "n":
            neighbour_list.remove(l)
    print("Neighbours after empty square removal: "+str(neighbour_list))
    if len(neighbour_list) > 0:
        for l2 in neighbour_list:
            if temp_running_dice_list[l2] == 0:
                neighbour_list.remove(l2)
        print("Neighbours after empty square removal II: "+str(neighbour_list))

    #Remove own squares
    if len(neighbour_list) > 0:
        for m in neighbour_list:
            if temp_running_player_list[m] == player:
                #print(str(m)+" is oneself too")
                neighbour_list.remove(m)
        print("Neighbours after own square removal: "+str(neighbour_list))
    if len(neighbour_list) > 0:
        for m2 in neighbour_list:
            if m2 in ai_sq_list:
                neighbour_list.remove(m2)
        print("Neighbours after own square removal II: "+str(neighbour_list)) #empty & 
        
    #Remove opponents too strong
    if len(neighbour_list) > 0:
        for n2 in neighbour_list:
            if i[1] == 8:
                pass
                #if temp_running_dice_list[n2] > i[1]:
                #    neighbour_list.remove(n2)
            else:
                if temp_running_dice_list[n2] >= i[1]: # >= means only attack when with more dice, > means a tie is good too
                    neighbour_list.remove(n2)
    if len(neighbour_list) > 0:
        for n3 in neighbour_list:
            if i[1] == 8:
                pass
                #if temp_running_dice_list[n3] > i[1]:
                #    neighbour_list.remove(n3)
            else:
                if temp_running_dice_list[n3] >= i[1]: # >= means only attack when with more dice, > means a tie is good too
                    neighbour_list.remove(n3)
            
        print("Neighbours too strong removed II: "+str(neighbour_list))
        #print("Attack list: "+str(neighbour_list))
    
    return neighbour_list
'''
def target_comparison(target_list, others_list, temp_running_dice_list):

    comparison_list = []

    target_dice_list = []

    best_target = 0

    if len(others_list) > 0:

        for i in target_list:

            comparison_list.append(distance_comparison(i[0], others_list))
        
            target_dice_list.append(temp_running_dice_list[i[0]])

        #print("comparison_list")
        #print("Targets and their best distances:")
        #print(target_list)
        #print(target_dice_list)
        #print(comparison_list)

        minimum_distance = min(comparison_list)

        if comparison_list.count(minimum_distance) == 1:
            best_target = target_list[comparison_list.index(minimum_distance)]
        elif comparison_list.count(minimum_distance) > 1:
            for i in comparison_list:
                if i > minimum_distance:
                    
                    target_list.remove(target_list[comparison_list.index(i)])
                    target_dice_list.remove(target_dice_list[comparison_list.index(i)])
                    comparison_list.remove(i)
                best_target = target_list[target_dice_list.index(min(target_dice_list))]
                
        #if best_target != 0:
        #print("The best target is: "+str(best_target))

    #Every square is already together
    else:
        for i in target_list:
            #target_list already exists
            target_dice_list.append(temp_running_dice_list[i[0]])
        best_target = target_list[target_dice_list.index(min(target_dice_list))]
    
    return best_target

def distance_comparison(target, others_list):
    
    temp_distance_list = []

    xx = target%6
    if xx == 0:
        xx = 6
    yy = (target+5)//6

    #print("Target's coordinates: "+str((xx, yy)))
    
    for i in others_list:
        xi = i%6
        if xi == 0:
            xi = 6
        yi = (i+5)//6

        #print("Other's coordinates: "+str((xi, yi)))

        temp_distance_list.append(abs(xi-xx)+abs(yi-yy))

    #print("Regarding "+str(target))
    #print("Others list: "+str(others_list))
    #print("   Distance: "+str(temp_distance_list))

    #print("Minimum distance: "+str(min(temp_distance_list)))
    #print("Index of min. d.: "+str(temp_distance_list.index(min(temp_distance_list))))
    #print("Item in the list:"+str(others_list[temp_distance_list.index(min(temp_distance_list))]))
    
    #the_selection = others_list[temp_distance_list.index(min(temp_distance_list))] 

    #print("The selection: "+str(the_selection))

    #print("Distance    list: "+str(temp_distance_list))
    #print("Minimum distance: "+str(min(temp_distance_list)))

    minimum_distance_to_target = min(temp_distance_list)

    return minimum_distance_to_target

def ai_stage2(player, temp_running_player_list, temp_running_dice_list):

    ai_attacked_list = []

    temp_ai_ini_sq_list = []
    temp_ai_ini_sq_list = [i for i, x in enumerate(temp_running_player_list) if x == player]
    
    while temp_ai_ini_sq_list[-1] > 36:
        temp_ai_ini_sq_list = temp_ai_ini_sq_list[:-2]

    ai_ini_sq_list = []
    for i in temp_ai_ini_sq_list:
        ai_ini_sq_list.append(i)

    temp_biggest_piece_group = (biggest_piece(temp_ai_ini_sq_list))[1]

    print("ai_ini_sq_list")
    print(ai_ini_sq_list)

    ai_dice_only_list = []
    for i in ai_ini_sq_list:
        ai_dice_only_list.append(temp_running_dice_list[i])

    print("ai_dice_only_list")
    print(ai_dice_only_list)

    temp_biggest_piece_dice = []
    for i in temp_biggest_piece_group:
        temp_biggest_piece_dice.append(temp_running_dice_list[i])
    
    print("Biggest group:")
    print(temp_biggest_piece_group)
    print(temp_biggest_piece_dice)

    biggest_piece_group = []
    biggest_piece_dice = []

    for i in range(len(temp_biggest_piece_group)):
        if temp_biggest_piece_dice[i] > 1:
            biggest_piece_group.append(temp_biggest_piece_group[i])
            biggest_piece_dice.append(temp_biggest_piece_dice[i])
    
    print("Among the biggest group that can attack:")
    print(biggest_piece_group)
    print(biggest_piece_dice)

    for i in biggest_piece_group:
        xi = i%6
        if xi == 0:
            xi = 6
        yi = (i+5)//6

        neighbour_list = []
        for (xx,yy) in ((xi-1,yi),(xi,yi-1),(xi,yi+1),(xi+1,yi)):
            if 0 < xx < 7 and 0 < yy < 7:
                neighbour_list.append((xx,yy))

        neighbour_list1 = []
        for k in neighbour_list:
            neighbour_list1.append((k[1]-1)*6+k[0])
        #print("Neighbours: "+str(neighbour_list1))

        #Remove own squares
        if len(neighbour_list1) > 1:
            for l in neighbour_list1:
                if temp_running_player_list[l] == player:
                    neighbour_list1.remove(l)
                    #print("Neighbours after own square removal: "+str(neighbour_list1))
        #Remove non_existent squares
        if len(neighbour_list1) > 1:
            for l in neighbour_list1:
                if temp_running_player_list[l] == "n":
                    neighbour_list1.remove(l)
                    #print("Neighbours after empty square removal: "+str(neighbour_list1))

        print("neighbour_list1")
        print(neighbour_list1)

        pass
            
    #for i in biggest_piece:
    #    pass


    #ai_attack_sq_list = []
    #ai_attack_dice_list = []

    #if max(ai_dice_only_list) >= 2:
    #    print("Could attack")
    #    for i in range(len(ai_ini_sq_list))
    #        if ai_dice_only_list
    #    for i in ai_dice_only_list:
    #        if i > 1:
    #            ai_attack_sq_list.append(i)




    '''
    ai_only_sq_list = []
    ai_only_dice_list = []
    ai_dice_list = []

    ai_ini_sq_co_list = []
    ai_only_sq_co_list = []

    if len(ai_ini_sq_list) > 0:
        for j in ai_ini_sq_list:
            x = j%6
            if x == 0:
                x = 6
            y = (j+5)//6
            ai_ini_sq_co_list.append((x,y))
            if temp_running_dice_list[j] > 1:
                ai_dice_list.append((j, temp_running_dice_list[j]))
                #ai_only_dice_list.append(temp_running_dice_list[j])
    
    print("Stage 2")
    print("ai_ini_sq_list")
    print(ai_ini_sq_list) #all squares after initial attack, including squares of 1
    print("ai_ini_sq_co_list")
    print(ai_ini_sq_co_list)
    print("ai_dice_list")
    print(ai_dice_list) #tuples of squares with 2 or more dice ready for round 2
    
    for i in ai_dice_list:
        ai_only_sq_list.append(i[0])
        ai_only_dice_list.append(i[1])
        
    for j in ai_only_sq_list:
        x = j%6
        if x == 0:
            x = 6
        y = (j+5)//6
        ai_only_sq_co_list.append((x,y))

    print("ai_only_sq_list")
    print(ai_only_sq_list) 
    print("ai_only_sq_co_list")
    print(ai_only_sq_co_list) 
    print("ai_only_dice_list")
    print(ai_only_dice_list)

    biggest_piece_group = biggest_piece(ai_ini_sq_list)[1]

    print("Biggest group:")
    print(biggest_piece_group)

    for i in biggest_piece_group:
        pass

    ai_ini_sq_minus_biggest_list = []
    for i in ai_ini_sq_list:
        ai_ini_sq_minus_biggest_list.append(i)
        for j in biggest_piece_group:
            if i == j:
                ai_ini_sq_minus_biggest_list.remove(i)

    print("ai_ini_sq_minus_biggest_list")
    print(ai_ini_sq_minus_biggest_list)

    

    for i in biggest_piece_group:
        xi = i[0]%6
        if xi == 0:
            xi = 6
        yi = (i[0]+5)//6

        neighbour_list = []
        for (xx,yy) in ((xi-1,yi),(xi,yi-1),(xi,yi+1),(xi+1,yi)):
            if 0 < xx < 7 and 0 < yy < 7:
                neighbour_list.append((xx,yy))

        neighbour_list1 = []
        if len(neighbour_list) > 0:
            #Back to squarenumber from coordinates
            for k in neighbour_list:
                neighbour_list1.append((k[1]-1)*6+k[0])
        #print("Neighbours: "+str(neighbour_list1))

        #Remove own squares
        if len(neighbour_list1) > 1:
            for l in neighbour_list1:
                if running_player_list[l] == player:
                    neighbour_list1.remove(l)
                    #print("Neighbours after own square removal: "+str(neighbour_list1))
        #Remove non_existent squares
        if len(neighbour_list1) > 1:
            for l in neighbour_list1:
                if running_player_list[l] == "n":
                    neighbour_list1.remove(l)
                    #print("Neighbours after empty square removal: "+str(neighbour_list1))
        if len(neighbour_list1) > 1:
            for m in neighbour_list1:
                for n in ai_attacked_list:
                    if m == n:
                        neighbour_list1.remove(m)
                        #print("Neighbours after already attacked square removal: "+str(neighbour_list1))

        target_list = []

        for m in neighbour_list1:
            if p1_sq_count < 12:
                target_list.append((m, running_dice_list[m]))
            elif running_player_list[m] == 1 or running_player_list[m] == 0:
                target_list.append((m, running_dice_list[m]))

        if len(target_list) > 0:
            target = target_list[0]
            if len(target_list) > 1:
                for n in target_list:
                    if n[1] < target[1]:
                        target = n
            if i[1] == 8 or i[1] > target[1]:
                fighting_algorithm(i, target, player, ai_attacked_list, temp_running_player_list, temp_running_dice_list) #
        
    '''

    #print("ai_only_dice_list")
    #print(ai_only_dice_list)
    #print(running_dice_list)
    #while len(ai_dice_list) > 0:

def fighting_algorithm(i, target, player, temp_running_player_list, temp_running_dice_list, ai_round_list):

    fighting_pair = [i[0], target[0]]
    
    dice1 = i[1]
    dice2 = target[1]     
    
    dicesum1 = 0
    dicesum2 = 0

    dice_list1 = []
    dice_list2 = []
    
    while dice1>0:
        if running_player_list[target[0]] == 1 and p1_sq_count > 18:
            roll1 = 1 #cheating was random.randint(2,6)
        else:
            roll1 = random.randint(1,6)
        dicesum1 += roll1
        dice_list1.append(roll1)
        dice1 -= 1
    while dice2>0:
        roll2 = random.randint(1,6)
        dicesum2 += roll2
        dice_list2.append(roll2)
        dice2 -= 1

    #new approach with lists and another function just to process
    attacker_info = []
    defender_info = []
    gamelog_info = []

    str1 = "P"+str(running_player_list[fighting_pair[0]])+" rolled a "+str(dicesum1)+" with "+str(dice_list1).strip("[]")
    if running_player_list[fighting_pair[1]] != 0:
        str2 = "P"+str(running_player_list[fighting_pair[1]])+" rolled a "+str(dicesum2)+" with "+str(dice_list2).strip("[]")
    else:
        str2 = "Grey rolled a "+str(dicesum2)+" with "+str(dice_list2).strip("[]")

    gamelog_info.append(str1)
    gamelog_info.append(str2)

    #Format: Attack player, Attack sq, Attack dice, Defense player, Defense sq, Defense dice
    temp_round_list = []

    if dicesum1 > dicesum2:
        #print("Attacker wins, the target was")
        #print(target[0])
        #ai_attacked_list.append(target[0])
        #print("ai_attacked_list")
        #print(ai_attacked_list)
        #str3 = "P"+str(running_player_list[fighting_pair[0]])+" wins"
        str3 = "P"+str(running_player_list[fighting_pair[0]])+" conquered"
        winner_colour = running_colour_list[player]
        
        gamelog_info.append(str3)
        gamelog_info.append(winner_colour)
        
        attacker_info.append(player)
        attacker_info.append(fighting_pair[0])
        attacker_info.append(1)
        attacker_info.append(winner_colour)
        
        defender_info.append(player)
        defender_info.append(fighting_pair[1])
        defender_info.append(running_dice_list[fighting_pair[0]]-1)
        defender_info.append(winner_colour)

        #temp_running_dice_list[fighting_pair[1]] = running_dice_list[fighting_pair[0]]-1
        #temp_running_dice_list[fighting_pair[0]] = 1
        #temp_running_player_list[fighting_pair[1]] = player

        #running_player_list[fighting_pair[1]] = player
        #running_dice_list[fighting_pair[1]] = running_dice_list[fighting_pair[0]]-1

        #running_dice_list[fighting_pair[0]] = 1

        temp_round_list.append(player)
        temp_round_list.append(fighting_pair[0])
        temp_round_list.append(1)
        temp_round_list.append(player)
        temp_round_list.append(fighting_pair[1])
        temp_round_list.append(temp_running_dice_list[fighting_pair[0]]-1)

        #attacking_mode = False
        
        '''
        running_player_list[fighting_pair[1]] = player
        
        running_dice_list[fighting_pair[1]] = running_dice_list[fighting_pair[0]]-1
        running_dice_list[fighting_pair[0]] = 1
        '''
        #draw_squares([fighting_pair[1]], running_colour_list[player])
        #draw_dice(fighting_pair[1], running_dice_list[fighting_pair[1]])
        #draw_squares([fighting_pair[0]], running_colour_list[player])
        #draw_dice(fighting_pair[0], running_dice_list[fighting_pair[0]])
        
        #p1_sq_list.append(fighting_pair[1])
        #print("running_player_list Right after attack")
        #print(running_player_list)
        fighting_pair = []
        #pause_hovering = False

    else:
        #print("Defender wins")
        if running_player_list[fighting_pair[1]] != 0:
            #str3 = "P"+str(running_player_list[fighting_pair[1]])+" wins"
            str3 = "P"+str(running_player_list[fighting_pair[1]])+" defended"
        else:
            #str3 = "Grey wins"
            str3 = "Grey defended"
        winner_colour = running_colour_list[running_player_list[fighting_pair[1]]]

        gamelog_info.append(str3)
        gamelog_info.append(winner_colour)
        
        attacker_info.append(player)
        attacker_info.append(fighting_pair[0])
        attacker_info.append(1)
        attacker_info.append(running_colour_list[player])
        
        defender_info.append(running_player_list[fighting_pair[1]])
        defender_info.append(fighting_pair[1])
        defender_info.append(running_dice_list[fighting_pair[1]])
        defender_info.append(running_colour_list[running_player_list[fighting_pair[1]]])

        temp_round_list.append(player)
        temp_round_list.append(fighting_pair[0])
        temp_round_list.append(1)

        #temp_running_dice_list[fighting_pair[0]] = 1

        #print("Temp lists right after a failing attack")
        #print(temp_running_player_list)
        #print(temp_running_dice_list)

        #attacking_mode = False
        #draw_squares([fighting_pair[1]], running_colour_list[running_player_list[fighting_pair[1]]])
        #draw_dice(fighting_pair[1], running_dice_list[fighting_pair[1]])
        #running_dice_list[fighting_pair[0]] = 1
        #draw_squares([fighting_pair[0]], running_colour_list[player])
        #draw_dice(fighting_pair[0], 1)
        fighting_pair = []
        #pause_hovering = False

    ai_round_list.append([attacker_info, defender_info, gamelog_info])
    return ai_round_list, temp_round_list

def ai_processing_one(ai_round_item, current_turn):
    attacker = ai_round_item[0]   
    draw_squares([attacker[1]], battle_colour)
    draw_dice(attacker[1], running_dice_list[attacker[1]], True)

def ai_processing_two(ai_round_item, current_turn):
    attacker = ai_round_item[0]
    defender = ai_round_item[1]
    gamelog_entry = ai_round_item[2]

    print("This stuff:")
    print("attacker "+str(attacker))
    print("defender "+str(defender))

    draw_squares([attacker[1]], attacker[3])
    draw_dice(attacker[1], attacker[2])
    draw_squares([defender[1]], defender[3])
    draw_dice(defender[1], defender[2])

    running_player_list[attacker[1]] = attacker[0]
    running_dice_list[attacker[1]] = attacker[2]

    running_player_list[defender[1]] = defender[0]
    running_dice_list[defender[1]] = defender[2]

    if running_dice_list != temp_running_dice_list:
        print("Lists different")

    for i in range(0, 37):
        if running_dice_list[i] != temp_running_dice_list[i]:
            #running_dice_list[i] = temp_running_dice_list[i]
            print(str(i)+" is different among the lists... running is "+str(running_dice_list[i])+" and temp is "+str(temp_running_dice_list[i]))

    #print(running_dice_list)
    #print(temp_running_dice_list)

    gamelog.insert(0, gamelog_entry)

    if len(gamelog) > 11:
        del gamelog[-1]

    btmline = 1008

    pygame.draw.rect(screen, panelcolour, pygame.Rect(22, 190, 400, 920)) 

    for i in range(len(gamelog)):
        log_surface = log_font.render(str(gamelog[i][0]), True, logcolour) 
        log_rect = log_surface.get_rect(midleft = (32, btmline-80*i)) 
        screen.blit(log_surface, log_rect)
        log_surface = log_font.render(str(gamelog[i][1]), True, logcolour) 
        log_rect = log_surface.get_rect(midleft = (32, btmline+22-80*i)) 
        screen.blit(log_surface, log_rect)
        log_surface = log_font.render(str(gamelog[i][2]), True, gamelog[i][-1]) 
        log_rect = log_surface.get_rect(midleft = (32, btmline+44-80*i)) 
        screen.blit(log_surface, log_rect)

def fireworks_animation_background():

    pygame.draw.rect(screen, midnight, pygame.Rect(0, 0, 1920, 1080))

    #title part
    pygame.draw.rect(screen, sapphire, pygame.Rect(35, 28, 359, 120)) #sapphire
    title_surface = title_font.render("TDICE", True, verydarkgrey) #(88, 88, 88)
    title_rect = title_surface.get_rect(midleft = (36, 125))  #+16
    screen.blit(title_surface, title_rect)

    #size bar
    pygame.draw.rect(screen, sapphire, pygame.Rect(35, 158, 359, 20)) # to (26, 40, 72)

    #p1 square
    pygame.draw.rect(screen, sapphire, pygame.Rect(429, 28, 120, 120))  

    p1_name_surface = player_name_font.render("P1", True, midnight) #(232, 232, 232)
    p1_name_rect = p1_name_surface.get_rect(midleft = (426, 125)) #410 for left #464 for right
    screen.blit(p1_name_surface, p1_name_rect)

    #new game button
    new_game_surface_1 = button_font.render("NEW", True, darkgrey) 
    new_game_surface_rect_1 = new_game_surface_1.get_rect(midleft = (1768, 110))
    new_game_surface_2 = button_font.render("GAME", True, darkgrey) 
    new_game_surface_rect_2 = new_game_surface_2.get_rect(midleft = (1768, 136))

    pygame.draw.rect(screen, sapphire, pygame.Rect(1766, 28, 120, 120)) #196, 92, 92
    screen.blit(new_game_surface_1, new_game_surface_rect_1)
    screen.blit(new_game_surface_2, new_game_surface_rect_2)

    #pause game button
    pause_surface_1 = button_font.render("PAUSE", True, midnight) 
    pause_surface_rect_1 = pause_surface_1.get_rect(midleft = (1768, 1024))
    pause_surface_2 = button_font.render("GAME", True, midnight) 
    pause_surface_rect_2 = pause_surface_2.get_rect(midleft = (1768, 1050))

    pygame.draw.rect(screen, sapphire, pygame.Rect(1766, 942, 120, 120)) 
    screen.blit(pause_surface_1, pause_surface_rect_1)
    screen.blit(pause_surface_2, pause_surface_rect_2)

    #end turn button
    end_turn_surface_1 = button_font.render("END", True, midnight) 
    end_turn_surface_rect_1 = end_turn_surface_1.get_rect(midleft = (1768, 874))
    end_turn_surface_2 = button_font.render("TURN", True, midnight) 
    end_turn_surface_rect_2 = end_turn_surface_2.get_rect(midleft = (1768, 900))

    pygame.draw.rect(screen, sapphire, pygame.Rect(1766, 792, 120, 120)) #(78, 102, 72)
    screen.blit(end_turn_surface_1, end_turn_surface_rect_1)
    screen.blit(end_turn_surface_2, end_turn_surface_rect_2)

    #all p1's squares and dice
    for i in range(1,37):
        if running_dice_list[i] > 0:
            draw_squares([i], sapphire) #sapphire 
        if running_dice_list[i] > 0:
            draw_dice(i, running_dice_list[i], celebrating=True, celebrating_colour = verydarkgrey)

    #fireworks_animation(120)

    #print(fireworks_timeunit)

    #while fireworks_timeunit > 0:
    #    fireworks_timeunit -= 1/120

    #    print(fireworks_timeunit)

    
        
        #pygame.draw.rect(screen, panelcolour, pygame.Rect(1766, 792, 18, 18))


    #pygame.display.flip()

def fireworks(fw_x_list, fw_y_list, fw_colour):
    fw_time = 120

    while fw_time > 0:

        clock.tick(66)
        
        fw_time -= 1/4

        fireworks_animation_background()

        if 90 < fw_time <= 120:
            for i in range(0, 1):
                for j in range(0,7):
                    pygame.draw.rect(screen, random.choice(hi_colour_list), pygame.Rect(fw_x_list[i]+3, int(fw_y_list[i] - 880 + 12 + 0.5*((953-10*j)/450)*((fw_time-90)**2))-8, 12, 12)) 
                pygame.draw.rect(screen, fw_colour, pygame.Rect(fw_x_list[i], int(fw_y_list[i] - 880 + 0.5*(88/45)*((fw_time-90)**2)), 18, 18)) #main particle
        
        #while len(fw_quantity) < 1:     
        #    fw_quantity.append(random.randint(82,122)) #72,162

        fw_quantity = [66]

        for i in range(0, 1):
            while len(fw_colour_list[i]) < fw_quantity[i]:
                fw_colour_list[i].append(random.choice(hi_colour_list))
                fw_trail_list[i].append(random.choice(hi_colour_list))
                fw_angle_list[i].append(random.randint(0,360))
                firework_distance_list[i].append(random.randint(36,108))
                fw_hyp_list[i].append(random.uniform(0.12, 1.02))
                #randint(0.72,1.02))
        if 60 < fw_time < 90:
            #d_factor = 1 - (0.2999999/4)*(fw_time-86)
            #d_factor =  0.596 - math.log(fw_time-83,26)
            #d_factor = d_factor * 0.56

            #d_factor = 66 - (66/6)*(fw_time-84)
            #d_factor = d_factor * 0.0056
            #d1 = 269 - ((280/11)*(fw_time-72)+(1/2)*(-7/6)*(fw_time-72)**2) #if 72 < fw_time < 90:
            #d1 *= 0.8
            #d1 = 525-((560/3)*(fw_time-66)+(1/2)*(-28/45)*(fw_time-66)**2) #didn't work for 66
            d1 = 600-(50/3)*(fw_time-66)+(1/2)*(-5/9)*((fw_time-66)**2)
            d1 *= 0.52
            #print(d_factor)
              
            #for i in range(0, 6):
            #    for j in range(fw_quantity[i]):
            #        pygame.draw.rect(screen, random.choice(trail_colour_list), pygame.Rect(int(fw_x_list[i]+firework_distance_list[i][j]*d_factor*(cos(radians(fw_angle_list[i][j]))))-2, int(fw_y_list[i] - 880 + firework_distance_list[i][j]*d_factor*(sin(radians(fw_angle_list[i][j]))))-2, 8, 8))
            #        pygame.draw.rect(screen, firework_colour_list[i][j], pygame.Rect(int(fw_x_list[i]+firework_distance_list[i][j]*d_factor*(cos(radians(fw_angle_list[i][j]))))+8, int(fw_y_list[i] - 880 + firework_distance_list[i][j]*d_factor*(sin(radians(fw_angle_list[i][j]))))+8, 8, 8))

            for i in range(0, 1):
                for j in range(fw_quantity[i]):

                    '''
                    dc1 = fw_colour_list[i][j][0]
                    if dc1 < 26:
                        dc1 = 26
                    dc2 = fw_colour_list[i][j][1]
                    if dc2 < 40:
                        dc2 = 40
                    dc3 = fw_colour_list[i][j][2]
                    if dc3 < 72:
                        dc3 = 72
                    '''

                    #print(dc1, dc2, dc3)

                    #dt1 = fw_trail_list[i][j][0]
                    #dt2 = fw_trail_list[i][j][1]
                    #dt3 = fw_trail_list[i][j][2]

                    pygame.draw.rect(screen, fw_trail_list[i][j], pygame.Rect(int(fw_x_list[i]+d1*fw_hyp_list[i][j]*(cos(radians(fw_angle_list[i][j])))), int(fw_y_list[i] - 880 + d1*fw_hyp_list[i][j]*(sin(radians(fw_angle_list[i][j])))+2-136+(0.5*(0.46)*(fw_time-66)**2)), 12, 12))
                    #pygame.draw.rect(screen, fw_colour_list[i][j], pygame.Rect(int(fw_x_list[i]+d1*fw_hyp_list[i][j]*(cos(radians(fw_angle_list[i][j]))))+6, int(fw_y_list[i] - 880 + d1*fw_hyp_list[i][j]*(sin(radians(fw_angle_list[i][j])))+8-136+(0.5*(0.46)*(fw_time-66)**2)), 12, 12))
                    pygame.draw.rect(screen, running_colour_list[1], pygame.Rect(int(fw_x_list[i]+d1*fw_hyp_list[i][j]*(cos(radians(fw_angle_list[i][j]))))+6, int(fw_y_list[i] - 880 + d1*fw_hyp_list[i][j]*(sin(radians(fw_angle_list[i][j])))+8-136+(0.5*(0.46)*(fw_time-66)**2)), 12, 12))
                    #fw_colour_list[i][j]
                    #(int(((dc1-26)/24))*fw_time+26, int(((dc2-40)/24))*fw_time+40, int(((dc3-72)/24))*fw_time+72)


        #if 80 < fw_time < 84:
        #    d_factor =  0.596 * 0.56
        #      
        #    for i in range(0, 6):
        #        for j in range(fw_quantity[i]):
        #            pygame.draw.rect(screen, (222, 222, 222), pygame.Rect(int(fw_x_list[i]+firework_distance_list[i][j]*d_factor*(math.cos(math.radians(firework_angle_list[i][j]))))-2, int(fw_y_list[i] - 880 + firework_distance_list[i][j]*d_factor*(math.sin(math.radians(firework_angle_list[i][j]))))-2+200-0.5*(100/8)*(fw_time-80)**2, 8, 8))
        #            pygame.draw.rect(screen, firework_colour_list[i][j], pygame.Rect(int(fw_x_list[i]+firework_distance_list[i][j]*d_factor*(math.cos(math.radians(firework_angle_list[i][j])))), int(fw_y_list[i] - 880 + firework_distance_list[i][j]*d_factor*(math.sin(math.radians(firework_angle_list[i][j]))))+200-0.5*(100/8)*(fw_time-80)**2, 8, 8))
        
        #for j in range(fw_quantity[0]):
        #    print(j)

        #if 86 < fw_time <= 90:
        #    for i in fw_quantity:
        #        for j in range(i):

                #for j in range(fw_quantity[i]):
                #    print(j)
                #pygame.draw.rect(screen, firework_list[i][j], pygame.Rect(fw_x_list[2]+fw_distance1*(math.cos(math.radians(j*10))), int(fw_y_list[2] - 880 + fw_distance1*(math.sin(math.radians(j*10)))), 8, 8))
        
        #if fw_time - 90 < 0.00001:
        '''
        for i in range(0, 6):
            while len(firework_colour_list[i]) < 36:
                #firework_list[i].append(random.choice(trail_colour_list))
                firework_colour_list[i].append(random.choice(hi_colour_list))
        
        if 86 < fw_time <= 90:
            fw_distance1 = 66 - (66/4)*(fw_time-86)
            fw_distance2 = 56 - (56/4)*(fw_time-86)
            fw_distance3 = 46 - (46/4)*(fw_time-86)
            
            for i in range(0,6):
                for j in range(0,36):
                    pygame.draw.rect(screen, firework_colour_list[i][j], pygame.Rect(fw_x_list[i]+fw_distance1*(math.cos(math.radians(j*10))), int(fw_y_list[i] - 880 + fw_distance1*(math.sin(math.radians(j*10)))), 8, 8))
                    pygame.draw.rect(screen, random.choice(trail_colour_list), pygame.Rect(fw_x_list[2]+fw_distance2*(math.cos(math.radians(j*10-6))), int(fw_y_list[2] - 880 + fw_distance2*(math.sin(math.radians(j*10-6)))), 8, 8))
                    pygame.draw.rect(screen, firework_colour_list[i][j], pygame.Rect(fw_x_list[i]+fw_distance3*(math.cos(math.radians(j*10))), int(fw_y_list[i] - 880 + fw_distance3*(math.sin(math.radians(j*10)))), 8, 8))
        '''

        if fw_time < 59.9:
            break

        #
        #    pygame.draw.rect(screen, fw_colour, pygame.Rect(fw_x_list[0], fw_y_list[0] - 880, 118, 118))
        
        pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption('TDICE')

sqwidth = 212
sqheight = 142
x = 0
y = 0
x_pos = 0
y_pos = 0
x_posd = 0
y_posd = 0
panelcolour = (236, 236, 236)
grey = (172, 172, 172)
darkgrey = (88, 88, 88)
verydarkgrey = (62, 62, 66)
highlighted = (236, 236, 236)
#white = (252, 252, 252)
green_bar = (0, 202, 88)
red_bar = (202, 0, 88)
battle_colour = (44, 46, 58)
dice_red = (222, 72, 42)
logcolour = (68, 70, 88)
rulescolour = (88, 76, 88)
midnight = (26, 40, 72)
sapphire = (22, 36, 66)

player_sq_num = [3,4,5]
sq_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

colour_list = [(168, 34, 38), (152, 80, 48), (198, 178, 38), (132, 168, 42), (32, 104, 100), (46, 88, 168), (108, 32, 108), (204, 92, 32), (16, 138, 150), (100, 78, 50), (185, 90, 138), (128, 164, 146)]                     

hi_colour_list = [(200, 22, 28), (202, 112, 32), (216, 202, 72), (152, 182, 22), (62, 142, 134), (82, 112, 182), (138, 24, 116), (218, 136, 60), (90, 164, 174), (124, 98, 64), (204, 116, 160), (154, 188, 172)]

trail_list = [(250, 212, 226), (255, 246, 152), (196, 218, 78), (220, 200, 226), (246, 176, 136), (212, 228, 238), (248, 198, 182), (212, 228, 212), (238, 196, 206), (212, 212, 192), (232, 202, 212), (248, 198, 182), (255, 252, 200)]

dice_num = [1,2,3,4,5,6]
empty_dice_num = [1,2,3,4]
empty_sq_num = [3,4,5,6,7,8]

p1_area_list = []

p1_sq_list = []

new_game = False

end_turn_button = False

attacking_mode = False

pause_hovering = False

clicking_pair = []

playing = False

current_turn = 0

timeleftunit = 120
timeleftunit1 = 120

turn_list = [1, 2, 3, 4, 5, 6, 7]

active_players = [0,12,12,12,12,12,12,12] #length is 8 for 1-7 to be used directly, using arbitrary "12" to set apart from all the 1s

turn_number = 0

gamelog = []

pxlen = [0,0,0,0,0,0,0,0]

px_sq_count_list = [0, 0, 0, 0, 0, 0, 0, 0]

dimmmer_switch = True

fw_colour_list = [[],[],[],[],[],[]]

fw_angle_list = [[],[],[],[],[],[]]

firework_distance_list = [[],[],[],[],[],[]]

fw_hyp_list = [[],[],[],[],[],[]]

fw_trail_list = [[],[],[],[],[],[]]

fw_quantity = []

more_fireworks = False

fw_time = 240

temp_running_player_list = []
temp_running_dice_list = []

pygame.draw.rect(screen, panelcolour, pygame.Rect(0, 0, 1920, 1080)) #background

player_name_font = pygame.font.Font('freesansbold.ttf', 68)
title_font = pygame.font.Font('freesansbold.ttf', 68)
button_font = pygame.font.Font('freesansbold.ttf', 32)
log_font = pygame.font.Font('freesansbold.ttf', 20)
rules_font = pygame.font.Font('freesansbold.ttf', 30)

rules = ["Welcome to TDICE,", "an offline single-player", "replica of KDICE,", "available at kdice.com.", "The rules are simple:", 
                "each square has", "anywhere from 1-8 dice.", "You are P1 and you can", "attack your opponents", "when you have two or", "more dice in a square.",
                                                            "Conquer the whole map,", "you shall be the winner.", "Click New Game to begin.", "Good luck!"]

for i in range(0,15):
    rules_surface = rules_font.render(rules[i], True, rulescolour) 
    rules_rect = rules_surface.get_rect(midleft = (36, 208+42*i)) 
    screen.blit(rules_surface, rules_rect)

title_surface = title_font.render("TDICE", True, panelcolour) #(88, 88, 88)
title_rect = title_surface.get_rect(midleft = (36, 125))  #+16

game_title()

#new game button
pygame.draw.rect(screen, (196, 92, 92), pygame.Rect(1766, 28, 120, 120))
new_game_surface_1 = button_font.render("NEW", True, panelcolour) 
new_game_surface_rect_1 = new_game_surface_1.get_rect(midleft = (1768, 110))
new_game_surface_2 = button_font.render("GAME", True, panelcolour) 
new_game_surface_rect_2 = new_game_surface_2.get_rect(midleft = (1768, 136))
screen.blit(new_game_surface_1, new_game_surface_rect_1)
screen.blit(new_game_surface_2, new_game_surface_rect_2)

#pause and resume game button
pause_surface_1 = button_font.render("PAUSE", True, panelcolour) 
pause_surface_rect_1 = pause_surface_1.get_rect(midleft = (1768, 1024))
pause_surface_2 = button_font.render("GAME", True, panelcolour) 
pause_surface_rect_2 = pause_surface_2.get_rect(midleft = (1768, 1050))

resume_surface_1 = button_font.render("PLAY", True, panelcolour) 
resume_surface_rect_1 = resume_surface_1.get_rect(midleft = (1768, 1024))

#end game button
end_turn_surface_1 = button_font.render("END", True, panelcolour) 
end_turn_surface_rect_1 = end_turn_surface_1.get_rect(midleft = (1768, 874))
end_turn_surface_2 = button_font.render("TURN", True, panelcolour) 
end_turn_surface_rect_2 = end_turn_surface_2.get_rect(midleft = (1768, 900))

running_lists()

while True:
    
    if playing == True:

        if sum(active_players) > 12:

            timeleftunit -= 1/30
            timeleftunit = int(timeleftunit)

            if timeleftunit <= 1/30:
                timeleftunit = 0
                end_turn_addup(current_turn)
                current_turn += 1
                if current_turn == 8:
                    current_turn = 1
                if current_turn != 1:

                    ai_result = aigaming(current_turn)
                    ai_round_list = ai_result[0]

                    temp_running_player_list = ai_result[1]
                    temp_running_dice_list = ai_result[2]

                    #print(running_player_list)
                    #print(temp_running_player_list)
                    #print(running_dice_list)
                    #print(temp_running_dice_list)

                    #ai_stage2(current_turn, temp_running_player_list, temp_running_dice_list)
                                        
                if active_players[current_turn] > 0:
                    timeleftunit = 120
                else:
                    timeleftunit = 0

            if current_turn == 1:
                #pygame.draw.rect(screen, (int(panelcolour[0] - (((236-26)/8)*(timeleftunit/(120/9)))), int(panelcolour[1] - (((236-40)/8)*(timeleftunit/(120/9)))), int(panelcolour[2] - (((236-72)/8)*(timeleftunit/(120/9))))), pygame.Rect(0, 0, 1920, 1080))
                if sum(active_players) > 12:
                    if timeleftunit > 36:
                        pygame.draw.rect(screen, green_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))
                    elif timeleftunit > 32:
                        bar_colour_one = int(202-(202/4)*(timeleftunit-32))
                        bar_colour_two = int(0 + (202/4)*(timeleftunit-32))
                        pygame.draw.rect(screen, (bar_colour_one, bar_colour_two, 88), pygame.Rect(232 + 197 * current_turn, 148, 120, 12))
                    else:
                        pygame.draw.rect(screen, red_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))
                
                #bar_colour_one = int(232-232/120*timeleftunit)
                #bar_colour_two = int(0 + 232/120*timeleftunit)

                #pygame.draw.rect(screen, (bar_colour_one, bar_colour_two, 0), pygame.Rect(232 + 197 * current_turn, 148, 120, 12))

                pygame.draw.rect(screen, panelcolour, pygame.Rect(232 + 197 * current_turn + 120 - (120-timeleftunit), 148, 120-timeleftunit, 12))
                pygame.draw.rect(screen, panelcolour, pygame.Rect(232 + 197 * current_turn - 197 - 3, 148, 6, 12))

                if current_turn != 7:
                    pygame.draw.rect(screen, panelcolour, pygame.Rect(429+197*6 - 3, 148, 6, 12))
            else:
                ai_round_action_num = len(ai_round_list)
                
                if ai_round_action_num > 0:

                    #reaction_time1 = [88, 98, 102]
                    #picked_reaction_time1 = random.choice(reaction_time1)
                    #reaction_time2 = [62, 68]
                    #picked_reaction_time2 = random.choice(reaction_time2)
                    
                    if timeleftunit == 96:
                        ai_processing_one(ai_round_list[0], current_turn)
                    if timeleftunit == 68:
                        ai_processing_two(ai_round_list[0], current_turn)

                        #if temp_running_dice_list == running_dice_list:
                        #    print("Dice lists same")
                        #else:
                        #    print("Dice lists different")
                        #    print(running_dice_list)
                        #    print(temp_running_dice_list)

                        #if running_dice_list == temp_running_dice_list:
                        #    pass
                        #else:
                            #print("running_dice_list")
                            #print(running_dice_list)
                            #print("temp_running_dice_list")
                            #print(temp_running_dice_list)

                            #for i in range(0, 37):
                                #if running_dice_list[i] != temp_running_dice_list[i]:
                                    #running_dice_list[i] = temp_running_dice_list[i]
                                    #pass
                                    #print(str(i)+" is different among the lists... running is "+str(running_dice_list[i])+" and temp is "+str(temp_running_dice_list[i]))

                        #for x in range(1,37):
                        #    print(running_dice_list.index(running_dice_list[x]))

                        #for x in running_dice_list:
                        #    print(running_dice_list.index(x))

                        #for x in running_dice_list:
                        #    if x == 0:
                        #        print(running_dice_list.index(x))
                                #pass

                        '''
                        if running_player_list == temp_running_player_list:
                            print("Player lists identical")
                        else:
                            print("Player lists not identical")
                            print("running_player_list")
                            print(running_player_list)
                            print("temp_running_player_list")
                            print(temp_running_player_list)

                        if running_dice_list == temp_running_dice_list:
                            print("Dice lists identical")
                        else:
                            print("Dice lists not identical")
                            print("running_dice_list")
                            print(running_dice_list)
                            print("temp_running_dice_list")
                            print(temp_running_dice_list)
                        '''

                        timeleftunit = 120

                        ai_round_action_num -= 1

                        del ai_round_list[0]

                #if timeleftunit > 36:
                #    pygame.draw.rect(screen, green_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))
                #else:
                #    pygame.draw.rect(screen, red_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))

                if sum(active_players) > 12:
                    if timeleftunit > 36:
                        pygame.draw.rect(screen, green_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))
                    elif timeleftunit > 32:
                        bar_colour_one = int(202-(202/4)*(timeleftunit-32))
                        bar_colour_two = int(0 + (202/4)*(timeleftunit-32))
                        pygame.draw.rect(screen, (bar_colour_one, bar_colour_two, 88), pygame.Rect(232 + 197 * current_turn, 148, 120, 12))
                    else:
                        pygame.draw.rect(screen, red_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))

                    pygame.draw.rect(screen, panelcolour, pygame.Rect(232 + 197 * current_turn + 120 - (120-timeleftunit), 148, 120-timeleftunit, 12))
                    pygame.draw.rect(screen, panelcolour, pygame.Rect(232 + 197 * current_turn - 197 - 3, 148, 6, 12))

                    if current_turn != 7:
                        pygame.draw.rect(screen, panelcolour, pygame.Rect(429+197*6 - 3, 148, 6, 12))

        for player in range(2,8):
            if sum(active_players) > 12:
                p27_list = [i for i, x in enumerate(running_player_list) if x == player]
                if len(p27_list) == 0:
                    active_players[player] = 0
                    pygame.draw.rect(screen, panelcolour, pygame.Rect(429-197+197*player, 28, 120, 120))  

        if len(p1_sq_list) == 0:
            new_game = True
            playing = True
            timeleftunit = 120
            new_game_setup()

        #Player 1 wins
        if sum(active_players) == 12 and active_players[1] == 12:

            timeleftunit = 240
            while timeleftunit > 0 and dimmmer_switch == True:
                #pygame.time.delay(88)
                timeleftunit -= 1/30
                timeleftunit = int(timeleftunit)
                #entire background
                pygame.draw.rect(screen, (int((210/240)*timeleftunit+26), int((196/240)*timeleftunit+40), int((164/240)*timeleftunit+72)), pygame.Rect(0, 0, 1920, 1080))

                #title part
                pygame.draw.rect(screen, (int((112/240)*timeleftunit+22), int((108/240)*timeleftunit+36), int((72/240)*timeleftunit+66)), pygame.Rect(35, 28, 359, 120)) #sapphire
                title_surface = title_font.render("TDICE", True, verydarkgrey) #(88, 88, 88)
                title_rect = title_surface.get_rect(midleft = (36, 125))  #+16
                screen.blit(title_surface, title_rect)

                d1 = running_colour_list[1][0]
                d2 = running_colour_list[1][1]
                d3 = running_colour_list[1][2]

                #size bar
                pygame.draw.rect(screen, (int(((d1-22)/240)*timeleftunit+22), int(((d2-36)/240)*timeleftunit+36), int(((d3-66)/240)*timeleftunit+66)), pygame.Rect(35, 158, 359, 20)) # to (26, 40, 72)

                #p1 square
                pygame.draw.rect(screen, (int(((d1-22)/240)*timeleftunit+22), int(((d2-36)/240)*timeleftunit+36), int(((d3-66)/240)*timeleftunit+66)), pygame.Rect(429, 28, 120, 120))  

                p1_name_surface = player_name_font.render("P1", True, (int((210/240)*timeleftunit+26), int((196/240)*timeleftunit+40), int((164/240)*timeleftunit+72))) #(232, 232, 232)
                p1_name_rect = p1_name_surface.get_rect(midleft = (426, 125)) #410 for left #464 for right
                screen.blit(p1_name_surface, p1_name_rect)

                #new game button
                new_game_surface_1 = button_font.render("NEW", True, (int((148/240)*timeleftunit+88), int((148/240)*timeleftunit+88), int((148/240)*timeleftunit+88))) 
                new_game_surface_rect_1 = new_game_surface_1.get_rect(midleft = (1768, 110))
                new_game_surface_2 = button_font.render("GAME", True, (int((148/240)*timeleftunit+88), int((148/240)*timeleftunit+88), int((148/240)*timeleftunit+88))) 
                new_game_surface_rect_2 = new_game_surface_2.get_rect(midleft = (1768, 136))

                pygame.draw.rect(screen, (int((174/240)*timeleftunit+22), int((56/240)*timeleftunit+36), int((26/240)*timeleftunit+66)), pygame.Rect(1766, 28, 120, 120)) #196, 92, 92
                screen.blit(new_game_surface_1, new_game_surface_rect_1)
                screen.blit(new_game_surface_2, new_game_surface_rect_2)

                #pause game button
                pause_surface_1 = button_font.render("PAUSE", True, (int((210/240)*timeleftunit+26), int((196/240)*timeleftunit+40), int((164/240)*timeleftunit+72))) 
                pause_surface_rect_1 = pause_surface_1.get_rect(midleft = (1768, 1024))
                pause_surface_2 = button_font.render("GAME", True, (int((210/240)*timeleftunit+26), int((196/240)*timeleftunit+40), int((164/240)*timeleftunit+72))) 
                pause_surface_rect_2 = pause_surface_2.get_rect(midleft = (1768, 1050))

                pygame.draw.rect(screen, (int((-22/240)*timeleftunit+22), int((26/240)*timeleftunit+36), int((50/240)*timeleftunit+66)), pygame.Rect(1766, 942, 120, 120)) 
                screen.blit(pause_surface_1, pause_surface_rect_1)
                screen.blit(pause_surface_2, pause_surface_rect_2)

                #end turn button
                end_turn_surface_1 = button_font.render("END", True, (int((210/240)*timeleftunit+26), int((196/240)*timeleftunit+40), int((164/240)*timeleftunit+72))) 
                end_turn_surface_rect_1 = end_turn_surface_1.get_rect(midleft = (1768, 874))
                end_turn_surface_2 = button_font.render("TURN", True, (int((210/240)*timeleftunit+26), int((196/240)*timeleftunit+40), int((164/240)*timeleftunit+72))) 
                end_turn_surface_rect_2 = end_turn_surface_2.get_rect(midleft = (1768, 900))

                pygame.draw.rect(screen, (int((56/240)*timeleftunit+22), int((66/240)*timeleftunit+36), int((6/240)*timeleftunit+66)), pygame.Rect(1766, 792, 120, 120)) #(78, 102, 72)
                screen.blit(end_turn_surface_1, end_turn_surface_rect_1)
                screen.blit(end_turn_surface_2, end_turn_surface_rect_2)

                #all p1's squares and dice
                for i in range(1,37):
                    if running_dice_list[i] > 0:
                        d1 = running_colour_list[1][0]
                        d2 = running_colour_list[1][1]
                        d3 = running_colour_list[1][2]
                        draw_squares([i], (int(((d1-22)/240)*timeleftunit+22), int(((d2-36)/240)*timeleftunit+36), int(((d3-66)/240)*timeleftunit+66))) #sapphire 
                    if running_dice_list[i] > 0:
                        draw_dice(i, running_dice_list[i], celebrating=True, celebrating_colour = (int((174/240)*timeleftunit+62), int((174/240)*timeleftunit+62), int((170/240)*timeleftunit+66)))
                
                #pygame.draw.rect(screen, panelcolour, pygame.Rect(22, 190, 400, 920)) 

                for i in range(len(gamelog)):
                    log_surface = log_font.render(str(gamelog[i][0]), True, (int((42/240)*timeleftunit+26), int((30/240)*timeleftunit+40), int((16/240)*timeleftunit+72))) 
                    log_rect = log_surface.get_rect(midleft = (32, btmline-80*i)) 
                    screen.blit(log_surface, log_rect)
                    log_surface = log_font.render(str(gamelog[i][1]), True, (int((42/240)*timeleftunit+26), int((30/240)*timeleftunit+40), int((16/240)*timeleftunit+72))) 
                    log_rect = log_surface.get_rect(midleft = (32, btmline+22-80*i)) 
                    screen.blit(log_surface, log_rect)
                    log_surface = log_font.render(str(gamelog[i][2]), True, (int(((gamelog[i][-1][0]-26)/240)*timeleftunit+26), int(((gamelog[i][-1][1]-40)/240)*timeleftunit+40), int(((gamelog[i][-1][2]-72)/240)*timeleftunit+72))) #gamelog[i][-1]
                    log_rect = log_surface.get_rect(midleft = (32, btmline+44-80*i)) 
                    screen.blit(log_surface, log_rect)

                pygame.display.update()
                #clock.tick(36)

            if timeleftunit <= 1/30:
                more_fireworks = True
                dimmmer_switch = False
                gamelog = []

                print("Time for fireworks")

                fw_x_list = []
                fw_y_list = []
                for i in range(0,1):
                    #fw_x_list.append(random.randint(120+280*i, 400+280*i))
                    fw_x_list.append(960)
                for i in range(0,1):
                    fw_y_list.append(1080+random.randint(-60,220))
                if len(running_colour_list) > 1:
                    fw_colour = running_colour_list[1]
                else:
                    fw_colour = green_bar

                fireworks(fw_x_list, fw_y_list, fw_colour)
                        
    if new_game == True:
        initial_setup()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                
                fw_x_list = []
                fw_y_list = []
                for i in range(0,1):
                    fw_x_list.append(960)
                    #fw_x_list.append(random.randint(820, 1020)) # for 6 is 120+280*i, 400+280*i
                for i in range(0,1):
                    fw_y_list.append(1080+36+random.randint(-60,220))
                if len(running_colour_list) > 1:
                    fw_colour = running_colour_list[1]
                else:
                    fw_colour = green_bar
                
                fireworks(fw_x_list, fw_y_list, fw_colour)
            
            if event.key == pygame.K_SPACE:
                if playing == True:
                    playing = False
                else:
                    playing = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.button == 2:
                print("Right click")
            #New game pressed
            if 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 28 <= pygame.mouse.get_pos()[1] <= 148:
                pygame.draw.rect(screen, panelcolour, pygame.Rect(0, 0, 1920, 1080))
                game_title()
                new_game = True
                playing = True
                running_lists()
                timeleftunit = 120
                new_game_setup()
                active_players = [0,12,12,12,12,12,12,12]
                gamelog = []
                dimmmer_switch = True

                #new game button colour reset
                new_game_surface_1 = button_font.render("NEW", True, panelcolour) 
                new_game_surface_2 = button_font.render("GAME", True, panelcolour) 

                #pause and resume game button colour reset
                pause_surface_1 = button_font.render("PAUSE", True, panelcolour) 
                pause_surface_2 = button_font.render("GAME", True, panelcolour) 

                #end game button colour reset
                end_turn_surface_1 = button_font.render("END", True, panelcolour) 
                end_turn_surface_2 = button_font.render("TURN", True, panelcolour) 
                
            #Pause game pressed
            if 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 942 <= pygame.mouse.get_pos()[1] <= 1062 and sum(active_players) > 12:
                if playing == True:
                    playing = False
                else:
                    playing = True

            if current_turn == 1 and playing == True:
                recognize_sq()
                #print("Just clicked "+str(hover_sq_num))
                # and 1071 >= pygame.mouse.get_pos()[1] >= 189 and 429 <= pygame.mouse.get_pos()[0] <= 1731
                if 1071 >= pygame.mouse.get_pos()[1] >= 189 and 429 <= pygame.mouse.get_pos()[0] <= 1731:
                    if hover_sq_num in p1_sq_list:
                        if len(clicking_pair) == 0 and running_dice_list[hover_sq_num] > 1:
                            timeleftunit = 120
                            pause_hovering = True
                            #hover_sq_list = []
                            #hover_sq_list.append(hover_sq_num)
                            clicking_pair.append(hover_sq_num)
                            #print("Clean slate, can attack")

                            #attacking_mode = True
                            #print(clicking_pair)
                            draw_squares([hover_sq_num], battle_colour)
                            draw_dice(hover_sq_num, running_dice_list[hover_sq_num], True)
                            #attacking_mode = False
                        else:
                            #print("Checking pair numbers:")
                            #print(clicking_pair)
                            
                            #attacking_mode = False
                            #print("Can't attack since it's against own square")
                            pause_hovering = False
                            attacking_mode = False
                            clicking_pair = []
                    else:
                        if len(clicking_pair) == 1 and running_player_list[hover_sq_num] != "n":
                            timeleftunit = 120
                            pause_hovering = True
                            #print("Already has P1, now is attacking another non P1 square")
                            #hover_sq_list = []
                            #hover_sq_list.append(hover_sq_num)
                            neighbour = False
                            clicking_pair.append(hover_sq_num)
                            
                            x1 = clicking_pair[0]%6
                            if x1 == 0:
                                x1 = 6
                            y1 = (clicking_pair[0]+5)//6

                            x2 = clicking_pair[1]%6
                            if x2 == 0:
                                x2 = 6
                            y2 = (clicking_pair[1]+5)//6

                            if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
                                neighbour = True
                                #attacking_mode = True
                                draw_squares([hover_sq_num], battle_colour)
                                draw_dice(hover_sq_num, running_dice_list[hover_sq_num], True)
                                
                                dice1 = running_dice_list[clicking_pair[0]]
                                dice2 = running_dice_list[clicking_pair[1]]

                                dice_list1 = []
                                dice_list2 = []

                                dicesum1 = 0
                                dicesum2 = 0

                                while dice1>0:
                                    roll1 = 6 #cheating was random.randint(1,6)
                                    dicesum1 += roll1
                                    dice_list1.append(roll1)
                                    dice1 -= 1
                                while dice2>0:
                                    if p1_sq_count > 18:
                                        roll2 = 1 #cheating was random.randint(2,6)
                                    else:
                                        roll2 = random.randint(1,6)
                                    dicesum2 += roll2
                                    dice_list2.append(roll2)
                                    dice2 -= 1
                                
                                str1 = "P"+str(running_player_list[clicking_pair[0]])+" rolled a "+str(dicesum1)+" with "+str(dice_list1).strip("[]")
                                if running_player_list[clicking_pair[1]] != 0:
                                    str2 = "P"+str(running_player_list[clicking_pair[1]])+" rolled a "+str(dicesum2)+" with "+str(dice_list2).strip("[]")
                                else:
                                    str2 = "Grey rolled a "+str(dicesum2)+" with "+str(dice_list2).strip("[]")

                                #print("running_player_list Right before attack")
                                #print(running_player_list)

                                if dicesum1 > dicesum2:
                                    #print("Player 1 wins")
                                    #str3 = "P"+str(running_player_list[clicking_pair[0]])+" wins"
                                    str3 = "P"+str(running_player_list[clicking_pair[0]])+" conquered"
                                    winner_colour = running_colour_list[running_player_list[clicking_pair[0]]]  #winner_colour = 
                                    attacking_mode = False
                                    running_player_list[clicking_pair[1]] = 1
                                    running_dice_list[clicking_pair[1]] = running_dice_list[clicking_pair[0]]-1
                                    running_dice_list[clicking_pair[0]] = 1
                                    draw_squares([clicking_pair[1]], p1_colour)
                                    draw_dice(clicking_pair[1], running_dice_list[clicking_pair[1]])
                                    draw_squares([clicking_pair[0]], p1_colour)
                                    draw_dice(clicking_pair[0], running_dice_list[clicking_pair[0]])
                                    
                                    #p1_sq_list.append(clicking_pair[1])
                                    #print("running_player_list Right after attack")
                                    #print(running_player_list)
                                    clicking_pair = []
                                    pause_hovering = False

                                    #if sum(active_players) == 12:
                                        #pygame.time.delay(888)
                                    #    playing = False
                                    #    victory_animation(120)
                                    #    break

                                else:
                                    #print("Player 2 wins")
                                    if running_player_list[clicking_pair[1]] != 0:
                                        #str3 = "P"+str(running_player_list[clicking_pair[1]])+" wins"
                                        str3 = "P"+str(running_player_list[clicking_pair[1]])+" defended"
                                    else:
                                        #str3 = "Grey wins"
                                        str3 = "Grey defended"
                                    winner_colour = running_colour_list[running_player_list[clicking_pair[1]]]
                                    attacking_mode = False
                                    draw_squares([clicking_pair[1]], running_colour_list[running_player_list[clicking_pair[1]]])
                                    draw_dice(clicking_pair[1], running_dice_list[clicking_pair[1]])
                                    running_dice_list[clicking_pair[0]] = 1
                                    draw_squares([clicking_pair[0]], p1_colour)
                                    draw_dice(clicking_pair[0], 1)
                                    clicking_pair = []
                                    pause_hovering = False

                                #clicking_pair = []
                            else:
                                neighbour = False
                                attacking_mode = False
                                #print("Need to clean up")
                                clicking_pair = []
                                pause_hovering = False
                            #print("Entering attacking mode")
                            #print(clicking_pair)
                        #elif attacking_mode == False and len(clicking_pair) == 2:
                            
                        else:
                            if len(clicking_pair) == 0:
                                pass
                                #First square isn't P1, won't work
                                
                            else:
                                pass
                                #Won't work, need to clean up

                            attacking_mode = False    
                            pause_hovering = False
                            clicking_pair = []
                        try:
                            if playing == True:
                                gamelog.insert(0, [str1, str2, str3, winner_colour])
                                #gamelog.insert(0, round_result)
                                if len(gamelog) > 11:
                                    del gamelog[-1]

                                btmline = 1008

                                pygame.draw.rect(screen, panelcolour, pygame.Rect(22, 190, 400, 920)) 

                                for i in range(len(gamelog)):
                                    log_surface = log_font.render(str(gamelog[i][0]), True, logcolour) 
                                    log_rect = log_surface.get_rect(midleft = (32, btmline-80*i)) 
                                    screen.blit(log_surface, log_rect)
                                    log_surface = log_font.render(str(gamelog[i][1]), True, logcolour) 
                                    log_rect = log_surface.get_rect(midleft = (32, btmline+22-80*i)) 
                                    screen.blit(log_surface, log_rect)
                                    log_surface = log_font.render(str(gamelog[i][2]), True, gamelog[i][-1]) 
                                    log_rect = log_surface.get_rect(midleft = (32, btmline+44-80*i)) 
                                    screen.blit(log_surface, log_rect)
                        except NameError:
                            pass
            #end turn button pressed
            if current_turn == 1 and 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 912 >= pygame.mouse.get_pos()[1] >= 792 and sum(active_players) > 12:
                timeleftunit = 0
                pygame.draw.rect(screen, panelcolour, pygame.Rect(426, 148, 126, 12)) 
                end_turn_addup(1)
                playing = True
                pygame.draw.rect(screen, (46, 72, 116), pygame.Rect(1766, 942, 120, 120))
                screen.blit(pause_surface_1, pause_surface_rect_1)
                screen.blit(pause_surface_2, pause_surface_rect_2)

    hovering_new_game_button()

    if current_turn == 1:
        hovering_end_turn_button()
    elif current_turn == 2:
        pygame.draw.rect(screen, panelcolour, pygame.Rect(1766, 792, 120, 120))

    hovering_pause_button(playing)

    p1_sq_list = [i for i, x in enumerate(running_player_list) if x == 1]
    
    if 1071 >= pygame.mouse.get_pos()[1] >= 189 and 429 <= pygame.mouse.get_pos()[0] <= 1731:
        recognize_sq()
    else:
        hover_sq_num = -1

    if attacking_mode == False and pause_hovering == False and sum(active_players) != 12:
        if hover_sq_num in p1_sq_list:
            #print(hover_sq_num)
            #hover_sq_list = []
            #just_hovered_sq_list = []
            #hover_sq_list.append(hover_sq_num)
            #previous_hovered_sq_num = hover_sq_num
            #just_hovered_sq_list.append(just_hovered_sq_num)
            draw_squares([x for i,x in enumerate(p1_sq_list) if i!=hover_sq_num], p1_colour)
            draw_squares([hover_sq_num], p1_hi_colour)
            #print(running_dice_list[hover_sq_num])
            #draw_dice(hover_sq_list[0], running_dice_list[hover_sq_num])
            for i in p1_sq_list:
                draw_dice(i, running_dice_list[i])

        else:
            #if previous_hovered_sq_num != hover_sq_num:
            #print("Not hovering")
            #print(p1_sq_list)
            draw_squares(p1_sq_list, p1_colour)
            for i in p1_sq_list:
                draw_dice(i, running_dice_list[i])

    #print(running_colour_list)
    #print(running_dice_list)
    #print(running_player_list)

    if sum(active_players) > 12:
        for q in range(1, 8):
            px_sq_count_list[q] = len([i for i, x in enumerate(running_player_list) if x == q])
        
        p1_sq_count = px_sq_count_list[1]

        all7len = sum(px_sq_count_list) 
        
        if all7len > 0:
            
            for i in range(1,8):
                pxlen[i] = int((int(px_sq_count_list[i])/all7len)*360)

            sumof7 = sum(pxlen)

            if sumof7 > 359:
                pxlen[1] -= sumof7 -359
                sumof7 = 359
            elif sumof7 < 359:
                pxlen[1] += 359 - sumof7
                sumof7 = 359

            for i in range(1,8):
                pygame.draw.rect(screen, running_colour_list[i], pygame.Rect(35+sum(pxlen[:i]), 158, pxlen[i], 20)) 

            for i in range(2,8):
                if i == 0:
                    active_players[int(str(i)[-1])] = 0

    pygame.display.update()
    clock.tick(18)
