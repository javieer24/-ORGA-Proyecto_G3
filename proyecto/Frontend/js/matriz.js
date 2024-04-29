
let color = "cyan" // Color de la celda seleccionada
let celda = "celda00" // Celda seleccionada por defecto
let figura = "circulo" // Imagen de la celda seleccionada

// Función que cambia el color de la celda seleccionada
const celdas = document.getElementsByClassName("celda_mat")
const lbl_color_selec = document.getElementById("color_seleccionado")
const lbl_figura_selec = document.getElementById("figura_seleccionado")


// Cuando se hace click en una celda, se llama a la función que la cambia y se pasa su id
for (var i = 0; i < celdas.length; i++) {
    celdas[i].addEventListener("click", function() {
        celda = this.id
        cambiar_color()
        cambiar_imagen()
    });
}

// Función que cambia el color de la celda seleccionada
function cambiar_color() {
    document.getElementById(celda).style.backgroundColor = color
}


// Función que cambia la imagen de la celda seleccionada
function cambiar_imagen() {
    document.getElementById(celda).innerHTML = "";

    if (figura == "") {
        return
    }

    var img = document.createElement("img")
    img.src = "/images/" + figura + ".png"
    document.getElementById(celda).appendChild(img)
}

// Funciones que cambian el color de la celda seleccionada
document.getElementById("col_cyan").addEventListener('click', function(e) {
    e.preventDefault()
    color = "cyan"
    lbl_color_selec.innerHTML = "Color: Cyan"
})
document.getElementById("col_yellow").addEventListener('click', function(e) {
    e.preventDefault()
    color = "yellow"
    lbl_color_selec.innerHTML = "Color: Amarillo"
})
document.getElementById("col_magenta").addEventListener('click', function(e) {
    e.preventDefault()
    color = "magenta"
    lbl_color_selec.innerHTML = "Color: Magenta"
})
document.getElementById("col_black").addEventListener('click', function(e) {
    e.preventDefault()
    color = "black"
    lbl_color_selec.innerHTML = "Color: Negro"
})

// Funciones que cambian la imagen de la celda seleccionada
document.getElementById("fig_circulo").addEventListener('click', function(e) {
    e.preventDefault()
    figura = "circulo"
    lbl_figura_selec.innerHTML = "Figura: Circulo"
})
document.getElementById("fig_triangulo").addEventListener('click', function(e) {
    e.preventDefault()
    figura = "triangulo"
    lbl_figura_selec.innerHTML = "Figura: Triángulo"
})
document.getElementById("fig_equis").addEventListener('click', function(e) {
    e.preventDefault()
    figura = "equis"
    lbl_figura_selec.innerHTML = "Figura: Equis"
})
document.getElementById("fig_estrella").addEventListener('click', function(e) {
    e.preventDefault()
    figura = "estrella"
    lbl_figura_selec.innerHTML = "Figura: Estrella"
})
document.getElementById("fig_eliminar").addEventListener('click', function(e) {
    e.preventDefault()
    figura = ""
    color = "white"
    lbl_color_selec.innerHTML = "Color: ..."
    lbl_figura_selec.innerHTML = "Figura: Eliminar"
})


// MANEJO APIS

const btn_impimir = document.getElementById('navbar_item_imprimir')

btn_impimir.addEventListener('click', async function(e) {
    e.preventDefault()
    console.log("Imprimiendo...")
    //obtener informacion de todas las celdas de la matriz
    let matriz = []
    for (var i = 0; i < celdas.length; i++) {
        let celda = celdas[i]
        let pos = { "fila": celda.id[5], "columna": celda.id[6] }
        let color = celda.style.backgroundColor
        let figura = celda.innerHTML.includes("img") ? celda.innerHTML.split("/")[3].split(".")[0] : ""

        // verificar si la celda tiene una imagen
        if (figura != "") {
            matriz.push({ pos, color, figura })
        }
    }

    // Verificar si la matriz esta vacia
    if (matriz.length == 0) {
        alert("Matriz vacía")
        return
    }

    console.log(matriz)

    try {
        // Llamada a la api
        const response = await fetch('http://localhost:4000/plotterserial/graficar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'matriz': matriz })
        })

        const data = await response.json()
        alert(data.mensaje)
        
    } catch (error) {
        console.log(error)
        
    }
})