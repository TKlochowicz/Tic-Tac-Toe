class Grid():
    def __init__(self):
        self.grid ={
            '1': "1", "2": "2", "3":"3",
            '4': "4", "5": "5", "6":"6",
            '7': "7", "8": "8", "9":"9",
        }
    #Displays the grid
    def display(self):
        print("\n")
        print(f" {self.grid['1']} | {self.grid['2']} | {self.grid['3']} ")
        print("-----------")
        print(f" {self.grid['4']} | {self.grid['5']} | {self.grid['6']} ")
        print("-----------")
        print(f" {self.grid['7']} | {self.grid['8']} | {self.grid['9']} ")
        print("\n")

    def check_for_winner(self):
        #Horizontal strips
        if self.grid['1'] == self.grid['2'] == self.grid['3']:
            return True
        if self.grid['4'] == self.grid['5'] == self.grid['6']:
            return True
        if self.grid['7'] == self.grid['8'] == self.grid['9']:
            return True
        #Vertical strips
        if self.grid['1'] == self.grid['4'] == self.grid['7']:
            return True
        if self.grid['2'] == self.grid['5'] == self.grid['8']:
            return True
        if self.grid['3'] == self.grid['6'] == self.grid['9']:
            return True
        #Diagonal strips
        if self.grid['1'] == self.grid['5'] == self.grid['9']:
            return True
        if self.grid['3'] == self.grid['5'] == self.grid['7']:
            return True
        
        return False
        