def introspection_info(obj):
    """
    Функция проводит интроспекцию объекта и возвращает информацию о нем.
    """
    obj_type = type(obj).__name__

    obj_module = getattr(obj, '__module__', 'built-in')

    obj_dir = dir(obj)

    attributes = [attr for attr in obj_dir if not callable(getattr(obj, attr, None))]
    methods = [attr for attr in obj_dir if callable(getattr(obj, attr, None))]

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }


if __name__ == "__main__":
    # Пример с числом
    number_info = introspection_info(42)
    print("Информация о числе 42:")
    print(number_info)

    # Пример с текстом
    text_info = introspection_info("Hello, World!")
    print("\nИнформация о строке:")
    print(text_info)


    class MyClass:
        def __init__(self, name):
            self.name = name

        def greet(self):
            return f"Hello, {self.name}!"


    my_object = MyClass("Alice")
    class_info = introspection_info(my_object)
    print("\nИнформация о пользовательском классе:")
    print(class_info)
