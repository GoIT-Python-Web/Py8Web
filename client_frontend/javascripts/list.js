const list = async () => {
  token = localStorage.getItem('tokenApp')
  // <li class="list-group-item">An item</li>
  const response = await fetch('http://localhost:8000/api/cats', {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })
  if (response.status === 200) {
    result = await response.json()
    for (el of result) {
      element = document.createElement('li')
      element.className = 'list-group-item'
      element.innerHTML = `id: ${el.id} name: <b>${el.nickname}</b> vaccinated: ${el.vaccinated}`
      cats.appendChild(element)
    }
  }
}

list()
