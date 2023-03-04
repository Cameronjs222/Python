let pId = []
let timeoutId = null

function reveal(Element) {
    pId.push(Element.innerText)
    Element.style.display = 'none'
    document.getElementById(Element.innerText + "S").style.display = 'block'
    console.log(pId)
}

function revert(Element) {
    var elementId = pId[pId.length - 1]
    timeoutId = setTimeout(() => {
        document.getElementById(elementId).style.display = 'block'
        Element.style.display = 'none'
    }, 500)
    var index = pId.indexOf(elementId)
    pId.splice(index, 1);
}