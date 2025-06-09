# File for the stored contacts
contact_file = "contacts.txt"

def get_contacts():
	# Function to reade from file
	contact = {}
	try:
		with open(contact_file, 'r') as file:
			for details in file:
				name, number, email, address = details.strip().split(',')
				contact[name] = (number, email, address)
	except FileNotFoundError:
		pass
	return contact

def save_contacts(contact):
	# Funtion to write contact in file
    with open(contact_file, 'w') as file:
        for name, (number, email, address) in contact.items():
            file.write(f"{name},{number},{email},{address}\n")

contact = get_contacts()
while True:
	# Choice for operation in contact book
	choose = input(f"\n1. Show Contacts\n2. Add Contact\n3. Search Contact\n4. Delete Contact\n5. Edit Contact\n6. Exit\n\nEnter your choice: ").capitalize()

	if(choose == '1' or choose == "Show Contacts"):
		if contact:
			print("\nAll contacts: ")
			for name, (number, email, address) in contact.items():
				print(f"Name: {name}, Number: {number}, E-mail: {email}, Address: {address}")
		else:
			print("\nNo contacts to show.")

	elif(choose == '2' or choose == "Add Contact"):
		# Adds the contact into the contact book
		name = input("\nEnter the name of the person: ").capitalize()
		number = (input("Enter the contact number of the person: "))
		if not(number.isdigit or len(number) != 10):
			print("The number should contain exactly 10 digit!!")
			continue
		email = input("Enter the E-mail of the person: ").lower()
		address = input("Enter the address of the person: ").capitalize()

		contact[name] = number, email, address
		print(f"Contact for {name} is added successfully.")
		save_contacts(contact)

	elif(choose == '3' or choose == "Search Contact"):
		# Searches the entered contact
		search = input("\nEnter the name you want to search: ").capitalize()
		if search in contact:
			print(f"{search} 's contact details are {contact[search]}")
		else:
			print("\nPerson not found in contact book!!!")

	elif(choose == '4' or choose == "Delete Contact"):
		# Deletes the entered contact
		delete = input("\nEnter the name you want to delete: ").capitalize()
		if delete in contact:
			print(f"Contact {delete} is deleted successfully.")
			del contact[delete]
			save_contacts(contact)
		else:
			print("\nContact not found!!!")

	elif(choose == '5' or choose == "Edit Contact"):
		# Edits the entered contact
		contact_edit = input("\nEnter the contact you want to edit: ").capitalize()

		if contact_edit in contact:
			
			edit = input(f"\na. Name\nb. Contact Number\nc. E-mail\nd. Address\n\nWhat do you want to edit in contact: ").capitalize()

			if(edit == 'A' or edit == "Name"):
				# Edits the nam,e of the entered contact
				new_name = input("\nEnter the new name: ").capitalize()
				contact[new_name] = number, email, address
				del contact[name]
				print("Name Updated.")

			elif(edit == 'B' or edit == "Contact Number"):
				# Edits the number of the entered contact
				new_number = (input("\nEnter the new number: "))
				if(new_number.isdigit and len(new_number == 10)):
					contact[name] = new_number, email, address
					print("Contact number updated.")
				else:
					print("The number should contain 10 digit!!")

			elif(edit == 'C' or edit == "E-mail"):
				# Edits the email of the entered contact
				new_email = input("\nEnter the new email of the person: ").lower()
				contact[name] = number, new_email, address
				print("E-mail updated.")

			elif(edit == 'D' or edit == "Address"):
				# Edits the address of the entered contact
				new_address = input("\nEnter the new address of the person: ").capitalize()
				contact[name] = number, email, new_address
				print("Address updated.")

			else:
				print("Invalid option!!!")

			# To save the changes
			if input("\nDo you want to save the changes to file? (yes/no): ").lower() == 'yes':
				save_contacts(contact)
				print("Changes saved.")
		else:
			print("Contact not found!!!")
	
	elif(choose == '6' or choose == "Exit"):
		print("\nExiting contact book.")
		break

	else:
		print("\nInvalid choice!!! Enter a valid option.")
		break
