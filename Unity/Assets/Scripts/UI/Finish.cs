using UnityEngine;
using UnityEngine.UI;

public class Finish : MonoBehaviour
{
    GameController ctrl;
    GameObject mainmenu;

    private void Update()
    {
        Button button = GetComponent<Button>();
        Canvas ren = GetComponent<Canvas>();
    }

    private void Awake()
    {
        ctrl = GameObject.FindGameObjectWithTag("GameController").GetComponent<GameController>();
        mainmenu = GameObject.FindGameObjectWithTag("MainMenu");
    }

    public void FinishGame()
    {
        mainmenu.SetActive(true);
    }
}
