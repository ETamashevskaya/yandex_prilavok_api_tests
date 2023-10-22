import sender_stand_request
import data


# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()   # Копируется словарь с телом запроса из файла data
    current_body["name"] = name  # Изменение значения в поле name

    return current_body    # Возвращается новый словарь с нужным значением name

# Функция для позитивной проверки
def positive_assert(kit_body):
    kit_body = get_kit_body(kit_body)    # В переменную kit_body сохраняется обновлённое тело запроса
    response = sender_stand_request.post_new_client_kit(kit_body)      # В переменную kit_response сохраняется результат запроса на создание набора:

    assert response.status_code == 201    # Проверяется, что код ответа равен 201
    assert response.json()["name"] == kit_body["name"]  # Проверяется, что в ответе поле name совпадает с полем name в запросе

# Функция негативной проверки, когда в ответе ошибка про символы
def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(kit_body)   # В переменную kit_body сохраняется обновлённое тело запроса
    response = sender_stand_request.post_new_client_kit(kit_body)    # В переменную response сохраняется результат

    assert response.status_code == 400     # Проверяется, что код ответа равен 400

# Функция для негативной проверки, когда name не передано в запросе:
def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)   # В переменную response сохраняется результат

    assert response.status_code == 400     # Проверяется, что код ответа равен 400

# Тест 1. Успешное создание набора
# Параметр name состоит из 1 символа
def test_create_user_1_letter_in_name_get_success_response():
    positive_assert("a")

# Тест 2. Успешное создание набора
# Параметр name состоит из 511 символов
def test_create_user_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Ошибка. Параметр name состоит из пустой строки
def test_create_user_empty_name_get_error_response():
    kit_body = get_kit_body("")  # В переменную kit_body сохраняется обновлённое тело запроса
    negative_assert_code_400(kit_body)   # Проверка полученного ответа

# Тест 4. Ошибка. Параметр name состоит из 512 символов
def test_create_user_512_letter_in_name_get_error_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_create_user_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_create_user_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора. Параметр name состоит из спецсимволов
def test_create_user_spesial_simbol_in_name_get_success_response():
    positive_assert("№%@,")

# Тест 8. Успешное создание набора. Параметр name содержит спецсимволы
def test_create_user_probel_in_name_get_success_response():
    positive_assert(" Человек и КО")

# Тест 9. Успешное создание набора. Параметр name содержит цифры
def test_create_user_has_number_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Ошибка. В запросе нет параметра name
def test_create_user_no_name_get_error_response():
    kit_body = data.kit_body.copy()  # Копируется словарь с телом запроса из файла data в переменную kit_body
    kit_body.pop("name")   # Удаление параметра name из запроса
    negative_assert_no_name(kit_body)  # Проверка полученного ответа

# Тест 12. Ошибка. Тип параметра name: число
def test_create_user_number_type_name_get_error_response():
    kit_body = get_kit_body(123)  # В переменную user_body сохраняется обновлённое тело запроса
    response = sender_stand_request.post_new_client_kit(kit_body)  # В переменную kit_response сохраняется результат запроса на создание пользователя:

    assert response.status_code == 400    # Проверка кода ответа