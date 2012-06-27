#!/bin/sh
# Setting up the sync with tds file-storage

# Asking user for login&password
echo "Enter your login: "
read login
echo "Enter your password: "
read password

# Saving password to file
echo $password > $HOME/.rsyncpass
# Setup sasafity permission to the file with password
chmod 640 $HOME/.rsyncpass

# Getting path to sync-folder
folder=$1

# Creating file with exclude rules
echo ".*" > $HOME/.rsyncexclude

# Getting absolute path to rsync-command
rsync=`whereis rsync`

# First sync
echo "First syncronization. Please wait..."
$rsync --update --progress --times --exclude-from $HOME/.rsyncexclude --recursive --stats --password-file=$HOME/.rsyncpass $folder/ rsync://$login@tech.tdigitals.ru/dropbox/

# Creating crontab-file
echo "MAILTO=\"\"
*/3 * * * * if [ \`ps x | grep -v grep | grep rsync | wc -l\` -eq 0 ]; then $rsync --update --times --delete --exclude-from $HOME/.rsyncexclude --recursive --stats --password-file=$HOME/.rsyncpass rsync://$login@tech.tdigitals.ru/dropbox/ $folder/ && $rsync --update --times --exclude-from $HOME/.rsyncexclude --recursive --stats --password-file=$HOME/.rsyncpass $folder/ rsync://$login@tech.tdigitals.ru/dropbox/;else echo \"syncing is in process\";fi" > $HOME/crontab
# And adding crontasks
crontab $HOME/crontab && rm $HOME/crontab

echo "That's all!"