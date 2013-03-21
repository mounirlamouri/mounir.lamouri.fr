Title: OpenID: provide your own identity
Date: 2009-12-03 15:31
Tags: openid, privacy

OpenID is really interesting. I will not explain in details what it is
about because [openid.net](http://openid.net/) or [wikipedia](http://en.wikipedia.org/wiki/OpenID) will probably do that
better than me. Basically, it's a try to get an unique way to log on
various websites. For example, with OpenID, you can get authenticated on
Facebook with your Google account [^1]. Actually, OpenID is much
more than a standard way to log on, it lets you externalizing the
authentication server. That means you can use the OpenID account linked
to your Yahoo! account ^foobar^ [^2] or even the one linked to your wordpress
blog or any any one you may already have [^3]. That also means you
can use your own !

Why should you use your own server to provide your own identity on
Internet ? Actually, this question should be "Why should I trust
someone else to provide my identity on Internet ?". Indeed, with
OpenID, you can externalize the authentication but that also means
centralizing it. Having a lot of identities on Internet is annoying :
you must file the same information, you have a lot of passwords, you
don't always remember your username... But having the same account to
log everywhere makes you very dependent on this account. If your OpenID
provider closes its service, ask you to pay for it, doesn't respect your
privacy, or anything else, you will be in a bad situation.

To prevent this situation, the best solution is to run and use your own
OpenID server. If you already have one for anything else, adding OpenID
is going to be easy. There is even a [page with some solutions](http://wiki.openid.net/Run-your-own-identity-server).
[phpMyID](http://siege.org/projects/phpMyID) is really appreciated because it's lean but it's designed to
provide only one account. That means you will not be able to offer an
OpenID server to your friends. That's why I prefer [SimpleID](http://simpleid.sourceforge.net/). How to
setup the server will be maybe for another entry but I suppose anyone
interested to do that will know how to found the information [^4].

The simplest way is to delegate your authentication. That means you can
use an OpenID account from [myOpenID](http://www.myopenid.com) or any OpenID provider and, in
your blog or any web page you control, you can add these lines in the
HTML HEAD section:

    <link rel="openid.server" href="http://www.myopenid.com/server" />
    <link rel="openid.delegate" href="http://username.myopenid.com/" />

The example is using myOpenID but it could be wordpress, Yahoo! or
anything else. *openid.server* is the server you want to use.
*openid.delegate* is the OpenID account your provider told you to use
(like username.wordpress.com for wordpress).  
This solution lets you use your blog URL (or any webpage you want) as an
OpenID account and it will transparently use the specified server. That
means you will be able to change the server when you want without
breaking your OpenID account. So, you are not as much dependent from the
provider as you were. Unfortunately, there will always be a third party
which you have to trust while you are using someone else as a provider.

Maybe you should now ask one of your geeky friend if she/he didn't setup
an OpenID server or do it yourself ?

[^1]: [http://developers.facebook.com/news.php?blog=1&story=246](http://developers.facebook.com/news.php?blog=1&story=246)
[^2]: [http://openid.yahoo.com/](http://openid.yahoo.com/)
[^3]: Look at [http://openid.net/get-an-openid/](http://openid.net/get-an-openid/)
[^4]: Some hints: [http://www.intertwingly.net/blog/2007/01/03/OpenID-for-non-SuperUsers](http://www.intertwingly.net/blog/2007/01/03/OpenID-for-non-SuperUsers)
