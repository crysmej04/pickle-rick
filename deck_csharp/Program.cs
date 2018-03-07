//continuing to work on...
using System;

namespace deck_csharp
{
    class Program
    {
        static void Main(string[] args)
        {
             Card jon = new Card("jon", "black", 1);
             Console.WriteLine(jon.val);
             Deck bob = new Deck().reset();
             Console.WriteLine(bob.cards.Count);
            Deck troy = new Deck();
            Player bill = new Player("Rick");
            Console.WriteLine(troy.cards.Count);

            bill.draw(troy);
            Console.WriteLine(bill.hand.Count);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            bill.draw(troy);
            Console.WriteLine(bill.hand.Count);
            bill.discard(4);
            Console.WriteLine(bill.hand.Count);
            
        }
    }
}