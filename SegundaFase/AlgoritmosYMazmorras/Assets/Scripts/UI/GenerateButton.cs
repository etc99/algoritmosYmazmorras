using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
public class GenerateButton : MonoBehaviour
{

    [SerializeField]
    public GameObject parameterPanel;
    [SerializeField]
    public TMP_InputField heightInput;
    [SerializeField]
    public TMP_InputField seedInput;
    [SerializeField]
    public TMP_InputField widthInput;
    [SerializeField]
    public TMP_InputField iterationsInput;

    [SerializeField]
    public TMP_Text errorText;

    // Start is called before the first frame update
    void Start()
    {
        // En función de el algoritmo seleccionado habilitar/deshabilitar botones
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void CreateDungeon()
    {
        Debug.Log("Pulsado generar!");
        int height, width, iterations, seed;
        height = parseParams(heightInput);
        width = parseParams(widthInput);
        seed = parseParams(seedInput);
        iterations = parseParams(iterationsInput);


    }

    private int parseParams(TMP_InputField TMP_InputField)
    {
        int result;
        if (int.TryParse(TMP_InputField.text, out result))
        {
            return result;
        }
        else
        {
            return -1;
        }
    }
}
