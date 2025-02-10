#### centreAroundComponent()


 void TopLevelWindow::centreAroundComponent ( Component \* componentToCentreAround, 
 
 int width, 
 int height ) 

This will set the bounds of the window so that it's centred in front of another window.If your app has a few windows open and want to pop up a dialog box for one of them, you can use this to show it in front of the relevant parent window, which is a bit neater than just having it appear in the middle of the screen.If componentToCentreAround is nullptr, then the currently active TopLevelWindow will be used instead. If no window is focused, it'll just default to the middle of the screen.