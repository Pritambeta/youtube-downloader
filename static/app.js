function copyURL(th) {
    let copiedURL = document.getElementById("downloadURL").value;
    let textarea = document.createElement("textarea");
    textarea.innerHTML = copiedURL;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
    th.innerHTML = "Copied!";
    setTimeout(() => {
        th.innerHTML = "Copy"
    }, 2000);
}
function get_size(byte) {
    let size = byte;
    let units = ["B", "KB", "MB", "GB"];
    const p = 1024;
    let unit = units[0];
    let mySize = size;
    if (size >= p) {
        unit = units[1];
        mySize = size / p;
    }
    if (size >= p * p) {
        unit = units[2];
        mySize = size / (p * p);
    }
    if (size >= p * p * p) {
        unit = units[3];
        mySize = size / (p * p * p);
    }
    let findDot = mySize.toString().indexOf(".");
    let last = mySize.toString().substring(findDot);
    let last2 = last.substring(0, 3);
    let first = mySize.toString().substring(findDot, 0);
    return first + last2 + " " + unit;
}


$(document).ready(function () {

    $("#form").on("submit", function (e) {
        e.preventDefault();
        youtubeURL = $("#url").val();
        window.youtubeURL = youtubeURL;
        sendData = {
            "youtube-url": youtubeURL,
        }
        $("#dash").html(`<svg class="spinner" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M222.7 32.15C227.7 49.08 218.1 66.9 201.1 71.94C121.8 95.55 64 169.1 64 255.1C64 362 149.1 447.1 256 447.1C362 447.1 448 362 448 255.1C448 169.1 390.2 95.55 310.9 71.94C293.9 66.9 284.3 49.08 289.3 32.15C294.4 15.21 312.2 5.562 329.1 10.6C434.9 42.07 512 139.1 512 255.1C512 397.4 397.4 511.1 256 511.1C114.6 511.1 0 397.4 0 255.1C0 139.1 77.15 42.07 182.9 10.6C199.8 5.562 217.6 15.21 222.7 32.15V32.15z"/></svg>`);

        $.post("/get-options", sendData, function (data, status) {
            // console.log(data);
            select = "";
            data.data.forEach(element => {
                select += `<option value="${element.itag}">${element.mime_type} @ ${element.resolution}: ${get_size(element.filesize)}</option>`
            });
            $("#dash").html(`
            
            <div class="selectForm">
            <img src="${data.thumbnail_url}" alt="${data.title}" class="thumbnail-image">

            <p class="title">${data.title}</p>

            <div>
                <select id="selectType" class="select">
                ${select}
                </select>
                <button class="btn" id="getLinkBtn">Get Link</button>
            </div>
        </div>
            
            `);

            $("#getLinkBtn").click(function () {
                tokenItag = $("#selectType").val();
                sendData = {
                    "itag": tokenItag,
                    "youtube_url": youtubeURL,
                };
                $("#dash").html(`<svg class="spinner" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M222.7 32.15C227.7 49.08 218.1 66.9 201.1 71.94C121.8 95.55 64 169.1 64 255.1C64 362 149.1 447.1 256 447.1C362 447.1 448 362 448 255.1C448 169.1 390.2 95.55 310.9 71.94C293.9 66.9 284.3 49.08 289.3 32.15C294.4 15.21 312.2 5.562 329.1 10.6C434.9 42.07 512 139.1 512 255.1C512 397.4 397.4 511.1 256 511.1C114.6 511.1 0 397.4 0 255.1C0 139.1 77.15 42.07 182.9 10.6C199.8 5.562 217.6 15.21 222.7 32.15V32.15z"/></svg>`);

                $.post("/get-download-link", sendData, function (data, status) {
                    url = data.url;
                    console.log(data);
                    $("#dash").html(`
                <div class="getLink">
                <input type="url" id="downloadURL" class="input" readonly placeholder="Your Download URL"
                    value="${url}">
                <div class="btnBox">
                    <button class="btn" id="copyBtn" onclick="copyURL(this)">Copy</button>
                    <a target="_blank" href="${url}" class="btn downloadLink">Download Now</a>
                    <button class="btn" onclick="continueBrowse()">Continue</button>
                </div>
            </div>
                `);
            });
        });
        
    });
});


})

    function continueBrowse() {
       location.reload();
    }