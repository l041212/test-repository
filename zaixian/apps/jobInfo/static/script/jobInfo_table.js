
$(document).ready(function(){
    backBtnListener();
    saveBtnListener();
    initAction();
    initSelectorChange();
});

function initAction(){
    if($("[name='action']").val()!="write"){
        $("#saveBtn").remove();
    }
}

function backBtnListener(){
    $("#backBtn").on("click",function(){
        window.location.href="/jobInfo/list/";
    });
}

function saveBtnListener(){
    $("#saveBtn").on("click",function(){
        var path="/jobInfo/save/";
        var parameter=$(".job-info form").serialize();
        $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:parameter,
            dataType:"text",
            async:false,
            success:
                function(data){
                    console.log(data);
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

function initSelectorChange(){
    $("[name='_property']").val($("[name='property']").val());
    $("[name='_rank']").val($("[name='rank']").val());
    $("[name='_property']").on("change",function(){
        $("[name='property']").val($("[name='_property']").val());
    });
    $("[name='_rank']").on("change",function(){
        $("[name='rank']").val($("[name='_rank']").val());
    });
}