const FRONTEND_URL = "http://www.pdp-adapting.com:80";
const DONE = 4;
const SUCCESS = 200;


/**
 * Create the awesome object that lets you update the page without refreshing
 */
function createXmlHttpRequestObject()
{
    let xmlHttp;

    try {
        //If Internet Explorer is used
        if (window.ActiveXObject) {
            xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        //If any other *modern* browser is used
        else {
            xmlHttp = new XMLHttpRequest(); //built-in function
            console.debug(xmlHttp.readyState);
        }
        return xmlHttp;
    } catch (e) {
        alert("Can't create the xmlHttp object.");
    }
}


function fetchData(URL) {
    let xmlHttp = createXmlHttpRequestObject();
    xmlHttp.open("GET", URL, false);
    xmlHttp.send(null);

    if (xmlHttp.readyState === DONE && xmlHttp.status === SUCCESS) {
        return xmlHttp;
    }
}


function updateVotes() {

    let data;
    let lines;

    // Update votes
    data = fetchData(FRONTEND_URL + "/vote_count_ajax_all/");
    lines = data.responseText.split("\n");

    for (let i = 0; i < lines.length; i++) {
        id = lines[i].split(" ")[0];
        votes = lines[i].split(" ")[1];
	elem =  document.getElementById("ajaxId" + id);
	if (typeof elem !== "undefined" && elem !== null) {
            elem.textContent = votes;
        }
    }
}
