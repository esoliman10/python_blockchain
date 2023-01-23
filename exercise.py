name = "Kamote Smith"
age = 20

def print_data():
    print(name + " is " + str(age) + " years old.")

print_data()

def print_data(name, age):
    print(name + " is " + str(age) + " years old.")

print_data("Kamote Smith", 20)
print_data("JR Smith", 30)

# Create a function which calculates and returns the number of decades a person has lived.
def calculate_decades(age):
    decade = age // 10
    print("You have lived for " + str(decade) + " decades.")

calculate_decades(25)