
contacts = []


#---------------------------------functions--------------------------------------------------
def new_contact(contacts,name, fone, email):
  print("--------------------New Contact-----------------")
  
  contact = {"name":name,"fone":fone, "email":email, "favorite": False}
  contacts.append(contact) 
  print(f"The new contact {name} has been added to your contact list")
  return

def edit_contact(contacts, index):
  print("--------------------Edit Contact-----------------")
  index = index - 1
  for index_list, contact in  enumerate(contacts):
    if index_list == index:
      name = input("Enter a name: ")
      fone = input("Enter a fone: ")
      email = input("Enter a email: ")
      contact.update({"name":name,"fone":fone, "email":email, "favorite":False})
      print(f"the contact {index + 1} has been updated to . name: {contact["name"]}, fone: {contact["fone"]},  e-mai: {contact["email"]}")
  return

def favorite(contactcs, index):
  print("------------Mark a Contact with Favorite------------")
  index = index - 1
  contact = contactcs[index]
  contact.update({"favorite":True})
  return

def show_list(contacts):
  print("-------------------Contact List--------------------")
  for index, contact in  enumerate(contacts):
    index = index + 1
    favorite = "*" if contact["favorite"] == True else " "
    print(f"[{favorite}] {index}. name: {contact["name"]}, fone: {contact["fone"]},  e-mai: {contact["email"]}")
  return

def favorite_list(contacts):
  print("---------------Favorite List----------------")
  lista_favorite= []
  for contact in contacts:
    if contact["favorite"] == True:
      lista_favorite.append(contact)
  
  for index, contact_favorite in enumerate(lista_favorite):
    index = index + 1
    favorite = "*" if contact_favorite["favorite"] == True else " "  
    print(f"[{favorite}] {index}. name: {contact_favorite["name"]}, fone: {contact_favorite["fone"]},  e-mai: {contact_favorite["email"]}")
  return

def delete_contact(contacts, index):
  print("--------------------Delete Contact-----------------")
  index = index - 1
  contact = contacts[index]
  contacts.remove(contact)
  print(f" O contact {index +1} has been deleted")
  return
#--------------------------------------------------------------------------
    
#------------------------------menu----------------------------------------
while True:
  print("-------------------Menu List--------------------")
  print("1. New Contact")
  print("2. Edit Contact")
  print("3. Mark a Contact with Favorite")
  print("4. show Contact List")
  print("5. Show Contact List Favorite")
  print("6. delete a Contact")
  print("7. Exit")
#-------------------------------------------------------------------------


#------------------------------execution-----------------------------------
  choice = int(input("Choose an operation: "))

  if choice == 1:
    print("Enter a new contact, The contact must have a name, phone number, and email")
    print("--------------------------------------------------------------------------")
    name = input("Enter a name: ")
    fone = input("Enter a fone: ")
    email = input("Enter a email: ")
    new_contact(contacts, name, fone, email)
  elif choice == 2:
    show_list(contacts)
    index = int(input("what contact you want edit? "))
    edit_contact(contacts, index )
  elif choice == 3:
     show_list(contacts)
     index = int(input("what contact you want mark with Favorite? "))
     favorite(contacts, index)
  elif choice == 4:
    show_list(contacts)
  elif choice == 5:
    favorite_list(contacts)
  elif choice == 6:
    show_list(contacts)
    index = int(input("what contact you want delete? "))
    delete_contact(contacts, index)
  elif choice == 7:
    break

    


    


