
function initTableIdentityCheckBox(object){
    $(object).find("tbody tr").each(function(){
        var parent=$(this).find("td:eq(0)");
        var id=$(parent).text();
        parent.html("");
        var checkbox=document.createElement("input");
        parent.append(checkbox);
        checkbox.setAttribute("type", "checkbox");
        checkbox.setAttribute("value", id);
        checkbox.setAttribute("name", "id");
    });
}

function initTableHandlerButton(object){
     $(object).find("tbody tr").each(function(){
        var parent=$(this).find("td:last-child");
        parent.html("");
        var updateBtn=document.createElement("button");
        parent.append(updateBtn);
        updateBtn.setAttribute("type", "button");
        updateBtn.setAttribute("class", "btn btn-sm btn-success tableItemBtn");
        updateBtn.setAttribute("name", "itemUpdateBtn");
        updateBtn.innerHTML="update";
        var deleteBtn=document.createElement("button");
        parent.append(deleteBtn);
        deleteBtn.setAttribute("type", "button");
        deleteBtn.setAttribute("class", "btn btn-sm btn-danger tableItemBtn");
        deleteBtn.setAttribute("name", "itemDeleteBtn");
        deleteBtn.innerHTML="delete";
    });
}

function initPaginator(object,data,action){
    $(object).find("ul").remove();
    if(JSON.parse(data["page_object_list"]).length>0){
        var disFlag=[
            [data["page_previous_p"],parseInt(data["page_number"])-2],
            [data["page_previous"],parseInt(data["page_number"])-1],
            ["True",parseInt(data["page_number"])],
            [data["page_next"],parseInt(data["page_number"])+1],
            [data["page_next_n"],parseInt(data["page_number"])+2]
        ];
        var ul=document.createElement("ul");
        $(object).append(ul);
        ul.setAttribute("class","pagination pagination-sm");
        var previous=document.createElement("li");
        ul.appendChild(previous);
        previous.setAttribute("class","page-item");
        previous.setAttribute("value",parseInt(data["page_number"])-1);
        if(data["page_previous"]!="True"){
            $(previous).addClass("disabled");
        }
        var a=document.createElement("a");
        previous.appendChild(a);
        a.setAttribute("class","page-link");
        a.setAttribute("href","#");
        a.innerText="<";
        for(var i=0;i<disFlag.length;i++){
            if(disFlag[i][0]!="False"){
                var page=document.createElement("li");
                ul.appendChild(page);
                page.setAttribute("class","page-item");
                page.setAttribute("value",disFlag[i][1]);
                if(disFlag[i][1]==parseInt(data["page_number"])){
                    $(page).addClass("active");
                }
                var a=document.createElement("a");
                page.appendChild(a);
                a.setAttribute("class","page-link");
                a.setAttribute("href","#");
                a.innerText=disFlag[i][1];
            }
        }
        var next=document.createElement("li");
        ul.appendChild(next);
        next.setAttribute("class","page-item");
        next.setAttribute("value",parseInt(data["page_number"])+1);
        if(data["page_next"]!="True"){
            $(next).addClass("disabled");
        }
        var a=document.createElement("a");
        next.appendChild(a);
        a.setAttribute("class","page-link");
        a.setAttribute("href","#");
        a.innerText=">";
        $("[name='page_count']").attr("value",data["page_count"]);
        $(ul).find("li[class!='page-item disabled']").each(function(){
            $(this).on("click",function(){
                $("input[name='page_number']").val($(this).val());
                action();
            });
        });
    }
}