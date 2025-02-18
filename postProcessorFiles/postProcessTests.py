

# Helper functions ------------------------------
def test(fileLines, codesList):
    """
        Name: test()
            This is a function used only in the test/terminal version of the software to
            see if the output of the
    """

    print()
    print("--TESTS--")

    # Status variables
    laserStatus = False
    retractStatus = False
    laserAndRetract = False
    parenthesesCheck = False
    doubleMacro = False
    warmingLayer = True
    doubleLaser = False
    doubleRetract = False
    testCount = 0
    testCountPass = 0
    parenthesesStack = []
    warmingStatus = False

    # Count variables
    retractHighCount, retractLowCount = 0, 0
    laserHighCount, laserLowCount = 0, 0
    warmingHighCount, warmingLowCount = 0, 0
    fastMoveCount = 0

    # Counts of macros and making sure only laser or retract is active
    for line in fileLines:
        for segment in line:
            for character in segment:
                if character == '(':
                    parenthesesStack.append(character)
                if character == ')':
                    if len(parenthesesStack) < 1:
                        parenthesesCheck = True
                    else:
                        parenthesesStack.pop()
            # Identification of warming layer start/end
            if segment == '(WARM PLATE)':
                warmingStatus = True
            if segment == '(LAYER:0)':
                warmingStatus = False

            if not warmingStatus:
                if segment == 'F3600':
                    fastMoveCount += 1

            # Warming high count
            if segment == codesList.laserHighWarming:
                warmingHighCount += 1

            # Warming low count
            if segment == codesList.laserLowWarming:
                warmingLowCount += 1

            # Laser high
            if segment == codesList.laserHighPrinting:
                if laserStatus:
                    doubleLaser = True
                    print('oops')
                    print(line)
                laserHighCount += 1
                retractStatus = False

            # Laser low
            if segment == codesList.laserLowPrinting:
                laserLowCount += 1
                laserStatus = True

            # Retract high
            if segment == codesList.retractHigh:
                retractHighCount += 1
                laserStatus = False

            # Retract low
            if segment == codesList.retractLow:
                retractLowCount += 1
                retractStatus = True

        if retractStatus and laserStatus:
            print('we done goofed')
            print(line)
            laserAndRetract = True

        # Double macros in any line
        if codesList.retractHigh in line and codesList.laserHighPrinting in line:
            doubleMacro = True
        if codesList.retractLow in line and codesList.laserLowPrinting in line:
            doubleMacro = True
        if codesList.retractHigh in line and codesList.laserLowPrinting in line:
            doubleMacro = True
        if codesList.retractLow in line and codesList.laserHighPrinting in line:
            doubleMacro = True

        lastLine = line

    # Check for other macros in warming layer
    warmingStatus = False
    for line in fileLines:
        for segment in line:
            if segment == '(WARM PLATE)':
                warmingStatus = True
            if segment == '(LAYER:0)':
                warmingStatus = False
            if warmingStatus:
                if segment[0] == 'M':
                    if segment == codesList.laserHighWarming or segment == codesList.laserLowWarming:
                        pass
                    else:
                        warmingLayer = False

    if len(parenthesesStack) > 0:
        parenthesesCheck = True

    # Test counts
    testCount += 1
    if warmingHighCount == warmingLowCount:
        print("WARMING COUNT: PASS")
        testCountPass += 1
    else:
        print("WARMING COUNT: FAIL")

    print('WARMING HIGH COUNT: ' + str(warmingHighCount))
    print('WARMING LOW COUNT: ' + str(warmingLowCount))
    print()

    testCount += 1
    if laserHighCount == laserLowCount:
        print("LASER COUNT: PASS")
        testCountPass += 1
    else:
        print("LASER COUNT: FAIL")

    print('LASER HIGH COUNT: ' + str(laserHighCount))
    print('LASER LOW COUNT: ' + str(laserLowCount))
    print()

    testCount += 1
    if retractHighCount == retractLowCount:
        print("RETRACT COUNT: PASS")
        testCountPass += 1
    else:
        print("RETRACT COUNT: FAIL")

    print('RETRACT HIGH COUNT: ' + str(retractHighCount))
    print('RETRACT LOW COUNT: ' + str(retractLowCount))
    print()

    testCount += 1

    # Removing for first fast move in first layer
    fastMoveCount -= 1

    if fastMoveCount == retractHighCount:
        print("FAST MOVE/RETRACT TEST: PASS")
        testCountPass += 1
    else:
        print("RETRACT COUNT: FAIL")

    print('FAST MOVE COUNT: ' + str(fastMoveCount))
    print()

    testCount += 1
    if laserHighCount == retractHighCount:
        print("PAIR COUNT: PASS")
        testCountPass += 1
    else:
        print("PAIR COUNT: FAIL")

    testCount += 1
    if laserAndRetract:
        print("LASER/RETRACT TEST: FAIL")
    else:
        print("LASER/RETRACT TEST: PASS")
        testCountPass += 1

    testCount += 1
    if warmingLayer:
        print("WARMING LAYER TEST: PASS")
        testCountPass += 1
    else:
        print("WARMING LAYER TEST: FAIL")

    testCount += 1
    if doubleMacro:
        print("DOUBLE MACRO TEST: FAIL")
    else:
        print("DOUBLE MACRO TEST: PASS")
        testCountPass += 1

    testCount += 1
    if parenthesesCheck:
        print("MATCHING PARENTHESES TEST: FAIL")
    else:
        print("MATCHING PARENTHESES TEST: PASS")
        testCountPass += 1

    print("TEST RESULTS: %d/%d PASSED" % (testCountPass, testCount))
    print("--END--")
    print()
