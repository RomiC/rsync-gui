#!/bin/sh
# Setting up the sync with tds file-storage

# Usage message
usage() {
	cat << EOF

usage: $0 [options] folder_to_sync

$0 setup crontab task for syncing with TDS-dropbox via rsync

OPTIONS:
  -u	Login (would be promted, if not given)
  -p	Password (would be promted, if not given)
  -h	Print this message

EOF
}

# Parsing input parametrs
login=
password=

while getopts "u:p:h" opt; do
case $opt in
	u)
		login=$OPTARG
		;;
	p)
		password=$OPTARG
		;;
	h)
		usage
		exit 0
		;;
	?)
		usage
		exit 1
		;;
esac
done

# Getting last parametr – path to folder to sync
shift $((OPTIND-1))
folder=$@

# Checking if folder to sync is given
if [ -z $folder ]
then
	echo "ERROR >>> folder_to_sync is undefined!"
	usage
	exit 1
fi

# Asking user for login&password if they not given
if [ -z $login ]
then
	echo "Enter your login: "
	read login
fi

if [ -z $password ]
then
	echo "Enter your password: "
	read password
fi

# Saving password to file
echo $password > $HOME/.rsyncpass
# Setup sasafity permission to the file with password
chmod 640 $HOME/.rsyncpass

# Creating file with exclude rules
echo ".*" > $HOME/.rsyncexclude

# Getting absolute path to rsync-command
rsync=`whereis rsync`

# First sync
echo "First sync. Please wait..."
$rsync --update --progress --times --exclude-from $HOME/.rsyncexclude --recursive --stats --password-file=$HOME/.rsyncpass rsync://$login@tech.tdigitals.ru/dropbox/ $folder/

# Creating crontab-file
echo "MAILTO=\"\"
*/3 * * * * if [ \`ps x | grep -v grep | grep rsync | wc -l\` -eq 0 ]; then $rsync --delete --update --times --exclude-from $HOME/.rsyncexclude --recursive --stats --password-file=$HOME/.rsyncpass $folder/ rsync://$login@tech.tdigitals.ru/dropbox/ && $rsync --update --times --delete --exclude-from $HOME/.rsyncexclude --recursive --stats --password-file=$HOME/.rsyncpass rsync://$login@tech.tdigitals.ru/dropbox/ $folder/;else echo \"syncing is in process\";fi" > $HOME/crontab
# And adding crontasks
crontab $HOME/crontab && rm $HOME/crontab

echo "That's all!"