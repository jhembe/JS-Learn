# let's initiate our pet lis
my_pets = ['Zophie','Pooka','Fat-tail'];

# start to ask user
# let's use while loop, she should put entries unitill she decides
# to stop
num1 = 20;
num2 = 0;
div = 0;
try:
    div = num1/num2;
except ZeroDivisionError:
    print("Pass numbers greater than Zero");
    
hello = "heyy";
hello.capitalize

while True:
    name = input("Enter a pet's name : ");
    if name == '':
        break;
    
    # chek for pet availability status
    pet_status = name in my_pets;
    
    if pet_status == False:
        print("There is no such pet")
        response = input("Do you want to add the name :").lower();
        if response == 'yes':
            my_pets = my_pets + [name]
        else:
            break;
    


## now let's printout the list again
print("Here are the pet names :");
for pet in my_pets:
    print(pet);

            
