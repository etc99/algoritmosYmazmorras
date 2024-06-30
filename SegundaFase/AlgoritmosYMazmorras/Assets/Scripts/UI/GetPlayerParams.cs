using System.Collections;
using System.Collections.Generic;
using TMPro;
using System;
using UnityEngine;

public class InvalidParametersException : Exception
{

}


public class GetPlayerParams : MonoBehaviour
{

    [SerializeField] private TMP_InputField HeightParameterUI;
    [SerializeField] private TMP_InputField WidthParameterUI;
    [SerializeField] private TMP_InputField SeedParameterUI;
    [SerializeField] private TMP_InputField IterationsParameterUI;


    public IDungeonParameters GetDungeonParameters()
    {
        List<String> SizeableDungeons = new List<String> { "prim", "eller", "kruskal", "binary", "aldous-broder", "dfs" };
        List<String> IterativeDungeons = new List<String> { "tesselation" };
        List<String> SizeableIterativeDungeons = new List<String> { "cellular" };

        String algorithm = PlayerPrefs.GetString("Endpoint");
        int? seed = null;

        if (int.TryParse(SeedParameterUI.text, out int parsed_seed))
        {
            seed = parsed_seed;
        }

        if (SizeableDungeons.Contains(algorithm))
        {
            int height = getInputFieldValue(HeightParameterUI);
            int width = getInputFieldValue(WidthParameterUI);

            return new SizeableDungeonParameters(height, width, seed);
        }
        else if (IterativeDungeons.Contains(algorithm))
        {
            int iterations = getInputFieldValue(IterationsParameterUI);
            return new IterativeDungeonParameters(iterations, seed);
        }
        else
        {
            int height = getInputFieldValue(HeightParameterUI);
            int width = getInputFieldValue(WidthParameterUI);
            int iterations = getInputFieldValue(IterationsParameterUI);
            return new SizeableIterativeDungeonParameters(height, width, iterations, seed);
        }

    }





    private int getInputFieldValue(TMP_InputField inputField)
    {
        if (inputField.text != "")
        {
            return int.Parse(inputField.text);
        }
        throw new InvalidParametersException();
    }

}