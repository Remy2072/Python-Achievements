import math

#Vervang de 0-en met de juiste berekeningen

trees               = 333           #hoeveel bomen zijn er in totaal?
shadedTrees         = math.ceil(222) #hoeveel bomen staan er in de schaduw (afgerond naar boven)
sunnyTrees          = 111           #hoeveel in de zon?

shadeOutputModifier = 80            #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 146           #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = 116.8         #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = 16.206        #hoeveel appels geven alle zonnige bomen? 
shadedOutput        = 25929.6      #hoeveel appels geven alle schaduw bomen?
totalOutput         = 42135.6      #hoeveel appels zijn er in totaal?

owners              = 3             #met hoeveel mensen verdelen we de appels?

eatCount            = 0             #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = 14.045         #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = 14.045         #hoeveel appels mag ik verkopen?

print(cut)