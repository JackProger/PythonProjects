import random
sim = '1234567890!@#$%^&*-+=QWERTYUIOPASDFGHJKLZXCVBNMqwertyunbfdasfhjkiolpmn_'
numb = int(input('Количество паролей'))
length = int(input('Количество символов'))

for i in range(numb):
   password = ''
   for x in range(length):
      password += random.choice(sim) 
   print(password)   
sav = input("Сохранить[да/нет]")
if sav == "да":
   file = open('password.txt', 'a')
   file.write("\n" + password)
   file.close()
else:
   print('Back')
   

            
    
    
  
             
             
             
     
                 

             
   
     
   




         

    

