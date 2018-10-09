
$(document).ready(function(){
    initDataSubmit();
});

function initDataSubmit(){
    $("#submit").on("click",function(){
        var id=$("input[name='id']").eq(0).val();
        var path="/userinfo/save/";
        var parameter=$("form").eq(0).serialize();
        path=(id!=""&&id!=undefined)?(path+id+"/"):path;
        console.log($("form").eq(0));
        $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:parameter,
            dataType:"json",
            async:false,
            success:
                function(data){
                console.log(data['name']);
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