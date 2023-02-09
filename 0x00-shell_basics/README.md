pwd => Displays current working directory.
ls => Display the contents list of your current directory.
cd ~ => changes the working directory to the user’s home directory.
ls -l => Display current directory contents in a long format.
ls -a => Display current directory contents, including hidden files (starting with .). Use the long format.
ls -la => Display current directory contents. i) Long format, ii) with user and group IDs displayed numerically, iii) And hidden files (starting with .)
mkdir /tmp/my_first_directore => Create a script that creates a directory named my_first_directory in the /tmp/ directory.
mv betty /tmp/my_first_directory/ => Move the file betty from /tmp/ to /tmp/my_first_directory.
rm /tmp/my_first_directory/betty => Delete the file betty. The file betty is in /tmp/my_first_directory.
rm -r /tmp/my_first_directory => Delete the directory my_first_directory that is in the /tmp directory.
cd .. => Write a script that changes the working directory to the previous one.
ls -la . .. /boot => Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the 
current directory and th  parent of the working directory and the /boot directory (in this order), in long format.
file iamafile => Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your   script.
ln -s /bin/ls => Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
cp -u *.html .. => Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only    copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. You can        consider that all HTML files have the extension .html
