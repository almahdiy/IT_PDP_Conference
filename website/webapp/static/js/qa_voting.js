const FRONTEND_URL = "http://127.0.0.1:80";
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
        return xmlHttp.responseXML;
    }
}


function updateVotes() {
    console.trace();
    console.group("Process Logs");
    console.count("Process: ");

    let data;
    let vote_count;
    let question_count;

    // Fetch question count
    data = fetchData(FRONTEND_URL + "/question_count");
    question_count = data.firstChild.textContent;
    console.debug("Question count:" + question_count);

    // Update votes
    for (let i = 1; i <= question_count; i++) {
        data = fetchData(FRONTEND_URL + "/vote_count_ajax/" + i);
        vote_count = data.firstChild.textContent;
        document.getElementById("ajaxId" + i).textContent = vote_count;
    }

    console.groupEnd();
}
