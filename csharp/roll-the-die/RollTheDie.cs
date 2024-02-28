using System;

public class Player
{
    public int RollDie()
    {
        System.Random random = new (); 
        return random.Next(1, 18);
    }

    public double GenerateSpellStrength()
    {
        System.Random random = new (); 
        return random.Next((int)0.0, (int)100.0);
    }
}
