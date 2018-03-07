using System;

namespace human 
{

    public class Wizard : Human
    {
        public new string name;
        public new int health { get; set; }
        public new int strength { get; set; }
        public new int intelligence { get; set; }
        public new int dexterity { get; set; }
    
        public Wizard(string givenname) : base(givenname) 
        {
            name = givenname;
            strength = 3;
            intelligence = 25;
            dexterity = 3;
            health = 50;
        }

        public void heal(object target)
        {
            Wizard person = target as Wizard;
            if(person == null)
            {
                Console.WriteLine("Failed to Heal");
            }
            else
            {
                person.health += intelligence * 10;
            }
        }    
    }
}