#author:DMH 1/13/22

last_initials = ['B','D','H','E','G','G','H','R','M','L','I','N','N','O','P','P','X','T','S','S','P']

first_names =[["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin" "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

def name_initial():
    initial_num = 0
    for row_num, row in enumerate(first_names):
        for name_num, name in enumerate(row):
                full_name = first_names[row_num][name_num]
                full_name += (" " + last_initials[name_num])
                print(full_name)


name_initial()
