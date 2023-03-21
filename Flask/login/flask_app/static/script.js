var log = false
var reg = false
function login(){
    let log_div = document.getElementsByClassName('login')
    for (let i = 0; i<log_div.length; i++){
        log_div[i].style.display = 'block'
    }
    let reg_div = document.getElementsByClassName('register')
    console.log(reg_div)
    for (let i = 0; i<reg_div.length; i++){
        reg_div[i].style.display = 'none'
    }
    let logDiv = document.getElementById(formContainerLog)
    let regDiv = document.getElementById(formContainerReg)
    logDiv.style.height = 'auto'
    regDiv.style.height = '0px'
    log = true
    console.log(true)
}
function register(){
    let log_div = document.getElementsByClassName('login')
    for (let i = 0; i<log_div.length; i++){
        log_div[i].style.display = 'none'
    }
    let reg_div = document.getElementsByClassName('register')
    console.log(reg_div)
    for (let i = 0; i<reg_div.length; i++){
        reg_div[i].style.display = 'block'
    }
    let logDiv = document.getElementById(formContainerLog)
    let regDiv = document.getElementById(formContainerReg)
    regDiv.style.height = 'auto'
    logDiv.style.height = '0px'
    reg = true
    console.log(true)
}
