    // 퀘스트 매니저 인스턴스
    private static Traning1GameManager _instance;


    //대화창 만들기
    public Traning1QuestManager questManager;       //수정
    public GameObject TalkNPCName;
    public GameObject TalkText;
    public GameObject TalkPanel;
    public GameObject selectPanel;
    public GameObject firstSelectionText;
    public GameObject secondSelectionText;

    //퀴즈패널 오브젝트
    public GameObject quizContent;
    public GameObject quizPanael;
    public GameObject quizSelectPanel;


    // 퀴즈 해설 - 퀴즈때와 panel이 달라야 할거같아!
    public GameObject answerContent;
    public GameObject answerPanel;

    [SerializeField]
    private GameObject pressSpaceButton;
    public Traning1TalkManager talkManager;     //수정
    private GameObject scanObject;



    // 퀘스트 별 대화 진행 상황
    public int talkIndex;

    // 선택지 답안.
    public int answerIndex;
    // 다음 번에 대화 창을 닫을지 결정.
    public bool closeNextTalk;
    // 3번일때, 이동할 talkindex (talkChange)
    private int talkChange;


    // 첫번째 버튼을 선택했을 경우.
    public bool selectFirstBtn;
    // 두번째 버튼을 선택했을 경우.
    public bool selectSecondBtn;

    //퀴즈 패널 컨트롤
    // 퀴즈 첫번째 버튼 선택
    public bool quizFirstBtn;
    // 퀴즈 두번째 버튼 선택
    public bool quizSecondBtn;


    // 퀴즈 대화가 진행중인지?
    private bool isQuizProcessing;

    // 일반 대화
    // 대화창 열기 혹은 닫기
    public bool isAction;
    // 대화 선택창 열기 혹은 닫기
    public bool isSelectAction;
    // 버튼 선택중인 상황을 나타냄(선택중  true, 아님 false)
    public bool isSelecting;

    //퀴즈 시작 여부
    //IsAction과 같은 역할(패널을 켜줌)
    public bool quizAction;
    //IsSelectAction과 같은 역할(버튼 화면을 켜줌)
    public bool quizSelectAction;
    //IsSelecting과 같은 역할(선택여부를 판단)
    public bool quizSelecting;

    // 퀴즈 해설
    // isAction과 같은 역할(패널을 켜줌)
    public bool answerAction;



    private void Awake()
    {
        if (_instance == null)
        {
            _instance = this;
        }
        else if (_instance != this)
        {
            Destroy(gameObject);
        }


        // 초기화
        initQuizSelection();
        initPanels();
        initSelections();
        isQuizProcessing = false;
        closeNextTalk = false;
        answerIndex = 0;
        isSelecting = false;
        //퀴즈 패널
        quizSelecting = false;
    }
    void Start()
    {
        //scene1QuestManager = Scene1QuestManager.getScene1QeustManager();
        questManager = Traning1QuestManager.getTraning1QeustManager();      //수정
        talkManager = Traning1TalkManager.getTraning1TalkManager();     //수정
        pressSpaceButton.SetActive(false);

        //replaceTextObject.SetActive(false);
        talkIndex = 0;

    }

    public static Traning1GameManager GetTraning1GameManager()      //수정
    {
        if (_instance == null)
        {
            return null;
        }
        return _instance;
    }

    public void Action(GameObject scanObj)
    {
        scanObject = scanObj;
        ObjectData objData = scanObject.GetComponent<ObjectData>();
        Talk(objData.id, objData.isNpc, scanObject.name);

        // 일반 대화 패널
        TalkPanel.SetActive(isAction);
        selectPanel.SetActive(isSelectAction);

        //Quiz패널
        quizPanael.SetActive(quizAction);
        quizSelectPanel.SetActive(quizSelectAction);

        // 퀴즈 해설 패널
        answerPanel.SetActive(answerAction);

    }


    void Talk(int id, bool isNpc, string objName)
    {
        //Debug.Log(closeNextTalk);

        // 다음번에 닫힘?
        if (closeNextTalk)
        {
            // 퀴즈 대화일 경우.(퀴즈에서 틀린경우)
            if (isQuizProcessing)
            {
                talkIndex = talkChange;
                closeNextTalk = false;
            }
            // 일반 대화일 경우.(올바른 대답을 하지 않은 경우)
            else
            {
                talkIndex = talkChange;
                initPanels();
                closeNextTalk = false;
                return;
            }
        }

        // 선택지를 고른 경우.
        if (isSelecting && (selectFirstBtn == true || selectSecondBtn == true))
        {
            // 올바른 답을 선택한 경우.
            if (answerIndex == 1 && selectFirstBtn || answerIndex == 2 && selectSecondBtn)
            {
                talkIndex++;
            }
            isSelecting = false;
        }
        //퀴즈 로직 - 선택지를 고른 경우.
        if (quizSelecting && (quizFirstBtn == true || quizSecondBtn == true))
        {
            // 정답을 맞춘 경우.
            if (answerIndex == 6 && quizFirstBtn || answerIndex == 7 && quizSecondBtn)
            {
                talkIndex++;
            }
            quizSelecting = false;
        }
        // 안고르고 대화 넘기려는 경우.
        if (quizSelecting)
        {
            return;
        }
        if (isSelecting)
        {
            return;
        }
        
        // 대화 데이터 가져와ㅏㅏㅏ
        int questTalkIndex = questManager.GetQuestTalkIndex(id);
        string recTalkData = talkManager.GetTalk(id + questTalkIndex, talkIndex);

        // 대화 없어? - 퀘스트 끝남 혹은 대사가 없는 친구임!
        if (recTalkData == null)
        {
            // 창 다 닫아!!!
            initPanels();
            talkIndex = 0;
            string nextQuestName = questManager.CheckQuest(id);
            if (nextQuestName == "퀘스트 완료!")
            {
                // 퀘스트를 모두 마쳤으니 씬을 넘어가자!
                SceneManager.LoadScene(1);
            }
            return;
        }
        string[] talkDataArr = recTalkData.Split(":");
        // 대화 데이터!
        string talkData = talkDataArr[0];
        // 대화 유형
        int order = Int32.Parse(talkDataArr[1]);

        if(order == 0)
        {
            isQuizProcessing = false;
            isAction = true;
        }

        // 일반 선택 부분에서 답이 틀림!
        if (order == 3)
        {
            closeNextTalk = true;

            // '선택중' 상태를 false로 두자!
            isSelecting = false;
            quizSelecting = false;
            // 몇번 talk로 이동할 거야?
            talkChange = Int32.Parse(talkDataArr[2]);
            //퀴즈 패널 비활성화

            // 일반 대화 창 열어!! 왜냐 이번 대화까지는 보여주고 창을 닫아야 하기 때문이지!
            isAction = true;
        }
        // 일반 선택 시작이야
        if (order == 1 || order == 2)
        {
            // 선택지에 text를 바꿔주자!
            firstSelectionText.GetComponent<TextMeshProUGUI>().text = talkDataArr[2];
            secondSelectionText.GetComponent<TextMeshProUGUI>().text = talkDataArr[3];
            // 선택 bool value 초기화 해주자!
            initSelections();
            //용도가 무엇? - 질문의 답이 무엇인지 저장해두자!
            answerIndex = order;
            //일반 선택 활성화
            isSelecting = true;
            isSelectAction = true;
            isAction = true;
            // 퀴즈 진행중 아님 = =
            isQuizProcessing = false;
        }
        if (order == 4)
        {
            //비디오 넣기
            if(talkDataArr[2] == "watchTraining1Video")
            {

            }

        }
        if (order == 5)
        {
            answerContent.GetComponent<TextMeshProUGUI>().text = talkData;
            // 퀴즈 답변
            answerAction = true;
            isQuizProcessing = true;
        }
        if (order == 6 || order == 7)
        {
            isQuizProcessing = true;
            // 선택 bool value 초기화!
            initQuizSelection();
            // 정답을 미리 저장해주자!
            answerIndex = order;

            quizAction = true;
            quizSelecting = true;
            quizSelectAction = true;
        }

        if (order == 8)
        {
            closeNextTalk = true;
            isSelecting = false;
            selectFirstBtn = false;
            selectSecondBtn = false;
            isSelectAction = false;

            //퀴즈 패널 비활성화
            quizSelecting = false;
            quizAction = false;
            quizSelectAction = false;
        }
        if (isAction)
        {
            TalkText.GetComponent<TextMeshProUGUI>().text = talkData;
            TalkNPCName.GetComponent<TextMeshProUGUI>().text = objName;
        }
        if (quizAction)
        {
            // 퀴즈 정보 넣자!
            quizContent.GetComponent<TextMeshProUGUI>().text = talkDataArr[0];
        }
        

        
        talkIndex++;
    }

    public void initSelections()
    {
        selectFirstBtn = false;
        selectSecondBtn = false;
    }

    public void initQuizSelection()
    {
        quizFirstBtn = false;
        quizSecondBtn = false;
    }

    public void initPanels()
    {
        isAction = false;
        isSelectAction = false;
        quizAction = false;
        quizSelectAction = false;
        answerAction = false;
    }


    public void setFirstValue()
    {
        selectSecondBtn = false;
        selectFirstBtn = true;
        Action(scanObject);
    }
    public void setSecoundValue()
    {
        selectFirstBtn = false;
        selectSecondBtn = true;
        Action(scanObject);
    }

    public void setQuizFirstValue()
    {
        quizFirstBtn = true;
        quizSecondBtn = false;
        Action(scanObject);
    }

    public void setQuizSecondValue()
    {
        quizFirstBtn = false;
        quizSecondBtn = true;
        Action(scanObject);
    }


}



        talkData.Add(1000000, new string[]
        {
            "안녕하세요?<color=red>강아지 모의 산책 체험</color>에 오신걸 환영합니다.:0",
            "퀴즈는 총 3문제로 <color=red>2문제이상</color> 정답을 맞출시 통과입니다." + System.Environment.NewLine +"통과하지 못하신 경우, 짧은 동영상 시청을 통해 완료하실 수 있습니다.:0",
            "퀴즈를 진행하시겠습니까?:1:예:아니요",
            "마음의 준비가 되시면 다시 말을 걸어주세요:3:0",
            // 정답을 맞췄는지 각각 0,1,2 인덱스에 저장.
            "Q1. 강아지가 짖을 때 보호자는 큰 소리로 혼을 내 짖는 것을 멈추게 한다.:7",
            "다시한번 생각해보세요:3:4",
            "잘하셨습니다. 강아지가 짖을 때 큰소리로 혼을 내는 경우, 강아지 입장에서는 자신을 칭찬해주고 있다고 생각할 수 있습니다.:5",
            "Q2. 강이지가 짖을 때 보호자는 목줄을 쎄게 잡아당겨 제지한다.:7",
            "다시한번 생각해보세요:3:7",
            "잘하셨습니다. 강아지가 짖을 때 큰소리로 혼을 내는 경우, 강아지 입장에서는 자신을 칭찬해주고 있다고 생각할 수 있습니다.:5",
            "Q3. 강아지가 짖을 때 보호자는 강아지가 짖고 있는 타겟을 외면한다.:6",
            "다시한번 생각해보세요:3:10",
            "잘하셨습니다. 강아지가 짖을 때 큰소리로 혼을 내는 경우, 강아지 입장에서는 자신을 칭찬해주고 있다고 생각할 수 있습니다.:5",
            "동영상을 시청하시겠습니까?:1:예:아니요",
            "동영상을 시청하고싶으시다면 다시 말을 걸어주세요:3:13",
            ":4:watchTraining1Video",
            "축하합니다. 강아지 모의 산책 체험을 완료하셨습니다.:0"
        });