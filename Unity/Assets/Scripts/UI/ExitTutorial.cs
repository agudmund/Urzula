using UnityEngine;

public class ExitTutorial : MonoBehaviour {

    GameObject cam,menu,hand;
    Animator anim,handAnim;

    private void Awake()
    {
        cam = GameObject.FindGameObjectWithTag("MainCamera");
        menu = GameObject.FindGameObjectWithTag("MainMenu");
        //hand = GameObject.FindGameObjectWithTag("TutorialHand");

        //handAnim = hand.GetComponent<Animator>();
        anim = cam.GetComponent<Animator>();
    }

    public void OnMouseDown()
    {
        //menu.SetActive(true);
        anim.SetInteger("tutLevel", 0);
        //handAnim.SetInteger("TutLevel", 0);
    }
}
