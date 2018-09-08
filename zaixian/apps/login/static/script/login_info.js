
$(document).ready(function(){
    initDataRegister();
});

function initDataRegister(){
    var path="/login/register/";
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
                $("#registerModal .modal-body").html(data);
                $("#registerModal .modal-body").html($("#registerModal .modal-body form").clone());
                $("#registerModal .card-header").remove();
                $("#registerModal .card-footer").remove();
                $("#registerModal .modal-body .card").attr("class","card");
                dataRegisterListener();
        },
        error:
            function(xhr){
                if(xhr.status!='200'){
                    console.log(xhr);
                }
            }
    });
}

function dataRegisterListener(){
    $("#registerSubmitBtn").on("click",function(){
        var path="/login/save/";
        var parameter=$("#registerModal form").serialize();
        $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:parameter,
            dataType:"text",
            async:false,
            success:
                function(data){
                    if(data=="True"){
                        alert('register message was saved...');
                        $("#registerModal").modal("hide");
                        $(".modal-backdrop").remove();
                    }
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