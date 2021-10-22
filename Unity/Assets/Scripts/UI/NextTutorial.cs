using System.Collections;
using UnityEngine;

public class NextTutorial : MonoBehaviour {

    GameObject cam, hand;
    Animator anim,handAnim;
    AudioCtrl actrl;
    public int nextIndex;

    private void Awake()
    {
        cam = GameObject.FindGameObjectWithTag("MainCamera");
        actrl = GameObject.FindGameObjectWithTag("AudioCtrl").GetComponent<AudioCtrl>();
        hand = GameObject.FindGameObjectWithTag("TutorialHand");

        anim = cam.GetComponent<Animator>();
        handAnim = hand.GetComponent<Animator>();
    }

    public void OnMouseDown()
    {
        handAnim.SetInteger("TutLevel", nextIndex-1);
        StartCoroutine(NextPage());
    }

    IEnumerator NextPage()
    {
        yield return new WaitForSeconds(3);
        anim.SetInteger("tutLevel", nextIndex);
        handAnim.SetInteger("Transition", nextIndex);
        actrl.Play(actrl.pageFlip, 1, .2f);
    }
}
