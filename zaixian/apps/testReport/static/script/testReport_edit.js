
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
        window.location.href="/testReport/list/";
    });
}

function saveBtnListener(){
    $("#saveBtn").on("click",function(){
        var path="/testReport/save/";
        var parameter=$(".testReport form").serialize();
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
                        $(".alert-success").addClass("active");
                        if($("[name='id']").val()!=undefined&&$("[name='id']").val()!=""){
                            setTimeout(function(){
                                $(".alert-success").removeClass("active");
                            },2000);
                        }else{
                            $("#saveBtn").remove();
                            setTimeout(function(){
                                $("#backBtn").trigger("click");
                            },1000);
                        }
                    }else{
                        $(".alert-danger").addClass("active");
                        setTimeout(function(){
                            $(".alert-danger").removeClass("active");
                        },2000);
                    }
                    console.log(data);
            },
            error:
                function(xhr){
                    if(xhr.status!='200'){
                        $(".alert-danger").addClass("active");
                        setTimeout(function(){
                            $(".alert-danger").removeClass("active");
                        },2000);
                        console.log(xhr.status);
                    }
                }
        });
    });
}

function initSelectorChange(){
    $("[name='_status']").val($("[name='status']").val());
    $("[name='_status']").on("change",function(){
        $("[name='status']").val($("[name='_status']").val());
    });
}