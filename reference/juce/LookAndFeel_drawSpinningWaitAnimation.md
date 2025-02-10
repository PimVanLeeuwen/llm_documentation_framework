#### drawSpinningWaitAnimation()


 virtual void LookAndFeel::drawSpinningWaitAnimation ( Graphics & , const Colour & colour, int x, int y, int w, int h ) pure virtual 
 

Draws a small image that spins to indicate that something's happening.This method should use the current time to animate itself, so just keep repainting it every so often.Implemented in LookAndFeel\_V2.