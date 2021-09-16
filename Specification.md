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

## Use Case Name: Share flashcards (add to their account)
## Summary
A user who is logged in will be able to share flashcards with other users.

## Actors
* The User.
* The App.

## Preconditions
* The user has to be logged in.

## Triggers
* The user must select the “Share Flashcards” option.

## Primary Sequence
* The System prompts the user to enter the username of the user they want to share their flashcards with.
* The System then shares the flashcards.

## Primary Postconditions
* The other user should have the shared flashcards.

## Alternative Sequences
* The user entered a username that is not associated with any other users.
* The System displays an error message.
* The System asks the user to enter a valid username.

## Use Case Name: Convert Markdown Notes to PDF
## Summary
A user who is logged in will be able to convert their markdown notes into a pdf file.

## Actors
* The User.
* The App.

## Preconditions
* The user has to be logged in.

## Triggers
* The user must select the “Convert Markdown Notes to PDF” option.

## Primary Sequence
* The System prompts the user to insert a name for their PDF file.
* The System then converts the notes into a PDF file.

## Primary Postconditions
* The System should display a download link for the file.

## Use Case Name: Share Notes with other people (add to their account)
## Summary
A user who is logged in will be able to share their notes with other users.

## Actors
* The User.
* The App.

## Preconditions
* The user has to be logged in.

## Triggers
* The user must select the “Share Notes” option.

## Primary Sequence
* The System prompts the user to enter the username of the user they want to share their notes with.
* The System then shares the notes.

## Primary Postconditions
* The other user should have the shared notes.

## Alternative Sequences
* The user entered a username that is not associated with any other users.
* The System displays an error message.
* The System asks the user to enter a valid username.

## Use Case Name: Total time studying (having app open) (daily/weekly/monthly)
## Summary
A user who is logged in will be able to see how long they have been using the app.

## Actors
* The User.
* The App.

## Preconditions
* The user has to be logged in.

## Triggers
* The user must select the “Total Time” option.

## Primary Sequence
* The System asks the user to select daily, weekly, or monthly.
    * Selecting daily will display a list of days that the user had the app open, as well as the average of how much time the user had the app open on a daily basis.
          * Selecting a day will display the total time the user had the app open on that day.
    * Selecting weekly will display a list of weeks that the user had the app open, as well as the average of how much time the user had the app open on a weekly basis.
          * Selecting a week will display the total time the user had the app open during that week.
    * Selecting monthly will display a list of months that the user had the app open, as well as the average of how much time the user had the app open on a monthly basis.
          * Selecting a month will display the total time the user had the app open during that month.

## Primary Postconditions
* The System should display the total time that they have had the app open.
* The System shows the option to hide the display.

