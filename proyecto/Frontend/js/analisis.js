// Función que cambia el color de la celda seleccionada
const btn_analizar = document.getElementById('navbar_item_analizar')
const text_area = document.getElementById('archivo_texto')

const btn_anterior = document.getElementById('btn_anterior')
const btn_siguiente = document.getElementById('btn_siguiente')

lista_impresiones = []
matriz_pointer = 0

function clear_matriz() {
    for (var i = 0; i < celdas.length; i++) {
        celdas[i].style.backgroundColor = "white"
        celdas[i].innerHTML = ""
    }

    document.getElementById('lbl_matriz').innerHTML = "Matriz: ..."
    document.getElementById('lbl_archivo').innerHTML = "Archivo: ..."
}

function reset_data() {
    lista_impresiones = []
    matriz_pointer = 0
}


btn_analizar.addEventListener('click', async function(e) {
    e.preventDefault()

    try {

        texto = text_area.value

        if (texto == "") {
            alert("No se ha ingresado texto")
            return
        }
        
        const response = await fetch('http://localhost:4000/plotterserial/analizar', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'texto': texto })
        });

        // Verificar si la respuesta es exitosa
        if (!response.ok) {
            throw new Error('Error en la solicitud');
        }

        // Parsear la respuesta como JSON
        const data = await response.json();
        
        clear_matriz()
        reset_data()

        // Verificar si la respuesta es exitosa
        data.impresiones.forEach(element => {
            parsed = JSON.parse(element)
            lista_impresiones.push(JSON.parse(element))
        })

        alert(data.mensaje)
        
        if (lista_impresiones.length > 0){
            llenar_matriz()
        }

    } catch (error) {
        console.log(error)
    }

})

function llenar_matriz(){
    clear_matriz()
    impresion = lista_impresiones[matriz_pointer]

    document.getElementById('lbl_matriz').innerHTML = "Matriz: " + impresion.id

    // Llenar la matriz
    impresion.sentencias.forEach(sentencia => {
        fila = sentencia.fila
        columna = sentencia.columna
        celda = document.getElementById("celda" + fila.toString() + columna.toString())
        celda.style.backgroundColor = sentencia.color.toLowerCase()

        var img = document.createElement("img")
        img.src = "../Frontend/images/" + sentencia.figura.toLowerCase() + ".png"
        celda.appendChild(img)
    })

    // Logica de los botones
    if (matriz_pointer == 0){
        btn_anterior.disabled = true
    } else {
        btn_anterior.disabled = false
    }

    if (matriz_pointer == lista_impresiones.length - 1){
        btn_siguiente.disabled = true
    } else {
        btn_siguiente.disabled = false
    }

}

btn_anterior.addEventListener('click', (e) => {
    e.preventDefault()
    if (matriz_pointer > 0) {
        matriz_pointer--
        llenar_matriz()
    }
})

btn_siguiente.addEventListener('click', (e) => {
    e.preventDefault()
    if (matriz_pointer < lista_impresiones.length - 1) {
        matriz_pointer++
        llenar_matriz()
    }
})

