using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Markup;
using System.Xml.Linq;

public static class DifferenceOfSquares
{

    public static int CalculateSquareOfSum(int max)
    {
       var numberList = Enumerable.Range(0, max).ToList();
       var sumNum = numberList.Sum();
       return (int)Math.Pow(2, sumNum);
    }

    public static int CalculateSumOfSquares(int max)
    {
        var numberList = Enumerable.Range(0, max).ToList();

        for (int i = 0; i <= max; i++)
        {
            Math.Pow(2, i);
            
        }
        
            
        

    }

    public static int CalculateDifferenceOfSquares(int max)
    {
        return 9;
    }
}