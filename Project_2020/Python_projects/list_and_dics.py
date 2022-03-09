def run():
    my_list =[1,"Hey there", True, 4.5]
    my_dict ={"firstname":"Mauricio", "Lastname":"Vargas"}

    super_list = [
        {"firstname":"Mauricio", "Lastname":"Vargas"},
        {"firstname":"David", "Lastname":"Vargas"},
        {"firstname":"Gabriel", "Lastname":"Vargas"},
        {"firstname":"Natalia", "Lastname":"Vargas"},
        {"firstname":"Sofia", "Lastname":"Vargas"},
        {"firstname":"Valentina", "Lastname":"Vargas"},
        ]
        
    super_dict = {
        "natural_numbers":[1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating nums": [1.1,4.5,6.43]
        }
        
    for key, value in super_dict.items():
        print(key, " ", value)

if __name__=='__main__':
    run