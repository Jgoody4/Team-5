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

## Use Case Name: Shuffle Flashcards (Memorization)
* Non-functional requirement : System will respond to user input within 1 second. 
### Summary
* A user who is logged in will be able to shuffle their flashcards into a new order, different from the previous order.

### Actors
* The User.  
* The App.

### Preconditions
* The user has to be logged in.

### Triggers
* The user must select the “Shuffle” option.

### Primary Sequence
* The System shows a loading message that says “Shuffling…”
* The System shuffles the flashcards.

### Primary Postconditions
* The flashcards should be shuffled.
*	The flashcards are displayed in a new order.

### Alternate Postconditions
* The flashcard order does not change because there is only one card.

## Use Case Name: Use Pomodoro Timer (Time Management)
### Summary
* A user who is logged in will be able to set up a Pomodoro Timer, that is, a timer that tracks study time and break time.

### Actors
* The User.
* The App.

### Preconditions
* The user has to be logged in.

### Triggers
* The user must select the “Timer” option.

### Primary Sequence
* The System prompts the user to enter a time (in minutes) for dedication to study.
    * If the user enters an invalid time (negative/zero time or other symbols that aren’t numbers), System prompts the user to enter a valid time (a strictly positive integer) and clears the user’s input.
* The System prompts the user to enter a time (in minutes) for break time.
    * Same as (1a)

### Primary Postconditions
* The System should display a timer that starts counting down from the time the user specified for studying.
* When the timer counts down to zero, the System should play a sound, then display a timer that starts counting down from the time the user specified for breaks.
* Repeat these two steps until the user logs off or stops the timer.

## Use Case Name: Render Markdown Notes (Notetaking)
### Summary
* A user who is logged in will be able to format their notes using Markdown syntax.

### Actors
* The User.
* The App.

### Preconditions
* The user has to be logged in.

### Triggers
* The user must select the “Create Notes” option.

### Primary Sequence
* The user should begin typing notes into the app.
* If desired, the user may enclose some or all text in special characters to format their text.

### Primary Postconditions
* The System should display the text (formatted if desired) automatically.

## Use Case Name: Organize Notes into Folders (Notetaking)
### Summary
* A user who is logged in will be able to create folders for their notes and add notes into these folders. Folders may also be edited or deleted.

### Actors
* The User.
* The App.

### Preconditions
* The user has to be logged in.

### Triggers
* The user must select the “Notes” option.

### Primary Sequence
* The user should be asked to name the folder they want to create.
* The user presses “Done” when finished coming up with a name.
* The System creates a folder for notes with the given name.
    * If desired, the user may “Edit” the name of the folder.
    * The user may also “Delete” the folder, along with its contents.
    * Folders may be nested within one another.

### Primary Postconditions
* The System should display that a folder has been created with the user-inputted name.

## Use Case Name: Share flashcards (Memorizing)
### Summary
* A user who is logged in will be able to share flashcards with other users.

### Actors
* The User.
* The App.

### Preconditions
* The user has to be logged in.

### Triggers
* The user must select the “Share Flashcards” option.

### Primary Sequence
* The System prompts the user to enter the username of the user they want to share their flashcards with.
* The System then shares the flashcards.

### Primary Postconditions
* The other user should have the shared flashcards.

### Alternative Sequences
* The user entered a username that is not associated with any other users.
* The System displays an error message.
* The System asks the user to enter a valid username.

## Use Case Name: Convert Markdown Notes to PDF (Notetaking)
### Summary
* A user who is logged in will be able to convert their markdown notes into a pdf file.

### Actors
* The User.
* The App.

### Preconditions
* The user has to be logged in.

### Triggers
* The user must select the “Convert Markdown Notes to PDF” option.

### Primary Sequence
* The System prompts the user to insert a name for their PDF file.
* The System then converts the notes into a PDF file.

### Primary Postconditions
* The System should display a download link for the file.

## Use Case Name: Share Notes with other people (Notetaking)
### Summary
* A user who is logged in will be able to share their notes with other users.

### Actors
* The User.
* The App.

### Preconditions
* The user has to be logged in.

### Triggers
* The user must select the “Share Notes” option.

### Primary Sequence
* The System prompts the user to enter the username of the user they want to share their notes with.
* The System then shares the notes.

### Primary Postconditions
* The other user should have the shared notes.

### Alternative Sequences
* The user entered a username that is not associated with any other users.
* The System displays an error message.
* The System asks the user to enter a valid username.

## Use Case Name: Total Time Studying (having app open) (daily/weekly/monthly) (Time Management)
### Summary
* A user who is logged in will be able to see how long they have been using the app.

### Actors
* The User.
* The App.

### Preconditions
* The user has to be logged in.

### Triggers
* The user must select the “Total Time” option.

### Primary Sequence
* The System asks the user to select daily, weekly, or monthly.
    * Selecting daily will display a list of days that the user had the app open, as well as the average of how much time the user had the app open on a daily basis.
          * Selecting a day will display the total time the user had the app open on that day.
    * Selecting weekly will display a list of weeks that the user had the app open, as well as the average of how much time the user had the app open on a weekly basis.
          * Selecting a week will display the total time the user had the app open during that week.
    * Selecting monthly will display a list of months that the user had the app open, as well as the average of how much time the user had the app open on a monthly basis.
          * Selecting a month will display the total time the user had the app open during that month.

### Primary Postconditions
* The System should display the total time that they have had the app open.
* The System shows the option to hide the display.
D
## Use Case Name : Overhead view of all Flashcards (Memorizing)
### Summary 
* A user who is logged in will be able to take his flashcards and display an overhead view of them all.

### Actors
* The user 
* The app

### Pre conditions 
* A user must be logged in

### Triggers
* Must select the “memorizing” option. Then select “overhead view”.

### Primary Sequence
* The flashcards will start changing view to an overhead and user will be able to see all flashcards
The user will be able to click cards away.

### Primary Postconditions 
* If the user clicks “done” then the overhead view of cards will go back into a shuffled order or regular memorization. 

## Use Case Name : Percentage system / Analytic tool for right and wrong answers recorded. (Memorizing)
### Summary
* A user who is logged in and in the “memorizing” part of the app will be able to see their results after all the flashcards have been flipped and studied.

### Actors 
* The user 
* The app

### Preconditions 
* A user must be logged in 

### Triggers
* User must click on “memorize” and by default when the user starts flipping cards and memorizing the analytic tool will mark cards right or wrong and use basic math.

### Primary Sequence 
* The user will use the memorizing feature like normal and at the end of the flashcards he/she will get a percentage of right and wrong answers.
* The user will be asked to study the wrong answers or they can start with shuffled cards again.

### Primary post conditions
* If user clicks to study wrong answers then the cards will only show the wrong answers they got. 
* If user doesn’t want to study wrong answers then memorizing feature goes back to normal and repeats the analytic tool for the next iteration of memorizing. 

## Use Case Name : Syntax Highlighting (Notetaking)
### Summary
* The user will be able to format parts of their notes as code, as if they were writing in an IDE.

### Actors
* The user 
* The app

### Preconditions
* The user must be logged in, and viewing notes with the “notes” feature.

### Triggers
* The user must encase the text they wish to view as code with three backticks once at the beginning of the segment.

### Primary Sequence 
* The user types three backticks, a multi-line code block should appear.
* The user will be able to select a language of choice in the top-left corner of this block by hovering over it with the mouse.
* Code will automatically highlight key words typed.

### Primary post conditions
* User will be able to format code within the notes.

## Use Case Name: Create time blocks (Time Management)
### Summary
* The user sets a certain range of time that schedules their study time.

### Actors
* The App.
* The User.

### Preconditions
* The user has logged in.

### Triggers
* The user must select the “Add Time Blocks” option.

### Primary Sequence
* The System will prompt the user to enter a time from and a time to (positive integers only).
* The System prompts the user to enter what the time block is for by entering the description.
* The User presses “enter” to create the time block.
* The System then creates a time block specified by the user’s input.

### Primary Postconditions
* The time block made should be shown. 
* The time block should be able to be dismissed automatically. 

### Alternate Postconditions
* The time block should be able to be dismissed manually if the user wants to.

## Use Case Name: Reminder popup (Time Management)
### Summary
* The app reminds the user to study with a popup notification based on the time block they have created.

### Actors
* The App.

### Preconditions
* The user has created time blocks.

### Triggers
* The user must turn on notifications in the app.

### Primary Sequence
* The System displays the message “Reminders On” once notification is turned on.
* The System will take note of the time blocks created to know when to show a reminder.

### Primary Postconditions
* A reminder popup should be shown.
* The system shows an option to clear reminder(s).

### Alternate Postconditions
* The reminder does not show if the time block is dismissed.

## Use Case Name: Input a Markdown File and Output Flash Cards. (Memorizing)
### Summary
* Generate flash cards based on the user’s inputs.

### Actors
* The App.
* The User.

### Preconditions
* The user has logged in.

### Triggers
* The user must select the add button to input a markdown file.

### Primary Sequence
* The System prompts the user to input notes to memorize.
* The User presses “done” when finished inputting.
* The System then creates flash cards based on the inputs.

### Primary Postconditions
* The flash cards are made and shown to the user.

### Alternate Postconditions
* The user has inputted an empty file.
    * The System will display a message “Error: empty inputs. Cannot output flash cards”
    * The System will prompt the user to input notes again. 

## Use Case Name: A Timer (Time Management)
### Summary
* A user who is logged in will be able to start and end a working timer.

### Actors
* The User.
* The App.

### Preconditions
* The user has to be logged in.

### Triggers
* The user can select the “Set Timer” option.

### Primary Sequence
* The System will let the user enter a specific amount of time in the format of 00:00:00.
* The System also displays a pause and quit option.

## Primary Postconditions
* If the user selects the pause option, the timer will stop.
* If the user selects the quit option, the timer will be set back to 00:00:00, and will not change until the user selects the Set Timer option.
* If the timer finishes, the System will display a message, stating “Timer is Done.”
* The user will be able to close the message, and the timer will remain at 00:00:00 until the user selects the Set Timer option.

### Alternative Sequences
* The user entered something that was not in the format of 00:00:00.
* The System will display an error message.
* The System will ask the user to enter an amount of time in the correct format.
