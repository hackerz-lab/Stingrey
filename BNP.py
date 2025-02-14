#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Marttin Saji (GitHub: @hackerz-lab)
# Subscription Script v1.3.7
# Compatible with Kali Linux & Termux

import random
import time
import sys
from colorama import Fore, Style, init
from faker import Faker

init(autoreset=True)
fake = Faker()

def print_banner():
    print(Fore.RED + """
                                                                                                                                                          
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                 .-==:.      .-==:                                                                    
                                                             .=-   ..          ..  :=.                                                                
                                                          .=.                         :-.                                                             
                                                        .*                              .=.                                                           
                                                      -=                                  .-                                                          
                                                    =:                                      -                                                         
                                                  -:                                          =                                                       
                                                .*-                         .                  *.                                                     
                                              .-#++-                        =                   -                                                     
                                             .=-=:*@=                       :                    :.                                                   
                                            .-=.-:*@@=.                                          .=.                                                  
                                           ::     *@@@*-                                          .=.                                                 
                                    .:    .:     .+@@@@@=                    .                     :-                                                 
                                    -#=-  .      --%@@@@+.:                  -                     .::                                                
                                    *#@%+=.      :.#@@@+ .-=                 =                      .-                                                
                                    =:@@@=  .-:   -=%@@   *=.-               =                       --                                               
                                     *@@%.  .:.  :***@=   * .--              -                       ::                                               
                                     -%@%        .:=+%.   .  .::             :                        --                                              
                                      *@:           .:         ..                                     ::                                              
                                      :%              =   .*=   ..                                     ..                                             
                                       .             ..    .. == :.                                    =-                                             
                                      +                   .    .:++:                                   -:                                             
                                      %             -     .       .*-                                                                                 
                                                 =:*:                         .                                                                       
                                                 .         .                  :                         :.                                            
                                     =     :+    +-        -                  :         :               =:                                            
                                     %     :=    +*.      .+                  -        -=.              +-                                            
                                     %     .:    *@:       =                  =        =#.              +-                                            
                                     =      .    +@-       .  ..             .+        +*.              +-                                            
                                               :.=#+.         ..             .+        +-               +-                                            
                                    .          =-=-#:       -  .             .*        =.               =:                                            
                                    :         .*=+:=.      .+                .+        :.               -:                                            
                                    =         -%=**:=      .-                 -        .                :.                                            
                                    +         =@=++:#.                                 :.               ..                                            
                                    +         =@=:. -:       .                         .                ..                                            
                                    =      .. =@*:   =      .=.               :        :.                                                             
                                    -      :: =*++.  :      .+-               =        =:               .                                             
                                    . .  .++= ==:+:.  +      -+               -        -.         :                                                   
                                      #: :%%* ::-%*=. :      :+               -        .         .+                                                   
                                     #@:.:@@* .=%@@@%%%%     :=               =*. ::             .*                                                   
                                     @+=#:@@*  +@@+:...@     .:              .+.                 :*                                                   
                                     @.%.=@#  ..=%-   ##@     .  ..           - :%+-- :.         .= .                                                 
                                     @ %:@#     :=.   ##..       ::           :.-  .. =:          . .   .                                             
                                        =@#     :#-  *#. #                    --      +-          . .   ..                                            
                                        .@#     .#- .+.   -       .          .@#    -:=:           ..   :.                                            
                                        :@=     .*=+.     :. .   .=:         .@@*   --..          .-.   :.                                            
                                        .#.     =##:      .+.-   -+.         .@@%-  ::            :*.   =:                                            
                                        :*                  ==   --          .@@@*   :.           :*.   =-                                            
                                      .---                  -*   ..          .*@@*  .+:           .-.   =-                                            
                                    -::+                    .+     .         .:@@*  -#-            .    =-                                            
                                   .=-                      .=  .: -.        :*@@+  :=:             .   +-                                            
                                   ..                       .-  -- =:        -@@*. ::.             :=   +-                                            
                                    +                        :  :: :.        =@#:  ::              :=   +-                                            
                                    -.                       .   .           ==:  :::.             .:   +-                                            
                                     *                       .  .            -   .:.--                  +-                                            
                                     -                       . .:   :.       =   .: =-              .:  +-                                            
                                                             . .:   -.       +  :=  -:              -=  +-                                            
                                                             : ::   +:       *-#+.  ..              ..  =:                                            
                                                            .- :-   =:       # ..                    .. :.                                            
                                     +                      .= :-   -.       #     ..                -= :.                                            
                                     +                       . ..   .        #  .- ::                :- :.                                            
                                      =                      .. .            *  :* ==                   .                                             
                                      :                      :*              +  -* ==                 ::                                              
                                                             .:      :       +  -* ==            .*   -=                                              
                                         .                    .:..   -.      =  -* -=            :#    .                                              
                                        .                     :=--   +.      -  -* --            :%:   -:                                             
                                        =                     .:--  .#:      : .*+ --            :%+   ==                                             
                                        =.                     .-..:#@:      . :%+ :-            .+.:  ::                                             
                                        .-                     :=:+%@@:      - :@+ ..            .-:=   .                                             
                                        .-                    .+==@@@@:      + :@*                . ::  -:                                            
                                                             :*@*=@@@@:     .# :@*                  -+  -:                                            
                                                          :++=@@%=#@@@:     :% :@*                 .:=:                                               
                                                        -*#@%=@@@++@@@-     -% :@*                .=.+=  -:                                           
                                          .          .**%@@@%=@@@++@@@=     +% :@*                :*:=:. :.                                           
                                         .=     .-++==@@@@@@%=@@@*=%@@+     *@-:@*                .=:=--  .                                           
                                          ::-:.  +=::.@@@*@@%=@@@%=*@@*.    #@*:@*                 .-+..  =:                                          
                                            .    =+.. %@@.%@%=@@@@=*@@#.    %@%:@#:                 -+ =- :.                                          
                                                 :#:. #@@ :@%+@@@@==@@*.    @@%.*@+                 :- ..                                             
                                                 .#:. *@@ .*%+@@@@*:#@+.    @@@=-@*                  .  =- :                                          
                                                  *:  =@@  :@#@@@@@-*@+     @@@#-@#:                    -: *:                                         
                                                  *:  .@@  .@#@@@@@-+@+     @@@#.*@+                 ..  :.-.                                         
                                                  =.   @@  -%*@@@@@=:#=     @@@%--@*                 -=  +-                                           
                                                  +:   @@  +@%@@@@@= #=     @@@@#.-%=                -+   . =.                                        
                                                  -:   @@ .#%*@@@@@*:+:     @@@@@*.-+.               :-   *:#.                                        
                                                  =*.  @@ .%==@@@@@@-       @@@@@@*.--                .   -:=.                                        
                                                  -%:  @@ .%.:@@@@@@-       @@@@@@@*:                 ::   =.                                         
                                                  =@:  @@ :% .*@@@@@-       @@@@@@@@#=:               ==   #::                                        
                                                  =@:  @@ -%  =@@@@@+.     .@@@@@@%*++- .-==: :.      --   *:+                                        
                                                  =#.  @@ *%  =@@@@@%:     :@@@@*+-.    :#*+- -.   ::  ..  +.*.                                       
                                                  =-   @@ %* .=#@@@@@:     =@@*=.       :=         :::+*=  +.#.                                       
                                                  =.   %@ @: :++@@@@@-     *%=.       :..         .-.:==::=#.*                                        
                                                  =.   %%:%  :*=@@@@@-     #-        :-.         :-:     .:#*=                                        
                                                  =.   ##*%  :+=@@@@@=     #        ::.         +..        ::*.                                       
                                                  =.   #+@%  .:=@@@@@*.    =        ..         *:            :+:                                      
                                                  +: . *+@+    -@@@@@#.    :       ::         *.              .:-                                     
                                                  +: . +@@:   .+@@@@@@:           :=         #.                 =                                     
                                                  =.   *@@    :@@@@@+*.   =      -+          .                   #                                    
                                                  =.   *@@   :#%@@@= -.   #     :=          %                                                         
                                                  =.   %@+  :@@%@+   :    #    .-          .                      .                                   
                                                  =.   @@. :@@@#:    :    =   .:           #                                                          
                                                  =.   @@.@@@%*   =-      .  .=           .                                                           
                                                  -.   @@:%%*    :.      .  .*            *.                                                          
                                                  .    @@*      ::    .  =:.=             -                                                           
                                                  .    @#  :          :  *#              -                                                            
                                                      =@. .+          :  #               *.                                                           
                                                      ##  -%       .:.:  +               :                                                            
                                                 .    %:  +#    .: :=.:  :              .                                                             
                                                 :.   %  =+- -- .:..  .                 =.                                                            
                                                 =:   =  ==  --   ::    -               :.                                                            
                                                 *-  -  -         ..    *                                                                             
                                                 +:  =  =               #              -.                                                             
                                                 :.  .  .               #              =:                                                             
                                                    +. -         ::  .  =              :.                                                             
                                                :.  :            ::  :. :                                                                             
                                                =: -.                =. .             :.                                                              
                                                +- *.                +:               =:                                                              
                                                -: .                 *:.              .                                                               
                                                  +:                 =.-                                                                              
                                                  -.                """ + Style.RESET_ALL)
    print(Fore.CYAN + "[" + Fore.WHITE + "*" + Fore.CYAN + "]" + Fore.YELLOW + " Initializing Secure Subscription Protocol v2.0")
    print(Fore.CYAN + "[" + Fore.WHITE + "*" + Fore.CYAN + "]" + Fore.YELLOW + " Connecting to Netflix/Prime Video API Gateway...\n")

def generate_fake_card():
    cards = [
        ('4' + ''.join([str(random.randint(0,9)) for _ in range(15)]), 'Visa'),
        ('5' + ''.join([str(random.randint(0,9)) for _ in range(15)]), 'Mastercard')
    ]
    return random.choice(cards)

def loading_animation():
    animations = ["⣾⣽⣻⢿⡿⣟⣯⣷", "⠁⠂⠄⡀⢀⠠⠐⠈"]
    for _ in range(1):
        for i in range(len(animations[0])):
            sys.stdout.write(Fore.GREEN + "\rProcessing payment " + animations[0][i] + " ")
            sys.stdout.flush()
            time.sleep(40)
    print("\n")

def main():
    print_banner()
    
    email = input(Fore.CYAN + "[" + Fore.WHITE + "+" + Fore.CYAN + "]" + Fore.WHITE + " Enter your email: ")
    password = input(Fore.CYAN + "[" + Fore.WHITE + "+" + Fore.CYAN + "]" + Fore.WHITE + " Enter your password: ")
    
    print(Fore.YELLOW + "\n[!] Encrypting credentials...")
    time.sleep(20)
    
    loading_animation()
    
    card_number, card_type = generate_fake_card()
    exp_date = f"{random.randint(1,12):02d}/{random.randint(23,30)}"
    cvv = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
    
    print(Fore.GREEN + "[✓] Subscription Successful!")
    print(Fore.CYAN + "\n--------- Subscription Details ---------")
    print(Fore.YELLOW + f"Email: {email}")
    print(f"Password: {'*' * len(password)}")
    print(f"Card Number: {card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}")
    print(f"Card Type: {card_type}")
    print(f"Expiry Date: {exp_date}")
    print(f"CVV: {cvv}")
    print(Fore.CYAN + "-----------------------------------------")
    
    print(Fore.RED + "\n[!] WARNING: This is Illegal! this subscription has no warranty.")
    print(Fore.RED + "[!] Your credentials were not stored or transmitted.")
    print(Fore.BLUE + "\nCreated by Marttin Saji | GitHub: @hackerz-lab")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Operation cancelled by user")
        sys.exit(0)
