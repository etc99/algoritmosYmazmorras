using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public interface IDungeonParameters
{
    public string toQueryParameters();
}


public class SizeableDungeonParameters : IDungeonParameters
{

    int Height {get; set;}
    int Width {get; set;}
    int? Seed { get; set;}


    public SizeableDungeonParameters(int height, int width, int? seed)
    {
        Height = height;
        Width = width;
        Seed = seed;
    }

    public string toQueryParameters()
    {
        string queryString =  $"?height={Height}&width={Width}";

        if (Seed != null)
        {
            queryString += "&seed=" + Seed.ToString();
        }
        return queryString;
    }



}

public class IterativeDungeonParameters : IDungeonParameters
{

    int? Seed { get; set;}
    int Iterations {get; set;}

    public IterativeDungeonParameters(int iterations, int? seed)
    {
        Seed = seed;
        Iterations = iterations;
    }

    public string toQueryParameters()
    {
        string queryString =  $"?iterations={Iterations}";

        if (Seed != null)
        {
            queryString += "&seed=" + Seed.ToString();
        }
        return queryString;
    }
}


public class SizeableIterativeDungeonParameters : IDungeonParameters
{
    int? Seed { get; set;}
    int Iterations {get; set;}
    int Height {get; set;}
    int Width {get; set;}

    public SizeableIterativeDungeonParameters(int height, int width, int iterations ,int? seed)
    {
        Height = height;
        Width = width;
        Iterations = iterations;
        Seed = seed;
    }

    public string toQueryParameters()
    {
        string queryString =  $"?iterations={Iterations}&height={Height}&width={Width}";
        if (Seed != null)
        {
            queryString += "&seed=" + Seed.ToString();
        }
        return queryString;
    }
}


