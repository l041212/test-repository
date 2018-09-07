
$(document).ready(function(){
    initNavigator();
    searchBtnListener();
});

function initNavigator(){
    $(".collapse").removeClass("show");
    $(".nav-link").removeClass("active");
    $("#collapseTwo").addClass("show");
    $("#collapseTwo .nav-link:eq(0)").addClass("active");
}

function searchBtnListener(){
    var construct=function(){
        var path="/jobInfo/listData/";
        path+=$("input[name='page_limit']:eq(0)").val()+"/";
        path+=$("input[name='page_number']:eq(0)").val()+"/";
        var parameters=$("form").serialize();
        $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:parameters,
            dataType:"json",
            async:false,
            success:
                function(data){
                    constructJobInfoTable(data);
            },
            error:
                function(xhr){
                    if(xhr.status!='200'){
                        console.log(xhr);
                    }
                }
        });
     };
    construct();
}

function updateBtnListener(type,text){
    $("[name='itemUpdateBtn']").text(text);
    $("[name='itemUpdateBtn']").each(function(){
        $(this).attr("data-toggle","modal");
        $(this).attr("data-target","#inviteModal");
        $(this).on("click",function(){
            var id=$(this).parent().parent().find("[name='id']").val();
            $("#inviteModal #jobInfo_id").val(id);
            var path="/login/unTester/";
            var parameters=$("form").serialize();
            $.ajax({
                url:path,
                type:"post",
                contentType:"application/x-www-form-urlencoded",
                data:parameters,
                dataType:"json",
                async:false,
                success:
                    function(data){
                        constructInviteModalBody(data);
                        inviteConfirmListener();
                },
                error:
                    function(xhr){
                        if(xhr.status!='200'){
                            console.log(xhr);
                        }
                    }
            });
        });
    });
}

function inviteConfirmListener(){
    $("#inviteModal #inviteConfirm").on("click",function(){
        var path="/testReport/save_invite/";
        var parameters=new Object();
        parameters["jobInfo_id"]=$("#jobInfo_id").val();
        parameters["users_id"]=new Array();
        $("#inviteModal .modal-body input[type='checkbox']:checked").each(function(){
            parameters["users_id"].push(this.value);
        });
        console.log(parameters);
        if(parameters["users_id"].length>0){
            $.ajax({
                url:path,
                type:"post",
                contentType:"application/x-www-form-urlencoded",
                data:parameters,
                dataType:"text",
                async:false,
                success:
                    function(data){
                        if(data=="True"){
                            location.href="/testReport/list_invite/";
                        }
                },
                error:
                    function(xhr){
                        if(xhr.status!='200'){
                            console.log(xhr);
                        }
                    }
            });
        }
    });
}

function initTesterStatus(){
    $("table:eq(0) tbody tr").each(function(){
        switch ($(this).find("td:eq(5)").text()){
            case "0":
                $(this).find("td:eq(5)").text("测试中");
                break;
            case "1":
                $(this).find("td:eq(5)").text("生成中");
                break;
            case "2":
                $(this).find("td:eq(5)").text("已生成");
                break;
        }
    });
}

function userRoleReWrite(){
    var role=$("[name='user_role']").val();
    if(role!="hr"&&role!="admin"){
        $("#createBtn").remove();
        $("#deleteBtn").remove();
        $("[name='itemDeleteBtn']").remove();
        updateBtnListener("read","查看");
    }
}

function constructInviteModalBody(data){
    text="";
    for(var i=0;i<data.length;i++){
        text+="<span style='white-space: nowrap'><input type='checkbox' value='"+data[i]["id"]+"'>"+data[i]["name"]+"</span>";
        text+="&nbsp;&nbsp;&nbsp;";
    }
    $("#inviteModal .modal-body").html(text);
}

function constructJobInfoTable(data){
    var tbody=$("#table #card-body-conent tbody");
    tbody.html("");
    var pageObjectList=JSON.parse(data["page_object_list"]);
    for(var i=0;i<pageObjectList.length;i++){
        if(parseInt(pageObjectList[i]['id_count'])<=0){
            var tr=document.createElement("tr");
            tbody.append(tr);
            var td=document.createElement("td");
            tr.append(td);
            td.innerText=pageObjectList[i]['id'];
            var td=document.createElement("td");
            tr.append(td);
            td.innerText=pageObjectList[i]['name'];
            var td=document.createElement("td");
            tr.append(td);
            td.innerText=pageObjectList[i]['id_count'];
            var td=document.createElement("td");
            tr.append(td);
            td.innerText=pageObjectList[i]['match_count'];
            var td=document.createElement("td");
            tr.append(td);
            td.innerText=pageObjectList[i]['status_count'];
            var td=document.createElement("td");
            tr.append(td);
            td.setAttribute("class","td_status");
            td.innerText=pageObjectList[i]['status'];
            var td=document.createElement("td");
            tr.append(td);
        }
    }
    initTableIdentityCheckBox($("#table table")[0]);
    initTableHandlerButton($("#table table")[0]);
    updateBtnListener('write', '邀请');
    initTesterStatus();
    userRoleReWrite();
    $("[name='itemDeleteBtn']").remove();
    initPaginator($("#tail")[0],data,function(){
        $("#searchBtn").trigger("click");
    });
}