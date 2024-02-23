using System;

static class AssemblyLine
{
    public static double SuccessRate(int speed)
    {
        if (speed == 0)
        {
            return 0;
        }
        if (speed <= 4 && speed >=1)
        {
            return 1;
        }
        if (speed <=8 && speed >= 5)
        {
            return 0.9;
        }
        if (speed == 9)
        {
            return 0.8;
        }
        else
        {
            return 0.77;
        }
    }
    
    public static double ProductionRatePerHour(int speed)
    {
        throw new NotImplementedException("Please implement the (static) AssemblyLine.ProductionRatePerHour() method");
    }

    public static int WorkingItemsPerMinute(int speed)
    {
        throw new NotImplementedException("Please implement the (static) AssemblyLine.WorkingItemsPerMinute() method");
    }
}
