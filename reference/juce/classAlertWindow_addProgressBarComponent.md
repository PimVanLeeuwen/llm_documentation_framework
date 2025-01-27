#### addProgressBarComponent()


 void AlertWindow::addProgressBarComponent ( double & progressValue, 
 
 std::optional< ProgressBar::Style > style = std::nullopt ) 

Adds a progressbar to the window.Parameters

 progressValue a variable that will be repeatedly checked while the dialog box is visible, to see how far the process has got. The value should be in the range 0 to 1.0 
 
 style determines the style the ProgressBar should adopt. By default this use a style automatically chosen by the LookAndFeel, but you can force a particular style by passing a nonoptional value. 



See alsoProgressBar::setStyle