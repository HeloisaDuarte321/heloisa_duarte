
# Percentual (%) significa o resto da divisão


print ('''

                     $$$                       
                    $   $                      
                     $$$                       
                     $ $                       
                     $ $                       
                   $$$ $$$                     
                 $$  $$$  $$$                  
               $$  $$$$$$$   $                 
              $               $                
             $                 $               
             $                 $               
             $     $$$$$$$$$$$$$$$             
             $    $               $            
             $    $   $$$$$$$$$$$$$            
             $   $   $           $$$           
             $   $   $ $$$   $$$  $$           
             $   $   $ $$$   $$$  $$           
             $   $   $           $$$           
             $    $   $$$$$$$$$$$$$            
             $     $$$$$$$$$$$$$$              
             $                 $               
             $    $$$$$$$$$$$$$$               
             $   $  $  $  $  $                 
             $  $$$$$$$$$$$$$$                 
             $  $   $  $  $  $                 
             $   $$$$$$$$$$$$$$$               
            $$$                 $$$            
          $$   $$$         $$$$$   $$          
        $$        $$$$$$$$$          $$$       
       $  $$                     $$$$   $$     
    $$$$$   $$$$$$$$      $$$$$$$       $ $    
  $      $$         $$$$$$              $ $$   
 $    $    $                            $ $ $  
 $     $   $              $$$$$$$$$$$   $ $ $$ 
 $$$    $   $  $$$$$$$$$$$$          $   $ $ $$
$   $$$$    $  $                     $   $ $$ $
$$$    $   $$  $                     $$  $ $  $
$   $  $  $$   $                      $  $$$  $
$     $$ $$    $               $$$    $  $ $  $

    Digite números o mais rapido possível e a cada número par
    você vai ganhar 1 ponto!!
       
    Digite 0 para encerarrar o jogo.

''')

palpite = None
acertos = 0
erros = 0

while True:
    palpite = int(input())
    conta = palpite % 2
    if palpite == 0:
        break
    else:
        if conta == 0:
            print('Par')
            acertos += 1
        else:
            print('Ímpar')
            erro += 1

print ('\nResultado:\n')
print (f'ACERTOS: {acertos}')
print (f'ERROS: {erros}')

#print
