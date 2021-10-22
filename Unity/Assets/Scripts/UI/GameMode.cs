using UnityEngine;
using UnityEngine.UI;

public class GameMode : MonoBehaviour
{
    public void SetMode()
    {
        Dropdown drop = GetComponent<Dropdown>();
        PlayerPrefs.SetInt("gamemode", drop.value);
    }
}
