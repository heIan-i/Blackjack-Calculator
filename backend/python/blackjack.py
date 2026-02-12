import numpy as np

class Blackjack:
  def __init__(self, decks):
    self.dealer_hand = 0
    self.player_hand = 0
    self.decks = decks
    self.card_prob = np.array(decks*[4, 4, 4, 4, 4, 4, 4, 4, 4, 16])
    self.total = 52*decks
    self.dealer_probMatrix = np.zeros(23)
    self.transition_matrix = np.zeros((23, 23))
    self.payoffMatrix = np.zeros(6)
    self.count = 0
    self.true_count = 0

  def resetDeck(self):
    self.count = np.array(self.decks*[4, 4, 4, 4, 4, 4, 4, 4, 4, 16])
    self.count = 0
    self.true_count = 0

  def initialize_game(self):
    dealer_card = int(input("Input dealer's card (1–10): "))
    self.drawCardDealer(dealer_card)

    player_card1 = int(input("Input player card 1 (1–10): "))
    self.drawCardPlayer(player_card1)

    player_card2 = int(input("Input player card 2 (1–10): "))
    self.drawCardPlayer(player_card2)
 
  def drawCardPlayer(self, card):
    self.player_hand += card
    if card==1 and self.player_hand<12:
      self.player_hand += 10
    self.card_prob[card-1] -= 1
    self.total -= 1
    self.update_count(card)

  def drawCardDealer(self, card):
    self.dealer_hand += card
    if card==1 and self.dealer_hand<12:
      self.dealer_hand += 10
    self.card_prob[card-1] -= 1
    self.total -= 1
    self.update_count(card)
    self.dealer_probMatrix[self.dealer_hand] = 1

  def update_count(self, card):
    if card in [2, 3, 4, 5, 6]:
      self.count += 1
    elif card in [10, 1]:  # Count 10s and Aces as high
      self.count -= 1
    
    remaining_decks = np.sum(self.card_prob) / 52
    self.true_count = self.count / remaining_decks if remaining_decks > 0 else 0

  def fillTransitionMatrix(self):
    for i in range(23):
      for j in range(23):
        if j > 16:
          if j == i:
            self.transition_matrix[i][j]=1
        else:
          if i<=j:
            self.transition_matrix[i][j]=0;
          elif i>j+10:
            self.transition_matrix[i][j]=0
          else:
            self.transition_matrix[i][j]=self.card_prob[i-j-1]/self.total

  def dealerMarkov(self):
    return self.transition_matrix @ self.transition_matrix @ self.transition_matrix @ self.transition_matrix @ self.transition_matrix @ self.transition_matrix @ self.dealer_probMatrix
  
  def calc_payoff(self, playerHand):
    self.fillTransitionMatrix()
    dealerHand = self.dealerMarkov()
    croppedDealer = np.array([dealerHand[17], dealerHand[18], dealerHand[19], dealerHand[20], dealerHand[21], dealerHand[22]])
    res = np.zeros([2])
    hitPayoff = np.zeros((6,10))
    for i in range(6):
      for j in range(10):
        if j+playerHand > 21:
          hitPayoff[i][j] = -1
        elif i == 5:
          hitPayoff[i][j] = 1
        elif i < j+playerHand:
          hitPayoff[i][j] = 1
        elif i == j+playerHand:
          hitPayoff[i][j] = 0
        else:
          hitPayoff[i][j] = -1
    splitPayoff = np.zeros((6))
    for i in range(6):
      if i == 5:
        splitPayoff[i] = 1
      if i<playerHand:
        splitPayoff[i] = 1
      elif i==playerHand:
        splitPayoff[i] = 0
      else:
        splitPayoff[i] = -1
    res[0] = (croppedDealer.T @ hitPayoff @ self.card_prob)/30
    res[1] = (croppedDealer.T @ splitPayoff)/6
    return res;

  def resetGame(self):
    self.dealer_hand = 0
    self.player_hand = 0
    self.dealer_probMatrix = np.zeros([23])

  def print_payoff(self):
    payoff = self.calc_payoff(self.player_hand);
    print("Hit:", payoff[0])
    print("Stand:", payoff[1])
    print("Double Down:", 2*payoff[0])
    print("Split:", self.calc_payoff(self.player_hand/2))
    print("Surrender: -0.5")
    print("Insure:", 2*self.card_prob[9]/self.total + -1*(1-(self.card_prob[9]/self.total)))

def run_game():
    game = Blackjack(decks=1)

    while True:
        game.initialize_game()
        while True:
          game.print_payoff()
          choice = input("\nAction? (h/s/d/p/u): ").strip().lower()
          if choice == 'h':
            game.drawCardPlayer
          elif choice == 's':
            break
          elif choice == 'd':
            game.drawCardPlayer
            break
          elif choice == 'p':
            game.player_hand = game.player_hand/2
          elif choice == 'u':
            break

        # Show result and ask to continue
        game.resetGame()
        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again != 'y':
            break

# Run it
if __name__ == "__main__":
    run_game()

  


#Do you want to continue?
#recurse 

