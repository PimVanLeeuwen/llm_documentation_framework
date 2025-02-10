#### setStyle()


 void ProgressBar::setStyle ( std::optional< Style > newStyle ) 
 

Sets the progress bar's current style.You can use this to force getResolvedStyle() to return a particular value. If a nonnullopt style is passed, that style will always be returned by getResolvedStyle(). Otherwise, if nullopt is passed, getResolvedStyle() will return its LookAndFeel's getDefaultProgressBarStyle().See alsogetStyle, getResolvedStyle