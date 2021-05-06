import * as mongodb from 'mongodb';

# "GET" Request via Ajax in JScript to foods database
const Http = new XMLHttpRequest();
const url='https://api.nal.usda.gov/fdc/v1/foods/list?api_key=DEMO_KEY';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}

 Mongo mongo = new Mongo("127.0.0.1",27017);
 		DB db = mongo.getDB("foods_info");
 		DBCollection collection = db.getCollection("foods");
 		DBCursor csr = collection.find();
 		for (DBObject dbObject : csr) {
			System.out.println(dbObject);
 		}
 		WriteResult save = collection.save(new BasicDBObject() {{
 			this.append("user", 333);
 		}});
 		save = collection.save(new BasicDBObject() {{
 			this.append("user", "regine");
 		}});
 		System.out.println(save.toString());
 		WSRequest url = play.libs.WS.url("https://api.nal.usda.gov/fdc/v1/foods/list?api_key=DEMO_KEY");
 		final HttpResponse httpResponse = url.get();
 		System.out.println(httpResponse.getString());
 		final Object parse = JSON.parse(httpResponse.getString().replaceAll("\\.", "_"));
	
 		collection.save((DBObject) parse);

# GET data from Farmers Market API with Ajax: TODO: $ not defined error
#  function getResults(zip) {
#      // or
#      // function getResults(lat, lng) {
#      $.ajax({
#          type: "GET",
#          contentType: "application/json; charset=utf-8",
#          // submit a get request to the restful service zipSearch or locSearch.
#          url: "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=" + zip,
#          // or
#          // url: "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/locSearch?lat=" + lat + "&lng=" + lng,
#          dataType: 'jsonp',
#          jsonpCallback: 'searchResultsHandler'
#      });
#  }
#  # iterate through the JSON result object.
# function searchResultsHandler(searchResults) {
#      for (var key in searchresults) {
#          alert(key);
#          var results = searchresults[key];
#          for (var i = 0; i < results.length; i++) {
#              var result = results[i];
#              for (var key in result) {
#                  //only do an alert on the first search result
#                  if (i == 0) {
#                      alert(result[key]);
#                  }
#              }
#          }
#      }
#  }

#  getResults(19348)