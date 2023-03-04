console.log('Hello world')

const form = document.forms[0]

console.log(form)

form.addEventListener('submit', async (event) => {
  event.preventDefault()
  const response = await fetch('http://localhost:8000/api/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      username: form.username.value,
      password: form.password.value,
    }),
  })
  console.log(response.status, response.statusText)
  console.log(response)
  if (response.status === 200) {
    result = await response.json()
    localStorage.setItem('tokenApp', result.access_token)
    window.location = '/list.html'
  }
})
