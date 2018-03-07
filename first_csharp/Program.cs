using System;

namespace human
{
    class Program
    {
        static void Main(string[] args)
        {
            
            // Console.WriteLine("...human testing...");
            Human troy = new Human("Troy");
            Console.WriteLine(troy.name);
            Human sam = new Human("Sam", 5, 7, 5, 120);
            Console.WriteLine("Character Name: " + troy.name + " Health: " + troy.health + " Intelligence: " + troy.intelligence + " Dexterity: " + troy.dexterity + " Strength: " + troy.strength);
            Console.WriteLine("Character Name: " + sam.name + " Health: " + sam.health + " Intelligence: " + sam.intelligence + " Dexterity: " + sam.dexterity + " Strength: " + sam.strength);
            Console.WriteLine(troy.name + " is attacking " + sam.name);
            troy.attack(sam);
            Console.WriteLine("Character Name: " + troy.name + " Health: " + troy.health + " Intelligence: " + troy.intelligence + " Dexterity: " + troy.dexterity + " Strength: " + troy.strength);
            Console.WriteLine("Character Name: " + sam.name + " Health: " + sam.health + " Intelligence: " + sam.intelligence + " Dexterity: " + sam.dexterity + " Strength: " + sam.strength);

            Console.WriteLine("...wizard testing...");
            Wizard andonon = new Wizard("Andonon");
            Console.WriteLine("Wizard Name: "+andonon.name);
            Console.WriteLine("Wizard Intelligence: "+andonon.intelligence);
            Console.WriteLine(" ...wizard andonon is healing humnan troy testing...");
            
            Console.WriteLine("Troy.health: "+troy.health);
            Console.WriteLine("Andonon.health: "+andonon.health);            
            andonon.heal(troy); // expect this to fail. Wizard heals Wizards
            andonon.heal(andonon); // expect to work
            Console.WriteLine("Troy.health: "+troy.health);
            Console.WriteLine("Andonon.health: "+andonon.health);

        }
    }
}