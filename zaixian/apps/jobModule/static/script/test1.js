
$(document).ready(function(){
    initSelectorChange();
});

function initSelectorChange(){
    $("[name='_jobInfo_status']").val($("[name='jobInfo_status']").val());
    $("[name='_jobInfo_status']").on("change",function(){
        $("[name='jobInfo_status']").val($("[name='_jobInfo_status']").val());
    });
}