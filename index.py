from os import path


class Calculations:
    # This class calculates the Present Value (PV) and Delta
    # on user provided inputs for the Future Value (FV), Rate (r)
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

    @classmethod
    def compute_delta(cls, present_value1, present_value2, rate1, rate2):
        try:
            delta_present_value = present_value2 - present_value1
            delta_rate = rate2 - rate1
            output = delta_present_value/delta_rate

            delta = round(output, 2)
            return delta

        except ZeroDivisionError:
            print "Delta cannot be computed for no rate change"


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

    user_option = str(raw_input("This program can compute Present Value"
                                " or Delta. What would you like to"
                                " compute: pv/delta?"))

    while run_again == 'y':
        while user_option == 'pv' or user_option == 'delta':
            try:
                future_value_1 = float(raw_input("Future Value: "))
                rate_1 = float(raw_input("Rate: "))
                number_of_periods_1 = float(raw_input("Number of periods: "))

                pv1 = Calculations(future_value_1, rate_1, number_of_periods_1)

                # Display Present Value and save it in a file Calculations.txt
                pv1_computed = pv1.compute_present_value()
                file.writelines('#' + '\n')
                output = (str(pv1) + "; the computed PV=$" + str(pv1_computed))
                print output
                file.writelines(output + '\n')

                if user_option == 'delta':
                    # Prompt user for second set of inputs for
                    # PresentValue2 for Delta computation
                    print "Second set of inputs for Delta"
                    future_value_2 = float(raw_input("Future Value: "))
                    rate_2 = float(raw_input("Rate: "))
                    number_of_periods_2 = float(raw_input("Number of"
                                                          " periods: "))

                    pv1 = Calculations(future_value_1, rate_1,
                                       number_of_periods_1)
                    pv2 = Calculations(future_value_2,
                                       rate_2, number_of_periods_2)

                    pv2_computed = pv2.compute_present_value()
                    output = (str(pv2) + "; the computed PV=$"
                              + str(pv2_computed))
                    print output
                    file.writelines(output + '\n')

                    # Call Method to compute Delta
                    delta_computed = Calculations.compute_delta(pv1_computed,
                                                                pv2_computed,
                                                                rate_1, rate_2)

                    if (str(delta_computed)) == 'None':
                        file.writelines("Delta cannot be computed"
                                        " for no rate change" + '\n')
                    else:
                        delta_output = "The computed Delta is " \
                                       + str(delta_computed) + "$/%"

                        print delta_output
                        file.writelines(delta_output + '\n')

                run_again = str(raw_input("Would you like to"
                                          " continue computing Present"
                                          " Value and Delta again: y/n?"))

                if run_again == 'y':
                    user_option = str(raw_input("What would you like to"
                                                " compute: pv/delta?"))

            except ValueError:
                run_again = str(raw_input("You need to enter a valid number."
                                          " Would you like to try again:y/n?"))

            while run_again != 'y' and run_again != 'n':
                run_again = str(raw_input("You did not enter one of the"
                                          " provided choices. Would you like"
                                          " to try again: y/n?"))

            if(run_again == 'n'):
                print "This program has now concluded. Hope you enjoyed!"
                break

        while user_option != 'pv' and user_option != 'delta':
            user_option = str(raw_input("You did not enter one of the"
                                        " provided choices. Would you like to"
                                        " try again: pv/delta?"))


if __name__ == '__main__':
    main()
