#### contains()


 virtual bool ComponentPeer::contains ( Point< int > localPos, bool trueIfInAChildWindow ) const pure virtual 
 

Checks if a point is in the window.The position is relative to the topleft of this window, in unscaled peer coordinates. If trueIfInAChildWindow is false, then this returns false if the point is actually inside a child of this window.