
addEventListener("load", setCommitteeMenuHandlers)

function setCommitteeMenuHandlers() {
    const buttons = document.querySelectorAll(".js-committee__button");
    for (const button of buttons)
        button.addEventListener("click", clickHandler(button.dataset.memberProfile, button));
}

function clickHandler(data, button) {
    const profile = JSON.parse(data);
    function handleClick() {
        console.log(profile);
    }
    return handleClick;
}
