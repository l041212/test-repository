
$(document).ready(function(){
    initCreateBtn();
    initCategoryLabel();
    initCatalogueTableListener();
});

function initCreateBtn(){
    $("#createBtn").on("click",function(){
        var path="/blog/catalogueInit/write/";
        path+=$("a[class='nav-link active']").parent().find("input[name='category_id']").val()+"/";
        $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:"",
            dataType:"text",
            async:false,
            success:
                function(data){
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

function initCategoryLabel(){
    var path="/blog/categoryAllList/";
     $.ajax({
        url:path,
        type:"post",
        contentType:"application/x-www-form-urlencoded",
        data:"",
        dataType:"json",
        async:false,
        success:
            function(data){
                constructCategoryLabel(data);
        },
        error:
            function(xhr){
                if(xhr.status!='200'){
                    console.log(xhr);
                }
            }
    });
}

function initCatalogueTableListener(){
    var construct=function(){
        var path="/blog/catalogueListData/";
        path+=$("input[name='page_limit']:eq(0)").val()+"/";
        path+=$("input[name='page_number']:eq(0)").val()+"/";
        var parameter=$("form:eq(0)").serialize();
         $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:parameter,
            dataType:"json",
            async:false,
            success:
                function(data){
                    constructCatalogueTable(data);
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
    $("#frame_content .nav-link").each(function(){
        $(this).on("click",function(){
            $("[name='page_number']").val("1");
            construct();
        });
    });
}

function initUpdateBtn(){
    $("button[name='itemUpdateBtn']").each(function(){
        $(this).on("click",function(){
            var path="/blog/catalogueInit/write/";
            path+=$("a[class='nav-link active']").parent().find("input[name='category_id']").val()+"/";
            path+=$(this).parent().parent().find("td:eq(0) input").val()+"/";
            $.ajax({
                url:path,
                type:"post",
                contentType:"application/x-www-form-urlencoded",
                data:"",
                dataType:"text",
                async:false,
                success:
                    function(data){
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
    });
}

function constructCategoryLabel(data){
    if(data!=undefined&&data.length>0){
        for(var i=0;i<data.length;i++){
            var li=document.createElement("li");
            $(".nav-tabs").append(li);
            li.setAttribute("class","nav-item");
            var id=document.createElement("input");
            $(li).append(id);
            id.setAttribute("type","hidden");
            id.setAttribute("name","category_id");
            id.setAttribute("value",data[i]["id"]);
            var a=document.createElement("a");
            $(li).append(a);
            a.setAttribute("class","nav-link");
            a.innerText=data[i]["label"];
            a.setAttribute("href","#");
            $(a).on("click",function(){
                $(".nav-tabs .nav-item a").removeClass("active");
                $(this).addClass("active");
                $("#search input[name='category_id']").val($(this).parent().find("input[name='category_id']").val());
            });
        }
        if($("#search input[name='category_id']").val()==""){
            $(".nav-tabs .nav-item a:eq(0)").addClass("active");
            $("#search input[name='category_id']").val($(".nav-tabs input[name='category_id']:eq(0)").val());
        }else{
            $(".nav-tabs input[name='category_id']").each(function(){
                if($(this).val()==$("#search input[name='category_id']").val()){
                    $(this).parent().find("a").addClass("active");
                }
            });
        }
        //$(".nav-tabs .nav-item a:eq(0)").addClass("active");
        //$("#search input[name='category_id']").val($(".nav-tabs input[name='category_id']:eq(0)").val());
    }
}

function constructCatalogueTable(data){
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
        td.innerText=pageObjectList[i]['title'];
        var td=document.createElement("td");
        tr.append(td);
        td.innerText=pageObjectList[i]['context'];
        var td=document.createElement("td");
        tr.append(td);
        td.innerText=pageObjectList[i]['updateTime'];
        var td=document.createElement("td");
        tr.append(td);
    }
    initTableIdentityCheckBox($("#table table")[0]);
    initTableHandlerButton($("#table table")[0]);
    initPaginator($("#tail")[0],data,function(){$("#searchBtn").trigger("click");});
    initUpdateBtn();
}