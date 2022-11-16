contacts = []

while(True):
    response = input('(1)add contact (2)print contacts (3)Exit: ')

    if response == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
        person_email = input('Email: ')

        person_data = {
            'name': person_name,
            'surname': person_surname,
            'phone': person_phone,
            'email': person_email
        }

        contacts.append(person_data)
    elif response == '2':
        for contact in contacts:
             print("---Contact---")
             print(f"{contact['name']} {contact['surname']}")
             print(f"{contact['phone']}")
             print(f"{contact['email']}")
             
    elif response == '3':
         print('Goodbye.ヾ(•ω•`)o')
         exit()
    else:
        print('Type between 1, 2 or 3.')