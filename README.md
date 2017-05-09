# songtransfer

The purpose of this script is to take a txt file of paths to songs and move
all of the files to a single directory.

A little bit of background.

Before Spotify, millenials everywhere downloaded music through nefarious and
questionable means such as Napster, Kazaa, and Limewire. But where and how were
these stored? Personally, I partitioned my downloads about monthly, and kept
each monthly directory in a parent annual directory. Much of the music is
garbage though, but there are also quality gems in some of those folders, and I
wanted to move all of these 'good' ones to a single folder instead of have it
spread out through many.

So before using this script, first generate a list of all the paths to all the
songs (mp3s/m4as/wavs/etc). On a UNIX system, this can be done by recursively
grepping and outputting to a txt file. Next, delete all songs that you aren't
interested in moving to the separate directory. This was 8500 songs for me, so
it can take some time...but a whole lot less than manually moving each.

Finally, move this script AND the .txt to the directory if the paths in the txt
are relative, and run it in the terminal. I realize you can probably achieve the
same thing all in the terminal, but I've done some basic file moving in Python
so just stuck with that.
