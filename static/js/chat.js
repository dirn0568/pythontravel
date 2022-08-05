document.getElementById('chat_send').addEventListener('keydown', function(){
    if (window.event.keyCode == 13) {
        document.getElementById('chat_data').submit();
    }
});