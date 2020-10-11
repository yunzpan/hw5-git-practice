import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. 
        # But returning will allow for unit testing of your unit test, 
        # and allow you to check your answer with the autograder.  This is optional today.

        '''
        A = hw5_cards.Card(1, 12)
        self.assertEqual(A.rank,12)
        self.assertEqual(A.rank_name, "Queen")
 

        return A.rank_name, A.rank_name
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, 
        its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have
        #  return statements. But returning will allow for unit 
        # testing of your unit test, and allow you to check your 
        # answer with the autograder.  This is optional today.

        '''
        A = hw5_cards.Card(1, 12)
        self.assertEqual(A.suit,1)
        self.assertEqual(A.suit_name,"Clubs")
        return A.suit_name,A.suit_name   
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance 
        that is created with suit=3, rank=13, 
        it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        B = hw5_cards.Card(3, 13)
        #self.assertEqual(B.rank,13)
        self.assertEqual(B.rank_name,"King")
        #self.assertEqual(B.suit, 3)
        self.assertEqual(B.suit_name, "Spades")
        return B.__str__(),B.__str__()
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a deck instance, 
        it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.deck = hw5_cards.Deck()
        self.assertEqual(len(self.deck.cards),52)
        return len(self.deck.cards),52  

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, 
        it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert 
        statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        
        self.deck = hw5_cards.Deck()
        card = self.deck.deal_card()
        self.assertIsInstance(card,hw5_cards.Card)
        return card,hw5_cards.Card 
        
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, 
        the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.deck = hw5_cards.Deck()
        self.deck.deal_card()
        self.assertEqual(len(self.deck.cards),51)
        return len(self.deck.cards),51   
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, 
        the deck has one more card in it afterwards. 
        (Please note that you want to use deal_card function first 
        to remove a card from the deck and then add the same card 
        back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.deck = hw5_cards.Deck()
        before = self.deck.cards
        card = self.deck.deal_card()
        replace_card = self.deck.replace_card(card)
        after = self.deck.cards
        self.assertEqual(len(after),52)
        return len(before),len(after),52
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method 
        with a card that is already in the deck, 
        the deck size is not affected.(The function must 
        silently ignore it if you try to add a card that’s 
        already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_test = hw5_cards.Card(1, 1)
        self.deck = hw5_cards.Deck()
        self.deck.replace_card(c_test)
        card_list = self.deck.cards
        self.assertIn(c_test.__str__(), [c.__str__() for c in self.deck.cards])
        self.assertEqual (len(card_list),52)
        return len(card_list),52


if __name__=="__main__":
    unittest.main()