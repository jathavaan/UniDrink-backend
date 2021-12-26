function getLeague() {
    return document.getElementById('select-league').value;
}

function populateTable() {
    const form = document.getElementById('select-league-form');
    let league = getLeague();
    console.log(league);

    form.addEventListener('submit', event => {
        event.preventDefault();
    })
}