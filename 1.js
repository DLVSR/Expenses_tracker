let c = 0;
inc.onclick = function(){
    c++;
    myh1.textContent = c;
}
de.onclick = function(){
    c--;
    myh1.textContent = c;
}
re.onclick = function(){
    c=0;
    myh1.textContent = c;
}