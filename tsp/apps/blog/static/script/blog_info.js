
$(document).ready(function(){
    initTable();
    initSubmit();
    initSingleSelector("author_id","id","name","/library/authorAllList/");
});

function initTable(){
    var value=$("input[name='action']").val();
    if(value=="read"){
        $(".card-footer").remove();
    }
}

function initSubmit(){
    $("#submit").on("click",function(){
        var path="/blog/catalogueSave/";
        var parameter=$("form").serialize();
        $.ajax({
            url:path,
            type:"post",
            contentType:"application/x-www-form-urlencoded",
            data:parameter,
            dataType:"text",
            async:false,
            success:
                function(data){
                    if(data=="SUCCESS"){
                        backCatalogueList();
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

function backCatalogueList(){
    var path="/blog/catalogueList/";
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
}

function initSingleSelector(name,value,label,path){
    $.ajax({
        url:path,
        type:"post",
        contentType:"application/x-www-form-urlencoded",
        data:"",
        dataType:"json",
        async:false,
        success:
            function(data){
                constructSelector(name,value,label,data);
        },
        error:
            function(xhr){
                if(xhr.status!='200'){
                    console.log(xhr);
                }
            }
    });
}

function constructSelector(name,value,label,data){
    var select=document.createElement("select");
    $("input[name='"+name+"']").after(select);
    select.setAttribute("class","form-control");
    select.setAttribute("name","_"+name);
    var option=document.createElement("option");
    $(select).append(option);
    for(var i=0;i<data.length;i++){
        var option=document.createElement("option");
        $(select).append(option);
        option.setAttribute("value",data[i][value])
        option.innerText=data[i][label]
        if($("input[name='"+name+"']").val()==data[i][value]){
            option.setAttribute("selected","selected");
        }
    }
    $(select).change(function(){
        $("input[name='"+name+"']").val($("select[name='_"+name+"']").val());
    });
}