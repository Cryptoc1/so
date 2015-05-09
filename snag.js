// basically just grab the user's request
// then parse it into json so we can cool do shit with it

// require packages!! alright
var http = require("http");

// do shit with title, like uh mainly getting info!!!! B)
function get(title) {
	// base url
	var base = 'http://omdbapi.com/'

	// connect to the api
	var request = http.get(base + '?t=' + title, function(response) {
		var body = "";

		// read and assign data
		response.on('data', function(chunk) {
			body += chunk;
		});

		// parse data once it's done
		response.on('end', function() {
			if (response.statusCode === 200) {
				try {
					var movie = JSON.parse(body);
					console.log(movie);
				} catch(error) {
					console.error("Error: Couldn't parse JSON? " + error);
				}
			} else {
				console.error("Error: Couldn't snag info for " + title + " :/");
			}
		});

	});

	request.on('error', function() {
		console.error("Error: Connection failed :/");
	})

}

module.exports.get = get;