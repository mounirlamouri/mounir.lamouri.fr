Title: Filter TinderboxPushLog by pusher or revision id
Date: 2010-09-30 21:38
Tags: tbpl
Planets: mozilla

I wrote two small patches [^1] that let you filter tinderboxpushlog
with the pusher or the revision id. This is available in
[http://tests.themasta.com/tinderboxpushlog/](http://tests.themasta.com/tinderboxpushlog/) since a few days.

So, now, you can specify these new arguments in tinderboxpushlog URL:

    pusher=<pusher_email_address> - filter pushes to show those done by the given user.
    rev=<12_rev_id_chars> - filter pushes to show the one containing the given revision id.

For example, this URL will only show the push containing the revision id
071d28940876: [http://tests.themasta.com/tinderboxpushlog/?tree=MozillaTry&rev=071d28940876](http://tests.themasta.com/tinderboxpushlog/?tree=MozillaTry&rev=071d28940876).

The main use case of that feature is to make tinderboxpushlog more
friendly when trying to look at a push on the try server: you can avoid
the noise made by other pushes.  
Unfortunately. `rev` doesn't try to search the given revision id and you
will have to browse the pushes until one appears.

If someone wants to add a UI for this feature, have a look at [bug
576544](https://bugzilla.mozilla.org/show_bug.cgi?id=576544).

[^1]: [bug 549275](https://bugzilla.mozilla.org/show_bug.cgi?id=549275) and [bug 598556](https://bugzilla.mozilla.org/show_bug.cgi?id=598556).
