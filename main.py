from src.predictor import NexoraEngine

def iniciar():
    engine = NexoraEngine("IconicHats")
    df = engine.cargar_datos('data/ventas_iconic.csv')
    
    if df is not None:
        STOCK_ACTUAL = 40 # Cambia esto según lo que tengas en bodega
        dias, pred, quiebre = engine.entrenar_y_predecir(df, STOCK_ACTUAL)
        
        print(f"\n--- Nexora Analytics: Reporte para {engine.tienda} ---")
        
        if quiebre:
            dias_restantes = quiebre - df['dia'].max()
            print(f"📅 Fecha estimada de agotamiento: Día {quiebre}")
            
            # SISTEMA DE ALERTAS (Punto 3)
            if dias_restantes <= 5:
                print("🚨 ¡ALERTA CRÍTICA! El stock se agota en menos de 5 días. Reabastecer URGENTE.")
            else:
                print(f"✅ Tienes {dias_restantes} días de margen antes del quiebre.")
                
            # GENERAR GRÁFICA (Punto 1)
            engine.generar_grafica(df, dias, pred, STOCK_ACTUAL)
    else:
        print("❌ Error: No se encontró el archivo CSV en la carpeta 'data/'.")

if __name__ == "__main__":
    iniciar()