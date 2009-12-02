'''
Created on Sep 18, 2009
An extenssion of the bpnn.NN class that adds features including...
* map input array from a variable dictionary
* map output array to a variable

@author: wroscoe
'''
import __init__
import pyfann

def load_Net_from_DB(self, db, dictVars):
    self.set_SelfVars(db.get_Net(dictVars))


class Net(bpnn.NN):
    #extension of bpnn
    def __init__(self, net_name, inputMap = [], outputMap = []):
        print len({'a': 1})
        
        self.inputMap = inputMap
        self.outputMap = outputMap

        self.name = net_name
        ni = len(self.inputMap)
        nh = ni +1
        no = len(self.outputMap)
        
        bpnn.NN.__init__(self, ni, nh, no)
        
    def load_Net_from_DB(self, db, dictVars):
        self = db.get_Net(dictVars)
        
    def save_Net_to_DB(self, db):
        db.put_Net(self.name, self)
        
        
    def map_to_arrInputs(self, dictFeatureVars = {"in1": 1,"in2": 3,"in3": 3}):
        arrInputs = []
        if len(dictFeatureVars) <> (len(self.inputMap)):
            raise "dictFeatureVars(%s) needs to be the same size as self.inputMap(%s)"% (len(dictFeatureVars), (len(self.inputMap)))
        else: 
            for input in self.inputMap:
                arrInputs.append(dictFeatureVars[input])
        return arrInputs
    
    def map_from_arrOutputs(self, arrOutputs = []):
        dictOutputs = {}
        print 'outputMap: % ', self.outputMap
        for i in range(len(arrOutputs)):
            dictOutputs[self.outputMap[i]] = arrOutputs[i]
        return dictOutputs
        
    #send a dict and return output array

        
    
    
    def run(self, dictInputs = {'var1': 1, 'var2':-1, 'var3':0}):
        arrInputs = self.map_to_arrInputs(dictInputs)
        arrOutputs = self.update(arrInputs)
        dictOutputs = self.map_from_arrOutputs(arrOutputs)
        print "Net name: %", self.name
        print "Outputs: %", dictOutputs
        return dictOutputs
        
if __name__ == '__main__':
    N = Net('net_name', ['var1', 'var2', 'var3'], ['out1', 'out2'])
    pat2 = [
        [[1,-1,1], [1,-1]],
        [[1,1,1], [1,1]],
        [[-1,1,1], [-1,1]],
    ]
    
    N.train(pat2, 400)
    N.test(pat2)
    print 'this is run output' 
    print N.run()
    print N.save_Net_to_DB(__init__.db)
    print N.name
    N.load_Net_from_DB(__init__.db, {'name': 'net_name'})
