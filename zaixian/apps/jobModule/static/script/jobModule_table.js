
$(document).ready(function(){
    backBtnListener();
    saveBtnListener();
    initAction();
    jobInfoSelectorListener();
    initSelectorChange();
});

function initAction(){
    if($("[name='action']").val()!="write"){
        $("#saveBtn").remove();
    }
}

function backBtnListener(){
    $("#backBtn").on("click",function(){
        window.location.href="/jobModule/list/";
    });
}

function saveBtnListener(){
    $("#saveBtn").on("click",function(){
        var path="/jobModule/save/";
        var parameter=$(".job-module form").serialize();
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

function jobInfoSelectorListener(){
    var funct=function(){
        var path="/jobInfo/unModule/";
        var parameter=$(".job-info form").serialize();
        $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:parameter,
            dataType:"json",
            async:false,
            success:
                function(data){
                   constructJobInfoSelector(data);
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
    };
    if ($("[name='jobInfo_id']").val()==''){
        $("[name='jobInfo_name']").css("display", "none");
        funct();
    }else{
        $("[name='_jobInfo_id']").remove();
    }
}

function constructJobInfoSelector(data){
    for(var i=0;i<data.length;i++){
        var option=document.createElement("option");
        $("[name='_jobInfo_id']").append(option);
        option.setAttribute("value",data[i]["id"]);
        option.innerText=data[i]["name"];
    }
    $("[name='_jobInfo_id']").on("change",function(){
        $("[name='_jobInfo_status']").val("0");
    });
}

function initSelectorChange(){
    $("[name='_jobInfo_status']").val($("[name='jobInfo_status']").val());
    $("[name='_jobInfo_id']").on("change",function(){
        $("[name='jobInfo_id']").val($("[name='_jobInfo_id']").val());
    });
    $("[name='_jobInfo_status']").on("change",function(){
        $("[name='jobInfo_status']").val($("[name='_jobInfo_status']").val());
    });
}