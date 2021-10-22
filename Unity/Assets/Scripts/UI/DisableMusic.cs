using UnityEngine;

public class DisableMusic : MonoBehaviour
{
    AudioCtrl audioctrl;
    //public SVGAsset[] icons;

    private void Awake()
    {
        audioctrl = GameObject.FindGameObjectWithTag("GameController").GetComponent<AudioCtrl>();
    }
    private void Start()
    {
        int active = PlayerPrefs.GetInt("music");
        if (active == 1)
        {
            //GetComponent<SVGRenderer>().vectorGraphics = icons[0];
        }
        //else GetComponent<SVGRenderer>().vectorGraphics = icons[1];
    }


    private void OnMouseDown()
    {
        if (audioctrl.music)
        {
            //GetComponent<SVGRenderer>().vectorGraphics = icons[1];
            audioctrl.music = false;
        }
        else
        {
            //GetComponent<SVGRenderer>().vectorGraphics = icons[0];
            audioctrl.music = true;
        }
        if (audioctrl.sound)
        {
            audioctrl.ToggleMusic();
        }
    }
}
