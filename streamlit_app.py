import streamlit as st
from PIL import Image

st.set_page_config(page_title="Шифратор", page_icon="🔐")

st.title("🔐 Шифратор повідомлень")
st.write("Виберіть тип коду, введіть текст і натисніть потрібну кнопку.")

# Інструкції
with st.expander("ℹ️ Інструкції та підказки"):
    st.write("‼️ Для кольорового коду при розшифровці вписуйте кожен код ргб через пробіл. Розділові знаки також через пробіл.")
    st.write("приклад: 7C7E7D FE2917 0913CD 0913CD B7F0FB , FFC699 B7F0FB E39BE4 0913CD C2D2EB !")
    st.write("❗ Шифр Стенів може розшифровувати не всі символи, але зашифровує всі.")
    st.write("💡 Ви також можете легко скопіювати виведений код або розшифрований текст натиснувши панель виводу знизу.")

# Кодова мапа
def get_code_mappings(code_type):
    if code_type == "Стенів":
        decode_map = {'❌': 'A', '@': 'B', '✋🏻': 'C', '⭐': 'D', '💲': 'E', '🧨': 'F', '🌪️': 'G', '💣': 'H',
                      '⚡': 'I', '🦴': 'J', '⚓': 'K', '*': 'L', '🌒': 'M', '💀': 'N', '❓': 'O', '🌲': 'P',
                      '⚛️': 'Q', '&': 'R', '#': 'S', '⛵': 'T', '🗡️': 'U', '%': 'V', '👓': 'W', '🪐': 'X',
                      '❗': 'Y', '🌀': 'Z'}
    elif code_type == "Автора":
        decode_map = {'Ǝ': 'A', '⧖': 'B', '☍': 'C', '⫘': 'D', '▽': 'E', '⨒': 'F', '⨕': 'G', 'φ': 'H',
                      '⍽': 'I', '⏚': 'J', '≷': 'K', '⍋': 'L', '𖦹': 'M', '◇': 'N', '山': 'O', '☂': 'P',
                      '⍾': 'Q', '⋑': 'R', 'И': 'S', '⊡': 'T', '☊': 'U', '꩜': 'V', '⌶': 'W', '⋈': 'X',
                      '∪': 'Y', 'ż': 'Z'}
    elif code_type == "Кольоровий":
        decode_map = {
            '00C3E3': 'A', '01B400': 'B', '9F3982': 'C', 'C2D2EB': 'D', 'FE2917': 'E',
            'B021F5': 'F', 'E9D0D4': 'G', '7C7E7D': 'H', 'FFE745': 'I', 'CEC0BF': 'J',
            '140603': 'K', '0913CD': 'L', 'B6642C': 'M', '8BC50F': 'N', 'B7F0FB': 'O',
            'F6C1D5': 'P', 'FEE8AC': 'Q', 'E39BE4': 'R', 'FFFCF3': 'S', 'FF2685': 'T',
            '004912': 'U', '863807': 'V', 'FFC699': 'W', '0098BF': 'X', 'FF6C0F': 'Y', 'FF9C2A': 'Z'
        }
    encode_map = {v: k for k, v in decode_map.items()}
    return encode_map, decode_map

def encrypt(text, encode_map, split=False):
    result = [encode_map.get(c.upper(), c) for c in text]
    return ' '.join(result) if split else ''.join(result)

def decrypt(text, decode_map, split=False):
    if split:
        items = text.split()
        result = [decode_map.get(c, c) for c in items]
    else:
        result = [decode_map.get(c, c) for c in text]
    return ''.join(result)

# Вибір коду
code_type = st.selectbox("Оберіть код:", ["Стенів", "Автора", "Кольоровий"])
encode_map, decode_map = get_code_mappings(code_type)

# Очистка до створення поля вводу
if "text_input" not in st.session_state:
    st.session_state.text_input = ""

if st.button("🗑️ Очистити поле"):
    st.session_state.text_input = ""
    st.rerun()

# Поле вводу
st.text_area("Введіть текст:", key="text_input")

# Кнопки дій
col1, col2 = st.columns(2)
output = ""

with col1:
    if st.button("🔐 Зашифрувати"):
        split = (code_type == "Кольоровий")
        output = encrypt(st.session_state.text_input, encode_map, split)
        st.success("Зашифровано!")

with col2:
    if st.button("🔓 Розшифрувати"):
        split = (code_type == "Кольоровий")
        output = decrypt(st.session_state.text_input, decode_map, split)
        st.success("Розшифровано!")

# Вивід результату
if output:
    st.text_area("Результат:", output)
    st.code(output, language="text")

# Зображення
image = Image.open('colorcode.png')
st.image(image, caption='Кольоровий код', use_container_width=True)

