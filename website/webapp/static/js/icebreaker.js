function changeColor(c, event) {
    document.body.style.backgroundColor = c;
    console.debug(event);
    event.cancelBubble = true;
    if(event.stopPropagation) event.stopPropagation();
}