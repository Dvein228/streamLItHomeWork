
import streamlit as st


st.set_page_config(page_title="Міні-тест Python", page_icon="🐍")
st.title(" Міні-тест на знання Python")
st.write("Перевір свої знання Python! Дай відповіді на 3 запитання.")

st.subheader("1. Яка команда використовується для виведення тексту?")
answer1 = st.radio(
    "Вибери правильну відповідь:",
    ["input()", "print()", "int()"],
    key="q1"
)
st.subheader("2. Який тип даних використовується для цілих чисел?")
answer2 = st.radio(
    "Вибери правильну відповідь:",
    ["str", "float", "int"],
    key="q2"
)

st.subheader("3. Яке ключове слово використовується для перевірки умови?")
answer3 = st.radio(
    "Вибери правильну відповідь:",
    ["for", "if", "while"],
    key="q3"
)


if st.button("Перевірити результати"):

    # Лічильник правильних відповідей
    score = 0

    # Перевірка відповідей
    if answer1 == "print()":
        score += 1

    if answer2 == "int":
        score += 1

    if answer3 == "if":
        score += 1

    # Виведення результату
    st.subheader("Результати тесту")
    st.write(f"Твій результат: {score} із 3")

    st.progress(score / 3)

    percentage = score / 3 * 100
    st.write(f"Успішність: {percentage:.0f}%")

    if score == 3:
        st.success("Вітаю! Усі відповіді правильні!")
        st.balloons()
    elif score == 2:
        st.info("Гарний результат! Ще трохи практики!")
    elif score == 1:
        st.warning("Є над чим попрацювати!")
    else:
        st.error("Спробуй ще раз! Вивчай Python!")