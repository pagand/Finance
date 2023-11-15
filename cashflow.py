import json
import matplotlib.pyplot as plt


# Load the data from the 2023.json file
with open('2023.json') as f:
    data = json.load(f)

# this is the format of the json file
# "January": {"Income": 
# {"Payroll Deposit, SFU":{date: amount}, "Accounts Payable": {date: amount}, ... },
# {"Savings":
# {Customer Transfer Dr. MB-TRANSFER:{date: amount} ,...},
# {"Expenses": 
# {"American Express":{date: amount}, "WITHDRAWAL" :{date: amount}}
# }, ... }

# Extract the cashflow values for each month from the loaded data
# compute each month
def main():
    cashflow = []
    incomes_plot = {}
    expenses_plot = {}
    savings_plot = {}
    for month in data:
        # Income
        incomes = data[month]["Income"]
        income_values = list(incomes.values())
        # compute the sum for the dictionary values in the list
        income_values = [sum(i.values()) for i in income_values]
        income_category = list(incomes.keys())
        total_incomes = sum(income_values)
        print(income_category)
        # put all the income values in  income_plot dictioanry for each category, on each month.
        # if specific category is not in the dictionary, add it to the dictionary. put zero for previous months
        # if some categories does not have values, put zero for that month
        for i in income_category:
            if i not in incomes_plot:
                incomes_plot[i] = [0] * len(data)
            incomes_plot[i][list(data).index(month)] = income_values[income_category.index(i)]


        # Expenses
        expenses = data[month]["Expenses"]
        expenses_values = list(expenses.values())
        expenses_values = [sum(i.values()) for i in expenses_values]
        expense_category = list(expenses.keys())
        total_expenses = sum(expenses_values)
        # put all the expenses values in  expenses_plot dictioanry for each category, on each month.
        for i in expense_category:
            if i not in expenses_plot:
                expenses_plot[i] = [0] * len(data)
            expenses_plot[i][list(data).index(month)] = expenses_values[expense_category.index(i)]

        # Savings
        savings = data[month]["Savings"]
        savings_values = list(savings.values())
        savings_values = [sum(i.values()) for i in savings_values]
        savings_category = list(savings.keys())
        total_savings = sum(savings_values)
        # put all the savings values in  savings_plot dictioanry for each category, on each month.
        for i in savings_category:
            if i not in savings_plot:
                savings_plot[i] = [0] * len(data)
            savings_plot[i][list(data).index(month)] = savings_values[savings_category.index(i)]


        # Calculate the cashflow for each month
        

        cashflow.append(total_incomes + total_expenses + total_savings)

        # Print the cashflow for each month
    print(cashflow)
    # plot the cashflow over time
    plt.figure(figsize=(10, 5))
    plt.plot(list(data), cashflow, label='Cashflow')
    # plot the summation of the cashflow over time
    plt.plot(list(data), [sum(cashflow[:i]) for i in range(1, len(cashflow)+1)], label='Cumulative Cashflow')
    plt.xlabel('Month')
    plt.legend(loc='best')

    # let's move the Bill Payement, MB-QUESTRADE from expenses to savings
    # remove the Bill Payement, MB-QUESTRADE from expenses_plot dictionary
    invest = expenses_plot.pop('Bill Payment')
    # add the Bill Payement, MB-QUESTRADE to savings_plot dictionary and make the values negative
    # savings_plot['Bill Payment'] = invest
    # make all the values in the saving_plot dictionary negative
    # savings_plot = {k: [-i for i in v] for k, v in savings_plot.items()}
    

    # plot the  incomes_plot, expenses_plot, savings_plot
    plt.figure(figsize=(10, 5))
    plt.stackplot(list(data), incomes_plot.values(), labels=incomes_plot.keys())
    plt.legend(loc='upper left')
    plt.title('Income')

    plt.figure(figsize=(10, 5))
    plt.stackplot(list(data), expenses_plot.values(), labels=expenses_plot.keys())
    plt.legend(loc='best')
    plt.title('Expenses')

    plt.figure(figsize=(10, 5))
    plt.stackplot(list(data), savings_plot.values(), labels=savings_plot.keys())
    # plot the negative of invest on the same graph as savings
    plt.plot(list(data), [-i for i in invest], label='Invested')
    plt.title('Savings')
    plt.legend(loc='best')


    plt.show()

if __name__ == "__main__":
    main()


