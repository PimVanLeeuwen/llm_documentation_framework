#### launchThread()


 void ThreadWithProgressWindow::launchThread ( Priority priority = Priority::normal ) 
 

Starts the thread and returns.This will start the thread and make the dialog box appear in a modal state. When the thread finishes normally, or the cancel button is pressed, the window will be hidden and the threadComplete() method will be called.Parameters

 priority the priority to use when starting the thread see Thread::Priority for values