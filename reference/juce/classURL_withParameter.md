#### withParameter()


 URL URL::withParameter ( const String & parameterName, const String & parameterValue ) const nodiscard 
 

Returns a copy of this URL, with a GET or POST parameter added to the end.Any control characters in the value will be URLencoded.e.g. calling "withParameter ("amount", "some fish") for the url "www.fish.com"
would produce a new url whose <tt>toString (true)</tt> method would return
"www.fish.com?amount=some+fish".See alsogetParameterNames, getParameterValues