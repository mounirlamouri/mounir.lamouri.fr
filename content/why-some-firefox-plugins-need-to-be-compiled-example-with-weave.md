Title: Why some Firefox plugins need to be compiled, example with Weave
Date: 2009-11-25 21:56
Tags: firefox, gentoo, mozilla, weave
Planets: mozilla

Gentoo let the user installing a few Firefox and Thunderbird plugins via
the package manager and people often consider it is useless. Actually,
there are at least two reasons why it can be useful.  
The first one is obvious : when installing a plugin with the package
manager, you are sure it will be available for every users (except if it
is manually disabled by the user). For example, you can install
[noscript](http://noscript.net/) for security reasons directly by enabling
*restrict-javascript* USE flag.  
The other reason is the compilation. Indeed, most plugins are
platform-independent but some of them are not and those ones are not
guarantee to work on your computer. For example, you can install Firefox
on a lot of different platforms. If you stay with GNU/Linux, you can
install Firefox 3.5 on alpha, amd64 (x86-64), arm, hppa, ia64, ppc,
ppc64, x86 [^1]. This is true at least with Gentoo. It goes without
saying if a plugin has a platform-dependent part, it will not provide a
binary for all these platforms.

Concretely, I tried to install [Weave](https://mozillalabs.com/weave/) 1.0 beta 1 and 2 from
[addons.mozilla.org](https://addons.mozilla.org/en-US/firefox/addon/10868). When launching Firefox, I got this output in the
Weave Activity Log view:

    2009-11-25 12:34:02     Service.Main         INFO      Loading Weave 1.0b2 in 5 sec.
    2009-11-25 12:34:08     Engine.Bookmarks     DEBUG     Engine initialized
    2009-11-25 12:34:09     Engine.Forms         DEBUG     Engine initialized
    2009-11-25 12:34:10     Engine.History       DEBUG     Engine initialized
    2009-11-25 12:34:10     Engine.Passwords     DEBUG     Engine initialized
    2009-11-25 12:34:10     Engine.Prefs         DEBUG     Engine initialized
    2009-11-25 12:34:10     TabTracker           DEBUG     Failed to load json: this.changedIDs is undefined JS Stack trace: ([object Object])@trackers.js:125 < Utils_jsonLoad("weave/changes/tab_tracker.json",[object Object],(function (json) {for (let id in json) {this.changedIDs[id] = 1;}}))@util.js:559 < T_loadChangedIDs()@trackers.js:123 < T__init()@trackers.js:76 < TabTracker__init()@tabs.js:356 < TabTracker()@tabs.js:345 < ()@engines.js:161 < Engine__init()@engines.js:179 < _init()@engines.js:303 < TabEngine()@tabs.js:56 < EngMgr_register(TabEngine,5,[object Array])@engines.js:113 < EngMgr_register([object Array])@engines.js:106 < WeaveSvc__registerEngines()@service.js:379 < _onStartup([object Object])@service.js:278 < notify([object XPCWrappedNative_NoHelper])@util.js:624
    2009-11-25 12:34:11     Engine.Tabs          DEBUG     Engine initialized
    2009-11-25 12:34:11     Service.Main         INFO      Resetting client syncID from _onStartup.
    2009-11-25 12:34:11     Service.Main         INFO      Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9.1.4) Gecko/20091109 Gentoo Firefox/3.5.4
    2009-11-25 12:34:11     Service.Util         WARN      Component @labs.mozilla.com/Weave/Crypto;1 requested, but doesn't exist on this platform.
    2009-11-25 12:34:11     Service.Main         DEBUG     Crypto check failed: TypeError: Svc.Crypto is null
    2009-11-25 12:34:11     Service.Main         ERROR     Could not load the Weave crypto component. Disabling Weave, since it will not work correctly.
    2009-11-25 12:34:11     Service.Main         INFO      Weave Sync disabled

If you unzip the xpi file, you will found a *platform/* directory which
is containing platform-dependent files. If we stay with GNU/Linux, we
have *Linux/*, *Linux_x86_64-gcc3/* and *Linux_x86-gcc3/*
directories. If we launch *'file
platform/Linux/components/WeaveCrypto.so*', we got:

    platform/Linux/components/WeaveCrypto.so: ELF 32-bit LSB shared object, ARM, version 1 (SYSV), dynamically linked, not stripped

So, x86, x86-64 and arm are supported, not surprising. But my old
Powerbook G4 (PowerPC) is not. Actually, it would be if I was using
MacOS X instead of GNU/Linux.

I don't know if addons.mozilla.org should specify the supported
platforms for platform-dependent plugins because arm, x86 and x86-64 are
covering most of the target systems. Actually, as far as I know PowerPC
is fully supported only by Gentoo and Debian. Anyway, if you are using
an unconventional platform, you may want to compile your own weave
plugin and probably a few others.

Luckily, weave has just been updated to 1.0b2 in the Gentoo tree :)

[^1]: mips is working with Firefox 2.0.0.19 and sparc with Firefox 3.0.11
