(function (window) {
  var container = {};
  function getJsonFromUrl() {
    var url = location.search;
    var query = url.substr(1);
    var result = {};
    query.split('&').forEach(function (part) {
      var item = part.split('=');
      result[item[0]] = decodeURIComponent(item[1]);
    });
    return result;
  }

  function zeppelin(accountId) {
    container.accountId = accountId;

    var storedAccountId = localStorage.getItem('accountId');
    if (storedAccountId) {
      return;
    }

    var params = getJsonFromUrl();
    if (params['utm_source']) {
      localStorage.setItem('source', params['utm_source']);
    }
    if (params['utm_medium']) {
      localStorage.setItem('medium', params['utm_medium']);
    }
    if (params['utm_campaign']) {
      localStorage.setItem('campaign', params['utm_campaign']);
    }
    if (params['utm_content']) {
      localStorage.setItem('content', params['utm_content']);
    }
    localStorage.setItem('accountId', accountId);
  }

  window.zeppelin = zeppelin;
})(window);
