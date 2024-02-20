from caesar import caesar

# Your code goes here
def welcoming_screen():
    print('''
        
\t\t\t\t\t _  _  _       _                                     
\t\t\t\t\t| || || |     | |                          _         
\t\t\t\t\t| || || | ____| | ____ ___  ____   ____   | |_  ___  
\t\t\t\t\t| ||_|| |/ _  ) |/ ___) _ \|    \ / _  )  |  _)/ _ \ 
\t\t\t\t\t| |___| ( (/ /| ( (__| |_| | | | ( (/ /   | |_| |_| |
\t\t\t\t\t \______|\____)_|\____)___/|_|_|_|\____)   \___)___/ \n
\t\t\t    _   _   _ ____  ____    _____                           _____    ___     ____                           _____   
\t\t\t   / \ | | | |  _ \|  _ \  | ____|_ __   ___ _ __ _   _ _ _|_   _|  ( _ )   |  _ \  ___  ___ _ __ _   _ _ _|_   _| 
\t\t\t  / _ \| | | | |_) | |_) | |  _| | '_ \ / __| '__| | | | '_ \| |    / _ \/\ | | | |/ _ \/ __| '__| | | | '_ \| |   
\t\t\t / ___ \ |_| |  __/|  __/  | |___| | | | (__| |  | |_| | |_) | |   | (_>  < | |_| |  __/ (__| |  | |_| | |_) | |   
\t\t\t/_/   \_\___/|_|   |_|     |_____|_| |_|\___|_|   \__, | .__/|_|    \___/\/ |____/ \___|\___|_|   \__, | .__/|_|    
\t\t\t                                                  |___/|_|                                        |___/|_|                                                                                                            
\t\t\t\t\t\t\t\t\t\t\t\t __  __            _     _            
\t\t\t\t\t\t\t\t\t\t\t\t|  \/  | __ _  ___| |__ (_)_ __   ___  
\t\t\t\t\t\t\t\t\t\t\t\t| |\/| |/ _` |/ __| '_ \| | '_ \ / _ '
\t\t\t\t\t\t\t\t\t\t\t\t| |  | | (_| | (__| | | | | | | |  __/
\t\t\t\t\t\t\t\t\t\t\t\t|_|  |_|\__,_|\___|_| |_|_|_| |_|\___|                       
    
        ''')

while True:
    # render welcoming screen
    welcoming_screen() 
    direction = input("Select your direction (e/d): ")
    if direction == 'e':
        print("Your encrypt text is: result ")
    inputUser = str(input("Input text to encrypt: "))
    shift = str(input("Shift count: "))
    
    if len(inputUser) > 5 and len(inputUser) < 25:
       encode = caesar(inputUser, shift, 1)
        
    

