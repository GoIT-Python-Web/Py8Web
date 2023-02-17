console.log('Chat page')
let protocol = null

if (window.location.protocol === 'http:') {
    protocol = 'ws://'
} else  {
    protocol = 'wss://'
}

const socket = new WebSocket(`${protocol}${window.location.host}/ws`)

socket.onopen = (e) => {
    console.log(e)
    console.log('Hello WebSocket!')
}

socket.onmessage = (e) => {
    text = e.data
    $('.chat').append(`<div class="users__item">${text}</div>`)
}

$(function() {
    $('.msg').on('submit', (e) => {
        e.preventDefault()
        const message = $('#msg').val()
        $('#msg').val('')
        socket.send(message)
    })
})