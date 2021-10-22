using UnityEngine;

public class AudioCtrl : MonoBehaviour
{
    public bool music,sound;
    AudioSource aSource,mMusic;
    public AudioClip menu,menuClick,newGame,pageFlip;
    GameObject cam;
    AudioListener listen;
    public float pitchIndex;

    /// <summary>
    /// Runtime Essentials
    /// </summary>

    private void Awake()
    {
        cam = GameObject.FindGameObjectWithTag("MainCamera");
        listen = cam.GetComponent<AudioListener>();
        music = RestoreMusicPrefs();
        sound = RestoreSoundPrefs();
        aSource = GetComponent<AudioSource>();

        pitchIndex = 1;
    }

    private void Start()
    {
        MenuMusic();
    }

    private void FixedUpdate()
    {
        Clean();
    }

    /// <summary>
    /// Controls
    /// </summary>
    public void Play(AudioClip current, float pitch = 1, float volume = 1)
    {
        if (sound)
        {
            if (aSource == null)
            {
                aSource = gameObject.AddComponent(typeof(AudioSource)) as AudioSource;
            }

            if (aSource.isPlaying)
            {
                aSource = gameObject.AddComponent(typeof(AudioSource)) as AudioSource;
            }
            aSource.clip = current;
            aSource.pitch = pitch;
            aSource.volume = volume;
            aSource.Play();

            AdjustPitch(pitch);
        }
    }
    void MenuMusic()
    {
        mMusic = gameObject.AddComponent(typeof(AudioSource)) as AudioSource;
        mMusic.clip = menu;
        mMusic.volume = .215f;
        mMusic.loop = true;
        if (music) mMusic.Play();
    }

    /// <summary>
    /// Toggles
    /// </summary>
    public void ToggleSound()
    {
        if (sound)
        {
            PlayerPrefs.SetInt("sound", 1);
            listen.enabled = true;
            if (music)
            {
                mMusic.Play();
            }
        }
        else
        {
            PlayerPrefs.SetInt("sound", 0);
            listen.enabled = false;
            AudioSource[] aSources = GetComponents<AudioSource>();
            foreach(AudioSource aSource in aSources)
            {
                aSource.Stop();
            }
        }
    }
    public void ToggleMusic()
    {
        if (music)
        {
            PlayerPrefs.SetInt("music", 1);
            mMusic.Play();
        }
        else
        {
            PlayerPrefs.SetInt("music", 0);
            mMusic.Stop();
        }
    }

    /// <summary>
    /// Preferences
    /// </summary>
    bool RestoreMusicPrefs()
    {
        bool active;
        active = PlayerPrefs.GetInt("music") == 1 ? true : false;
        return active;
    }
    bool RestoreSoundPrefs()
    {
        bool active;
        active = PlayerPrefs.GetInt("sound") == 1 ? true : false;
        // default to on while there is no menu button
        active = true;
        return active;
    }

    /// <summary>
    /// Utilites
    /// </summary>
    void AdjustPitch(float pitch)
    {
        if (pitch == pitchIndex)
        {
            pitchIndex = pitchIndex + .1f;
        }
        if (pitchIndex > 1.2)
        {
            pitchIndex = .8f;
        }
    }
    void Clean()
    {
        AudioSource[] aSources = GetComponents<AudioSource>();
        foreach(AudioSource a in aSources)
        {
            if (!a.isPlaying)
            {
                a.volume = 0;
                a.enabled = false;
                Destroy(a);
            }
        }
    }
}
