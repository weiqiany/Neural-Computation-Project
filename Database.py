import scipy.io as sio
from sklearn.ensemble import RandomForestRegressor
from concordanceIndex import cIndex
class Database(object):

    def __init__(self,filename):
        self.fileName = filename
        self.train = {}
        self.validation = {}
        self.test = {}

    def read(self):
        dataset = sio.loadmat(self.fileName)
        self.features = dataset['Features']
        self.censor = dataset['Censored']
        self.survival = dataset['Survival']

    def process(self):
        #generate training, validation, test sets from the given data
        numSamples = len(self.survival)
        numTrain = int(numSamples/2)
        numValidation = int(numSamples/4)
        numTest = numSamples - numTrain - numValidation
        self.train['features'] = self.features[:,0:(numTrain-1)]
        self.train['censor'] = self.censor[0:(numTrain-1)]
        self.train['survival'] = self.survival[0:(numTrain-1)]
        self.validation['features'] = self.features[:, numTrain:(numTrain + numValidation - 1)]
        self.validation['censor'] = self.censor[numTrain:(numTrain + numValidation - 1)]
        self.validation['survival'] = self.survival[numTrain:(numTrain + numValidation - 1)]
        self.test['feature'] = self.features[:,(numTrain + numValidation):(numSamples-1)]
        self.test['censor'] = self.censor[(numTrain + numValidation):(numSamples-1)]
        self.test['survival'] = self.survival[(numTrain + numValidation):(numSamples-1)]

    def featureSelection(self):
        #select features
        rf = RandomForestRegressor()
        rf.fit(self.train['features'],self.train['survival'])
        validationPrediction = rf.predict(self.validation['feature'])
        featureImportance = rf.feature_importances_
        featureIndex = sorted(range(len(featureImportance)), key=lambda k: featureImportance[k])
        selectedFeatures = []
        selectedFeaturesValidation = []
        improvement = 1.0
        nsf = 10
        cid = cIndex(validationPrediction,self.validation['survival'],self.validation['censor'])
        cid_prev = cIndex(validationPrediction,self.validation['survival'],self.validation['censor'])
        while improvement > 0.1:
            for i in range(nsf):
                selectedFeatures.append(self.train['feature'][featureIndex[i],:])
                selectedFeaturesValidation.append(self.validation['feature'][featureIndex[i],:])

            rf.fit(selectedFeatures,self.train['survival'])
            validationPrediction = rf.predict(selectedFeaturesValidation)
            cid = cIndex(validationPrediction, self.validation['survival'], self.validation['censor'])
            improvement = cid / cid_prev - 1
            cid_prev = cid
            nsf += 10

        self.randomForest = rf
        self.selectedFeaturesTest = []
        nsf -= 10
        for j in range(nsf):
            self.selectedFeaturesTest.append(self.test['feature'][featureIndex[i], :])
