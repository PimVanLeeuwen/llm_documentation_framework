#### setTitleBarButtonsRequired()


 void DocumentWindow::setTitleBarButtonsRequired ( int requiredButtons, 
 
 bool positionTitleBarButtonsOnLeft ) 

Changes the set of titlebar buttons being shown.Parameters

 requiredButtons specifies which of the buttons (close, minimise, maximise) should be shown on the title bar. This value is a bitwise combination of values from the TitleBarButtons enum. Note that it can be "allButtons" to get them all. The behaviour of native titlebars on macOS is slightly different: the maximiseButton flag controls whether or not the window can enter native fullscreen mode, and the zoom button can be disabled by making the window nonresizable. 
 
 positionTitleBarButtonsOnLeft if true, the buttons should go at the left side of the bar; if false, they'll be placed at the right 


Referenced by StandaloneFilterWindow::StandaloneFilterWindow().