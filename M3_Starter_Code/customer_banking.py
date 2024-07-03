
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance = float(input("Please set savings balance for savings account "))
    interest_rate = float(input("Please set interest rate for savings account "))
    months = int(input("Please set months for savings account "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, interest_rate, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print('Your interest earned is $ ', format(interest_earned, ",.2f"))
    print('Your new balance is $ ', format(updated_savings_balance, ",.2f"))

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    cd_balance = float(input("Please set CD balance for CD account "))
    interest_rate = float(input("Please set interest rate for CD account "))
    months = int(input('Please set months '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, interest_rate, months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('You interest earned is ', format(interest_earned, ",.2f"))
    print('Your updated CD account balance is ', format(updated_cd_balance, ",.2f"))
    
if __name__ == "__main__":
    # Call the main function.
    main()