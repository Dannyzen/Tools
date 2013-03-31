#mover.sh
#Built to move files and/or directories containing files from a 'stage' directory to a network folder as well as ensuring a local backup
d=`date +%m-%d-%H_%M_%S`
mkdir $d
#back it up first
echo "->backing up"
rsync -av --exclude $d --exclude 'mover.sh'  * ../music/ 
#copy it to the new date
echo "->copying to date folder" 
rsync -av --exclude $d --exclude 'mover.sh' * $d 
#rename anything with a space, and move it to the right place
echo "->renaming in the case there are spaces"
rename 's/ /_/g' *
shopt -s extglob 
echo !(mover.sh|$d) | xargs rm -rv .
#shuttle that folder to the nas and if it has an exit of 0 rm that folder
echo "->shuttling to nas"
rsync -av $d danzen@net:/c/media/Music && rm -rf $d 
