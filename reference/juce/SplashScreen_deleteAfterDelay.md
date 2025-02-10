#### deleteAfterDelay()


 void SplashScreen::deleteAfterDelay ( RelativeTime minimumTotalTimeToDisplayFor, 
 
 bool removeOnMouseClick ) 

Tells the component to autodelete itself after a timeout period, or when the mouse is clicked.You should call this after finishing your app's initialisation work.Note that although you could call deleteAfterDelay() as soon as you create the SplashScreen object, if you've got a long initialisation procedure, you probably don't want the splash to timeout and disappear before your initialisation has finished, which is why it makes sense to not call this method and start the selfdelete timer until you're ready.It's safe to call this method from a nonGUI thread as long as there's no danger that the object may be being deleted at the same time.Parameters

 minimumTotalTimeToDisplayFor how long the splash screen should stay visible for. Note that this time is measured from the constructiontime of this object, not from the time that the deleteAfterDelay() method is called, so if you call this method after a long initialisation period, it may be deleted without any further delay. 
 
 removeOnMouseClick if true, the window will be deleted as soon as the user clicks the mouse (anywhere)