def __defining_seating(self):
        """
        Crea una lista de tamaño num_rows + 1.
        Cada posición (excepto la 0) contiene un diccionario { letra: None }.
        """
        # 1. Obtenemos la tupla (rows_list, seats_string) del avión privado
        rows_data, seats_string = self.__aircraft.seating_plan()

        # 2. Inicializamos la lista seating (empezamos con el índice 0 como None)
        self.__seating = [None]

        # 3. Recorremos el número de filas (usando el tamaño de la lista de la tupla)
        # Empezamos desde 1 porque la posición 0 ya es None
        for i in range(1, len(rows_data)):
            
            # CREAMOS UN DICCIONARIO NUEVO PARA ESTA FILA
            row_dict = {}
            for char in seats_string:
                row_dict[char] = None  # Insertamos cada letra con valor None
            
            # 4. Insertamos el diccionario de la fila en nuestra lista de asientos
            self.__seating.append(row_dict)