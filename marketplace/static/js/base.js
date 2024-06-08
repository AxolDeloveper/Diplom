function create_selector(name, is_class = false) {
    const prefix = is_class ? '.' : '#';
    return `${prefix}${name}`
}

function search() {
        const search_value = $(create_selector(SEARCH_INPUT_SELECTOR_NAME)).val()

        if(!search_value){
            alert('Введите значение для поиска')
        }

        location.href = `/search/${search_value}`
}



$(() => {
    $(create_selector(SEARCH_BTN_SELECTOR_NAME)).click(() => {
        () => {search()}
    })

//    $(create_selector(LOGOUT_BTN_SELECTOR)).click((event) => {
//        event.preventDefault()
//        const csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val()
//        $.post('/logout/', {csrfmiddlewaretoken: csrfmiddlewaretoken}, () => {
//            location.reload()
//        })
//    })
})