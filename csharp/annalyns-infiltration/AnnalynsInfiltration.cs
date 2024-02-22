using System;

static class QuestLogic
{
    public static bool CanFastAttack(bool knightIsAwake)
    {
        return !knightIsAwake;
    }

    //Instead of checking each combination individually, need to think about the overall requirements for a successful spying operation. 
    //For example, spying can be successful as long as not everyone is asleep. 
    public static bool CanSpy(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake)
    {
        return knightIsAwake || archerIsAwake || prisonerIsAwake;
    }

    public static bool CanSignalPrisoner(bool archerIsAwake, bool prisonerIsAwake)
    {
        return !archerIsAwake && prisonerIsAwake;
    }

    public static bool CanFreePrisoner(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake, bool petDogIsPresent)
    {
        if (!knightIsAwake && !archerIsAwake && prisonerIsAwake && petDogIsPresent)
        {
            return true;
        }
        if (!knightIsAwake && !archerIsAwake && prisonerIsAwake && !petDogIsPresent)
        {
            return true;
        }
        if (knightIsAwake && !archerIsAwake && !prisonerIsAwake && petDogIsPresent)
        {
            return true;
        }
        if (knightIsAwake && !archerIsAwake && prisonerIsAwake && petDogIsPresent)
        {
            return true;
        }
        else
        {
            return !knightIsAwake && !archerIsAwake && !prisonerIsAwake && petDogIsPresent;
        }
        
    }
}
