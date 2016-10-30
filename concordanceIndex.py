def cIndex(predictY,trueY,censor):
    num = len(predictY); #number of samples
    numOrderPair = 0; #number of orderable pair
    sumCInd = 0; #sum of concordance index
    for i in range(num):
        py = predictY[i] #y_i_hat
        ty = trueY[i] #y_i
        for j in range(num):
            if j != i:
                py1 = predictY[j] #y_j_hat
                ty1 = trueY[j] #y_j
                dif = py - py1
                dif1 = ty - ty1
                if censor[i] == 0 and censor[j] == 0: #if both are not censored
                    numOrderPair += 1 #update number of orderable pairs
                    if dif != 0 and dif1 != 0:
                        if (dif >0 and dif1 >0) or (dif <0 and dif1<0): #check if y_i - y_j and y_i_hat - y_j_hat have the same sign
                            sumCInd += 1 #add 1 to sum of concordance index
                    if dif == 0 and dif1 == 0: #if y_i - y_j and y_i_hat - y_j_hat both equals to 0
                        sumCInd += 0.5 #add 0.5 to sum of concordance index
                if censor[i] == 1 and censor[j] == 0: #if i is censored and j is not censored
                    if ty < ty1: #update number of orderable pairs and sum of concordance index if y_i is smaller than y_i_hat
                        numOrderPair += 1
                        if dif <0:
                            sumCInd += 1
                if censor[i] == 0 and censor[j] == 1: #if j is censored and i is not censored
                    if ty > ty1: #update number of orderable pairs and sum of concordance index if y_i_hat is smaller than y_i
                        numOrderPair += 1
                        if dif > 0:
                            sumCInd += 1
    cInd = sumCInd / numOrderPair #average over number of orderable pairs
    return cInd
