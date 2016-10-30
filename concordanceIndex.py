def cIndex(predictY,trueY,censor):
    num = len(predictY);
    numOrderPair = 0;
    sumCInd = 0;
    for i in range(num):
        py = predictY[i]
        ty = trueY[i]
        for j in range(num):
            if j != i:
                py1 = predictY[j]
                ty1 = trueY[j]
                dif = py - py1
                dif1 = ty - ty1
                if censor[i] == 0 and censor[j] == 0:
                    numOrderPair += 1
                    if dif != 0 and dif1 != 0:
                        if (dif >0 and dif1 >0) or (dif <0 and dif1<0):
                            sumCInd += 1
                    if dif == 0 and dif1 == 0:
                        sumCInd += 0.5
                if censor[i] == 1 and censor[j] == 0:
                    if ty < ty1:
                        numOrderPair += 1
                        if dif <0:
                            sumCInd += 1
                if censor[i] == 0 and censor[j] == 1:
                    if ty > ty1:
                        numOrderPair += 1
                        if dif > 0:
                            sumCInd += 1
    cInd = sumCInd / numOrderPair
    return cInd
