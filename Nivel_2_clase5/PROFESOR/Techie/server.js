const express = require('express');
const path = require('path');
const { GoogleGenerativeAI } = require("@google/generative-ai");

const app = express();
// const PORT = 3000;
// Alwaysdata establece estas variables de entorno
// const PORT = process.env.ALWAYSDATA_HTTPD_PORT || 3000;
// const IP = process.env.ALWAYSDATA_HTTPD_IP || '0.0.0.0'; 
// Port de alwaysdata.net : 8100
const PORT = process.env.PORT || 8100;
const IP = process.env.IP || '0.0.0.0'; 


// Inicializar el cliente de Google Generative AI
const genAI = new GoogleGenerativeAI("AIzaSyDZxiV4RhLFyRLQ2lRlkqV0lUOmL2DAED8");
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

// Middleware para parsear JSON
app.use(express.json());
app.use(express.static('public'));

// Ruta para manejar las solicitudes a la API de Google Generative AI
app.post('/node/api/generate', async (req, res) => {
    const { prompt } = req.body;

    try {
        const result = await model.generateContent(prompt);
        res.json({ response: result.response.text() });
    } catch (error) {
        console.error(error);
        res.status(500).send('Error al generar el contenido');
    }
});

// Ruta principal
app.get('/node', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

/*
app.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
    //console.log("Servidor escuchando en http://localhost:"+PORT);
});
*/

app.listen(PORT, IP, () => {
    console.log(`Aplicación Node.js corriendo en http://${IP}:${PORT}`);
});

