
export PATH=$PATH:/Users/danny/pear/bin
#if [ -f `brew --prefix`/etc/bash_completion.d/git-completion.bash  ]; then
#  . `brew --prefix`/etc/bash_completion.d/git-completion.bash 
#  fi
#GIT_PS1_SHOWDIRTYSTATE=true

# Cron Operations
#job process saves entries
alias jobprocess='php ~/sailthru/www/queues/job.php --debug --host http://sailthru-sb.com'
#transactional
alias mailprocess='php ~/sailthru/www/queues/send.php --debug --host http://sailthru-sb.com'

#campaigns
alias blastmail='php ~/sailthru/www/queues/blast.php --debug --host http://sailthru-sb.com'
alias blastgen='php ~/sailthru/www/crons/blast_generate.php --debug --host sailthru-sb.com'
alias send='blastgen && blastmail'

alias mplp='php ~/sailthru/www/queues/send.php --debug --host http://sailthru-sb.com --name send_lp'
alias eventprocess='php ~/sailthru/www/queues/event.php --debug --host http://sailthru-sb.com'
#to count
alias countprocess='php ~/sailthru/www/queues/count.php --debug --host http://sailthru-sb.com'
alias alert='php ~/sailthru/www/queues/alert_realtime.php --debug --host http://sailthru-sb.com'


# Handy Aliases
alias mail="python /Users/danny/test.py"
alias la="ls -la"
alias lrt="la -lrt"
alias deploy_mailer="php ~/deploy/deploy-jar.php mailer qa"
alias ap="sudo apachectl graceful"
alias ms="mongo sailthru"
alias gate="ssh sailthru@ec2-184-72-234-254.compute-1.amazonaws.com";
alias simport="cd ~; scp sailthru@184.72.234.254:/tmp/dump.tgz .; tar xvfz dump.tgz; php ~/sailthru/www/scripts/sandbox_import.php --host sailthru-sb.com --directory /Users/danny/tmp/dump --debug; rm -rf /Users/danny/tmp;"
alias simportdev="cd ~; scp sailthru@184.72.234.254:/tmp/dump.tgz .; tar xvfz dump.tgz; php ~/sailthru/www/scripts/sandbox_import.php --host sailthru-dev.com --directory /Users/danny/tmp/dump --debug; rm -rf /Users/danny/tmp;"
alias sbp='source ~/.bash_profile'
alias vbp='vim ~/.bash_aliases'
alias cmd='cat ~/.bash_aliases'
alias sdep="ssh sailthru@ec2-184-72-234-254.compute-1.amazonaws.com 'php deploy/deploy-web.php danny $1 $2'"
alias mvim='mvim $1'
alias simport="cd ~; scp sailthru@184.72.234.254:/tmp/dump.tgz .; tar xvfz dump.tgz; php ~/sailthru/www/scripts/sandbox_import.php --host sailthru-sb.com --directory /Users/danny/tmp/dump --debug; rm -rf /Users/vaibhav/tmp; cd /Users/danny/Sailthru;"
alias pull='git pull origin'
alias master='git checkout master'
alias develop='git checkout develop'
alias s='cd ~/sailthru'
alias vi='vim'

alias branch='git checkout -b $1'
#startup
alias sshdanny='ssh sovolo@64.22.112.181 -p21098'
alias mc='memcached'
alias db='mongod' 
alias jm='java -jar /Users/danny/dev/mailer/dist/SailthruMailer.jar ~/sailthru/java/mailer/config/sandbox.properties'
#mailprocess push any email over to /tmp/email.txt
#eventprocess
#jobprocess
#countprocess
#/Users/danny/mailer/deploy/mailer/dist/sailthru-mailer.jar
alias mailer_deploy='cp -R /Users/danny/mailer/dist/lib /Users/danny/mailer/deploy/mailer/dist && cp /Users/danny/mailer/dist/sailthru-mailer.jar /Users/danny/mailer/deploy/mailer/dist && php /Users/danny/mailer/deploy/deploy-jar.php mailer qa'
alias deploy_mailer='php ~/deploy/deploy-jar.php mailer qa'
#run proc remotely
alias go="ssh sailthru@ec2-184-72-234-254.compute-1.amazonaws.com \"ssh ec2-east-qa-env1 'php /sailthru/www/queues/proc.php --debug --host sailthru-qa.com'\""
alias again="ssh sailthru@ec2-184-72-234-254.compute-1.amazonaws.com \"ssh ec2-east-qa-env1 'sudo /etc/init.d/memcached restart && sudo /usr/sbin/apachectl graceful'\""

alias push='$HOME/copy.sh'
alias s="cd /home/sailthru/sailthru/"
alias sdep="ssh sailthru@ec2-184-72-234-254.compute-1.amazonaws.com 'php deploy/deploy-web.php danny $1'"
alias gate="ssh sailthru@ec2-184-72-234-254.compute-1.amazonaws.com"
