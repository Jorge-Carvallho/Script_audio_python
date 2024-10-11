import pygame

pygame.init() # inicia o pygame
pygame.mixer.init() # inicia o mixer do áudio
pygame.mixer.music.load('ex021.mp3') # carrega o arquivo da música
pygame.mixer.music.play() # play no áudio
while pygame.mixer.music.get_busy(): # entra no loop caso o áudio seja True (estiver tocando) ele executa
    pass
   




   





    
   

      

       

   
   
