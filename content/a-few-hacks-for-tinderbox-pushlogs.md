Title: A few hacks for Tinderbox Pushlogs
Date: 2011-02-11 03:31
Tags: mozilla, tbpl
Planets: mozilla

A month ago, I've introduced a few new features in [Tinderbox Pushlog](http://tbpl.mozilla.org)
and Ehsan threatened me to write a blog post about them, so I do.

My first contributions to Tinderbox Pushlog were two filters you had to
pass in parameter in the URL [^1]. In the mean time I thought of
another filter: show only unstarred jobs to help people watching the
tree (especially philor). I used this momentum to write a few other
patches:

-   Show a UI to filter by pusher email or toggle unstarred jobs filter
    (you might have notice that between "Infrastructure" and
    "Timezone") ;
-   Click on a pusher name to filter his pushes (re-click to unfilter) ;
-   Add some keybings: U to toggle unstarred jobs filter, P and N to
    navigate between current unstarred failing jobs ;
-   Make all of this working with HTML5's PushState/PopState (aka
    History API) so you can copy/paste the URL to have the same filters
    applied (need Firefox 4+ for that feature).

I realize that the keybindings will not work with Vimperator but if you
use this extension you might be used to that kind of annoyance and know
the workarounds.

I hope these new features will make some people's life easier!

[^1]: See [this blog post](../../2010/09/filter-tinderboxpushlog-by-pusher-or-revision-id.html).
