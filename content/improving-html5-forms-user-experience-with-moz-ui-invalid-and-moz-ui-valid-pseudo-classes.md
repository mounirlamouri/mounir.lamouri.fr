Title: Improving HTML5 Forms' user experience with :-moz-ui-invalid and :-moz-ui-valid pseudo-classes
Date: 2011-05-08 21:00
Tags: css, firefox, html5

As you might have noticed, with Firefox 4, we have introduced the form
validation in the browser. You can have more information about what that
means in a [previous blog post](../../2010/11/html5-forms-validation-in-firefox-4.html). Because of the validation made by the
browser, we needed to have a feedback to show users that a form element
is currently invalid thus preventing users trying to submit a form while
it contains errors.

I'm not a technical person, what should I remember?
---------------------------------------------------

At Mozilla, we want your experience with forms to be much better.
Currently, the tools available to web authors are not powerful enough to
do a good <acronym title="User Interface">UI</acronym> with
simple code. If the tools are not good, we are going to see bad form
UI's. Because forms are very important in your life on the web, we chose
to create two tools to help web authors make your web experience better.
If these tools are appreciated by web authors and accepted by other
browser vendors, they might be integrated into the HTML specifications
and be widely used.

Why these new pseudo-classes?
-----------------------------

CSS3 specification comes with two pseudo-classes named :invalid and
:valid which respectively match invalid and valid form elements in the
document. During Firefox 4 beta process, we have introduced a default
style to :invalid pseudo-class adding a red glow to all invalid form
elements. Unfortunately, this was very bad for
<acronym title="User eXperience">UX</acronym>. The most obvious
issue is that we were showing required element with a red glow as soon
as the page was loaded thus moving user attention to them. Going from
this issue, we thought it would be better to create two pseudo-classes
with some UX rules. The goal was to provide a simple way for authors to
style invalid and valid elements while following UX rules. These
pseudo-classes are named :-moz-ui-invalid and :-moz-ui-valid. And
:invalid no longer has a default style on Firefox 4 but :-moz-ui-invalid
has one instead.

When are they applied?
----------------------

To follow these rules, we had a look at [this interesting article](http://www.alistapart.com/articles/inline-validation-in-web-forms/) by
[Luke Wroblewski](http://www.alistapart.com/authors/w/lwroblewski).
Then I've been working with [Alexander Limi](http://limi.net/),
[Jonas Sicking](https://twitter.com/sickingJ/),
[Tantek Çelik](http://tantek.com/) and [Justin Dolske](https://blog.mozilla.com/dolske/) and we have
decided to focus on two issues: element being invalid when the page is
loaded (the user attention is uselessly focused on those elements) and
validity status being changed while you are typing (the user is
distracted by the UI changes).

The former issue has been fixed with a simple rule: as long as the
element's value hasn't been changed by the user, both pseudo-classes
can't apply. Though, if the user tries to submit the form in an invalid
state, the pseudo-classes will apply even if the value hasn't been
changed. This is to make it clear for the user which elements are
currently invalid and need to be fixed.  
For the later issue, we do not want to distract the users while typing.
So, when an element is focused as valid, if it was matching
:-moz-ui-valid it will match it until the element is blurred even if the
element becomes invalid. Though, to help the user make an element valid,
if, when focused, an element is matching :-moz-ui-invalid, it will match
:-moz-ui-valid or :-moz-ui-invalid depending of the validity while
typing. In other words, we want to help the user to fix an invalid
element but do not want to distract him while interacting with a valid
one. For example, when you have to enter an email address, you will have
to type "*username*" which isn't a valid email address but you
actually wanted to type "*username@domain.com*" and this is a valid
email address.

<style>
  .test-val { margin: 5px; }
  .test-val:-moz-ui-valid { box-shadow: 0 0 1.5px 1px green; }
  .test-val:-moz-ui-invalid { box-shadow: 0 0 1.5px 1px red; }
</style>

<div>
You can try it on the following text field. A green glow is when
:-moz-ui-valid applies and a red one is when :-moz-ui-invalid applies.
The text field is required and expect a valid email address. Firefox 4
is required.

<form onsubmit="return false;">
<input class="test-val" type="email" required></input><input type="submit" value="Submit"></input>
</form>
<br>
</div>

Follows a deeper explanation of the algorithm for those who want to know
the details. For more information, it's better to dig into [the code](https://hg.mozilla.org/mozilla-central/).

To match :-moz-ui-invalid, all of the following conditions have to be
true:

1.  The element is invalid;
2.  The element is not focused, or had either :-moz-ui-invalid applying
    before it was focused;
3.  The element has no form owner or its form owner doesn't have the
    novalidate attribute set;
4.  The element has already been modified or the user tried to submit
    the form owner while invalid.

There is one exception: if the element is invalid because of a custom
error, the only conditions that have to be fulfilled in the condition
number 3.

To match :-moz-ui-valid, all of the following conditions have to be
true:

1.  The element is either valid or isn't allowed to have
    :-moz-ui-invalid applying;
2.  The element is not focused, or had either :-moz-ui-valid or
    :-moz-ui-invalid applying before it was focused;
3.  The element has no form owner or its form owner doesn't have the
    novalidate attribute set;
4.  The element has already been modified or the user tried to submit
    the form owner while invalid.

You can also have a look at the Mozilla Developer Network documentation:
[:-moz-ui-invalid](https://developer.mozilla.org/en/CSS/%3A-moz-ui-invalid)
and [:-moz-ui-valid](https://developer.mozilla.org/en/CSS/%3A-moz-ui-valid).

Examples
--------

You can simply show a red glow when the element is invalid and a green
one when it is valid:

    :-moz-ui-invalid {
      box-shadow: 0 0 1.5px 1px red;
      /* This is actually the default Firefox style. */
    }
    :-moz-ui-valid {
      box-shadow: 0 0 1.5px 1px green;
    }

You can also change an image positioned next to the form element:

    span.validator {
      width: 16px;
      height: 16px;
      display: inline-block;
      background-size: 100%, 100%;
    }
    :-moz-ui-valid + span {
      background-image: url("images/valid.png");
    }
    :-moz-ui-invalid + span {
      background-image: url("images/invalid.png");
    }

With the corresponding HTML code (for example):

    <input type='email'><span class='validator'>

Looking for feedback
--------------------

We are looking for feedback from authors and implementors. As an author,
you should keep in mind that this feature is experimental and could be
removed and changed at any time. Though, we are looking for feedbacks
and we encourage you to try it and tell us what should be tweaked. You
can open a bug on [bugzilla](https://bugzilla.mozilla.org/) or
[send me an email](mailto:%6d%6c%61%6d%6f%75%72%69%20%28%61%74%29%20%6d%6f%7a%69%6c%6c%61%2e%63%6f%6d).
As implementors, we would love to see other implementations trying to fix that
issue to be able to discuss a specification.
