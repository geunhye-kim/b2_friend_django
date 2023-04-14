
function notuser() {
    alert('권한이 없습니다');
}

function edit(id) {
    let comment_data = document.querySelector('#comment' + id)
    document.querySelector('.comment_control' + id).remove()
    content = comment_data.textContent
    comment_data.remove()
    let edit_comment = document.querySelector('#comment_edit' + id)

    edit_comment.innerHTML =
        "<p id='comment{{comment.id}}' class='card-text'>" +
        "<input class='comm' type='text' name='comment' value='" + content + "'>" +
        "</input>" +
        "</p>" +
        "<div style='float: right'>" +
        "<input type='hidden' name='csrfmiddlewaretoken' value='" + document.getElementsByName('csrfmiddlewaretoken')[0].value + "'>" +
        "<input type='submit' class='btn btn-outline-dar' value='수정'></input>" +
        "</div>"
}