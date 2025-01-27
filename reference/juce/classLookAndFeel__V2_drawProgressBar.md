#### drawProgressBar()


 void LookAndFeel\_V2::drawProgressBar ( Graphics & , ProgressBar & , int width, int height, double progress, const String & textToShow ) overridevirtual 
 

Draws a progress bar.If the progress value is less than 0 or greater than 1.0, this should draw a spinning bar that fills the whole space (i.e. to say that the app is still busy but the progress isn't known). It can use the current time as a basis for playing an animation.To determine which style of progressbar to draw call getResolvedStyle().(Used by progress bars in AlertWindow).See alsogetResolvedStyle Implements ProgressBar::LookAndFeelMethods.Reimplemented in LookAndFeel\_V4.