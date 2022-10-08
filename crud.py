import requests

class send_payload:
    def __init__(self):
        self.payload_insert = {"id": '',"firstname":'',"lastname":'',"phone":'',"address":'',"email":''}
        self.payload_select = {}
        self.payload_update = {"id":'',"lastname":'', "address":''}
        self.payload_delete = {"id":''}
    def choose(self):
        chs = input("\n\nPlease choose what you want to do: \n\n" + "press 1: To Insert Data in the Database\n" + "press 2: To Read All Data in the Database \n" + "press 3: To Update some info in the Database\n" +"press 4: To Delete Specific User in the Database\n"+"press 5: To Exit Program \n\n>>>")        
        return chs

obj_send_payload = send_payload()
while True:
    chosen = obj_send_payload.choose()


    if chosen == "1":
        input_firstname = input("Enter Firstname: ")
        obj_send_payload.payload_insert["firstname"] = input_firstname

        input_lastname = input("Enter Lastname: ")
        obj_send_payload.payload_insert["lastname"] = input_lastname

        input_phone = input("Enter Phone number: ")
        obj_send_payload.payload_insert["contact"] = input_phone

        input_address = input("Enter Address: ")
        obj_send_payload.payload_insert["address"] = input_address

        input_email = input("Enter Email: ")
        obj_send_payload.payload_insert["email"] = input_email

        print(obj_send_payload.payload_insert)

        r= requests.post('http://localhost:2022/users',json=obj_send_payload.payload_insert)
        print(r.text)

    elif chosen == "2":
        r= requests.get('http://localhost:2022/users',json=obj_send_payload.payload_select)
        print(r.text)
        
    elif chosen == "3":

        input_id = input("ID:")
        obj_send_payload.payload_update["id"] = input_id

        input_lastname = input("Enter Lastname: ")
        obj_send_payload.payload_update["lastname"] = input_lastname

        input_address = input("Enter Address: ")
        obj_send_payload.payload_update["address"] = input_address
        
        print(obj_send_payload.payload_update)

        r= requests.put('http://localhost:2022/users',json=obj_send_payload.payload_update)
        print(r.text)

        
    elif chosen == "4":
        input_id = input("Enter ID You Wish to delete: ")
        obj_send_payload.payload_delete["id"] = input_id
        r= requests.delete('http://localhost:2022/users',json=obj_send_payload.payload_delete)
        print(r.text)
    elif chosen == "5":
        print("Program Terminated")
        break
    else:
        print("Wrong Input, Please Try Again!! \n")