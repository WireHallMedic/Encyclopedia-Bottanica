# Encyclopedia-Bottanica
A bot for storing text and image files, to be recalled upon command in Discord.

Text files are stored in ./text, and should be formatted in line with the provided examples. In short, any line starting with an @ is interperted as the name (and therefore call for) all text that follows until another name or EoF.

Image files are stored in ./images.

Calling "!contents" or "!toc" will return a list of the files that the bot has access to.
Calling "!<name of text file>" will return a list of topics within that file.
Calling "!<name of topic>" will return the text for that topic.
Calling "!<name of image file>" will return that image file.

File extensions are obfuscated from the user, and not included in the above calls. e.g., call "!example file" rather than "!example file.txt".

Changes to files, including addition/deletion, are picked up upon starting the application. Restart the application after making changes.

This bot uses the old style of interperting commands (ie, not @bot.command()) to avoid having to have an additional word between the bang and the actual command, as commands are not known until runtime.
