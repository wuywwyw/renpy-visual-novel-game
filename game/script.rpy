# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('Arya', color="#c8ffc8")
define d = Character('Daenerys', color="#c8c8ff")


# The game starts here.

label start:

    # Add background music
    
    play music "/audio/Stonekeepers ft. Christine Smit - New Dawn Is Rising.mp3"
    
    # Add background image of glade, with fade animation 
    scene glade
    with fade

    # Show a character (Arya), show narration
    show a
    a "Hi I'm Arya. I'm looking for my needle."

    # Show a on the left, and show d on the right, 
    # both with dissolve animation
    show a at left
    show d at right
    with dissolve
    
    # Display lines of dialogue.
    
    d "Do you know who am I?"
    
    a "..."
    
    d "I'm Daenerys of the House Targaryen, the First of Her Name, 
    The Unburnt, Queen of the Andals, the Rhoynar and the First Men, 
    Queen of Meereen, Khaleesi of the Great Grass Sea, 
    Protector of the Realm, Lady Regent of the Seven Kingdoms, 
    Breaker of Chains and Mother of Dragons."
    
    d "Wanna walk with me? I may give you some clue."

    a "..."
    
    a "Sure."

    scene castle
    with fade

    "After a short while, they reach the castle just at the end of the glade."

    "It's a scenic view Arya grown used to. Winter is especially beautiful here."

    show a at right

    "Daenerys turns to Arya. She looks tired."

    a "You seem like not sleep well, do you?"

    show d at left
    
    "Silence."
    
    a "I have done some research on sleep recently. Do you know 
    sleep is made up of a number of different stages?"
    
    "Daenerys started to show interests in what Arya has said."
    
    d "Tell me more about it."
    
    a "These stages are characterized by different patterns of EEG activity. 
    Before sleep, the EEG pattern is mostly BETA WAVES when you are awake
    and ALPHA WAVES during times of quiet relaxation. "
    
    a " Stage 1 of sleep is a general state of drowsiness that is defined by 
    the presence of Theta Waves in the EEG pattern. Theta Waves are quite fast 
    and erratic waves that are just a little slower than the waves shown during times of relaxation. 
    People that are woken during Stage 1 of sleep often will claim that 
    they were not actually asleep!"
    
    d "Emm...Sounds interesting."
    
    a "Stage 2 of sleep is characterized by slower and longer waves 
    accompanied by sleep spindles- short bursts of fast activity."
    
    a "Stage 3 has waves that are even slower and larger- known as DELTA WAVES. 
    
    a "During the fourth stage of sleep, the body’s metabolism is at its slowest 
    and the EEG pattern is almost exclusively made up of DELTA waves."
    
    a "When you sleep, you move quickly from stage 1 to stage 2, then to stage 3 
    and finally to stage 4. You spend about 30 minutes in stage 4 sleep 
    and then go back through the stages backwards. 
    To stage 3 then 2 then 1, and then something really weird happens."
    
    d "What happens then?"
    
    a "Suddenly the EEG waves become fast and desynchronized. 
    While you are still completely asleep, then pattern is very similar to that when you are awake.
    This is the deepest stage of sleep and is named after the fast eye movements 
    that people experience as it happens. These are known as RAPID EYE MOVEMENTS or REM. 
    This stage of sleep is called REM sleep or Paradoxical sleep. Because the person is asleep 
    yet the brain is clearly aroused. REM sleep is also accompanied by an increased heart rate, 
    and also by muscle relaxation and complete body paralysis. It seems that REM sleep is 
    most associated with dreaming. When people are woken during REM sleep about 70%
    report that they had been dreaming, compared to only 30% of those woken up during stages 3 and 4."
    
    d "I often wake during REM sleep..."
    
    a "That's not good though. During REM sleep, activity in other areas of the brain can 
    also be recorded as being active. These are PGO (pons geniculo occipital) spikes 
    that show that the visual centres of the brain are also active. This visual brain activity 
    appears to be related to the eye movements seen during REM sleep and to the visual aspects 
    of the dream itself. In fact, the full body paralysis that accompanies REM sleep is necessary 
    to prevent people acting out their dreams. Although some people do when they sleep walk. "
    
    a "You spend about 15minutes in REM sleep and then you begin the sleep cycle again by 
    going into stage 1, then stage 2 and so on."
    
    a "Now do you have some clue for my needle? "
    
    
label leaving:


    d "..."

    d "Can we leave this place first?""

menu:

    "Yes":
        jump leave

    "no":
        jump stay

label leave:

    d "Let's go into the castle."

    jump marry

label stay:

    d "Really? Do you want to hear more about biological science?"

    jump marry

label marry:

    "And so, they will build a visual novel biological science empire."
    
    # This ends the game.

    return
