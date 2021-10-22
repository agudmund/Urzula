using UnityEngine;

public class PlaceholderAd : MonoBehaviour
{
    public float start;
    GameController ctrl;

    private void Awake()
    {
        ctrl = GameObject.FindGameObjectWithTag("GameController").GetComponent<GameController>();
    }

    void FixedUpdate()
    {
        if (Time.time - start > 2)
        {
            gameObject.SetActive(false);
        }
    }
}
