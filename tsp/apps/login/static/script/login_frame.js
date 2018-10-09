$(document).ready(function(){
    initMenu();
});

function initMenu(){
    initMenuItem(document.getElementById("blogList"),"/blog/catalogueList/")
}

function initMenuItem(object,path){
    $(object).on('click',function(){
        var parameter=new Object();
        $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:parameter,
            dataType:"text",
            async:false,
            success:
                function(data){
                    $("#frame_content").html("");
                    $("#frame_content").html(data);
            },
            error:
                function(xhr){
                    if(xhr.status!='200'){
                        console.log(xhr);
                    }
                }
        });
    });
}