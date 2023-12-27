def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

def feet_to_meters(feet):
    meters = feet / 3.28084
    return meters

def kilograms_to_pounds(kilograms):
    pounds = kilograms * 2.20462
    return pounds

def pounds_to_kilograms(pounds):
    kilograms = pounds / 2.20462
    return kilograms
def tryexcept():
        global conversion_choice,value
        
        conversion_choice = input("Enter conversion direction (1 for A to B, 2 for B to A): ")
        
        if conversion_choice not in ["1","2"]:
            print("Error: Please enter a valid choice for conversion direction.")
            
        else:
            conversion_choice=int(conversion_choice)
            try:
                value = float(input("Enter the value to convert: "))
            except ValueError:
                print("Error: Please enter a valid numeric value.")
            


def unit_converter():
    while True:
        print("\n\t\t\t\tUnit Converter: Choose Conversion Type")
        print("\t\t1. Temperature Converter (Celsius to Fahrenheit and vice versa)")
        print("\t\t2. Length Converter (Meters to Feet and vice versa)")
        print("\t\t3. Weight Converter (Kilograms to Pounds and vice versa)")
        print("\t\t4. Exit\n\n")

        try:
            choice = int(input("Enter your choice (1, 2, 3, or 4 to exit): "))
        except ValueError:
            print("Error: Please enter a valid numeric choice.")
            continue

        if choice == 4:
            print("Exiting the program. Goodbye!")
            break

        if choice == 1:
            print("\nYou have chosen Celsius to Fahrenheit and vice versa\n")
            tryexcept()
            if conversion_choice == 1:
                converted_value = celsius_to_fahrenheit(value)
                print(f"{value} Celsius is approximately {converted_value:.2f} Fahrenheit.")
            elif conversion_choice == 2:
                converted_value = fahrenheit_to_celsius(value)
                print(f"{value} Fahrenheit is approximately {converted_value:.2f} Celsius.")
           
        elif choice == 2:
            print("\nYou have chosen Metres to Feet and vice versa\n")
            tryexcept()
            if conversion_choice == 1:
                converted_value = meters_to_feet(value)
                print(f"{value} meters is approximately {converted_value:.2f} feet.")
            elif conversion_choice == 2:
                converted_value = feet_to_meters(value)
                print(f"{value} feet is approximately {converted_value:.2f} meters.")
         
        elif choice == 3:
            print("\nYou have chosen Kg to Pounds and vice versa\n")
            tryexcept()
            if conversion_choice == 1:
                converted_value = kilograms_to_pounds(value)
                print(f"{value} kilograms is approximately {converted_value:.2f} pounds.")
            elif conversion_choice == 2:
                converted_value = pounds_to_kilograms(value)
                print(f"{value} pounds is approximately {converted_value:.2f} kilograms.")
           
        else:
            print("Error: Please enter a valid choice (1, 2, 3, or 4).")

if __name__ == "__main__":
    unit_converter()

