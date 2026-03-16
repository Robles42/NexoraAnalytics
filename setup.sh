#!/bin/bash
echo "Configurando Nexora-Analytics Engine..."

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    python -m venv venv
    echo "Entorno virtual creado."
fi

# Activar e instalar dependencias
source venv/bin/activate
pip install -r requirements.txt

echo "Todo listo. Para correr el programa usa: python main.py"