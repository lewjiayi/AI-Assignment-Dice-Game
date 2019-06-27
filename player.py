class Player:
    def __init__(self):
        dice_num = 5


    def checkScore(self, dice_face):
        score = sum(dice_face)
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return (score + 70)
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                return (score + 40)
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return (score + 50)
        elif len(setOfDice) == 3:
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                return score
            elif dice_face.count(list(setOfDice)[0]) == 3 \
            or dice_face.count(list(setOfDice)[1]) == 3 \
            or dice_face.count(list(setOfDice)[2]) == 3 :
                return (score + 30)
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                if x == 6:
                    six = True
            if not one and six:
                return (score + 60)
            if one and not six:
                return (score + 60)
        return score

    def checkState(self, dice_face):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return 1
        elif len(setOfDice) == 2:
            return 2
        elif len(setOfDice) == 3:
            return 3
        elif len(setOfDice) == 4:
            return 4
        elif len(setOfDice) == 5:
           return 5

    def play(self, dice_face, available_rerolls):
        pass

    # Average: 57.0
    def testPlay1(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:    
            d = 7
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    if x < d:
                        d = x
                        r = num
            return [r]
        elif len(setOfDice) == 4:
            if available_rerolls > 3:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 2:
                        return[num]
            else: 
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return[num]
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []
        
    # Average: 56.3
    def testPlay2(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:    
            d = 7
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    if x < d:
                        d = x
                        r = num
            return [r]
        elif len(setOfDice) == 4:
            if available_rerolls >= 3:
                r = []
                rnum = []
                for num, x in enumerate(dice_face):
                    if x == 1:
                        r.append(num)
                    if dice_face.count(x) == 2:
                        for y in rnum:
                            if y != x:
                                rnum.append(x)
                                r.append(num)
                return r
            elif available_rerolls <= 2:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 2:
                        return[num]
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    # Average: 58.1
    def testPlay3(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:    
            d = 7
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    if x < d:
                        d = x
                        r = num
            return [r]
        elif len(setOfDice) == 4:
            if available_rerolls >= 3:
                r = []
                rnum = []
                for num, x in enumerate(dice_face):
                    if x == 1:
                        r.append(num)
                    if dice_face.count(x) == 2:
                        for y in rnum:
                            if y != x:
                                rnum.append(x)
                                r.append(num)
                return r
            elif available_rerolls <= 2:
                r = []
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) != 2:
                        r.append(num)
                return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []
    
    # Average: 60.7
    def testPlay4(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:    
            d = 7
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    if x < d:
                        d = x
                        r = num
            return [r]
        elif len(setOfDice) == 4:
            if available_rerolls >= 4:
                r = []
                rnum = []
                for num, x in enumerate(dice_face):
                    if x == 1:
                        r.append(num)
                    if dice_face.count(x) == 2:
                        for y in rnum:
                            if y != x:
                                rnum.append(x)
                                r.append(num)
                return r
            elif available_rerolls <= 3:
                r = []
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) != 2:
                        r.append(num)
                return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    # Average: 57.3
    def testPlay5(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:    
            d = 7
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    if x < d:
                        d = x
                        r = num
            return [r]
        elif len(setOfDice) == 4:
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 2:
                    return[num]
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []
   
    # Average: 57.55
    def testPlay6(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
            return r
        elif len(setOfDice) == 4:
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 2:
                    return[num]
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    # Average: 56.7
    def testPlay7(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 2:
                    return[num]
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    # Average: 60.5
    def testPlay8(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            one = False
            six = False
            r = []
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    oneIndex = num
                if x == 6:
                    six = True
                if dice_face.count(x) == 2:
                    r.append(num)
                    duplicate = x
            if one and six:
                if duplicate == 1:
                    return r
                else:
                    return [r[0], oneIndex]
            else:
                return [r[0]]

        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    # Average: 66.0
    def testPlay9(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            r =[]
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
            return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    # Average: 62.5
    def testPlay10(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            r =[]
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if dice_face.count(x) == 2:
                    duplicate = num
                if x == 1:
                    one = True
                if x == 6:
                    six = True
            if one and six:
                return r
            return [duplicate]
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    # Average: 65.9, not stable
    def testPlay11(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            r =[]
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
            return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            m = 0
            r = []
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                if x == 6:
                    six = True
                if x > m:
                    m = x
                else:
                    r.append(num)
            if one and six:
                return r
            return []

    # Average: 66.1 sligth improvement of test9
    def testPlay12(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    if dice_face.count(x) == 2:
                        h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            r =[]
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
            return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    # Average: 65.45
    def testPlay13(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    if dice_face.count(x) == 2:
                        h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            r =[]
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
            return r
        elif len(setOfDice) == 5:
            h = 0
            for num, x in enumerate(dice_face):
                if x > h:
                    h = x
                    rn = num
            r = [0,1,2,3,4]
            r.remove(num)
            return r

    # Average: 67.2 test12 reroll low number at set == 4
    def testPlay14(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    if dice_face.count(x) == 2:
                        h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            r =[]
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                    if x > h:
                        h = x
                        hnum = num
                else:
                    duplicate = x
            if duplicate <= 3:
                r = [0,1,2,3,4]
                r.remove(hnum)
                return r
            return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    def testPlay15(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            d = 0
            duplicate = 7
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                elif dice_face.count(x) == 3:
                    duplicate = x
                if x > h:
                    if dice_face.count(x) == 2:
                        h = x
                if x > d:
                    d = x
                    dnum = num
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            if duplicate <= 1 :
                r = [0,1,2,3,4]
                r.remove(dnum)
                return r
            return r
        elif len(setOfDice) == 4:
            r =[]
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                    if x > h:
                        h = x
                        hnum = num
                else:
                    duplicate = x
            if duplicate <= 3:
                r = [0,1,2,3,4]
                r.remove(hnum)
                return r
            return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    def testPlay16(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    if dice_face.count(x) == 2:
                        h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            r =[]
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                    if x > h:
                        h = x
                        hnum = num
                else:
                    duplicate = x
            if available_rerolls >= 4:
                if duplicate <= 3:
                    r = [0,1,2,3,4]
                    r.remove(hnum)
                    return r
            return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                    r = num
                if x == 6:
                    six = True
            if one and six:
                return [r]
            return []

    def testPlay17(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    if dice_face.count(x) == 2:
                        h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            r =[]
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                    if x > h:
                        h = x
                        hnum = num
                else:
                    duplicate = x
            if duplicate <= 3:
                r = [0,1,2,3,4]
                r.remove(hnum)
                return r
            return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                if x == 6:
                    six = True
                    snum = num
            if one and six:
                r = [0,1,2,3,4]
                r.remove(num)
                return(r)
            return []

    def testPlay18(self, dice_face, available_rerolls):
        setOfDice = set(dice_face)
        if len(setOfDice) == 1:
            return []
        elif len(setOfDice) == 2:
            if dice_face.count(list(setOfDice)[0]) == len(dice_face) - 1 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 1:
                for num, x in enumerate(dice_face):
                    if dice_face.count(x) == 1:
                        return [num]
            elif dice_face.count(list(setOfDice)[0]) == len(dice_face) - 2 \
            or dice_face.count(list(setOfDice)[1]) == len(dice_face) - 2:
                return []
        elif len(setOfDice) == 3:
            r = []
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                if x > h:
                    if dice_face.count(x) == 2:
                        h = x
            if dice_face.count(list(setOfDice)[0]) == 2 \
            or dice_face.count(list(setOfDice)[1]) == 2 \
            or dice_face.count(list(setOfDice)[2]) == 2 :
                r.clear()
                for num, x in enumerate(dice_face):
                    if x < h:
                        r.append(num)
            return r
        elif len(setOfDice) == 4:
            r =[]
            h = 0
            for num, x in enumerate(dice_face):
                if dice_face.count(x) == 1:
                    r.append(num)
                    if x > h:
                        h = x
                        hnum = num
                else:
                    duplicate = x
            if available_rerolls >= 4:
                if duplicate <= 3:
                    r = [0,1,2,3,4]
                    r.remove(hnum)
                    return r
            return r
        elif len(setOfDice) == 5:
            one = False
            six = False
            for num, x in enumerate(dice_face):
                if x == 1:
                    one = True
                if x == 6:
                    six = True
                    snum = num
            if one and six:
                r = [0,1,2,3,4]
                r.remove(num)
                r.remove(0)
                return(r)
            return []

