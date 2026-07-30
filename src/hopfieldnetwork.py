class Network:

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
        x = Network.to_2d(x)
        row = len(x)
        col =len(x[0]) if isinstance(x[0],list) else 1 
        return row , col 


        
    @staticmethod    
    def bipolar(X):
        X  = Network.to_2d(X)
        rows , cols = Network.check_shape(X)

        result = []
        values = [-1 , 0 , 1]
        for i in range(rows):
            row_result = []
            for j in range(cols):
                val = X[i][j]
                if val not in values:
                    raise ValueError("patterns must be only -1 , 0 or 1 ")
                if val == 1 :
                    row_result.append(1)
                elif val == 0 :
                    row_result.append(-1)
                elif val == -1:
                    row_result.append(-1)
                
                
            result.append(row_result)

        return result 
        

    @staticmethod
    def connection_strength(X):
        rows , cols = Network.check_shape(X)
        results = []
        for i in range(cols):
            row_result = []
            for j in range(cols):
                Tij = 0
                if i == j:
                    Tij= 0   
                    row_result.append(Tij)
                else:
                    for k in range(rows):
                        Tij+= X[k][i]*X[k][j]
                    row_result.append(Tij)
            results.append(row_result)

        return results 


    def energy(self , X):
        X = Network.to_2d(X)
        rowx , colx = Network.check_shape(X)
        x = X[0]
        out = 0 
        for i in range(colx):
             for j in range(colx):
                 out+= self.connections[i][j]*x[i]*x[j]

        e = -0.5*out 

        return e
        
            

    def signal(self , noisy_pattern):
        X = Network.to_2d(noisy_pattern) 
        X = Network.bipolar(X)

        rows ,cols = self.shape
        rowx , colx = Network.check_shape(X)
        if colx != cols:
            raise ValueError(f"the dimensions  {colx} and {cols} don't match expected equal dimensions")
                
        if cols == colx:
            x = X[0]
            U =0 #theshold set to 0 ; any signal more than U would fire the neuron up
            for i in range(colx):
                neuron_signal = 0 
                for j in range(cols):
                    neuron_signal += self.connections[i][j] *x[j]

                if neuron_signal > U :
                    x[i] = 1 
                elif neuron_signal < U :
                    x[i] = -1 
                else:
                    pass

            energy  = self.energy(x)
            return x  , energy 
                    
                    
        
    def recall(self , x , max_sweep):
        if max_sweep<1 :
            raise ValueError("sweeps can't be less that 1")
        
        energies = []
        xs = []#this would append the copy of the x
        for i in range(max_sweep):
            result  = self.signal(x)

            x , energy   = result 
            energies.append(energy)
            xs.append(x.copy())
            
            if i>=1 and energies[i] == energies[i-1] and xs[i] == xs[i-1]:
                break 

        return x ,  energy

    
    
    @staticmethod
    def classify(state , patterns):#this tells if the states the network converged to is spurious or not
        stored = Network.bipolar(patterns)
        
        if state in stored:
            return "Not Spurious"

        else:
            return "Spurious"

                    
                    
                    
                    
    
    
    def __init__(self , data):
        self.data = data
        self.shape = Network.check_shape(self.data)
        self.binary = Network.bipolar(self.data)
        self.connections = Network.connection_strength(self.binary)
    def __repr__(self):
        return f"Network(data={self.data})"
        
    
    