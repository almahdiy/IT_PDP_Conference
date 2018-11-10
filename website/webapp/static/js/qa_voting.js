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
    let parsed;

    // Fetch ID, votes, and question body
    data = fetchData(FRONTEND_URL + "/vote_count_ajax_all/");
    lines = data.responseText.split("\n");

    var n = document.getElementById("questionsForm");
    while (n.firstChild) {
        n.removeChild(n.firstChild);
    }

    // Update ID, votes, and question body in rectangles
    for (let i = 0; i < lines.length; i++) {
        parsed = /([0-9]+) ([0-9]+) (.*)/.exec(lines[i]);
        id = parsed[1];
        votes = parsed[2];
        body = parsed[3];

        var div = document.createElement("div");
        div.setAttribute("class",  "inputGroup");

        var inp = document.createElement("inp");
        inp.setAttribute("id",  id);
        inp.setAttribute("name", "checkbox");
        inp.setAttribute("type", "checkbox");
        inp.setAttribute("value", id);

        var label = document.createElement("label");
        label.setAttribute("for", id);

        var p1 = document.createElement("p");
        p1.setAttribute("id", "ajaxId" + id + "Body");
        p1.textContent = body;

        var p2 = document.createElement("p");
        p2.setAttribute("id", "ajaxId" + id);
        p2.textContent = votes;

        label.appendChild(p1);
        label.appendChild(p2);
        inp.appendChild(label);
        div.appendChild(inp);

        document.getElementById("questionsForm").appendChild(div);
    }
}

