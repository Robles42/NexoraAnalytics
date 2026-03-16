import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

class NexoraEngine:
    def __init__(self, nombre_tienda):
        self.tienda = nombre_tienda
        self.model = LinearRegression()
        
    def cargar_datos(self, ruta_csv):
        if os.path.exists(ruta_csv):
            return pd.read_csv(ruta_csv)
        return None

    def entrenar_y_predecir(self, df, stock_actual):
        X = df[['dia']]
        y = df['ventas']
        self.model.fit(X, y)
        
        # Proyectar a 30 días
        dias_futuros = pd.DataFrame({'dia': range(1, 31)})
        predicciones = self.model.predict(dias_futuros)
        
        # Buscar día de quiebre
        dia_quiebre = next((d for d, p in zip(dias_futuros['dia'], predicciones) if p >= stock_actual), None)
        
        return dias_futuros, predicciones, dia_quiebre

    def generar_grafica(self, df, dias_futuros, predicciones, stock_limite):
        plt.figure(figsize=(10, 5))
        plt.scatter(df['dia'], df['ventas'], color='blue', label='Ventas Reales')
        plt.plot(dias_futuros, predicciones, color='red', linestyle='--', label='Tendencia IA')
        plt.axhline(y=stock_limite, color='orange', label=f'Límite Stock ({stock_limite})')
        
        plt.title(f'Proyección de Inventario: {self.tienda}')
        plt.xlabel('Día del Mes')
        plt.ylabel('Unidades')
        plt.legend()
        plt.grid(True)
        
        # Guardar en lugar de solo mostrar (útil para ReportGen AI)
        plt.savefig('reporte_actual.png')
        print("✅ Gráfica guardada como 'reporte_actual.png'")
        plt.show()