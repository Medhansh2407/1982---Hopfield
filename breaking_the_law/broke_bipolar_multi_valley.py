#we are esentially making and tailoring this for the multi - valley pattern to see if it breaks
class BrokenNetwork:

    @staticmethod
    def to_2d(x):
        is_2d = isinstance(x , list) and all(isinstance(row , list) for row in x)

        if is_2d:
            return x
        if isinstance(x , list):
            return [x]
        else:
            return [[x]]


    @staticmethod
    def check_shape(x): 
        x = BrokenNetwork.to_2d(x)
        dims =[]
        row = len(x)
        col =len(x[0]) if isinstance(x[0],list) else 1 
        dims.append(row)
        dims.append(col)
        return dims 


    @staticmethod
    def connection_strength(X):
        rows , cols = BrokenNetwork.check_shape(X)
        #return rows ,cols
        results = []
        for i in range(cols):
            row_result = []
            for j in range(cols):
                val = 0
                if i == j:
                    val= 0   
                    row_result.append(val)
                else:
                    for k in range(rows):
                        val+= X[k][i]*X[k][j]
                    row_result.append(val)
            results.append(row_result)

        return results 


    def energy(self , X):
        X = BrokenNetwork.to_2d(X)
        rowx , colx = BrokenNetwork.check_shape(X)
        x = X[0]
        out = 0 
        for i in range(colx):
             for j in range(colx):
                 out+= self.connections[i][j]*x[i]*x[j]

        e = -0.5*out 

        return e
        
            

    def signal(self , noisy_pattern):
        X = BrokenNetwork.to_2d(noisy_pattern)#this is the network 

        rows ,cols = self.shape
        rowx , colx = BrokenNetwork.check_shape(X)
        if cols == colx:
            x = X[0]
            U =3.0 #this is the threshold

            for i in range(colx):
                val = 0 
                for j in range(cols):
                    val += self.connections[i][j] *x[j] 

                if val > U :
                    x[i] = 1 
                elif val < U :
                    x[i] = 0 
                else:
                    pass

            energy  = self.energy(x)
            return x  , energy 
    
    

    @staticmethod
    def classify(state , patterns):
        if state in patterns:
            return "Not spurious"
    
        else:
            return "spurious"                
        
    
                    
        
    def recall(self , x , max_sweep):#so we would have a max sweep algorithm in which we would sweep in the energy landscape until we do not reach the
        #least energy
        energies = []
        xs = []
        for i in range(max_sweep):
            result  = self.signal(x)
            x , energy   = result 
            energies.append(energy)
            xs.append(x.copy())
            print(f"{x=} ,  {energy=}")

            if i>=1 and energies[i] == energies[i-1] and xs[i] == xs[i-1]:
                break 

        return x ,  energy
                    
    
    def __init__(self , data):
        self.data = data
        self.shape = BrokenNetwork.check_shape(self.data)
        self.connections = BrokenNetwork.connection_strength(self.data)
    def __repr__(self):
        return f"BrokenNetwork(data={self.data})"
    
    
    
    



patterns = [
    
    [ 1, 0 , 0 , 0 , 0] , 
    [ 1, 1, 1, 1 ,0 ] , 
    [0 , 0 , 0 , 0  , 0 ] , 
    [1 , 1 , 0 , 0  , 1]
    
    
]


# #the network initialisation 
net = BrokenNetwork(patterns)

#20%corruption
corrupted = [0 , 1 , 0 , 0 ,0]

print(net.recall(corrupted , 10 ))
state1 , energy1 = net.recall(corrupted , 10)#okay this does converge now lets try to corrupt even more 
print(BrokenNetwork.classify(state1 , patterns))

#40%corruption
corrupted1 = [0 , 1 , 1 , 0 ,0]

print(net.recall(corrupted1 , 10 ))
state2 , energy2 = net.recall(corrupted1 , 10)
print(BrokenNetwork.classify(state2 , patterns))


#60%corruption
corrupted2 = [1 , 1 , 0 , 1 ,0]
print(net.recall(corrupted2 , 10 ))
state3 , energy3 = net.recall(corrupted2 , 10)
print(BrokenNetwork.classify(state3 , patterns))
    
#print(net.connections)



#tried at U = 2 and at U =3 ; i would say that i am not really sure if the network on these two threshholds - coverged on its own or because of hte
#strong threshold - squashing and classifying all the values in one range  and thus creating somewhat similar points to the memory