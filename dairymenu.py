def print_menu():  
    print ("1. Вывести список задач")    
    print ("2. Добавить задачу")    
    print ("3. Отредактировать задачу")    
    print ("4. Завершить задачу")    
    print ("5. Начать задачу сначала")    
    print ("6. Выход")
loop=True        
while loop:             
   print_menu()        
   choice = input("Enter your choice [1-6]: ")   
   c = choice(int([1-6]))if c==1:             
   print ("Menu 1 has been selected")          
        elif c==2:        
   print ("Menu 2 has been selected")            
        elif c==3:        
   print ("Menu 3 has been selected")            
        elif c==4:        
   print ("Menu 4 has been selected")            
        elif c==5:       
   print ("Menu 5 has been selected")           
        elif c==6:        
   print ("Menu 5 has been selected")            
   loop=False     
        else:        
   print ("Wrong option selection. Enter any key to try again..")
