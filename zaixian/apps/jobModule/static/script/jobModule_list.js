
$(document).ready(function(){
    createBtnListener();
    searchBtnListener();
    initSelectorChange();
    initNavigator();
});

function initNavigator(){
    $(".collapse").removeClass("show");
    $(".nav-link").removeClass("active");
    $("#collapseOne").addClass("show");
    $("#collapseOne .nav-link:eq(2)").addClass("active");
}

function createBtnListener(){
    $("#createBtn").text("新建");
    $("#createBtn").on("click",function(){
        window.location.href="/jobModule/table/write/";
    });
}

function searchBtnListener(){
    var construct=function(){
        var path="/jobModule/listData/";
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
    deleteBtnListener();
    $("#searchBtn").text("查询");
    $("#searchBtn").on("click",function(){
        construct();
        deleteBtnListener();
    });
}

function initSelectorChange(){
    $("[name='_status']").val($("[name='status']").val());
    $("[name='_status']").on("change",function(){
        $("[name='status']").val($("[name='_status']").val());
    });
}

function deleteBtnListener(){
    var path="/jobModule/delete/";
    var request=function(path,parameters){
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
                            location.href="/jobModule/list/";
                        }
                },
                error:
                    function(xhr){
                        if(xhr.status!='200'){
                            console.log(xhr);
                        }
                    }
        });
    };
    $("#deleteBtn").text("删除");
    $("#deleteBtn").on("click",function(){
        var parameters=new Object();
        var ids=new Array();
        parameters["ids"]=ids;
        $("[name='id']:checked").each(function(){
            ids.push(this.value);
        });
        if(ids.length>0){
            request(path,parameters);
        }
    });
    $("[name='itemDeleteBtn']").text("删除");
    $("[name='itemDeleteBtn']").each(function(){
        $(this).on("click",function(){
            var id=$(this).parent().parent().find("[name='id']").attr("value");
            var parameters=new Object();
            var ids=new Array();
            parameters["ids"]=ids;
            ids.push(id);
            if(ids.length>0){
                request(path,parameters);
            }
        });
    });
}

function updateBtnListener(type,text){
    $("[name='itemUpdateBtn']").text(text);
    $("[name='itemUpdateBtn']").each(function(){
        $(this).on("click",function(){
            var id=$(this).parent().parent().find("[name='id']").attr("value");
            var url="/jobModule/table/"+type+"/"+id+"/";
            window.location.href=url;
        });
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

function constructJobInfoTable(data){
    var tbody=$("#table #card-body-conent tbody");
    tbody.html("");
    var pageObjectList=JSON.parse(data["page_object_list"]);
    for(var i=0;i<pageObjectList.length;i++){
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
        td.innerText=pageObjectList[i]['jobInfo_name'];
        var td=document.createElement("td");
        tr.append(td);
        td.innerText=pageObjectList[i]['jobInfo_status'];
        var td=document.createElement("td");
        tr.append(td);
    }
    initTableIdentityCheckBox($("#table table")[0]);
    initTableHandlerButton($("#table table")[0]);
    updateBtnListener('write', '编辑');
    initTesterStatus();
    userRoleReWrite();
    initPaginator($("#tail")[0],data,function(){
        $("#searchBtn").trigger("click");
    });
}