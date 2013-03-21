Title: HTML5 Forms Validation in Firefox 4
Date: 2010-11-10 18:00
Tags: firefox, html5

HTML5 Forms specifications introduce some new input types, attributes
and other awesome features. One of the transversal features is native
browser-side form validation.  
For Firefox 4, we tried to focus on that feature and ship it as complete
as possible. All following features descriptions are available with
[Firefox 4 beta 7](http://www.mozilla.com/firefox/beta/) except some which are
going to be available in following betas (it's clearly specified when that's the case).

Why browser-side form validation?
---------------------------------

The idea behind form validation in HTML5 Forms is to prevent using
JavaScript to check basic stuff in your forms: Is this email address
valid? Is this field filled in? Do passwords match? These are often
checked in JavaScript when you click on the submit button. You might
write your own javascript code or use a library but that will always be
a repetitive, boring and error-prone task. With forms validated by the
browser, you no longer have to care about those steps, just write simple
HTML.  
For the user, the validation being done by the browser is a guarantee of
quality with better accessibility and consistency.

How can I make my form using this feature?
------------------------------------------

If you use new attributes related to form validation or new input types
with internal validation, you will automatically opt in for form
validation by the browser (if supported by the browser). All new input
types introduced with HTML5 forms except *search* and *tel* benefit from
internal validation.  
Firefox 4 is going to support *email* and *url* and the validation will
check if the value is a valid email or url respectively.  
In addition, these attributes will provide an automatic validation
mechanism:

-   *required*: a required form control will be invalid if its value is
    empty. This is working for &lt;input&gt; and &lt;textarea&t;. If set on a
    &lt;input type='checkbox'&gt;, the element will have to be checked. On a
    group of &lt;input type='radio'&gt;, one of the radio button will have
    to be selected. If set on a &lt;input type='file'&gt;, a file will have
    to be selected.  

&lt;select&gt; will accept the *required* attribute in Firefox beta 8 (see
*What's next?*).

    <input required>
    <textarea required></textarea>

-   *pattern*: you can specify a regular expression [^1] to check
    the element's value. This can be used only on some &lt;input&gt; types
    (*text*, *search*, *tel*, *email* and *url*). When you use pattern,
    it's highly recommended to use the *title* attribute to describe the
    pattern.

<!-- -->

    <input type='tel' pattern='\d\d \d\d \d\d \d\d \d\d' title="Write a phone number in the format 'XX XX XX XX XX'">
    <input type='email' pattern=".*@company\.com" title="Enter you company email address">

-   *maxlength*: maxlength can already be used with Firefox 3.6 but it
    will only block the keyboard inputs made by the users on an
    &lt;input&gt; so they can't type more characters than the value
    specified in the maxlength attribute. In Firefox 4 beta 7, this
    applies on &lt;textarea&gt; too. In addition, if the value is set via
    .value, the element will become invalid if the new value has a
    length bigger than maxlength.

<!-- -->

    <input maxlength='10'>
    <textarea maxlength='140'></textarea>

How can I opt out?
------------------

You should probably think about that twice, If you have your own system
for form validation, you should probably try to disable it when the
browser can manage form validation instead of disabling the validation
by the browser for your own system. However, there might be other
reasons why you would want to disable form validation. Good reasons
might be if you want to use some new input types but you don't care
about checking the validity.  
The simplest way to opt out is to add the *novalidate* attribute to your
&lt;form&gt;. You can also set *formnovalidate* on your submit controls. You
should prefer *formnovalidate* than *novalidate* if you want to have one
submit control with form validation and another without.  
Detecting this feature is not really easy given that you want to have a
message being shown but you can't know for sure if the browser is going
to show something even if form validation seems to be supported. I will
try to write another post about that later.

How can I specify my validity rules?
------------------------------------

You can make an element invalid by calling
*.setCustomValidity(errorMsg)*. Doing some checks on *oninput()* and
calling *.setCustomValidity()* should be enough in most situations.  
*.setCustomValidity()* takes in parameter the error message. You can
pass the empty string to *.setCustomValidity()* if you want to remove
the custom error.  
With this method, you can check that two password fields have the same
value very easily:

    <script>
      function checkPassword(p1, p2)
      {
        if (p1.value != p2.value) {
          p2.setCustomValidity('passwords do not match');
        } else {
          p2.setCustomValidity('');
        }
      }
    </script>
    <input type='password' id='p1'>
    <input type='password' onfocus="checkPassword(document.getElementById('p1'), this);" oninput="checkPassword(document.getElementById('p1'), this);">

How can I change the text of the error message?
-----------------------------------------------

Each error types have a string associated describing the error. For
example, if an input element is required and has no value, the message
will be "Please fill out this field". Firefox will try to be as
clever as possible to show the best error message but you might want to
override it in some situations where the rules are very complex. For
example:

    <input type='email' required pattern='.*@company\.com'>

You might prefer to have a simple "Please, enter your corporate email
address." instead of three generic messages depending of the
unfulfilled constraint.  
To help with that, we have introduced a non-standard
*x-moz-errormessage* [^2] which let you specify an error message
for a given form control. Regardless of the error, if
*x-moz-errormessage* is present and different from the empty string, its
value will be used as the error message instead of the default one.  
This is non-standard so it should be used carefully. See
[http://www.w3.org/Bugs/Public/show_bug.cgi?id=10923](http://www.w3.org/Bugs/Public/show_bug.cgi?id=10923).
In addition, you should know that *.setCustomValidity()* lets you indirectly set
your own error message but we do not really like that because you will let the
browser think that the element is suffering from a custom error even if it is
not.

How can I change the error popup UI?
------------------------------------

Unfortunately, there is no way to change the UI. The popup is part of
the browser and it's currently not possible to style the browser from
the content. This might change later but that will not be done for
Firefox 4.  
If you think the current popup is ugly, you should know it's not final.
We will try to enhance that later, see [bug 602500](https://bugzilla.mozilla.org/show_bug.cgi?id=602500).
All comments are very welcome!

New CSS pseudo-classes and default styles
-----------------------------------------

[CSS3 UI](http://www.w3.org/TR/css3-ui/) introduce new pseudo-classes that HTML5 is now using like
*:invalid*, *:valid*, *:required* and *:optional*. Firefox 4 beta 7
supports all these pseudo-classes and adds a new pseudo-class:
*:-moz-submit-invalid* which applies on submit controls when a form has
an invalid element.  
*:invalid* has a default style which is a red *box-shadow*. This default
style is going to be removed when *:-moz-ui-invalid* will be added (see
*What's next?*). In the mean time, you can easily remove this default
style in your stylesheets:

    :invalid {
      box-shadow: none;
    }

What's next?
------------

It's a bit early to say what will be done after Firefox 4 but we already
know that a few things will be done in the following betas:

-   *required* attribute for &lt;select&gt;. You will be able to specify
    that a select element is required. This rule will be fulfilled if
    you select at least one option which has a value different from the
    empty string. See [bug 596511](https://bugzilla.mozilla.org/show_bug.cgi?id=596511). This might be fixed for beta 8.
-   Let &lt;output&gt; being subject from constraint validation. Output
    elements are currently barred from constraint validation but it
    seems to be too restrictive and *.setCustomValidity()* might be
    useful in some situations. See [bug 604673](https://bugzilla.mozilla.org/show_bug.cgi?id=604673). This might be fixed
    for beta 8.
-   Adding *:-moz-ui-invalid* and maybe *-moz-ui-valid* pseudo-classes.
    *:invalid* and *:valid* pseudo-classes are very bad for
    <acronym title="User interface">UI</acronym> and
    <acronym title="User experience">UX</acronym> perspectives.
    We want to introduce new pseudo-classes which would follow some UX
    rules. This will probably be the subject of a future blog post.
    Related bugs: [bug 605124](https://bugzilla.mozilla.org/show_bug.cgi?id=605124) and [bug 605125](https://bugzilla.mozilla.org/show_bug.cgi?id=605125).

[^1]: The regular expression will follow the JavaScript regular expression rules
and will be checked against the entire element's value.
[^2]: The prefix is the new recommendation, see [http://www.w3.org/Bugs/Public/show_bug.cgi?id=9590](http://www.w3.org/Bugs/Public/show_bug.cgi?id=9590)
