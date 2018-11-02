
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
        // Document is the webpage
        // The value of "food" is whatever the user typed in the input box
        food = encodeURIComponent(document.getElementById("userInput").value)
        // Sending the request / actually communicating with the Django part
        //the type of request, what you are sending to the django file, syncronous 
        xmlHttp.open("GET", "", true);
    }
    else 
    {

    }
}