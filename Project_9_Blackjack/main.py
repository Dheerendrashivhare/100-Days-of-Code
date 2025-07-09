import random


####################Blackjack Project#####################
def deal_card():
  """Returns a random card from the deck."""
  deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(deck)
  return card


# print(deal_card()

# def calculate_score(score_list:list):


def play_game():
  """Starts and manages a game of Blackjack."""
  user_cards = []
  computer_cards = []

  for _ in range(0, 2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  print(f"your cards: {user_cards} \n Computer cards : {computer_cards}")

  # def calculate_score():
  other_card_bool = True
  user_score = sum(user_cards)
  computer_score = sum(computer_cards)
  while other_card_bool:
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    if 11 in user_cards and 10 in user_cards:
      return "You win"
    elif 11 in computer_cards and 10 in computer_cards:
      return "Loose"

    if user_score >= 21:
      if 11 not in user_cards:
        return "loose"
      else:
        if (user_score - 10) >= 21:
          return "Loose"
    want_other_card = input(
        "Have you want the other card if yes then type yes: ")
    if want_other_card != 'yes':
      other_card_bool = False
    else:
      other_card = deal_card()
      print(f"Your new card is {other_card}")
      user_cards.append(other_card)

  while computer_score < 16:
    computer_cards.append(deal_card())
    print(f"Computer new card : {computer_cards[-1::]}")
    computer_score = sum(computer_cards)
  if computer_score >= 21:
    return "You win"
  if user_score > computer_score:
    return "You win"
  elif computer_score == user_score:
    return "Drow"
  else:
    return "You Loose"


print(play_game())

# # This is a Blackjack game.
# # The goal is to have a hand that totals closer to 21 than the dealer's hand without exceeding 21.
# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card

# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""
#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)

# def compare(user_score, computer_score):
#   """Compare user and computer scores and determine the result."""
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"
#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"

# def play_game():
#   """Starts and manages a game of Blackjack."""
#   user_cards = []
#   computer_cards = []
#   is_game_over = False

#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

#   while not is_game_over:
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(deal_card())
#       else:
#         is_game_over = True

#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))

# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#   play_game()
