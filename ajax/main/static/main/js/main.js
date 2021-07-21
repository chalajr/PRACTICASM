
function loadCards(search){
    fetch(`/search/${search}`)
    .then(response => response.text())
    .then(card => {
            document.getElementById('cardHolder').innerHTML = `${card}`
    })
}