function editComment(index) {
    var commentText = document.getElementById('comment_text_' + index).innerText;
    document.getElementById('edit_form_' + index).style.display = 'block';
    document.getElementById('comment_text_' + index).style.display = 'none';
    document.getElementsByName('edited_comment')[index - 1].value = commentText;
}

function deleteComment(index) {
    if (confirm('Are you sure you want to delete this comment?')) {
        document.getElementById('delete_form_' + index).submit();
    }
}