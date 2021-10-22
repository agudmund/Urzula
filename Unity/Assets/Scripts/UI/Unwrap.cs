using UnityEngine;

public class Unwrap : MonoBehaviour
{
    public GameObject placeholderAds;
    public GameObject pointer;

    public Texture[] soapAds;

    public void Clickings()
    {
        if(placeholderAds.active == true)
        {
            placeholderAds.SetActive(false);
        }
        else
        {
            placeholderAds.SetActive(true);
            placeholderAds.GetComponent<PlaceholderAd>().start = Time.time;
            placeholderAds.GetComponent<Renderer>().material.mainTexture = soapAds[Random.Range(0, soapAds.Length)];
        }
    }

    public void ShowPointer()
    {
        pointer.SetActive(true);
    }
}
