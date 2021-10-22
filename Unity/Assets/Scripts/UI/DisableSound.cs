using UnityEngine;

public class DisableSound : MonoBehaviour {

    AudioCtrl audioctrl;
    //public SVGAsset[] icons;

    private void Awake()
    {
        audioctrl = GameObject.FindGameObjectWithTag("GameController").GetComponent<AudioCtrl>();        
    }

    private void Start()
    {
        int active = PlayerPrefs.GetInt("sound");
        if (active == 1)
        {
            //GetComponent<SVGRenderer>().vectorGraphics = icons[0];
        }
        //else GetComponent<SVGRenderer>().vectorGraphics = icons[1];
    }

    private void OnMouseDown()
    {
        if (audioctrl.sound)
        {
            //GetComponent<SVGRenderer>().vectorGraphics = icons[1];
            audioctrl.sound = false;
        }
        else
        {
            //GetComponent<SVGRenderer>().vectorGraphics = icons[0];
            audioctrl.sound = true;
        }
        audioctrl.ToggleSound();
    }
}
