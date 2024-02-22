class Lasagna
{

    // TODO: define the 'ExpectedMinutesInOven()' method
    public int ExpectedMinutesInOven() => 40;

    // TODO: define the 'RemainingMinutesInOven()' method
    public int RemainingMinutesInOven(int minutesAleadyInOven)
    {
        return ExpectedMinutesInOven() - minutesAleadyInOven;
    }

    // TODO: define the 'PreparationTimeInMinutes()' method
    public int PreparationTimeInMinutes(int layers)
    {
        return layers*2;
    }

    // TODO: define the 'ElapsedTimeInMinutes()' method
    public int ElapsedTimeInMinutes(int layers, int minutesAleadyInOven)
    {
        return PreparationTimeInMinutes(layers) + minutesAleadyInOven;
    }

}

    
