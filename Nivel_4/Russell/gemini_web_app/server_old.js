// server.js (Backend Node.js) - Versión Actualizada

require('dotenv').config();
const express = require('express');
const cors = require('cors');
const path = require('path');

// CAMBIO CRUCIAL 1: Importar GoogleGenAI del SDK de Google
const { GoogleGenAI } = require('@google/genai');

// --- Configuración ---
const app = express();
const port = 3003;

// CAMBIO CRUCIAL 2: Inicialización del cliente con el nombre correcto de la clase (GoogleGenAI)
// Usamos 'ai' como nombre de variable para el cliente de la IA
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY }); 

// CAMBIO CRUCIAL 3: Definir el modelo como una cadena de texto (string).
// gemini-2.5-flash es el modelo más rápido y rentable para esta tarea.
const modelId = "gemini-2.5-flash"; 

// Middlewares
app.use(cors()); // Permite peticiones desde el frontend
app.use(express.json()); // Permite analizar el cuerpo de las peticiones JSON

// --- Endpoint de la API ---

/*
app.get('/', (req,res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
})
*/

app.use(express.static(path.join(__dirname)));

app.post('/generate-ideas', async (req, res) => {
    const { topic } = req.body;

    if (!topic) {
        return res.status(400).json({ error: 'El campo "topic" es requerido.' });
    }

    // 1. Crear el prompt (instrucción para Gemini)
    const prompt = `Actúa como experto en marketing digital. Genera 5 ideas de contenido creativas y detalladas sobre el siguiente tema: "${topic}". Las ideas deben ser adecuadas para un blog.`;

    try {
        // CAMBIO CRUCIAL 4: Llamada a la API de Gemini usando el método generateContent del cliente 'ai'.
        const response = await ai.models.generateContent({
            model: modelId,
            contents: prompt,
            config: {
                // maxOutputTokens reemplaza a maxNewTokens
                maxOutputTokens: 500, 
                // decodingMethod: 'greedy' ya no es necesario o es gestionado por defecto.
            }
        });

        // CAMBIO CRUCIAL 5: Devolver la respuesta al frontend
        // El resultado de generateContent se accede directamente a través de .text
        const generatedText = response.text; 
        
        res.json({ success: true, ideas: generatedText });

    } catch (error) {
        console.error('Error al llamar a la API de Gemini:', error);
        res.status(500).json({ success: false, error: 'Error interno del servidor al generar contenido.' });
    }
});

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor Node.js corriendo en http://localhost:${port}`);
    console.log(`¡Listo para recibir peticiones POST a http://localhost:${port}/generate-ideas!`);
});