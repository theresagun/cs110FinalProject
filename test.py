def main():
##########################################################################
    print('### Testing pacman model ###')
    testPacman = pacman.Pacman()

    print('# Test forward #')
    testPacman.forward(5)
    assert testPacman.getCoordinates() == (5,0)

    print('# Test right #')
    testPacman.right(60)
    assert testPacman.direction() == 60

    print('# Test left #')
    testPacman.left(60)
    assert testPacman.direction() == 300

    print('# Test eat #')
    testPacman.eat()
    assert testPacman.getCoordinates() == dot.getCoordinates()
##########################################################################
    print('### Testing ghost model ###')
    testGhost = ghost.Ghost()

    print('# Test forward #')
    testGhost.forward(5)
    assert testGhost.getCoordinates() == (5,0)

    print('# Test right #')
    testGhost.right(60)
    assert testGhost.direction() == 60

    print('# Test left #')
    testGhost.left(60)
    assert testGhost.direction() == 300

    print('# Test eat #')
    testGhost.eat()
    assert testGhost.getCoordinates() == testPacman.getCoordinates()
##########################################################################
    print('### Testing dot model ###')
    testDot = dot.Dot()

    print('# Test disappear')
    testDot.disappear()
    assert testDot.exist() == False
##########################################################################
    print('### Testing map model ###')
    testMap = map.Map()
    assert testMap.exist() == True
##########################################################################
    print('### Testing score model ###')
    testScore = score.Score()

    print('# Test current score #')
    testScore.currentScore(500)
    assert testScore.displayScore() == 500

    print('# Test high score #')
    testScore.highScore(5000)
    assert testScore.displayHighScore == 5000

    print('# Test number of lives #')
    testScore.loseLife(1)
    assert testScore.lives == lives - 1
main()
