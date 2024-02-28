using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Markup;
using System.Xml.Linq;

public static class DifferenceOfSquares
{

    public static int CalculateSquareOfSum(int max)
    {
       var sumNum = Enumerable.Range(0, max).Select(number => number).Sum();
       return sumNum^2;
    }

    public static int CalculateSumOfSquares(int max)
    {
        return Enumerable.Range(0, max + 1).Select(number => number * number).Sum();
    }

    public static int CalculateDifferenceOfSquares(int max)
    {
        var sumNum = Enumerable.Range(0, max).Select(number => number).Sum();
        var square = sumNum^2;
        var sqNum = Enumerable.Range(0, max + 1).Select(number => number * number).Sum();

        return square - sqNum;
    
    }
}