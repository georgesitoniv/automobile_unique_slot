import  { createNetworkInterface } from "apollo-client";

const networkInterface = createNetworkInterface({
  uri: 'http://localhost:8000/graphql/',
  opts:{
    credentials: 'include',
  },
});

networkInterface.use([{
  applyMiddleware(req, next) {
    if (!req.options.headers) {
      req.options.headers = {};
    }
    req.options.headers['x-csrftoken'] = getCookie('csrftoken');
    next();
  }
}]);

function getCookie(name) {
  var cookies = getCookies();
	return cookies[name];
}

function getCookies() {
  var cookies = {};
	for (let cookie of document.cookie.split('; ')) {
		let [name, value] = cookie.split("=");
		cookies[name] = decodeURIComponent(value);
	}
	return cookies;
}

export default networkInterface;
