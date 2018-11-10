function changeColor(c, event) {
    document.body.style.backgroundColor = c;
    event.cancelBubble = true;
    if(event.stopPropagation) event.stopPropagation();
}