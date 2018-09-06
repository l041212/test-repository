
$(document).ready(function(){
    createBtnListener();
    searchBtnListener();
    initSelectorChange();
});

function createBtnListener(){
    $("#createBtn").on("click",function(){
        window.location.href="/jobInfo/table/write/";
    });
}

function searchBtnListener(){
    var construct=function(){
        var path="/jobInfo/listData/";
        path+=$("input[name='page_limit']:eq(0)").val()+"/";
        path+=$("input[name='page_number']:eq(0)").val()+"/";
        var parameter=$("form").serialize();
        $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:parameter,
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
    $("#searchBtn").on("click",function(){
        construct();
    });
}

function initSelectorChange(){
    $("[name='_status']").val($("[name='status']").val());
    $("[name='_status']").on("change",function(){
        $("[name='status']").val($("[name='_status']").val());
    });
}

function updateBtnListener(){
    $("[name='itemUpdateBtn']").each(function(){
        $(this).on("click",function(){
            var id=$(this).parent().parent().find("[name='id']").attr("value");
            var url="/jobInfo/table/write/"+id+"/";
            window.location.href=url;
        });
    });
}

function constructJobInfoTable(data){
    var tbody=$("#table #card-body-conent tbody");
    tbody.html("");
    var pageObjectList=JSON.parse(data["page_object_list"]);
    console.log(pageObjectList);
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
        td.innerText=pageObjectList[i]['status'];
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
    }
    initTableIdentityCheckBox($("#table table")[0]);
    initTableHandlerButton($("#table table")[0]);
    updateBtnListener();
    initPaginator($("#tail")[0],data,function(){
        $("#searchBtn").trigger("click");
    });
}