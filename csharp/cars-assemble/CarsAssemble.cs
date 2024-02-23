using System;

static class AssemblyLine
{
    public static double SuccessRate(int speed)
    {
       return speed switch
    {
        0 => 0,
        >= 1 and <= 4 => 1,   // Using range matching for speed within 1 to 4
        >= 5 and <= 8 => 0.9, // Using range matching for speed within 5 to 8
        9 => 0.8,
        _ => 0.77 // Default case for any speed above 9
    };
    }
    
    public static double ProductionRatePerHour(int speed)
    {
        double prod = speed * 221; // Calculate base production rate

    // Apply success rate multiplier based on speed
    double successRate = speed switch
    {
        0 => 0, // No production for speed 0
        <= 4 => 1, // Full rate for speed 1 to 4
        <= 8 => 0.9, // 90% rate for speed 5 to 8
        9 => 0.8, // 80% rate for speed 9
        _ => 0.77 // 77% rate for speeds above 9
    };

    return prod * successRate; // Return the final production rate per hour
    }

    public static int WorkingItemsPerMinute(int speed)
    {
       
    double itemsPerMin = speed * 221 / 60.0; // Calculate items per minute as a double to maintain precision

    double successRate = speed switch
    {
        1 => 1, // Full rate for speed 1
        >= 5 and <= 8 => 0.9, // 90% rate for speeds 5 to 8
        9 => 0.8, // 80% rate for speed 9
        10 => 0.77, // 77% rate for speed 10
        _ => 1 // Default to full rate for other speeds (assumed to be 1 to 4 based on your original code)
    };

    return (int)(itemsPerMin * successRate); // Cast the final result to int and return
    }
}
