Title: The HTML progress element in Firefox
Date: 2011-07-06 13:37
Tags: html5, firefox

First of all, the progress element is going to be available with the
next version of Firefox and is already available in the Beta, Aurora and
Nightly [channels](https://www.mozilla.com/firefox/channel/).

<div>
<div>Progress element:</div>
<progress value="0.75"><small>*Your browser does not support the
progress element!*</small></progress>
</div>

<div>
<div>Indeterminate progress element:</div>
<progress><small>*Your browser does not support the progress
element!*</small></progress>
</div>
<br>

According to the specifications, and as you might imagine, <q>"the
progress element represents the completion progress of a
task"</q> [^1]. To specify this completion, you can set two
attributes: *value* and *max*. Note that *max* will be considered as
*1.0* when not specified. In addition, the progress element can be
indeterminate to represent that something is happening but you can't
evaluate the progress. To put the progress element in this state, you
have to remove the *value* attribute.  

    <!--
      1. Progress element at full capacity.
      2. Progress element at half capacity.
      3. Progress element at zero capacity.
      4. Indeterminate progress element.
    -->
    
    <progress value='1'></progress>
    <progress value='50' max='100'></progress>
    <progress value='0'></progress>
    <progress></progress>

In this article, I'm going to do an overview of this new element. If you
want an exhaustive documentation, you should have a look at the
[specifications](http://www.whatwg.org/specs/web-apps/current-work/multipage/the-button-element.html#the-progress-element)
or the [Mozilla Developer Network documentation](https://developer.mozilla.org/en/HTML/element/progress).

Native rendering
----------------

Using the new form widgets for authors make their life easier, their
code less complex and improve the semantic of their pages. But this also
improve user experience and this mostly comes with the native rendering
of those widgets.  
Native rendering means when you will see a progress element on a
website, except if the author ask otherwise, you will see a progress
element exactly like one in a native application. That means, on MacOS
X, you will see a blue bar on a grey background. On Windows Vista and 7,
you will see a green bar with an animation. On Windows XP, you will see
a green bar with chunks and on Linux/GTK, it will depends on your
theme.  
For the later, given that we are using your GTK engine/theme, if it is
bugged, you might see mis-rendered progress elements. It's very unlikely
[^2] unless you are using obscure engine but that means that it's
preferred to test with another engine/theme if the rendering seems buggy
with GTK. It is sad that we have to deal with that kind of issues but
that is the price to pay to have a native rendering. It might actually
explain why no other browser seems to have a native rendering on
Linux/GTK.

It goes without saying that, as usual, you can disable the native
rendering with *-moz-appearance: none;* or by setting *border* or
*background* CSS properties.

    <!--
      Native and non-native progress elements.
    -->
    <progress></progress>
    <progress style="-moz-appearance: none;"></progress>

How to style it?
----------------

Styling is one of the biggest unresolved issues of new form widgets. The
progress element is quite simple but there are no specifications
explaining how authors should style it so every browsers have their own
ways.

### ::-moz-progress-bar pseudo-element

Basically, the progress element is two div's. You can access to the
outer div by styling *progress* and to the inner one with
*::-moz-progress-bar* pseudo-element. However, even if you can style it
as much as you might expect, you will not be able to change the width
unless the progress element is indeterminate; the reasons are obvious.  

    <style>
      progress { background-color: red; border: 1px solid black; }
      progress::-moz-progress-bar { background-color: blue; }
    </style>
    <progress value='0.5'></progress>

It's interesting to see that Webkit has two pseudo-elements instead of
one [^3] but I do not see which use case this is solving that a
combination of *padding*, *border* and *background* wouldn't solve.  
Unfortunately, I did not find any documentation about styling this
element with Opera/Presto.

### :indeterminate pseudo-class

As said in the introductory paragraph, progress elements can be
indeterminate. It happens that there is already an *:indeterminate*
pseudo-class for checkboxes so we thought it would be a good idea to
allow you to select indeterminate progress elements in that state with
this pseudo-class. We did request to add this to the specifications, it
has been accepted and Webkit implemented it a few days ago.

    <style>
      progress:indeterminate {
        background-color: red; border: 1px solid black;
      }
      progress:indeterminate::-moz-progress-bar {
        background-color: white;
      }
    </style>
    <progress></progress>

Vertical progress bars
----------------------

A few form widgets can be vertical [^4]. Currently, the HTML
specifications say that as soon as the dimension of the widget are
vertical, the element should be shown as vertical. For a progress bar,
that means that the bar should go from bottom to top instead of left to
right (or right to left). Such a system would have required to add a
*:vertical* pseudo-class but unfortunately, for complex reasons
[^5], it happened to be hardly implementable. So, we came with
another system: if you want to request a form widget to be shown as
vertical, you can set the *-moz-orient* CSS property to *vertical*.
Then, the element will be rendered as requested even if the dimensions
are not appropriate. Note that if you don't specify a size to the
progress element and asks it to be vertical, the default dimensions will
be vertical. Note also that you can use *horizontal* keyword as well as
*vertical*.  

    <style>
      progress { -moz-orient: vertical; }
    </style>
    <!--
      1. Vertical progress element.
      2. Vertical progress element with horizontal dimensions.
      3. Horizontal progress element.
    -->
    <progress value='0.5'></progress>
    <progress value='0.5' style="height: 1em; width: 10em;"></progress>
    <progress value='0.5' style="-moz-orient: horizontal;"></progress>

DISCLAIMER: the way we allow vertical progress bar is far from being
stable (in the sens that it might change) and the current specifications
are not even close to our implementation.

Feedback
--------

Feedback is always welcome and can have a real impact at this state so
if you think something should be done differently, [send me an email](mailto:%6d%6c%61%6d%6f%75%72%69%20%28%61%74%29%20%6d%6f%7a%69%6c%6c%61%2e%63%6f%6d).
If you see a bug, feel free to [report it](https://bugzilla.mozilla.org/enter_bug.cgi?product=Core&component=DOM%3A%20Core%20%26%20HTML).

[^1]: [http://www.whatwg.org/specs/web-apps/current-work/multipage/the-button-element.html#the-progress-element](http://www.whatwg.org/specs/web-apps/current-work/multipage/the-button-element.html#the-progress-element)
[^2]: It's the case for at least the Equinox engine: [bug 657144](https://bugzilla.mozilla.org/show_bug.cgi?id=657144)
[^3]: [http://trac.webkit.org/wiki/Styling Form Controls](http://trac.webkit.org/wiki/Styling%20Form%20Controls)
[^4]: *meter*, *progress* and &lt;input type='range'&gt; if I recall correctly.
[^5]: See the thread in www-style mailing list: [http://lists.w3.org/Archives/Public/www-style/2011Apr/0386.html](http://lists.w3.org/Archives/Public/www-style/2011Apr/0386.html)
