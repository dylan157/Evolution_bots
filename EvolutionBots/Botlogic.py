from random import randint
import copy
from Botbuilder import Botbuilder

class Botlogic(object):

    def __init__(self):
        self.living_bots = []
        self.dead_bots = []


    def AI(self, who, maps):
        failed = 0 
        move_decided = False

        while not move_decided:

            thoughts = []
            thoughts.append(who.last_move)

            for generated_move in range((who.memory)-len(thoughts)):
                #This for loop generates an interger amount of moves to later test
                move_generated = False
                move_choice = ''
                failed_attempts = 0

                while not move_generated:
                    if failed_attempts > 5: break

                    rand_udlr = randint(0, 3)
                    rand_step = randint(1, who.sight)
                    move_choice = str(rand_udlr)+str(rand_step)

                    if move_choice in thoughts:
                        failed_attempts += 1
                        pass

                    else:
                        thoughts.append(move_choice)
                        move_generated = True

            for target in who.targets: #Check if generated moves land on targets. good to bad

                if "00" in thoughts: 
                    thoughts.remove("00")

                for generated_move in thoughts: #Check if generated move lands on targeted object

                    if len(thoughts) == 0:
                        pass

                    elif generated_move == "00":
                        break

                    elif generated_move[0] == "0":
                        if who.x - int(generated_move[1]) >= 0: # UP (-X, 0)
                            if maps.playerboard[(who.x - int(generated_move[1]))][who.y] == (target):
                                if maps.playerboard[(who.x - int(generated_move[1]))][who.y] not in (who.avoid):
                                    if int(generated_move[1]) > 1:
                                        generated_move = generated_move[:-1]
                                        generated_move += str(1)
                                    move_decided = True
                                    return generated_move
                                    break
                        else:
                            thoughts[thoughts.index(generated_move)] = "00"

                    elif generated_move[0] == "1":
                        if (who.x + int(generated_move[1])) < (len(maps.object_board)): # DOWN (+X, 0)
                            if maps.playerboard[(who.x + int(generated_move[1]))][who.y] == (target):
                                if maps.playerboard[(who.x + int(generated_move[1]))][who.y] not in (who.avoid):
                                    if int(generated_move[1]) > 1:
                                        generated_move = generated_move[:-1]
                                        generated_move += str(1)
                                    move_decided = True
                                    return generated_move
                                    break
                        else:
                            thoughts[thoughts.index(generated_move)] = "00"

                    elif generated_move[0] == "2":
                        if who.y + int(generated_move[1]) < (len(maps.object_board[0])): # RIGHT (0, +X)
                            if maps.playerboard[who.x][(who.y + int(generated_move[1]))] == (target):
                                if maps.playerboard[who.x][(who.y + int(generated_move[1]))] not in (who.avoid):
                                    if int(generated_move[1]) > 1:
                                        generated_move = generated_move[:-1]
                                        generated_move += str(1)
                                    move_decided = True
                                    return generated_move
                                    break
                        else:
                            thoughts[thoughts.index(generated_move)] = "00"

                    elif generated_move[0] == "3":
                        if who.y - int(generated_move[1]) >= 0: # LEFT (0, -X)
                            if maps.playerboard[who.x][(who.y - int(generated_move[1]))] == (target):
                                if maps.playerboard[who.x][(who.y - int(generated_move[1]))] not in (who.avoid):
                                    if int(generated_move[1]) > 1:
                                        generated_move = generated_move[:-1]
                                        generated_move += str(1)
                                    move_decided = True
                                    return generated_move
                                    break
                        else:
                            thoughts[thoughts.index(generated_move)] = "00"

            failed += 1
            
            if failed > who.memory: #if cant decide on move, pick random
                if "00" in thoughts:
                    thoughts.remove("00")
                if len(thoughts) > 0:
                    roulette = randint(0, len(thoughts)-1)

                    return thoughts[roulette]
            continue


    def board_transport(self, move_choice, who, map):
        if len(move_choice) == 2 and move_choice[0] in ('0', '1', '2', '3'):
          if move_choice[1] in str(range(0, len(map.object_board))): 
            if move_choice[0] == "0":
                if who.x - int(move_choice[1]) < 0: #UP
                    em = "You can't move there!"
                else:
                    who.x -= int(move_choice[1]) 

            elif move_choice[0] == "1":
                if (who.x + int(move_choice[1])) > (len(map.object_board)-1): #DOWN

                    em = "You can't move there!"
                else:
                    who.x += int(move_choice[1])
            elif move_choice[0] == "2":
                if who.y + int(move_choice[1]) > (len(map.object_board[0])-1): #RIGHT

                    em = "You can't move there!"
                else:
                    who.y += int(move_choice[1])
            elif move_choice[0] == "3":
                if who.y - int(move_choice[1]) < 0: #LEFT

                    em = "You can't move there!"
                else:
                    who.y -= int(move_choice[1])
            else:
                em = "What?"
        else:
            pass


    def move_results(self, map, bot):

        if map.object_board[bot.x][bot.y] in [map.chest_icon]:
            if map.memory_board[bot.x][bot.y] >= 3:
                map.playerboard[bot.x][bot.y], map.object_board[bot.x][bot.y] = map.dirt_icon, map.dirt_icon
                map.used_xy.remove(str(bot.x)+str(bot.y))
            bot.hunger += randint(3, 15)

        elif map.object_board[bot.x][bot.y] in [map.death_icon]: 
            if map.memory_board[bot.x][bot.y] >= 2:
                map.playerboard[bot.x][bot.y], map.object_board[bot.x][bot.y] = map.dirt_icon, map.dirt_icon
            bot.hunger += randint(1, 3)

        elif map.playerboard[bot.x][bot.y] in [map.grass_icon]: 
            bot.hunger += 1
        else:
            pass


    def bot_birth_check(self, bot, map):

        if bot.hunger >= bot.fertile:
            bot.babys += 1
            bot.hunger = int(bot.hunger*.5)
            spawn = copy.copy(bot)
            mutate = randint(1, 20)

            if mutate % randint(1, 2) == 0:
                if mutate % 3 == 0:
                    spawn.sight += 1

                elif mutate % 9:
                    if spawn.sight > 2:
                        spawn.sight  -=1

                if mutate % 7 == 0:
                    spawn.memory += 1

                if mutate % 19: 
                    if spawn.memory > 2:
                        spawn.memory  -= 1

                if mutate % 6 == 0:
                    spawn.dna += randint(1, 2)

                mutate = str(mutate)

                spawn.name += str("."+str(mutate))

            else: spawn.name += ".jr"

            map.living_bots.append(spawn)
            

        else: pass


    def bot_health_check(self, map):
        for bot in map.living_bots:
            if bot.life:
                if bot.hunger <= 0:
                        map.playerboard[bot.x][bot.y] = map.death_icon
                        map.object_board[bot.x][bot.y] = map.death_icon
                        map.memory_board[bot.x][bot.y] = 0
                        bot.life = False
                        map.living_bots.remove(bot)
                else:
                    map.memory_board[bot.x][bot.y] += 1 
