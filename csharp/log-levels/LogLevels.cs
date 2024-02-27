using System;

static class LogLine
{
    public static string Message(string logLine)
    {
        if (logLine.Contains("/r"))
        {
            string str = logLine.Substring(logLine.IndexOf(" "));
            string trimmedStr = str.Trim();
            return trimmedStr.Substring(str.IndexOf("/"));
        }
        else
        {
            string str = logLine.Substring(logLine.IndexOf(" "));
            return str.Trim();
        }
    }

    public static string LogLevel(string logLine)
    {
        char firstChar = '[';
        char secondChar = ']';

        int startPos = logLine.IndexOf(firstChar);
        int endPos = logLine.IndexOf(secondChar);

        

    }

    public static string Reformat(string logLine)
    {
        return "0";
    }
}
