#this is a basic recall  - in which i am testing that if it even converges to one valley or not 

import sys
from pathlib import Path 


project_root = Path(__file__).resolve().parent.parent


sys.path.append(str(project_root / "src"))
from hopfieldnetwork import Network 


#the implementation 

patterns = [
    [
        1, 1, 1, 1,
        0, 1, 0, 1,
        0, 0, 0, 0,
        1, 1, 0, 0
    ],
]

corrupted = [
    1, 1, 1, 1,
    0, 1, 0, 1,
    0, 0, 0, 0,
    1, 0, 0, 0
]


net = Network(patterns)
x , energy = net.recall(corrupted , 10)
print(x)
print(x in net.binary)#this would return true thus the network does converge in one valley as a check
