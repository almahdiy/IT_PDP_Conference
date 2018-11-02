
var API_URL = "http://127.0.0.1:8080/";

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.body.style.backgroundColor = "rgba(228, 228, 190, 1)";
}

//AJAX components

/** Ice Breaker Stuff 
 * for reference: https://www.youtube.com/watch?v=r80S2CnCjLs
*/

var xmlHttp = createXmlHttpRequestObject();


/** Create the awesome object that let you update the page
 * without refreshing
 */
function createXmlHttpRequestObject()
{
    var xmlHttp;

    //If Internet Explorer is used
    if(window.ActiveXObject)
    {
        try 
        {
            xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        catch(e)
        {
            xmlHttp = false;
        }
    }
    //If any other *modern* browser is used
    else
    {
        try 
        {
            xmlHttp = new XMLHttpRequest(); //built-in function
        }
        catch(e)
        {
            xmlHttp = false;
        }
    }

    //If you couldn't set the object then alert
    if(!xmlHttp)
        alert("Can't create the xmlHttp object.")
    else
        return xmlHttp;
}


/**
 * Takes the object that we just created and sends requests to
 * The server; gets called once the page loads
 */
function process() {
    
    // These states mean the object is free and ready to communicate with the server
    if(xmlHttp.readyState==4 || xmlHttp.readyState==0)
    {
        // alert('In Process');
        // Document is the webpage
        // The value of "food" is whatever the user typed in the input box
        //food = encodeURIComponent(document.getElementById("userInput").value)
        // Sending the request / actually communicating with the Django part
        //the type of request, what you are sending to the django file, syncronous 
        var id = document.getElementById("1").value;
        // alert(id)
        xmlHttp.open("GET", API_URL + "vote_count_ajax/" + id, true);
        //If we get information back, call this other function to do something
        //Send the request you made...
        xmlHttp.send(null); // the parameter is what you send with the request (i.e. with POSTs)
        xmlHttp.onreadystatechange = handleServerResponse;
        

    }
    //If the object is busy, wait for 1000 then timeout and call process() again
    else 
    {
        setTimeout('process()', 1000);
    }
}


function handleServerResponse() 
{
    // alert("handleServerResponse");
    //The server is going to send us an XML file in between "response" tags
    if(xmlHttp.readyState==4) //object is done communication
    {
        // alert("next is status")
        // alert(xmlHttp.responseXML)
        if(xmlHttp.status==200) //if communication went okay
        {
            // alert("Communication went well")
            //We now have an XML file
            xmlResponse = xmlHttp.responseXML;

            XMLDocumentElement = xmlResponse.XMLDocumentElement; //the XML root
            // alert(xmlResponse.firstChild.textContent)
            message = xmlResponse.firstChild.textContent;
            
            //Get the element by ID and set the inner html to that content
            // alert("message: " + message);
            // alert(document.getElementById("ajaxId1"));
            // alert("inner HTML: " + document.getElementById("ajaxId1").textContent);
            document.getElementById("ajaxId1").textContent = message;
            setTimeout('process()', 1000);
        }
        else{
            alert('Something went wrong!');
        }
    }
}