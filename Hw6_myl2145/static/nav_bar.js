const getSauceInput = ()=> $('.sauce_search').val();
function clearInput(){
    $('.sauce_search').val('');
}
function submitSearch(search_input){
    window.location.href = "/search_result/" + encodeURIComponent(search_input);
}
function emptyInput(target_input){
    if(target_input.trim()==''){
        return true;
    }
    return false;
}
$(document).ready(function(){
    $('.sauce_form').on('submit', function(e){
        e.preventDefault();
        let current_input = getSauceInput();
        if(!emptyInput(current_input)){
            submitSearch(current_input);
        }
        clearInput();
    });
});