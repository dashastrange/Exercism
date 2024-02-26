using System;

static class SavingsAccount
{
    public static float InterestRate(decimal balance)
    {
        return balance switch
        {
            < 0 => 3.213f,
            < 1000 => 0.5f,
            < 5000 => 1.621f,
            _ => 2.475f,

        };
    }

    public static decimal Interest(decimal balance)
    {
        return balance switch
        {
            <0m => balance/100 * 3.213m,
            >0m and <1000m => balance/100 * 0.5m,
            >= 1000m and < 5000m => balance/100 * 1.621m,
            _ => balance/100 * 2.475m

        };
    }

    public static decimal AnnualBalanceUpdate(decimal balance) => SavingsAccount.Interest(balance) + balance;
    public static int YearsBeforeDesiredBalance(decimal balance, decimal targetBalance)
    {
        int years = 0;
        while(balance < targetBalance){
            balance = SavingsAccount.AnnualBalanceUpdate(balance);
            years++;
        }
    return years;
 
    }
}
