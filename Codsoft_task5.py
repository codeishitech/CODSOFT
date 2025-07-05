class Contact_book:
    def __init__(self):
        self.contacts = {}   #creating an empty dictionary to store name of the contacts as key value pairs:
    def add_contact(self):  #function to add contacts
        name=input("Enter the name of the contact:")
        phone=input("Enter the phone number of the contact:")
        email = input("Enter the email address: ")
        address = input("Enter the residential address: ")
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")

    def remove_contact(self): #Function to delete/remove contact from your contact list.
        rname=input("Enter the contact name to be removed from the contact list: ")
        for name in self.contacts:   
            if name.lower() == rname.lower():   #This if-else ensures that our input for deletion is not case senstive. 
                self.contacts.pop(name)
                print("Contact removed successfully!")
                break
        else:
            print("Contact not found")
    
    def view_list(self):   #Function to view the contact book
        if self.contacts:
            print("Your Contact Book:")
            for name, detail in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone  : {detail['phone']}")
                print(f"Email  : {detail['email']}")
                print(f"Address: {detail['address']}")
        else:
            print("Your contact book is empty!")
    
    def search_book(self):   #Function to search the contact book
        sname=input("Enter the name of the contact you want to search:")
        for name, detail in self.contacts.items():
            if name.lower() == sname.lower():   # This if-else ensures that the search is not case senstive.
                print(f"\nName   : {name}")
                print(f"Phone  : {detail['phone']}")
                print(f"Email  : {detail['email']}")
                print(f"Address: {detail['address']}")
                print("Contact search successful!")
                break
        else:
            print("Contact not found")
    
obj=Contact_book()

while True:
    print("WELCOME TO THE CONTACT BOOK!")
    print("1.Add contact \n2.View contact \n3.Search contact \n4.Delete contact \n5.Exit the application")
    userin = input("Enter your choice:")
        #the user inputs the operations they want to perform and we use if-else to check which operation they want to perform:
    if userin == "1":
        obj.add_contact()
    elif userin == "2":
        obj.view_list()
    elif userin == "3":
        obj.search_book()
    elif userin == "4":
        obj.remove_contact()
    elif userin == "5":
        print("Thank you for using this application!")
        break
    else:
        print("Invalid choice. Please choose a valid choice among 1-5:")
        
            
                    