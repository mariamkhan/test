from os import path


class Calculations:
    # This class calculates the Present Value (PV)
    # on user provided inputs for the Fututre Value (FV), Rate (r)
    # Number of periods (n)

    def __init__(self, future_value,
                 rate, number_of_periods):
        self.future_value = future_value
        self.rate = rate
        self.number_of_periods = number_of_periods

    def __str__(self):
        return "For FV=$" + str(self.future_value) \
               + ", r=" + str(self.rate) + "%, n=" \
               + str(self.number_of_periods) + "year"

    def compute_present_value(self):
        output = self.future_value \
                 / pow((1 + (self.rate * 1.0) / 100), self.number_of_periods)

        present_value = round(output, 2)
        return present_value


def main():
    # This is the main program which creates an instance of the above
    # Calculations class. It allows the user to enter as many different
    # combinations of inputs. It also does error handling for when the
    # the user presses another key by mistake.
    run_again = 'y'
    i = 1

    # If the output file exists increment the name otherwise create a new file
    file_name = "Calculations" + str(i) + ".txt"
    while path.exists(file_name):
        file_name = "Calculations" + str(i) + ".txt"
        i += 1
    file = open(file_name, "w")

    print("This program computes the Present Value")

    while run_again == 'y':

        try:

            future_value = float(raw_input("Future Value: "))
            rate = float(raw_input("Rate: "))
            number_of_periods = float(raw_input("Number of periods: "))

            calculator = Calculations(future_value, rate, number_of_periods)

            # Display the output as well as save it in a file Calculations.txt
            output = (str(calculator) + "; the computed PV=$"
                      + str(calculator.compute_present_value()))
            print output
            file.writelines(output + '\n')

            run_again = str(raw_input("Would you like to"
                                      " continue computing Present"
                                      " Value: y/n?"))

        except ValueError:
            run_again = str(raw_input("You need to enter a valid number. "
                                      "Would you like to try again:y/n?"))

        while run_again != 'y' and run_again != 'n':
            run_again = str(raw_input("You did not enter one of the provided "
                                      "choices. Would you like to "
                                      "try again:y/n?"))

        if(run_again == 'n'):
            print "This program has now concluded. Hope you enjoyed!"
            break


if __name__ == '__main__':
    main()
