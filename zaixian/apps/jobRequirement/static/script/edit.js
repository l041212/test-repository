
$(document).ready(function(){
    //saveTableData();
});

/*
function saveTableData(){
    $("#submit").on("click",function(){
        var parameters=$("form").serialize();
        var path="/jobRequirement/save";
        $.ajax({
            url: path,
            data: parameters,
            type: "post",
            dataType: "text",
            async: false,
            success:function(data){
                console.log(data);
            },
            error:function (xhr){
                console.log(xhr.status);
            }
        });
    });
}
*/