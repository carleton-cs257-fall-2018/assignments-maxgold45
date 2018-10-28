function dropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}



initialize();

function initialize() {
    var element = document.getElementById('top_ten_button');
    if (element) {
        element.onclick = onTopTenButtonClicked;
    }
}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    return baseURL;
}

function onTopTenButtonClicked() {
    var url = getBaseURL() + '/movies/toptentitles';

    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(moviesList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < moviesList.length; k++) {
            tableBody += '<tr>';

            tableBody += '<td><a onclick="getMovie(' + moviesList[k]['id'] + ")\">"
                            + moviesList[k]['title'] + ', '
                            + moviesList[k]['release_date'] + '</a></td>';

            tableBody += '</tr>';
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function getMovie(movieID) {
    var url = getBaseURL() + '/movie/' + movieID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movieInfo) {
        var title = '<table><tr><th class="titleSize">' + movieInfo['title'] + ' (' + movieInfo['release_date'] + ')</th></tr>';
        title += '<tr><th>' + movieInfo['tagline'] + '</th></tr>';
        title += '<tr><td>' + movieInfo['overview'] + '</td></tr></table>';
        
        var tableBody = '<table><tr><th>' + "Movie Details" + '</th></tr>';
        tableBody += '<tr><td>' + "Revenue:" + '</td><td>$' +  movieInfo['revenue'] + '</td></tr>';
        tableBody += '<tr><td>' +  "Budget:" + '</td><td>$' + movieInfo['budget']   + '</td></tr>';
        tableBody += '<tr><td>' + "Language:"+ '</td><td>'  + movieInfo['language_code'] + '</td></tr>';
        tableBody += '<tr><td>' + "Runtime:" + '</td><td>'  + movieInfo['runtime']  + " minutes" + '</td></tr>';
        tableBody += '</table>';

        var resultsTableElement1 = document.getElementById('movie_title');
        var resultsTableElement2 = document.getElementById('movie_table');
        if (resultsTableElement1) {
            resultsTableElement1.innerHTML = title;
        }
        if (resultsTableElement2) {
            resultsTableElement2.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}
