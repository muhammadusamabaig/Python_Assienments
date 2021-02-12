class Battery():
    def __init__(self):
        self.battery_size=0
    @property
    def upgrade_battery(self):
        self.battery_size=85
        self.battery_size
    def get_range(self):
        return(self.battery_size)
        
class Admin():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self) :
        for i in self.privileges:
            print(i)
class  Privileges():
    def __init__(self):
        self.privileges=Admin()            