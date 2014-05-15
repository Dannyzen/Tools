var github = require('octonode');
var client = github.client('');
var inspect = require('util').inspect;

client.get('/orgs/sailthru/members', {per_page:100}, function (err, status, body, headers) {
        console.log('Sort!');
        
        body.sort(function (a,b) { return a.login.toLowerCase() > b.login.toLowerCase() ?1 :-1 ; });
        
        for(var i = 0; i < body.length; i++){
            console.log(body[i].login);
        }
    }
);
