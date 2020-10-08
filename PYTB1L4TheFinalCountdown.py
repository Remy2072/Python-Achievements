import time 

countdown = 1000

while countdown > 0:
    print(countdown)
    countdown -= 1 
    if countdown > 4:
        time.sleep(0.01)
    else: 
        time.sleep(1)   
print("""\
 .:::::::                                         
.::    .::                                       
.::    .::     .::    .::: .:: .:: .::   .::     
.: .::       .:   .::  .::  .:  .:: .:: .::      
.::  .::    .::::: .:: .::  .:  .::   .:::       
.::    .::  .:         .::  .:  .::    .::       
.::      .::  .::::   .:::  .:  .::   .::        
                                    .::   
    """)       
                                                 
                                          