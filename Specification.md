# REARRANGE THIS INTO GROUPS LATER

# Specifications

URL to Team 5 github repository :
 https://github.com/Jgoody4/Team-5.git

**Team 5 Members** :  
Justin Goodman (@Jgoody4)  
Sam Low (@qsaml)  
Yinglin (@yitan02)  
Joel Zapana (@jazapana) 

**Product name** :
Better Student

# Use Cases :

## Use Case Name: Shuffle Flashcards
Non-functional requirement : System will respond to user input within 1 second. 
## Summary
A user who is logged in will be able to shuffle their flashcards into a new order, different from the previous order.

## Actors
* The User.  
* The App.

## Preconditions
* The user has to be logged in.

## Triggers
* The user must select the “Shuffle” option.

## Primary Sequence
* The System shows a loading message that says “Shuffling…”
* The System shuffles the flashcards.

## Primary Postconditions
* The flashcards should be shuffled.
*	The flashcards are displayed in a new order.

## Alternate Postconditions
* The flashcard order does not change because there is only one card.

## Use Case Name: Use Pomodoro Timer
## Summary
A user who is logged in will be able to set up a Pomodoro Timer, that is, a timer that tracks study time and break time.

## Actors
* The User.
* The App.

## Preconditions
* The user has to be logged in.

## Triggers
* The user must select the “Timer” option.

## Primary Sequence
* The System prompts the user to enter a time (in minutes) for dedication to study.
    * If the user enters an invalid time (negative/zero time or other symbols that aren’t numbers), System prompts the user to enter a valid time (a strictly positive integer) and clears the user’s input.
* The System prompts the user to enter a time (in minutes) for break time.
    * Same as (1a)

## Primary Postconditions
* The System should display a timer that starts counting down from the time the user specified for studying.
* When the timer counts down to zero, the System should play a sound, then display a timer that starts counting down from the time the user specified for breaks.
* Repeat these two steps until the user logs off or stops the timer.

## Use Case Name: Render Markdown Notes
## Summary
A user who is logged in will be able to format their notes using Markdown syntax.

## Actors
* The User.
* The App.

## Preconditions
* The user has to be logged in.

## Triggers
* The user must select the “Create Notes” option.

## Primary Sequence
* The user should begin typing notes into the app.
* If desired, the user may enclose some or all text in special characters to format their text.

## Primary Postconditions
* The System should display the text (formatted if desired) automatically.

## Use Case Name: Organize Notes into Folders
## Summary
A user who is logged in will be able to create folders for their notes and add notes into these folders. Folders may also be edited or deleted.

## Actors
* The User.
* The App.

## Preconditions
* The user has to be logged in.

## Triggers
* The user must select the “Notes” option.

## Primary Sequence
* The user should be asked to name the folder they want to create.
* The user presses “Done” when finished coming up with a name.
* The System creates a folder for notes with the given name.
    * If desired, the user may “Edit” the name of the folder.
    * The user may also “Delete” the folder, along with its contents.
    * Folders may be nested within one another.

## Primary Postconditions
* The System should display that a folder has been created with the user-inputted name.
