# This program randomly quizzes the user by displaying the name of a state
# and asks the user to enter the state's capital
import random

# Create accumulators for correct and incorrect responses
correct_response = 0
incorrect_response = 0

# Create the dictionary keys and values for the quiz
state_capital = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
                 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
                 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
                 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
                 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
                 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
                 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
                 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
                 'Vermont': 'Montpelier', 'Virgina': 'Richmond', 'Washington': 'Olympia',
                 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Run a while loop asking the user to provide the capital of the state given
while True:
    # Using the keys() method to return just the keys from the dictionary for the state variable
    state = random.choice(list(state_capital.keys()))
    # Using the get() method to return the keys values, which is the state capitals
    correct_answer = state_capital.get(state)

    # Creating a variable for user input
    answer = input('What is the Capital of ' + state + '? (or enter 0 to quit):')

    # If the answer is any digit end the loop
    if answer.isdigit():
        break

    # if the answer is the correct answer
    elif answer.lower() == correct_answer.lower():
        print("That is correct")
        print()
        # Keep a running total of correct answers
        correct_response += 1

    # if the answer is incorrect
    else:
        print('That is incorrect')
        print()
        # keep a running total of incorrect answers
        incorrect_response += 1

# Print out the total of correct and incorrect answers when finished with the quiz
print('You had ' + str(correct_response) + ' correct responses and ' + str(incorrect_response)
      + ' incorrect responses.')