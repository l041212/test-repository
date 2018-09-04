
$(document).ready(function(){
    createBtnListener();
});

function createBtnListener(){
    $("#createBtn").on("click",function(){
        window.location.href="/jobInfo/table/write/";
    });
}