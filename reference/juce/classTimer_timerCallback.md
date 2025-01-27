#### timerCallback()


 virtual void Timer::timerCallback ( ) pure virtual 
 

The userdefined callback routine that actually gets called periodically.It's perfectly ok to call startTimer() or stopTimer() from within this callback to change the subsequent intervals.Implemented in BubbleMessageComponent, ImagePreviewComponent, and MidiKeyboardComponent.