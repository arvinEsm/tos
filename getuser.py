
users = []

while True : 
  
    name = input ('enter slave  name :' )
    family = input ('enter slave  fmaily  :' )
    idd = input ('enter slave  id  :' )
    access_level  = input ('enter slave  acces level   : ')

    dic = {
        "Name" : name , 
        "Family" : family ,
        "Idd" : idd ,
        "Access_level" : access_level
          }

    users.append(dic)

    Continue = input("if u wannaa add more type (yes/no)   : ").strip().lower()

    if Continue == 'yes':       
        True
    else : 
        break

for user in users :
    print (user)
