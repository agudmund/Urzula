using UnityEngine;

public class HowToPlay : MonoBehaviour {

    public GameObject CanvasPlane;
    GameObject cam;
    GameObject menu;
    Animator anim;

    private void Awake()
    {
        cam = GameObject.FindGameObjectWithTag("MainCamera");
        menu = GameObject.FindGameObjectWithTag("MainMenu");
        anim = cam.GetComponent<Animator>();
    }

    public void InitTutorial()
    {
        //menu.SetActive(false);
        anim.SetInteger("tutLevel",1);
    }
}
