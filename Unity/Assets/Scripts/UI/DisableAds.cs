using UnityEngine;

public class DisableAds : MonoBehaviour
{
    public GameObject placeholderAds;
    public GameObject placeholderBanner;
    public Texture[] soapAds;
    //public SVGAsset[] icons;
    bool disabled;

    public void OnMouseDown()
    {
        if (!disabled)
        {
            placeholderAds.SetActive(true);
            placeholderAds.GetComponent<PlaceholderAd>().start = Time.time;
            placeholderAds.GetComponent<Renderer>().material.mainTexture = soapAds[Random.Range(0, soapAds.Length)];
            placeholderBanner.SetActive(false);
            //GetComponent<SVGRenderer>().vectorGraphics = icons[0];
        }
    }

    public void LinkToAppStore()
    {
        Application.OpenURL("itms-apps:itunes.apple.com/app/tenoki/id123456789");
    }
}
