# Clase que representa un pedido (Order)
class Order:
    # Constructor de la clase Order, recibe la cantidad y el cliente
    def __init__(self, qtty, customer):
        self.customer = customer  # Almacena el nombre del cliente
        self.qtty = qtty          # Almacena la cantidad del producto

    # Método para imprimir la información del pedido
    def print(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")

    # Método para obtener la cantidad del pedido
    def get_qtty(self):
        return self.qtty

    # Método para obtener el nombre del cliente
    def get_customer(self):
        return self.customer


# Clase que representa un nodo en una lista enlazada
class Node:
    # Constructor de la clase Node, recibe los datos del nodo
    def __init__(self, data):
        self.data = data  # Almacena el objeto (en este caso, un pedido)
        self.next = None  # Referencia al siguiente nodo (None si es el último)

    # Método para obtener los datos almacenados en el nodo
    def get_data(self):
        return self.data

    # Método para establecer la referencia al siguiente nodo
    def set_next(self, next_node):
        self.next = next_node

    # Método para obtener la referencia al siguiente nodo
    def get_next(self):
        return self.next


# Clase que representa una cola (Queue) basada en una lista enlazada
class Queue:
    # Constructor de la cola, inicializa la referencia al primer y último nodo, y el tamaño de la cola
    def __init__(self):
        self.front = None  # Referencia al primer nodo (frente de la cola)
        self.rear = None   # Referencia al último nodo (final de la cola)
        self.size = 0      # Tamaño inicial de la cola

    # Método que devuelve el tamaño actual de la cola
    def size(self):
        return self.size

    # Método que verifica si la cola está vacía
    def is_empty(self):
        return self.size == 0

    # Método para obtener el primer elemento de la cola sin eliminarlo
    def front_element(self):
        if self.is_empty():  # Si la cola está vacía, retorna None
            return None
        return self.front.get_data()  # Retorna los datos del primer nodo

    # Método para agregar un nuevo elemento a la cola
    def enqueue(self, info):
        new_node = Node(info)  # Crea un nuevo nodo con la información recibida
        if self.is_empty():    # Si la cola está vacía, el nuevo nodo es el primero y último
            self.front = new_node
            self.rear = new_node
        else:  # Si no está vacía, añade el nuevo nodo al final
            self.rear.set_next(new_node)  # El último nodo apunta al nuevo nodo
            self.rear = new_node          # El nuevo nodo se convierte en el último
        self.size += 1  # Incrementa el tamaño de la cola

    # Método para eliminar el primer elemento de la cola
    def dequeue(self):
        if self.is_empty():  # Si la cola está vacía, retorna None
            return None
        data = self.front.get_data()  # Obtiene los datos del primer nodo
        self.front = self.front.get_next()  # Avanza el puntero al siguiente nodo
        self.size -= 1  # Decrementa el tamaño de la cola
        if self.is_empty():  # Si la cola está vacía, rear también debe ser None
            self.rear = None
        return data  # Retorna los datos del nodo eliminado

    # Método para imprimir el contenido completo de la cola
    def print_info(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.size}")  # Imprime el tamaño de la cola
        current = self.front  # Empieza por el primer nodo
        count = 1  # Contador para numerar los elementos
        while current is not None:  # Mientras no se llegue al final de la cola
            print(f"   ** Element {count}")
            if isinstance(current.get_data(), Order):  # Si el nodo contiene un pedido (Order)
                current.get_data().print()  # Llama al método print() del pedido
            current = current.get_next()  # Avanza al siguiente nodo
            count += 1  # Incrementa el contador
        print("******************************")


# Función principal que ejecuta el programa y prueba la cola
def main():
    queue = Queue()  # Crea una nueva instancia de la cola

    # Crear pedidos (Order) con cantidades y clientes diferentes
    order1 = Order(20, "cust1")
    order2 = Order(30, "cust2")
    order3 = Order(40, "cust3")

    # Agregar los pedidos a la cola
    queue.enqueue(order1)
    queue.print_info()  # Imprime la información de la cola

    queue.enqueue(order2)
    queue.print_info()  # Imprime la información de la cola

    queue.enqueue(order3)
    queue.print_info()  # Imprime la información de la cola

    # Ver el primer elemento (sin eliminarlo)
    print("Front element:")
    front_element = queue.front_element()  # Obtiene el primer elemento de la cola
    if isinstance(front_element, Order):  # Si el elemento es un pedido (Order)
        front_element.print()  # Imprime los detalles del pedido

    # Eliminar el primer elemento y mostrar el estado de la cola
    print("Dequeuing first element:")
    queue.dequeue()  # Elimina el primer elemento de la cola
    queue.print_info()  # Imprime la información de la cola actualizada

    # Eliminar otro elemento y mostrar el estado de la cola
    print("Dequeuing second element:")
    queue.dequeue()  # Elimina otro elemento de la cola
    queue.print_info()  # Imprime la información de la cola actualizada


# Punto de entrada del programa
if __name__ == "__main__":
    main()  # Ejecuta la función principal