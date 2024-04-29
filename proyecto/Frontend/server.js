const express = require('express');
const path = require('path');

const app = express();
const port = 3000; // Puedes cambiar el puerto si es necesario

// Ruta para servir archivos estáticos
app.use(express.static(path.join(__dirname, '')));

// Ruta para manejar cualquier solicitud y servir index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '', 'Page.html'));
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});