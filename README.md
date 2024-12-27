# multimodal-gameplay
Multimodal prediction of intent, confusion, and mental workload during gameplay. Development of agents to respond and to cognitive states and assist wtih gameplay. Agents that can adpapt to different cognitive states will result in more effective interactions. Internal mental state can be reflected in both explicit and implcit behavoir. 

But really - let's just have some fun! Agents can increase task performance, but how can interactions during gameplay increase enjoyment, playfulness as well.

## Multimodal Data

__Data Sources:__ Tobii Eye tracking, facial video, voice recording. Long-term = OpenBCI EEG Headset

### Confusion
__Video and Facial Action Units__
- Brow lowering (AU4) and eyelid tightening (AU7) were correlated with confusion in [D'Mello...Greasser 2014]
- strong correlation of participants’ pitch angles of head pose and yaw angles of head pose respectively, in addition to their roll angles of head pose, with confusion or non-confusion [Na Li 2023]
- Facial Expression Recognition (FER) open-source framework [Na Li 2023]
- Detectable difference in head pose in window leading up to confusion [Hosp 2021]

__Gaze__
- Significant difference in 25 gaze featres between confused on confident driving [Haghzare 2022]. Entropy.
-  Participants’ ranges of eye gaze angles were less in confusion than in non-confusion situations [Na Li 2023]
-  During errors the amount of gaze towards the agent increases, while during confusion the amount towards the environment increases. We conclude that these signals could tell the agent what and when to explain.[Wachowiak 2022]
-  Detectable difference in gaze in window leading up to confusion [Hosp 2021]

__EEG__
- Bi-LSTM predicting confusion [Zhaoheng Ni 2017]
- Conventional and end-to-end machine learning [Tao Xu 2023]

### Cognitive Load/Frustration
__Video Facial Action Units__
- Inner and outer brow raising (AU1, AU2) were correlated with frustration. [D'Mello...Greasser 2014]

Ramakrishnan, B Balasingam, and F Biondi. 2021. Cognitive load estimation
for adaptive human–machine system automation. In Learning control. Elsevier,
35–58


### Intent
Research needed, focusing on eye gaze.

## Agents

### Puzzle/Shrine Agent
__Purpose:__ The puzzle/shrine agents retrieves and stores the steps to solve a shrine when you enter. At first, it will help you through the steps when asked. Eventually as we build out the system and train it, it will prompt the player when confusun or frustration is detected. The long-term goal is to learn about the player: how long they are okay with being confused before offering help, best timing of agent to offer help.

### Monster Agent
__Purpose:__ The monster agents will detect the monster or boss that the player is fighting, the retrieve strategies for defteating it. First, it will only offer help when asked. As we build out the system it will give suggestions if player suffers multiple hits or dies and attempts the boss again. 

### Play Agent
__Purpose:__ In the long-term, after the model is trained, there will be an agent whose purpose is to maximize fun. As players mental state is tracked, it will use that information to suggest next steps. It will even make jokes depending on player actions and choices depending on mood.

