Title: Placeholder attribute in Firefox 3.7 alphas
Date: 2010-03-19 00:56
Tags: firefox, html5

The placeholder attribute for input and textarea elements is available
on Firefox 3.7 since developer preview 3.7a2.

The placeholder attribute is a new attribute from [HTML5 Forms
specifications](http://dev.w3.org/html5/spec/forms.html). The placeholder text is showed as a hint on input and
textarea elements when the element is empty and not focused. This kind
of behavior is already used by a lot of websites and even by Firefox
user interface [^1].  
If you are a web developer and you want to use the placeholder
attribute, you should know you can easily identify if the
<acronym title="User Agent">UA</acronym> knows about the
placeholder attribute with this simple code:

    if(!"placeholder" in document.createElement("input")) {
      // your fallback
    }

This way, you can have a sane fallback until you consider the
placeholder attribute is supported enough to remove the fallback.

At the moment, there are still some minor issues about the placeholder
like the style for Aero (Windows Vista and 7) [^2] and some
optimizations [^3]. However, there is a bigger issue related to the
ability to style the placeholder [^4]. Indeed, at the moment, there
is no specification about the placeholder style customization. Webkit
have decided to use a CSS pseudo-element "-web-input-placeholder"
but unfortunately, no consensus has been reached.

To know if your browser supports the placeholder attribute, just look at
the input field below. If you see "tulip orchid" that means your
browser support the placeholder attribute correctly. If you see only
"tulip" that means you browser has an issue with new lines in
placeholder text (WebKit has this issue [^5]). If you see nothing
that means your browser doesn't support placeholder at all.

<input placeholder="tulip orchid"></input>

This is my first contribution for the HTML5 Forms implementation in
Gecko/Firefox. Next steps may be the constraint validation API,
autofocus and other small stuff.

[^1]: Actually, Firefox is using the XUL 'emptytext' attribute for stuff like
the search box which is going to be replaced by the placeholder attribute.
[^2]: [https://bugzilla.mozilla.org/show_bug.cgi?id=548626](https://bugzilla.mozilla.org/show_bug.cgi?id=548626)
[^3]: [https://bugzilla.mozilla.org/show_bug.cgi?id=553097](https://bugzilla.mozilla.org/show_bug.cgi?id=553097)
[^4]: [https://bugzilla.mozilla.org/show_bug.cgi?id=457801](https://bugzilla.mozilla.org/show_bug.cgi?id=457801)
[^5]: I have opened a bug, [https://bugs.webkit.org/show_bug.cgi?id=36291](https://bugs.webkit.org/show_bug.cgi?id=36291)
