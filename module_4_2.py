
def test_function():
    def  inner_function():
        print("Я в области видимости функции test_function")
    inner_function()  # Ничего не выводит, так-как не возвращаем значение.


inner_function()  # Выдает ошибку, имя 'inner_function' не определено.
