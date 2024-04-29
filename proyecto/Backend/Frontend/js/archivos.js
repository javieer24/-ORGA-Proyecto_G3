const navbar_item_abrir = document.getElementById('navbar_item_abrir')
const navbar_item_nuevo = document.getElementById('navbar_item_nuevo')
const navbar_item_guardar = document.getElementById('navbar_item_guardar')
const file_input = document.getElementById('file_input')
const archivo_texto = document.getElementById('archivo_texto')


navbar_item_abrir.addEventListener('click', (e) => {
    e.preventDefault()
    console.log("abriendo...")

    file_input.click()
    // 

})

file_input.addEventListener('change', (e) => { //cuando se selecciona un archivo

    const file = e.target.files[0]

    if (file) {
        const reader = new FileReader()
        
        const fileName = file.name
        // Verificar que el archivo sea .olc
        const extension = fileName.split('.').pop()
        if (extension !== 'orga' && extension !== 'txt') {
            alert('El archivo seleccionado no es un archivo .orga')
            return
        }

        reader.onload = (event) => {
            const fileContent = event.target.result
            archivo_texto.value = (fileContent)
            document.getElementById('lbl_archivo').innerHTML = "Archivo: " + file.name
        }

        reader.readAsText(file)
    }

    file_input.value = null
})

navbar_item_nuevo.addEventListener('click', (e) => {
    e.preventDefault()
    console.log("nuevo...")
    archivo_texto.value = ''
    clear_matriz()
    reset_data()
})

navbar_item_guardar.addEventListener('click', (e) => {
    e.preventDefault()
    
    // Obtener el nombre del sessionStorage
    const nombreArchivo = 'archivo.orga'
    
    const contenido = archivo_texto.value
    if (contenido === '') {
        alert('No hay código para guardar')
        return
    }
    
    console.log("guardando...")
    guardarArchivo(nombreArchivo, contenido)
})

function guardarArchivo(nombre, contenido) {
    const blob = new Blob([contenido], { type: 'text/plain' })
    const url = URL.createObjectURL(blob)

    const a = document.createElement('a')
    a.href = url
    a.download = nombre
    a.textContent = 'Descargar'
    a.style.display = 'none'

    document.body.appendChild(a)

    a.click()

    document.body.removeChild(a)
    URL.revokeObjectURL(url)
}
