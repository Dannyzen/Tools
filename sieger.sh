function blast {                                                                                                           xbmc@zot
siege -b -c 1 -d 0 -r $1 http://qa3-horizon.dannyrosen.net/horizon/track\?url\=http://www.google.com && siege -b -c 1 -d 0 -r $1 http://qa3-horizon.dannyrosen.net/horizon/track\?url\=http://www.google.com && siege -b -c 1 -d 0 -r $1 http://qa3-horizon.dannyrosen.net/horizon/track\?url\=http://www.google.com
}
