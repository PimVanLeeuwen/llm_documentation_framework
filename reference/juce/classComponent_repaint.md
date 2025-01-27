#### repaint() [3/3]


 void Component::repaint ( Rectangle< int > area ) 
 

Marks a subsection of this component as needing to be redrawn.Calling this will not do any repainting immediately, but will mark the given region of the component as 'dirty'. At some point in the near future the operating system will send a paint message, which will redraw all the dirty regions of all components. There's no guarantee about how soon after calling repaint() the redraw will actually happen, and other queued events may be delivered before a redraw is done.The region that is passed in will be clipped to keep it within the bounds of this component.See alsorepaint()