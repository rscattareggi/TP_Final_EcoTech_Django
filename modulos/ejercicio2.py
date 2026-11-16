import json


class StockInvalidoError(Exception):
    """
    Excepción personalizada para stock inválido.
    """
    pass


class DispositivoEcologico:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(
                "El stock no puede ser negativo."
            )

        self.__stock = valor

    def ficha_tecnica(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Stock: {self.stock}"
        )


class PanelSolar(DispositivoEcologico):

    def __init__(
        self,
        nombre,
        precio,
        stock,
        potencia_watts,
        eficiencia
    ):
        super().__init__(nombre, precio, stock)

        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

    # POLIMORFISMO
    def ficha_tecnica(self):
        return (
            f"Panel Solar: {self.nombre}\n"
            f"Potencia: {self.potencia_watts}W\n"
            f"Eficiencia: {self.eficiencia}%\n"
            f"Precio: ${self.precio}\n"
            f"Stock: {self.stock}"
        )


class GestorInventario:

    @staticmethod
    def guardar_catalogo_json(
        lista_dispositivos,
        ruta_archivo
    ):

        datos = []

        for dispositivo in lista_dispositivos:
            datos.append({
                "nombre": dispositivo.nombre,
                "precio": dispositivo.precio,
                "stock": dispositivo.stock
            })

        with open(
            ruta_archivo,
            "w",
            encoding="utf-8"
        ) as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )


if __name__ == "__main__":

    catalogo = []

    try:
        panel1 = PanelSolar(
            "Panel Solar 400W",
            250000,
            15,
            400,
            92
        )

        catalogo.append(panel1)

        panel2 = PanelSolar(
            "Panel Solar Premium",
            350000,
            -5,
            600,
            95
        )

        catalogo.append(panel2)

    except StockInvalidoError as e:
        print("ERROR:", e)

    print("\n=== FICHA TÉCNICA ===")
    for producto in catalogo:
        print(producto.ficha_tecnica())
        print("-" * 30)

    GestorInventario.guardar_catalogo_json(
        catalogo,
        "catalogo_ecotech.json"
    )

    print("\nCatálogo exportado correctamente.")
