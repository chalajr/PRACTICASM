
function loadCards(search){

    fetch(`/search/${search}`)
    .then(response => response.text())
    .then( text => {
            document.getElementById('cardHolder').innerHTML = `${text}`
    })

}


