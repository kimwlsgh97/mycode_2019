var request = require('request'),
    cheerio = require('cheerio');

var url = "https://www.youtube.com";

request(url, function (err, res, html){
  if (!err){
    var $ = cheerio.load(html);
  }
})
