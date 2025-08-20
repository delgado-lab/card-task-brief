## Description of Task Files for card-task-brief  

Contact Jamil Palacios Bhanji (bhanji@psychology.rutgers.edu) or Mauricio Delgado (delgado@psychology.rutgers.edu) for information about this project. This description was last edited on May 2, 2023.  

This folder contains files to run a card guessing game based on Delgado et al. (2000).
- this task was built in PsychoPy Builder v2022.2.5 and requires PsychoPy to run  
- instructions to **change the number of trials**:  
    1. add/delete rows (1 per trial) in *card-task-brief-trials.csv* (specify win=1, loss=0)  
    2. add/delete elements in the ISI and ITI lists - the total elements (for each trial type) should equal the number of trials for each type (see "alter ISI/ITIs section below) - these lists are in the "setupvars" code component (in the *Instruction* routine)  


### Files included    

*card-task-brief-money.psyexp* -  PsychoPy Builder File (open this file to edit & run the experiment)  

*images/* - images used in the task  

*design/card-task-brief-blocks.csv* - specifies list of blocks (this version has only 1 block)  

*design/card-task-brief-trials.csv* - specifies list of trials ("Win1Lose0" column specifies a win=1 or loss=0)  

*cardtask-behavior.Rmd* - R markdown file with code to parse output csv files and generate events.tsv timing files in BIDS format - *this code requires editing to specify input/output file paths - it has not been tested with this version of the task*
  

### Experimental Design  
- 2 conditions (Win +$1, Loss -$.50)   
- 10 trials per condition (20 total)  

### Timing Information  

Total task duration (from "trigger" event) 3min 40s (220s) (does not include instructions)

Event Timing (each trial)  
1. Input guess 2s ("?" screen)  
2. Inter-stimulus-interval (ISI/ITI1) 1, 3, 5s (50%,30%,20%)  
3. Outcome RewardPunishment (50%,50%), or "no response" on missed response trials  
4. Inter-trial interval (ITI2) 6,8s (50%,50%)  

#### To alter ISI/ITIs  
- edit the lists in the BeginExperiment tab of the "setupvars" code component (in the *Instruction* routine)  
    - "iti1rew_code1" list specifies the ISIs in win trials (1 per trial)  
    - "iti2rew_code1" list specifies the ITIs following win trials (1 per trial)  
    - "iti1pun_code1" list specifies the ISIs in loss trials (1 per trial)  
    - "iti2pun_code1" list specifies the ITIs following loss trials (1 per trial)  

### Other details

Trials are pre-specified as win or loss trials in the *design/card-task-brief-trials.csv* file. The trial order is randomized in the PsychoPy "innertrials" loop. Based on the participants response for each trial, a random low (1-3) or high number (6-9) is then displayed on the outcome screen to fit the pre-specified win/loss trial type.  

A separate PsychoPy builder file is included to run a block of practice trials (*practice-card-task-brief.psyexp*)  

Keyboard input information:  
- "1" or "b" for "lower" guess  
- "2" or "y" for "higher" guess  - if multiple key presses are made, the first press is used  
- Initial screens accept "1" or "b" to advance  
- "trigger" routine expects "t" to begin experiment  

Adjusting size and position of screen elements:
- size and position of elements are specified in "blockvars" code component in the "blockstart" routine.  

### How to interpret fields in output files:

- "firstTrialITI.started" stores clocktime of experiment start time (4s blank screen starts at this time)  

- "quest_rew.started" and "quest_pun.started" store onset times for the "?" card screen for win and loss trials, respectively. **Must subtract "firstTrialITI.started" value to get time elapsed since the trigger event.**    

- "response_rew.rt" and "response_pun.rt" store response time for each trial. empty if no response.  

- "feedback_rew.started" and "feedback_pun.started" store onset times for the outcome display screen in win and loss trials, respectively. **Must subtract "firstTrialITI.started" value to get time elapsed since the trigger event.**   

"Win1Lose0" stores trial condition (1=win, 0=loss)

### References

Delgado, M.R., Nystrom, L.E., Fissell, C., Noll, D.C., &amp; Fiez, J.A. (2000). Tracking the hemodynamic responses to reward and punishment in the striatum. Journal of Neurophysiology, 84(6) 3072-77. doi 10.1152jn.2000.84.6.3072
