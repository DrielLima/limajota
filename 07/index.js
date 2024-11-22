function x(){
    const texto = prompt('Digite um número existente:')
    var n = parseInt(texto)
    const mydiv = document.getElementById('div')
    while (n >= 0){
        const newdiv = document.createElement('div')
        newdiv.innerHTML = n
        mydiv.appendChild(newdiv)
        n -= 1
    }
}