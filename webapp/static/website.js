/*
 * Max Goldberg and Alexis Engel
 * Javascript for Cinehub webapp
 */

initialize();

function initialize() {
    /* Initalizes the two search buttons, if not null.
     */

    var topTenButt = document.getElementById('top_ten_button');
    var searchButt = document.getElementById('search_button');
    if (topTenButt) {
        topTenButt.onclick = onTopTenButtonClicked;
    }
    if (searchButt) {
        searchButt.onclick = onSearchButtonClicked;
    }
}

function getBaseURL() {
    return window.location.protocol + '//' + window.location.hostname + ':' + api_port;
}

function onTopTenButtonClicked() {
    /* Displays on the page the top ten movies in the database along the left
     * hand column.
     */

    var url = getBaseURL() + '/movies/toptentitles';

    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(moviesList) {
        movieResultList(moviesList);
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function onSearchButtonClicked() {
    /* Dispalys on the page the search results along the left hand column.
     * The search results are narrowed down by the three dropdown menus.
     */

    var searchTerm = document.getElementById("searchTerm").value;

    var topic = document.getElementById("topicDrop");
    topic = topic.options[topic.selectedIndex].value;

    var sortBy = document.getElementById("sortByDrop");
    sortBy = sortBy.options[sortBy.selectedIndex].value;

    var sortOrder = document.getElementById("sortOrderDrop");
    sortOrder = sortOrder.options[sortOrder.selectedIndex].value;

    if (topic == "movies"){
        var url = getBaseURL() + '/movies/' + searchTerm + '?sort=' + sortBy + "&asc=" + sortOrder;
        fetch(url, {method: 'get'})
        .then((response) => response.json())
        .then(function(moviesList) {
            movieResultList(moviesList);
        })
        .catch(function(error) {
            console.log(error);
        });
    } 
    else if (topic == "actors") {
        var url = getBaseURL() + '/actors/' + searchTerm;
        fetch(url, {method: 'get'})
        .then((response) => response.json())
        .then(function(actorsList) {
            actorsResultList(actorsList);
        })
        .catch(function(error) {
            console.log(error);
        });
    }
    else { // Topic == director, producer, or writer.
        var url = getBaseURL() + '/crew/' + searchTerm + '/' + topic;
        fetch(url, {method: 'get'})
        .then((response) => response.json())
        .then(function(crewList) {
            crewResultList(crewList);
        })
        .catch(function(error) {
            console.log(error);
        });
    }
}

function movieResultList(moviesList) {
    /* Displays the list of movies given the JSON moviesList. Also, provides
     * links to display more details about a single movie.
     */
    var tableBody = '';
    for (var k = 0; k < moviesList.length; k++) {
        tableBody += '<tr>';
        tableBody += '<td><a onclick="getMovie(' + moviesList[k]['id'] + ")\">" + moviesList[k]['title'] + ', '
                    + moviesList[k]['release_date'] + '</a></td>';
        tableBody += '</tr>';
    }

    // Put the table body we just built inside the table that's already on the document.
    var resultsTableElement = document.getElementById('results_table');
    if (resultsTableElement) {
        resultsTableElement.innerHTML = tableBody;
    }
}

function getMovie(movieID) {
    /* Displays detailed information about a single movie.
     */

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

        // Display the above HTML in the document.
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

function actorsResultList(actorsList) {
    /* Displays all of the actors matching the search parameters.
     */

    var tableBody = '';
    for (var k = 0; k < actorsList.length; k++) {
        tableBody += '<tr>';
        tableBody += '<td><a onclick="getActor(' + actorsList[k]['id'] + ")\">" + actorsList[k]['name'] + '</a></td>';
        tableBody += '</tr>';
    }

    // Put the table body we just built inside the table that's already on the document.
    var resultsTableElement = document.getElementById('results_table');
    if (resultsTableElement) {
        resultsTableElement.innerHTML = tableBody;
    }
}

function getActor(actorID) {
    /* Displays all of the movies that an actor is in..
     */

    var url = getBaseURL() + '/actor/' + actorID;
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(characterList) {
        var title = '<table><tr><th class="titleSize">' + characterList[0]['name'] +
                    '</th></tr></table>';

        var tableBody = "";
        for (var k = 0; k < characterList.length; k++) {
            tableBody += '<tr>';
            tableBody += '<td><a class="link" onclick="getMovie(' + characterList[k]['movie_id'] + ")\">"
                            + characterList[k]['title'] + ': '
                            + characterList[k]['character_name'] + '</a></td>';
            tableBody += '</tr>';
        }

        // Put the table body we just built inside the table that's already on the document.
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

function crewResultList(crewList){
    /* Displays the crew list matching the search parameters.
     */

    var tableBody = '';
    for (var k = 0; k < crewList.length; k++) {
        tableBody += '<tr>';

        tableBody += '<td><a onclick="getCrew(' + crewList[k]['id'] + ")\">"
                  + crewList[k]['name'] + '</a></td>';

        tableBody += '</tr>';
    }

    // Put the table body we just built inside the table that's already on the document.
    var resultsTableElement = document.getElementById('results_table');
    if (resultsTableElement) {
        resultsTableElement.innerHTML = tableBody;
    }

}

function getCrew(crewID) {
    /* Displays all of the movies a single crew member is in.
     */

    var url = getBaseURL() + '/crew/' + crewID;
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(movieList) {
        var title = '<table><tr><th class="titleSize">' + movieList[0]['name'] +
                    '</th></tr></table>';

        var tableBody = "";
        for (var k = 0; k < movieList.length; k++) {
            tableBody += '<tr>';
            tableBody += '<td><a class="link" onclick="getMovie(' + movieList[k]['movie_id'] + ")\">"
                            + movieList[k]['title'] + ': '
                            + movieList[k]['job'] + '</a></td>';
            tableBody += '</tr>';
        }

        // Put the table body we just built inside the table that's already on the document.
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

