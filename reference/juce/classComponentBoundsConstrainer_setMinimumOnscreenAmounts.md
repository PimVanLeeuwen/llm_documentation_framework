#### setMinimumOnscreenAmounts()


 void ComponentBoundsConstrainer::setMinimumOnscreenAmounts ( int minimumWhenOffTheTop, int minimumWhenOffTheLeft, int minimumWhenOffTheBottom, int minimumWhenOffTheRight ) noexcept 
 

Sets the amount by which the component is allowed to go offscreen.The values indicate how many pixels must remain onscreen when dragged off one of its parent's edges, so e.g. if minimumWhenOffTheTop is set to 10, then when the component goes off the top of the screen, its yposition will be clipped so that there are always at least 10 pixels onscreen. In other words, the lowest yposition it can take would be (10 the component's height).If you pass 0 or less for one of these amounts, the component is allowed to move beyond that edge completely, with no restrictions at all.If you pass a very large number (i.e. larger that the dimensions of the component itself), then the component won't be allowed to overlap that edge at all. So e.g. setting minimumWhenOffTheLeft to 0xffffff will mean that the component will bump into the left side of the screen and go no further.