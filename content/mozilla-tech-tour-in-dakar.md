Title: Mozilla Tech Tour in Dakar
Date: 2011-05-26 15:11
Tags: mozilla, add-on sdk
Planets: mozilla

During the last week of April, I was part of a team from Mozilla that
was in Dakar for a Mozilla Tech Tour of a few universities. The team was
composed of Claire Corgnou, the volunteer behind [Bonjour Mozilla](http://bonjourmozilla.fr/),
Vivien Nicolas, who works on Firefox Mobile front-end, [Anthony
Ricaud](http://hanblog.info), web developer on mozilla.com and [William Quiviger](http://somethin-else.org/), who
works for the User Engagement team.

For the week that we were in Dakar, we gave speeches in universities
about Mozilla, who we are, what we stand for and how to contribute.
Claire, as a member of [WoMoz](http://womoz.org), gave a talk about the project. We also
conducted two technical workshops: one about HTML5/CSS3 and one about
the Add-on SDK. During these speeches and workshops, we had the chance
to meet students from Epitech Senegal,
<acronym title="École supérieure de technologie et de management de dakar">ESTM</acronym>,
<acronym title="École supérieure multinationale de télécommunication">ESMT</acronym>
and
<acronym title="Institut supérieur d'informatique">ISI</acronym>.

Our Mission
-----------

If we went to Dakar it's mostly thanks to [Mouhamadou Moustapha
Camara](https://twitter.com/mmkmou) who put a lot of energy to have us come. When we arrived, he
had planned everything, he was accompanying us everywhere and was doing
his best to make sure everything went smoothly. But we should also thank
William who really wants Mozilla to strengthen its community in Africa.
Actually, Senegal is a very good place to begin with [^1]: it is
the leading country of West Africa in term of new technologies.

Our goal was to strengthen the Mozilla community in Senegal. For what we
saw, in universities, student are really aware of FLOSS and the
exceptional power it could have in Africa. They were really open-minded
and had a real thirst for knowledge. However, even if they have a full
access to information, the conditions in Dakar are really different from
the ones we are used to. In Dakar, the power is very unstable and you
can spend hours without power [^2], the Internet connection isn't
really fast even if it's one of the best of the region. These are two
concrete issues and might be fixed soon.  
Another issue is cultural and might take longer to fix. For what we saw
students' English is very often weak and most of them had a hard time
reading the Add-on SDK documentation. This is unfortunate because most
of the technical documentation is in English. This is also a reminder
that part of Mozilla's mission is to promote the free flow of ideas and
information on the Internet and that implies localizing the information.
So, we should translate the documentation of the Add-on SDK.

From now on, Camara is going to lead the Mozilla Senegal community. That
means bringing people together who share Mozilla's vision and having
them work together on different projects. In Senegal, people mostly
speak French and [Wolof](https://secure.wikimedia.org/wikipedia/en/wiki/Wolof_language) and one project that seems to create a lot of
excitement is to translate Firefox to Wolof. That would be amazing to
have this done.

The Add-on SDK workshop
-----------------------

Vivien and I led a few Add-on SDK workshops. It probably was as
instructive for us as for the students. First of all none of us was an
Add-on SDK hacker before and we only chose to show this because it's a
very good first technical step into the Mozilla technologies. In
addition, it helped us to find some issues with how the Add-on SDK
currently works. Vivien has to write a blog post about this but, in a
nutshell, most students where using Windows and the Add-on SDK requires
Python which is a pain to install in a Windows environment. The user is
also required to use the command line and Windows users are usually not
used to it. During the workshops we gave a quick course of Javascript
then, we tried to show how to write a very simple extension. If time
permitted, the students were able to write their own extensions and we
tried to help them.  
As I mentioned above, the idea behind showing how the Add-on SDK works
was to help the students do the first step into the Mozilla
technologies. One of our constraints was that the attendees were from
freshmen to senior students and digging into mozilla-central code base
or classic extensions might have been a bit frightening for the
youngest. Being able to have a working extension made by themselves was
also one of the goals: a lesson is much more motivating if you are able
to produce something at the end of the day. Our hope was to motivate a
few of them to write their own extensions after the workshop; and we
know a few of them did.

I wrote two extensions for these workshops. The first of them is a
simple URL shortener extension using TinyURL and is available [here](https://gitorious.org/url-shortener/url-shortener).
I like this extension because it contains around 15 lines, it does
something really useful, uses three different modules and is simple
enough to understand it while reading it.  
The second extension is probably less simple if you don't have enough
HTML/CSS knowledge: it's an extension that allows the user to edit an
image in a web page. I actually wrote it quickly (so it's not finished,
patches accepted) while I thought I would not have an Internet
connection to present the first extension. I should actually improve it
a bit to be able to use Firefox as an image viewer/editing tool. It is
available [here](https://gitorious.org/image-editor/image-editor).

Conclusion
----------

The Tech Tour was concluded by an afternoon at the [AUF](http://www.auf.org/) who hosted a
workshop, an install party and a few talks. The same evening we had an
amazing Firefox 4 release party.  
The day before leaving, we met the authorities in a meeting organized by
[Jokkolabs](http://jokkolabs.net/). During this meeting, we talked about how the open source
and hybrid companies like Mozilla can be an economical model that might
fit Senegal's needs, and more generally, African's ones. You can't
completely change the mind of anyone in a couple of hours but I hope
that, at our scale, we have been able to help them understand there are
alternatives and these alternatives might be better for everyone.

Finally, I believe that what we did during this week is exactly what the
Mozilla Manifesto is about and I really hope we will be able to do it
again in the future!

You can found pictures of the Tech Tour on Flickr: [http://www.flickr.com/groups/mozillasn/](http://www.flickr.com/groups/mozillasn/)

[^1]: It's not exactly the first Mozilla tour in Africa but one of the first.
[^2]: This actually leads to an intolerable contrast between rich citizens who
can afford a generator and others who can't.
