# OBJECT :
# - field
# - behavior

# Membuat Class
class User:
    # class variabel
    total = 0    
    
    # contructor
    def __init__(self,name,email,role):
    # memiliki atribut/field name,email,role
        self.name = name
        self.email = email
        self.role = role 
        User.total+=1

    def ingfo(self):
        return f"Nama  : {self.name} | Email : {self.email} | Role  : {self.role}"

    def update_role(self,new_role):
        if self.role != "user" :
            self.role = new_role

# Membuat Object
user1 = User("Rahman","rahman@gmail.com","admin")
user2 = User("Qolbi","qolbi@gmail.com","user")

print(user1.name)
print(user2.name)
print(User.total)

print(user1.ingfo())
user1.update_role("user")
print(user1.ingfo())
user1.update_role("admin")
print(user1.ingfo())

