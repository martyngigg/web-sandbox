
function showfiles(event) {
    var fileinput = document.getElementById("fileinput");
    var files = fileinput.files;
    
    var filelist_div = document.getElementById("filelist");
    var desc = document.createElement("p");
    desc.innerHTML = "To be uploaded:";
    filelist_div.appendChild(desc)
    var new_ul = document.createElement("ul");
    // loop through files and print a line containing the filename
    var file;
    for (var i = 0; i < files.length; i++) {
        // get item
        file = files.item(i);
        var li = document.createElement("li");
        li.innerHTML = file.name;
        new_ul.appendChild(li);
    }
    filelist_div.appendChild(new_ul);

    var reset_desc = document.createElement("i");
    reset_desc.innerHTML = "Reload the page to clear the list";
    filelist_div.appendChild(reset_desc);
    
    // Enable the upload button
    var upload_btn = document.getElementById("startupload");
    upload_btn.className = upload_btn.className.replace( /(?:^|\s)disabled(?!\S)/g , '' );    
}
