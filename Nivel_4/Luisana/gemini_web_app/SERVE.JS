// server.js (Backend Node.js)

require('dotenv').config();
const express = require('express');
const cors = require('cors');
// 🚨 CAMBIO 1: Importación de la librería oficial de Google
const { GoogleGenAI } = require('@google/genai');

// --- Configuración ---
const app = express();
const port = 3000;

// 🚨 CAMBIO 2: Inicialización del cliente de Google GenAI
// La SDK busca automáticamente GEMINI_API_KEY en el entorno.
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY }); 

// Usamos un modelo moderno y eficiente para tareas de texto/chat
const modelId = "gemini-2.5-flash"; // Modelo eficiente, recomendado para tareas de texto/blog.

// Middlewares
app.use(cors()); // Permite peticiones desde el frontend
app.use(express.json()); // Permite analizar el cuerpo de las peticiones JSON

// --- Endpoint de la API ---
app.post('/generate-ideas', async (req, res) => {
    const { topic } = req.body;

    if (!topic) {
        return res.status(400).json({ error: 'El campo "topic" es requerido.' });
    }

    // 1. Crear el prompt (instrucción para Gemini)
    const prompt = `Actúa como experto en marketing digital. Genera 5 ideas de contenido creativas y detalladas sobre el siguiente tema: "${topic}". Las ideas deben ser adecuadas para un blog.`;

    try {
        // 🚨 CAMBIO 3: Llamada a la API usando el método generateContent
        const response = await ai.models.generateContent({
            model: modelId,
            // La entrada se pasa en formato de contenido (Content)
            contents: [{ role: "user", parts: [{ text: prompt }] }],
            config: {
                // Parámetros de configuración del modelo (ej. temperatura en lugar de decodingMethod)
                temperature: 0.7, // 0.7 es un buen valor para creatividad controlada
                maxOutputTokens: 500, // Limita la longitud de la respuesta
            }
        });

        // 🚨 CAMBIO 4: Extracción de la respuesta
        // El texto se extrae directamente de 'response.text'
        const generatedText = response.text;
        
        // 3. Devolver la respuesta al frontend
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