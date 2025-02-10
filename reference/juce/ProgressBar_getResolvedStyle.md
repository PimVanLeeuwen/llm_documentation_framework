#### getResolvedStyle()


 Style ProgressBar::getResolvedStyle ( ) const 
 

Returns the progress bar's current style if it has one, or a default style determined by the lookandfeel if it doesn't.Use this function in overrides of LookAndFeelMethods::drawProgressBar() in order to determine which style to draw.See alsogetStyle, setStyle, LookAndFeelMethods::getDefaultProgressBarStyle