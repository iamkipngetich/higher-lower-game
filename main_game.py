from data_game import data
import random


def format_data(account):
    """format the account data into printable formart"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the users guess and followers count and return if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # generate a random account from game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Ask user to choose between 'A' or 'B' ").lower()

    # Check if user is correct
    # get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their selection
    if is_correct:
        score += 1
        print(f"You are right you got {score}")
    else:
        game_should_continue = False
        print(f"You are wrong your final score {score}")

    # score keeping

    # make the game repeatable

    # make the account at position B becomes the next account A
