#in this i am checking if it converges to a multi valley system or not 
import sys
from pathlib import Path 


project_root = Path(__file__).resolve().parent.parent


sys.path.append(str(project_root / "src"))
from hopfieldnetwork import Network 

patterns = [
    
    [ 1, 0 , 0 , 0 , 0] , 
    [ 1, 1, 1, 1 ,0 ] , 
    [0 , 0 , 0 , 0  , 0 ] , 
    [1 , 1 , 0 , 0  , 1]
    
    
]


#the network initialisation 
net = Network(patterns)

#20%corruption
corrupted = [0 , 1 , 0 , 0 ,0]
state1 , energy1 = net.recall(corrupted , 10)#okay this does converge now lets try to corrupt even more 
print(Network.classify(state1 , patterns))

#40%corruption
corrupted1 = [0 , 1 , 1 , 0 ,0]
state2 , energy2 = net.recall(corrupted1 , 10)
print(Network.classify(state2 , patterns))


#60%corruption
corrupted2 = [1 , 1 , 0 , 1 ,0]
state3 , energy3 = net.recall(corrupted2 , 10)
print(Network.classify(state3 , patterns))

