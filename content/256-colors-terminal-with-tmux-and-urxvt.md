Title: 256 colors terminal with tmux and urxvt
Date: 2010-03-21 11:39
Tags: gentoo, tmux, urxvt

A few days ago, I was trying to change my vim theme for a 256-color one
and I realized urxvt was not supporting 256 colors out of the box.
Hopefully, there is a patch to get a 256 colors terminal with urxvt. It
is available in the the Gentoo package, you just have to enable the
*xterm-color* USE flag for rxvt-unicode like this:

    echo "x11-terms/rxvt-unicode xterm-color >> /etc/portage/package.use

If you recompile rxvt-unicode, you should now get more colors. You can
test it by using a 256-color vim theme like [desert256](http://www.vim.org/scripts/script.php?script_id=1243) [^1]. You
can also run:

    tput colors

I got 88 instead of 256. I don't know why but it's still a lot better
than 16 colors.

Now, you have to make sure tmux is using 256 colors otherwise you will
get a weird behavior. According to the [tmux FAQ](http://tmux.cvs.sourceforge.net/viewvc/*checkout*/tmux/tmux/FAQ), it is really easy
and you have to add a this line in *~/.tmux.conf*:

    set -g default-terminal "screen-256color"

In my system it was not working so I have to tell tmux my terminal
supports 256 colors by using '-2' argument. You can add this line to
your *~/.bashrc* to always call tmux with '-2':

    alias tmux="tmux -2"

Now, if you run *`tput colors`* in a tmux session, you should get 256.

If you are using vim, you should add this line to you *~/.vimrc*:

    set t_Co=256

Hope this is helping !

[^1]: To compare themes, you can try [http://code.google.com/p/vimcolorschemetest/](http://code.google.com/p/vimcolorschemetest/)
