
function loadCards(search, page){
    document.getElementById('cardHolder').innerHTML = ``
    
    fetch(`/search/${search}/${page}`)
    .then(response => response.text())
    .then( text => {
            document.getElementById('cardHolder').innerHTML = `${text}`
    })

    console.log(page)

}


