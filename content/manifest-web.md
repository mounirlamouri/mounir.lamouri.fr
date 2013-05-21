Title: The Web Manifest
Date: 2013-05-14 22:00
Tags:
Planets: mozilla
Status: draft

Some history
------------

Mozilla has been trying to push for quite some time a manifest format for web
applications [^1] after [Opera's Widgets](http://www.w3.org/TR/widgets/) lack of
traction. The original scope of that work was installed web applications such as
hosted web applications and packaged applications. The main difference with
widget being the hosted web applications support and the manifest being in JSON
instead of the infamous XML.

More recently, the manifest format specification has moved to the [SysApps
working group](http://www.w3.org/2012/sysapps/) as part of the [runtime
specification](http://www.w3.org/2012/sysapps/runtime/) and later on as part of [its own specification](http://www.w3.org/2012/sysapps/manifest/).
As of today, the "Manifest for Web Applications" specification should move back
to the WebApps working group [^2].

Fun fact: Marcos Caceres was the editor of Widgets. He is now the editor of the
new manifest specification.

Migrating to WebApps
--------------------

Moving this specification from the SysApps to the WebApps working group goes
further than simple administrative overhead or patent policy. Mozilla, as one of
the key players behind this work wants to increase the scope of the manifest.
SysApps is a group that has been created to specify APIs that are mostly outside
of the browser scope in order to make the Web Platform able to compete with
other platforms. Because of that, it is very likely that work that SysApps will
produce will be seen as not in scope for the browser even if that doesn't have
to be the case.

However, we believe that the manifest format doesn't have to be bound to
installed applications and we have a window of opportunity with hosted web
applications to make that happen.

Hosted web applications
-----------------------

Hosted web applications are web sites that have a manifest that gives metadata
to help the runtime to install them. For example, making twitter.com installable
would be as easy as hosting a manifest at the twitter.com domain that would have
metadata information such as the application name and icons.  
A simplified twitter.com manifest would look like this:

    {
      "version": "1.0",
      "name": "Twitter",
      "description": "Twitter for mobile",
      "developer": {
        "name": "Twitter",
        "url":"http://twitter.com"
      },
      "icons": {
        "30":"/images/larrybird-30.png",
        "60":"/images/larrybird-60.png",
        "128":"/images/larrybird-128.png"
      }
    }
<small>This is actually the real manifest stripped of localisation information.</small>

In other words, hosted web applications are simply web applications
that have the ability to be installed by a runtime and any web site with a
manifest can be given this ability.

This is probably one of the major features of the runtime proposed by Mozilla in
comparison to the W3C's Widgets standard: hosted web applications are pushing
the Web as an application platform. Unfortunately, an outstanding issue we have
encountered so far is that the Web Platform has pretty bad offline support [^3]
and fixing this is a priority to make the Web Platform competitive. This said,
there are already a couple of proposals around [^4].

The missing keystone
--------------------

Hosted web applications allow any web site to make itself installable in a
runtime but there is still a major lack that needs to be addressed to make the
manifest a key part of the Web Platform: for the moment, those manifests are not
discoverable. That means that there is no way for a service such as a search
engine to allow you to search installable web applications on the web. There is
also no way for a <abbr title='User Agent'>UA</abbr> to tell you that you can
create a shortcut or "install" (depending on the approach they want to have) the
web site you are visiting.

The main reason why we are moving the manifest specification from SysApps to
WebApps is to make the manifest go beyond packaged or hosted web applications
and have it available to any web site.

First of all, allowing web pages to declare a manifest should solve the problems
mentioned above: the manifests would be discoverable and UA such as web crawlers
could take advantage of this information.

Second, and probably a more controversial benefit is that some declarative
information that doesn't really fit into CSS or HTML could go into this
manifest. For example, we have already seen that a few icons can be specified
there. There is also the ability for a web site to request to be viewed
fullscreen or be in a specific orientation (could be useful for games). A year
ago, the Web Intents specification was trying to find out how to enable
discoverability of Intents handling: using an &lt;intent&gt; element has been
considered a good solution given the other alternatives. Plugging this into the
manifest would very likely have been a good solution for that use case.

Technical details
-----------------

For the moment, we believe that web pages could link a manifest the same way
they currently link the appcache manifest, by simply setting its URL in an
attribute in the HTML element, like:

    <!DOCTYPE html>
    <html foo='manifest.webapp'>
      <!-- ... -->
    </html>

However, this decision hasn't been really made yet and it is [open for
discussions](https://github.com/w3c/manifest/issues/17). We still don't know if
we would like to try to use the _manifest_ attribute and break
retro-compatibility for UA that do not support the new format. For others, JSON
vs AppCache manifest format should be enough to do the righ thing.  
Otherwise, we can use another name like _appmanifest_ but it might send the
wrong message.

Another approach would be to use a &lt;meta&gt; or &lt;link&gt; element. This
approach might be the safest given that the _manifest_ namespace is probably
free so it would be possible to have retro-compatibility with the appcache
manifest. We should decide what should be the behaviour of changing the URL of
the manifest while the page is loaded (or loading) if we take this approach
though.

Finally, the last technical question is about the scope of the manifest. Should
the manifest apply on every web page under the same origin? Should it only apply
to web pages that link to it? I would tend to prefer the former solution mostly
because it will keep us consistent with the way hosted web applications are
specified.

Feedback
--------

Getting feedback from web developers on all of this would be very valuable. If
you read until here and are interested in this, you should read the [manifest
specification](http://www.w3.org/2012/sysapps/manifest/) and look at the [GitHub
repository](https://github.com/w3c/manifest). Feel free to [open a GitHub issue](https://github.com/w3c/manifest/issues/new) or send an email to the [webbapps mailing-list](http://lists.w3.org/Archives/Public/public-webapps/).

[^1]: One of the first iterations being [http://mozilla.github.io/webapps-spec/](http://mozilla.github.io/webapps-spec/).
[^2]: See: [http://lists.w3.org/Archives/Public/public-sysapps/2013May/0122.html](http://lists.w3.org/Archives/Public/public-sysapps/2013May/0122.html) and [http://lists.w3.org/Archives/Public/public-webapps/2013AprJun/0641.html](http://lists.w3.org/Archives/Public/public-webapps/2013AprJun/0641.html).
[^3]: [http://alistapart.com/article/application-cache-is-a-douchebag](http://alistapart.com/article/application-cache-is-a-douchebag)
[^4]: A solution mostly pushed by Google is to use a [NavigationController](https://github.com/slightlyoff/NavigationController). Another solution mostly pushed by Mozilla
is to create a [new appcache format](http://lists.w3.org/Archives/Public/public-webapps/2013JanMar/0977.html).