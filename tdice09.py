import pygame, sys, random, time

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

    #global clicking_pair

    empty_sq = 0
    empty_sq_list = []

    temp_list = []
    temp_key_list = []

    px_sq = [[],[],[],[],[],[],[]]
    px_sq_num = [0, 0, 0, 0, 0, 0, 0]
    px_colour = [None, None, None, None, None, None, None]

    dice_for_sq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    colour_list = [(168, 34, 38), (152, 80, 48), (198, 178, 38), (132, 168, 42), (32, 104, 100), (46, 88, 168), (108, 32, 108)]     
    sq_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

    current_sq = 0

    p1_turn = True

    hover_sq_list = []

    #p1_colour = None
    #p1_hi_colour = None

    just_hovered_sq_num = 0

    #running_colour_list = [(0,0,0)]
    #running_dice_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #running_player_list = [0,"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]

    game_sq_list = sq_list
    game_colour_list = colour_list

    #end_turn_button = False
    
    #global currently_attacking
    #currently_attacking == False

    global clicking_pair
    clicking_pair = []

    p1_colour = None
    p1_hi_colour = None

    #should be zero*****
    current_turn = 1

    dice_colour = white

    pygame.draw.rect(screen, panelcolour, pygame.Rect(35, 200, 359, 920)) 
    gamelog = []

def draw_squares(square1, colour1):
    for i in square1:
        x = i%6
        if x == 0:
            x = 6
        y = (i+5)//6
        x_pos = x*(sqwidth+6) + 423 - sqwidth
        y_pos = y*(sqheight+6) + 183 - sqheight
        pygame.draw.rect(screen, colour1, pygame.Rect(x_pos, y_pos, sqwidth, sqheight)) 

def draw_dice(squarenumber, numberofdice, attacking_mode = False): 
    if numberofdice > 8:
        numberofdice == 8
    if attacking_mode == False:
        dice_colour = white
    else:
        dice_colour = dice_red

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
        x_posd = x1*(sqwidth+6) + 722 -212 -10 + 6 - sqwidth
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
        #else:
        #    pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+40, 18, 18)) 
        #    pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd+20, 18, 18))
        #    pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd, 18, 18))    
        #    pygame.draw.rect(screen, dice_colour, pygame.Rect(x_posd, y_posd-20, 18, 18))

def hovering_new_game_button():
    if 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 28 <= pygame.mouse.get_pos()[1] <= 148:
        pygame.draw.rect(screen, (222, 108, 132), pygame.Rect(1766, 28, 120, 120)) 
        screen.blit(new_game_surface_1, new_game_surface_rect_1)
        screen.blit(new_game_surface_2, new_game_surface_rect_2)
    else:
        pygame.draw.rect(screen, (196, 92, 92), pygame.Rect(1766, 28, 120, 120)) 
        screen.blit(new_game_surface_1, new_game_surface_rect_1)
        screen.blit(new_game_surface_2, new_game_surface_rect_2)

def hovering_end_turn_button():
    #print(end_turn_button)
    if end_turn_button == True:
        #print("End turn button hovering")
        if 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 942 <= pygame.mouse.get_pos()[1] <= 1062:
            pygame.draw.rect(screen, (100, 114, 92), pygame.Rect(1766, 942, 120, 120))  #(92, 112, 88)
            screen.blit(end_turn_surface_1, end_turn_surface_rect_1)
            screen.blit(end_turn_surface_2, end_turn_surface_rect_2)
        else:
            pygame.draw.rect(screen, (78, 102, 72), pygame.Rect(1766, 942, 120, 120)) 
            screen.blit(end_turn_surface_1, end_turn_surface_rect_1)
            screen.blit(end_turn_surface_2, end_turn_surface_rect_2)

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

    p1_sq_count=0
    p2_sq_count=0
    p3_sq_count=0
    p4_sq_count=0
    p5_sq_count=0
    p6_sq_count=0
    p7_sq_count=0
    
    pygame.draw.rect(screen, panelcolour, pygame.Rect(32, 156, 370, 16)) 

    active_players = [0,12,12,12,12,12,12,12]

    turn_list = [1, 2, 3, 4, 5, 6, 7]

    turn_number = 0

    current_turn = 0

    timeleftunit = 120

    #new_game = True

    playing = True

    if new_game == True:

        playing = True

        current_turn = 1

        attacking_mode = False
        #dice_colour = white

        #active_players = [0,12,12,12,12,12,12,12]

        running_colour_list = [(172, 172, 172)]
        running_dice_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        running_player_list = [0,"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]

        pygame.draw.rect(screen, panelcolour, pygame.Rect(22, 190, 400, 920)) 
        gamelog = []

        #Reset all 36 squares
        draw_squares(game_sq_list, panelcolour)

        for i in range(0,7):
            px_sq_num[i] = random.choice(player_sq_num)
            px_colour[i] = game_colour_list.pop(random.randrange(len(game_colour_list)))
            while px_sq_num[i] > 0:
                (px_sq[i]).append(game_sq_list.pop(random.randrange(len(game_sq_list))))
                px_sq_num[i] -= 1

        for i in range(0,7):
            #print("Entering building function:")
            #print((i+1), px_sq[i], px_colour[i])
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
                running_player_list[game_sq_list[0]] = 0                                                # was "e" and changed to 0
                draw_squares([game_sq_list[0]], grey)
                draw_dice(game_sq_list[0],new_dice)
                del game_sq_list[0]

        #print("This is the dice list")
        #print(running_dice_list)

        for i in range(1,37):
            draw_dice(i, running_dice_list[i])

        for i in range(1,8):
            #print(running_colour_list)
            pygame.draw.rect(screen, running_colour_list[1], pygame.Rect(429, 28, 120, 120))  
            pygame.draw.rect(screen, running_colour_list[2], pygame.Rect(429+197*1, 28, 120, 120)) 
            pygame.draw.rect(screen, running_colour_list[3], pygame.Rect(429+197*2, 28, 120, 120)) 
            pygame.draw.rect(screen, running_colour_list[4], pygame.Rect(429+197*3, 28, 120, 120)) 
            pygame.draw.rect(screen, running_colour_list[5], pygame.Rect(429+197*4, 28, 120, 120)) 
            pygame.draw.rect(screen, running_colour_list[6], pygame.Rect(429+197*5, 28, 120, 120)) 
            pygame.draw.rect(screen, running_colour_list[7], pygame.Rect(429+197*6, 28, 120, 120))  

            #end turn button
            #hover colour could be (92, 112, 88)
            pygame.draw.rect(screen, (78, 102, 72), pygame.Rect(1766, 942, 120, 120)) #main colour (78, 102, 72)

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

    screen.blit(end_turn_surface_1, end_turn_surface_rect_1)
    screen.blit(end_turn_surface_2, end_turn_surface_rect_2)

    p1_colour = running_colour_list[1]
    p1_hi_colour = hi_colour_list[colour_list.index(running_colour_list[1])]
    #print(p1_colour)
    #print(p1_hi_colour)

    p2_sq_list = []
    p3_sq_list = []
    p4_sq_list = []
    p5_sq_list = []
    p6_sq_list = []
    p7_sq_list = []

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
    #print(running_colour_list[current_turn])
    #print(running_player_list)
    #print(running_dice_list)

    end_turn_sq_list = []
    end_turn_sq_list_copy = []
    end_turn_sq_list_eliminite_8 = []
    end_turn_sq_list = [i for i, x in enumerate(running_player_list) if x == current_turn]
    end_turn_sq_list_copy = [i for i, x in enumerate(running_player_list) if x == current_turn]
    end_turn_sq_list_eliminite_8 = [i for i, x in enumerate(running_player_list) if x == current_turn]
    random_square_in_list = None

    #print(end_turn_sq_list)

    #too crowded
    #number_of_dice_to_add = len(end_turn_sq_list)

    #test
    number_of_dice_to_add = 1

    compare_1 = []
    compare_2 = []

    while len(end_turn_sq_list) > len(compare_2):

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
                #print(compare_2)

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

            if len(compare_1) > len(compare_2):
                compare_2 = compare_1
                compare_1 = []
            else: 
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

    biggest_piece = max(len(compare_1), len(compare_2))

    if biggest_piece >= 2:
        number_of_dice_to_add += biggest_piece

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

    draw_squares(end_turn_sq_list_copy, running_colour_list[current_turn])
    for i in end_turn_sq_list_copy:
        draw_dice(i, running_dice_list[i])

def aigaming(player):
    global ai_round_list

    ai_round_list = []
    #print("Starting AI again")
    #print("Player: "+str(player))
    ai_sq_list = []
    ai_dice_list = []
    ai_sq_list = [i for i, x in enumerate(running_player_list) if x == player]
   # print("The squares are: "+str(ai_sq_list))
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

            #Make sure they're an opponent/remove own squares and non_existent
            if len(neighbour_list1) > 1:
                for l in neighbour_list1:
                    if running_player_list[l] == player:
                        neighbour_list1.remove(l)
                    if running_player_list[l] == "n":
                        neighbour_list1.remove(l)
                    #if running_dice_list[l] == 0:
                    #    neighbour_list1.remove(l)

                for q in neighbour_list1:
                    if running_dice_list[q] == 0:
                        neighbour_list1.remove(q)
                #print("neighbour_list1, after removing self squares and non-squares")
                #print("Neighbours:")
                #print(neighbour_list1)

                target_list = []
                for m in neighbour_list1:
                    target_list.append((m, running_dice_list[m]))
                if len(target_list) > 0:
                    target = target_list[0]
                    if len(target_list) > 1:
                        for n in target_list:
                            if n[1] < target[1]:
                                target = n
                
                    #print("Player:")
                    #print(player)
                    #print("Attacker")
                    #print(i)
                    #print("Target")
                    #print(target)

                    if i[1] == 8 or i[1] > target[1]:
                        #print("Attack begins")
                        fighting_pair = [i[0], target[0]]
                        #print("Fighting pair")
                        #print(fighting_pair)
                        
                        dice1 = i[1]
                        dice2 = target[1]     

                        #print("Dice pair")
                        #print(dice1, dice2)
                        
                        dicesum1 = 0
                        dicesum2 = 0

                        dice_list1 = []
                        dice_list2 = []
                        
                        while dice1>0:
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

                        if dicesum1 > dicesum2:
                            #print("Attacker wins")
                            str3 = "P"+str(running_player_list[fighting_pair[0]])+" wins"
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
                                str3 = "P"+str(running_player_list[fighting_pair[1]])+" wins"
                            else:
                                str3 = "Grey wins"
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

                            #attacking_mode = False
                            #draw_squares([fighting_pair[1]], running_colour_list[running_player_list[fighting_pair[1]]])
                            #draw_dice(fighting_pair[1], running_dice_list[fighting_pair[1]])
                            #running_dice_list[fighting_pair[0]] = 1
                            #draw_squares([fighting_pair[0]], running_colour_list[player])
                            #draw_dice(fighting_pair[0], 1)
                            fighting_pair = []
                            #pause_hovering = False

                        ai_round_list.append([attacker_info, defender_info, gamelog_info])

                        '''
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
                        '''
        return(ai_round_list)

def ai_processing_one(ai_round_item, current_turn):
    print("ai_round_item")
    print(ai_round_item)
    #print("** Player **: "+str(current_turn))
    attacker = ai_round_item[0]
    print("Attacking info: "+str(attacker))
    
    draw_squares([attacker[1]], battle_colour)
    draw_dice(attacker[1], running_dice_list[attacker[1]], True)

def ai_processing_two(ai_round_item, current_turn):
    #print("Part 2")
    attacker = ai_round_item[0]
    defender = ai_round_item[1]
    gamelog_entry = ai_round_item[2]
    print("Defender info: "+str(defender))
    print("Game log entry: "+str(gamelog_entry))

    draw_squares([attacker[1]], attacker[3])
    draw_dice(attacker[1], attacker[2])
    draw_squares([defender[1]], defender[3])
    draw_dice(defender[1], defender[2])

    running_player_list[attacker[1]] = attacker[0]
    running_dice_list[attacker[1]] = attacker[2]

    running_player_list[defender[1]] = defender[0]
    running_dice_list[defender[1]] = defender[2]

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

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption('KDICE-TZ')

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
highlighted = (236, 236, 236)
white = (252, 252, 252)
green_bar = (0,202,0)
red_bar = (202, 0, 0)
battle_colour = (44, 46, 58)
dice_red = (222, 72, 42)
logcolour = (68, 70, 88)
rulescolour = (88, 76, 88)
#green_bar = (104,148,92)

player_sq_num = [3,4,5]
sq_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

colour_list = [(168, 34, 38), (152, 80, 48), (198, 178, 38), (132, 168, 42), (32, 104, 100), (46, 88, 168), (108, 32, 108)]                     

hi_colour_list = [(200, 22, 28), (202, 112, 32), (216, 202, 72), (152, 182, 22), (62, 142, 134), (82, 112, 182), (138, 24, 116)]

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
#playing = True

current_turn = 0

timeleftunit = 120

turn_list = [1, 2, 3, 4, 5, 6, 7]

active_players = [0,12,12,12,12,12,12,12] #length is 8 for 1-7 to be used directly， using arbitrary "12" to set apart from all the 1s

turn_number = 0

gamelog = []

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

pygame.draw.rect(screen, (158, 162, 166), pygame.Rect(35, 28, 359, 120)) 

title_surface = title_font.render("TDICE", True, panelcolour) #(88, 88, 88)
title_rect = title_surface.get_rect(midleft = (36, 125))  #+16
screen.blit(title_surface, title_rect)

#new game button
#hover colour (222, 108, 132)
pygame.draw.rect(screen, (196, 92, 92), pygame.Rect(1766, 28, 120, 120))
new_game_surface_1 = button_font.render("NEW", True, panelcolour) 
new_game_surface_rect_1 = new_game_surface_1.get_rect(midleft = (1768, 110))
new_game_surface_2 = button_font.render("GAME", True, panelcolour) 
new_game_surface_rect_2 = new_game_surface_2.get_rect(midleft = (1768, 136))
screen.blit(new_game_surface_1, new_game_surface_rect_1)
screen.blit(new_game_surface_2, new_game_surface_rect_2)

end_turn_surface_1 = button_font.render("END", True, panelcolour) 
end_turn_surface_rect_1 = end_turn_surface_1.get_rect(midleft = (1768, 1024))
end_turn_surface_2 = button_font.render("TURN", True, panelcolour) 
end_turn_surface_rect_2 = end_turn_surface_2.get_rect(midleft = (1768, 1050))

running_lists()

while True:
    
    #print("playing")

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
                    aigaming(current_turn)
                    
                if active_players[current_turn] > 0:
                    timeleftunit = 120
                else:
                    timeleftunit = 0

            if current_turn == 1:
                if timeleftunit > 36:
                    pygame.draw.rect(screen, green_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))
                else:
                    pygame.draw.rect(screen, red_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))

                pygame.draw.rect(screen, panelcolour, pygame.Rect(232 + 197 * current_turn + 120 - (120-timeleftunit), 148, 120-timeleftunit, 12))
                pygame.draw.rect(screen, panelcolour, pygame.Rect(232 + 197 * current_turn - 197 - 3, 148, 6, 12))

                if current_turn != 7:
                    pygame.draw.rect(screen, panelcolour, pygame.Rect(429+197*6 - 3, 148, 6, 12))
            else:
                #print(ai_round_list)
                ai_round_action_num = len(ai_round_list)
                #print("*** "+str(ai_round_action_num)+" ***")
                
                if ai_round_action_num > 0:

                    #reaction_time1 = [50, 60]
                    picked_reaction_time1 = 92
                    #reaction_time2 = [30, 40]
                    #picked_reaction_time2 = random.choice(reaction_time2)
                    picked_reaction_time2 = 62
                    
                    if timeleftunit == picked_reaction_time1:
                        ai_processing_one(ai_round_list[0], current_turn)
                    if timeleftunit == picked_reaction_time2:
                        ai_processing_two(ai_round_list[0], current_turn)
                        timeleftunit = 120

                        ai_round_action_num -= 1
                        del ai_round_list[0]

                if timeleftunit > 36:
                    pygame.draw.rect(screen, green_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))
                else:
                    pygame.draw.rect(screen, red_bar, pygame.Rect(232 + 197 * current_turn, 148, 120, 12))

                pygame.draw.rect(screen, panelcolour, pygame.Rect(232 + 197 * current_turn + 120 - (120-timeleftunit), 148, 120-timeleftunit, 12))
                pygame.draw.rect(screen, panelcolour, pygame.Rect(232 + 197 * current_turn - 197 - 3, 148, 6, 12))

                if current_turn != 7:
                    pygame.draw.rect(screen, panelcolour, pygame.Rect(429+197*6 - 3, 148, 6, 12))

        for player in range(2,8):
            p27_list = [i for i, x in enumerate(running_player_list) if x == player]
            if len(p27_list) == 0:
                active_players[player] = 0
                pygame.draw.rect(screen, panelcolour, pygame.Rect(429-197+197*player, 28, 120, 120))  

        if len(p1_sq_list) == 0:
            new_game = True
            playing = True
            timeleftunit = 120
            new_game_setup()

        if sum(active_players) == 12 and active_players[1] == 12:
            #coverup timer green bar
            pygame.draw.rect(screen, panelcolour, pygame.Rect(232 + 197, 148, 120, 12))
            #coverup end turn button
            pygame.draw.rect(screen, panelcolour, pygame.Rect(1766, 942, 120, 120))
            #playing = False
            pass

    if new_game == True:
        initial_setup()

    for event in pygame.event.get():

        #if playing == True:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 28 <= pygame.mouse.get_pos()[1] <= 148:
                #print("New game pressed")
                new_game = True
                playing = True
                running_lists()
                timeleftunit = 120
                new_game_setup()
                active_players = [0,12,12,12,12,12,12,12]
                #playing = True
                #new_game = True
            
            if current_turn == 1:
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
                            print("Clean slate, can attack")

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

                                #print("Square 1 has dice: "+str(dice1))
                                #print("Square 2 has dice: "+str(dice2))

                                dice_list1 = []
                                dice_list2 = []

                                dicesum1 = 0
                                dicesum2 = 0

                                while dice1>0:
                                    roll1 = random.randint(1,6)
                                    dicesum1 += roll1
                                    dice_list1.append(roll1)
                                    dice1 -= 1
                                while dice2>0:
                                    roll2 = random.randint(1,6)
                                    dicesum2 += roll2
                                    dice_list2.append(roll2)
                                    dice2 -= 1

                                #print("Player 1 rolled a: "+str(dicesum1)+" and his dice were: "+str(dice_list1))
                                #print("Player 2 rolled a: "+str(dicesum2)+" and his dice were: "+str(dice_list2))
                                
                                str1 = "P"+str(running_player_list[clicking_pair[0]])+" rolled a "+str(dicesum1)+" with "+str(dice_list1).strip("[]")
                                if running_player_list[clicking_pair[1]] != 0:
                                    str2 = "P"+str(running_player_list[clicking_pair[1]])+" rolled a "+str(dicesum2)+" with "+str(dice_list2).strip("[]")
                                else:
                                    str2 = "Grey rolled a "+str(dicesum2)+" with "+str(dice_list2).strip("[]")

                                #print("running_player_list Right before attack")
                                #print(running_player_list)

                                if dicesum1 > dicesum2:
                                    #print("Player 1 wins")
                                    str3 = "P"+str(running_player_list[clicking_pair[0]])+" wins"
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

                                else:
                                    #print("Player 2 wins")
                                    if running_player_list[clicking_pair[1]] != 0:
                                        str3 = "P"+str(running_player_list[clicking_pair[1]])+" wins"
                                    else:
                                        str3 = "Grey wins"
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
                                print("Need to clean up")
                                clicking_pair = []
                                pause_hovering = False
                            #print("Entering attacking mode")
                            #print(clicking_pair)
                        #elif attacking_mode == False and len(clicking_pair) == 2:
                            
                        else:
                            if len(clicking_pair) == 0:
                                print("First square isn't P1, won't work")
                                
                            else:
                                print("Won't work, need to clean up")

                            attacking_mode = False    
                            pause_hovering = False
                            clicking_pair = []
                            #print("Checking pair numbers:")
                            #print(clicking_pair)
                            #clicking_pair[1]
                            #clicking_pair_cleanup(clicking_pair)
                            #post_attack_list = [clicking_pair]
                            #post_attack_list.append(clicking_pair[1])
                            #draw_squares(post_attack_list, running_colour_list[clicking_pair[1]])
                            #draw_dice(hover_sq_num, running_dice_list[hover_sq_num])
                            #clicking_pair = []
                            #attacking_mode = False

                        #round_result = [str1, str2, str3, winner_colour]
                        #round_result = (round_result)
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


            if current_turn == 1 and 1766 <= pygame.mouse.get_pos()[0] <= 1886 and 1062 >= pygame.mouse.get_pos()[1] >= 942:
                timeleftunit = 0
                pygame.draw.rect(screen, panelcolour, pygame.Rect(426, 148, 126, 12)) 
                end_turn_addup(1)

    #if end_turn_button == False:
    #    pygame.draw.rect(screen, panelcolour, pygame.Rect(1766, 942, 120, 120)) 

    hovering_new_game_button()

    if current_turn == 1:
        hovering_end_turn_button()
    elif current_turn == 2:
        pygame.draw.rect(screen, panelcolour, pygame.Rect(1766, 942, 120, 120))

    p1_sq_list = [i for i, x in enumerate(running_player_list) if x == 1]
    
    if 1071 >= pygame.mouse.get_pos()[1] >= 189 and 429 <= pygame.mouse.get_pos()[0] <= 1731:
        recognize_sq()
    else:
        hover_sq_num = -1

    if attacking_mode == False and pause_hovering == False:
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
    
    #print("Trying this")
    #print(running_player_list.index(1))

    #print("Trying this")
    #for index, "1" in enumerate(running_player_list):
    #    print index, "1"

    #print(p1_colour)

    #print(running_colour_list)
    #print(running_dice_list)
    #print(running_player_list)

    p1_sq_count = len(p1_sq_list)
    p2_sq_count = len([i for i, x in enumerate(running_player_list) if x == 2])
    p3_sq_count = len([i for i, x in enumerate(running_player_list) if x == 3])
    p4_sq_count = len([i for i, x in enumerate(running_player_list) if x == 4])
    p5_sq_count = len([i for i, x in enumerate(running_player_list) if x == 5])
    p6_sq_count = len([i for i, x in enumerate(running_player_list) if x == 6])
    p7_sq_count = len([i for i, x in enumerate(running_player_list) if x == 7])

    px_sq_count_list = [0, p1_sq_count, p2_sq_count, p3_sq_count, p4_sq_count, p5_sq_count, p6_sq_count, p7_sq_count]

    all7len = sum(px_sq_count_list) 
    
    if all7len > 0:
        len1 = int((p1_sq_count/all7len)*360)
        len2 = int((p2_sq_count/all7len)*360)
        len3 = int((p3_sq_count/all7len)*360)
        len4 = int((p4_sq_count/all7len)*360)
        len5 = int((p5_sq_count/all7len)*360)
        len6 = int((p6_sq_count/all7len)*360)
        len7 = int((p7_sq_count/all7len)*360)

        sumof7 = len1 + len2 + len3 + len4 + len5 + len6 + len7

        if sumof7 > 359:
            len1 -= sumof7 -359
            sumof7 = 359
        elif sumof7 < 359:
            len1 += 359 - sumof7
            sumof7 = 359

        pygame.draw.rect(screen, p1_colour, pygame.Rect(35, 158, len1, 20)) 
        pygame.draw.rect(screen, running_colour_list[2], pygame.Rect(35+len1, 158, len2, 20)) 
        pygame.draw.rect(screen, running_colour_list[3], pygame.Rect(35+len1+len2, 158, len3, 20)) 
        pygame.draw.rect(screen, running_colour_list[4], pygame.Rect(35+len1+len2+len3, 158, len4, 20))      
        pygame.draw.rect(screen, running_colour_list[5], pygame.Rect(35+len1+len2+len3+len4, 158, len5, 20)) 
        pygame.draw.rect(screen, running_colour_list[6], pygame.Rect(35+len1+len2+len3+len4+len5, 158, len6, 20)) 
        pygame.draw.rect(screen, running_colour_list[7], pygame.Rect(35+len1+len2+len3+len4+len5+len6, 158, len7, 20)) 

        for i in (len2, len3, len4, len5, len6, len7):
            if i == 0:
                active_players[int(str(i)[-1])] = 0

    pygame.display.update()
    clock.tick(18) #18