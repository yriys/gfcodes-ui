import streamlit as st

st.set_page_config(page_title="Шифратор", page_icon="🔐")

st.title("🔐 Шифратор повідомлень")
st.write("Виберіть тип коду, введіть текст і натисніть потрібну кнопку.")

# Коди
def get_code_mappings(code_type):
    if code_type == "Стенів":
        decode_map = {
            '❌': 'A', '@': 'B', '✋🏻': 'C', '⭐': 'D', '💲': 'E', '🧨': 'F', '🌪️': 'G', '💣': 'H',
            '⚡': 'I', '🦴': 'J', '⚓': 'K', '*': 'L', '🌒': 'M', '💀': 'N', '❓': 'O', '🌲': 'P',
            '⚛️': 'Q', '&': 'R', '#': 'S', '⛵': 'T', '🗡️': 'U', '%': 'V', '👓': 'W', '🪐': 'X',
            '❗': 'Y', '🌀': 'Z'
        }

    elif code_type == "Автора":
        decode_map = {
            'Ǝ': 'A', '⧖': 'B', '☍': 'C', '⫘': 'D', '▽': 'E', '⨒': 'F', '⨕': 'G', 'φ': 'H',
            '⍽': 'I', '⏚': 'J', '≷': 'K', '⍋': 'L', '𖦹': 'M', '◇': 'N', '山': 'O', '☂': 'P',
            '⍾': 'Q', '⋑': 'R', 'И': 'S', '⊡': 'T', '☊': 'U', '꩜': 'V', '⌶': 'W', '⋈': 'X',
            '∪': 'Y', 'ż': 'Z'
        }

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

# Функції
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

# Введення тексту
text_input = st.text_area("Введіть текст:")

# Обробка кнопок
col1, col2 = st.columns(2)

output = ""

with col1:
    if st.button("🔐 Зашифрувати"):
        split = (code_type == "Кольоровий")
        output = encrypt(text_input, encode_map, split)
        st.success("Зашифровано!")

with col2:
    if st.button("🔓 Розшифрувати"):
        split = (code_type == "Кольоровий")
        output = decrypt(text_input, decode_map, split)
        st.success("Розшифровано!")

# Результат
if output:
    st.text_area("Результат:", output)
    st.code(output, language="text")
