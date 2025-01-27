#### runThread()


 bool ThreadWithProgressWindow::runThread ( Priority priority = Priority::normal ) 
 

Starts the thread and waits for it to finish.This will start the thread, make the dialog box appear, and wait until either the thread finishes normally, or until the cancel button is pressed.Before returning, the dialog box will be hidden.Parameters

 priority the priority to use when starting the thread see Thread::Priority for values 
 



Returnstrue if the thread finished normally; false if the user pressed cancel