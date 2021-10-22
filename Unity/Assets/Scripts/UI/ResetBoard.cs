using UnityEngine;

public class ResetBoard : MonoBehaviour {

    GameController ctrl;
    AudioCtrl actrl;

    private void Awake()
    {
        ctrl = GameObject.FindGameObjectWithTag("GameController").GetComponent<GameController>();
        actrl = GameObject.FindGameObjectWithTag("AudioCtrl").GetComponent<AudioCtrl>();
    }

    private void OnMouseDown()
    {
        actrl.Play(actrl.menuClick, actrl.pitchIndex);
    }
}
