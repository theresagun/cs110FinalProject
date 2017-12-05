import pygame
import main

def main():
##########################################################################
    print('### Testing pacman model ###')
    testPacman = pacman.Pacman()

    print('# Test up #')
    testPacman.turnUp()
    assert testPacman.direction == 1

    print('# Test right #')
    testPacman.turnRight()
    assert testPacman.direction == 0

    print('# Test left #')
    testPacman.turnLeft()
    assert testPacman.direction == 2

    print('# Test down #')
    testPacman.turnDown()
    assert testPacman.direction == 3

##########################################################################
    print('### Testing ghost model ###')
    testGhost = ghosts.Ghost()

    print('# Test up #')
    testGhost.turnUp()
    assert testGhost.direction == 1

    print('# Test right #')
    testGhost.turnRight()
    assert testGhost.direction == 0

    print('# Test left #')
    testGhost.turnLeft()
    assert testGhost.direction == 2

    print('# Test down #')
    testGhost.turnDown()
    assert testGhost.direction == 3

##########################################################################
'COPY & PASTE TESTING GHOST MODEL FOR DIFFERENT COLOR GHOSTS'
##########################################################################
    print('### Testing dot model ###')
    testDot = dot.Dot()

    print('# Test disappear')
    testDot.disappear()
    assert testDot.exist() == False
##########################################################################
    print('### Testing map model ###')
    testMap = maps.Map()
    assert testMap.exist() == True
##########################################################################
main()
