using UnityEngine;

public class NewGame : MonoBehaviour {

    GameController ctrl;
    AudioCtrl actrl;

    void Awake()
    {
        ctrl = GameObject.FindGameObjectWithTag("GameController").GetComponent<GameController>();
        actrl = ctrl.GetComponent<AudioCtrl>();
    }

    public void ClickIt()
    {
        ctrl.Reset();
        actrl.Play(actrl.newGame,1);
    }


}
