import streamlit as st
from typing import Final
from dtx_ollama import chat

# --- تنظیمات صفحه ---
st.set_page_config(page_title="DT Chatbot", page_icon="🍕", layout="wide")

# --- تنظیمات ظاهر فارسی اصلاح شده ---
STREAMLIT_STYLE: Final[str] = """
<style>
    @import url('https://fonts.cdnfonts.com/css/iransansx');
    
    html, body, p, h1, h2, h3, h4, h5, h6, input, textarea, li, div {
        font-family: 'IRANSansX', tahoma !important;
    }
    
    /* در اینجا .stHeading را اضافه کردیم */
    .block-container, section, input, textarea, div.stMarkdown, div.stHeading {
        direction: rtl;
        text-align: right;
    }

    .stChatInput {
        direction: rtl;
    }
</style>
"""
st.markdown(
    body=STREAMLIT_STYLE,
    unsafe_allow_html=True
)

# --- دستورالعمل سیستم ---
# دستورات سخت‌گیرانه برای جلوگیری از افزودنِ خودسرانه غذا به سفارش
SYSTEM_PROMPT: Final[str] = (
    "تو صندوق‌دار رستوران هستی. پاسخ‌های تو فقط باید شامل جدول‌های استاندارد مارک‌داون باشد.\n"
    "قانون مهم: فقط و فقط اقلامی را در جدول سفارش بنویس که کاربر دقیقاً نام برده است. هیچ غذای اضافه‌ای به لیست اضافه نکن.\n"
    "منو: پیتزا پپرونی (۲۵۰)، پیتزا مخلوط (۲۸۰)، چیزبرگر (۲۱۰)، نوشابه (۲۰)، سالاد (۱۸)، پاستا (۲۸) هزارتومان.\n"
    "۱. برای 'لیست غذا': حتما یک جدول با ستون‌های | ردیف | نام غذا | قیمت | بساز.\n"
    "۲. برای 'سفارش': حتما یک جدول با ستون‌های | نام غذا | تعداد | قیمت کل | بساز.\n"
    "۳. قانون: حتما هر ردیف جدول را در یک خط جداگانه بنویس تا درست نمایش داده شود.\n"
    "۴. قانون محاسبات: اگر جمع بالای ۵۰ بود ارسال رایگان، در غیر این صورت ۱۰ هزار تومان هزینه ارسال اضافه کن و جمع نهایی را بنویس."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "🍕 سلام! به رستوران DT خوش آمدید. برای دیدن منو بنویس 'لیست غذا' یا سفارش خود را بگو."}
    ]

# --- سایدبار ---
with st.sidebar:
    st.subheader("تنظیمات")
    st.markdown("""<hr style="height:2px;border:none;background:linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">""", unsafe_allow_html=True)
    
    model_choice = st.selectbox("انتخاب مدل:", ["llama3.1:8b", "gemma2:2b"])
    if st.button("پاک کردن چت"):
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "assistant", "content": "🍕 سلام! دوباره خوش آمدید."}
        ]
        st.rerun()

# --- نمایش اصلی ---
st.header("🍕 دستیار هوشمند رستوران DT", divider="rainbow")

# نمایش تاریخچه پیام‌ها
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message("assistant" if message["role"] == "assistant" else "user"):
            st.markdown(message["content"])

# --- دریافت و پردازش ورودی ---
user_prompt = st.chat_input("سفارش خود را بنویسید...")

if user_prompt:
    user_prompt = user_prompt.strip() # جلوگیری از پردازش اسپیس
    
    if user_prompt:
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.write(user_prompt)

        with st.spinner("درحال پردازش..."):
            ans, _, _ = chat(messages=st.session_state.messages, model_name=model_choice)
        
        st.session_state.messages.append({"role": "assistant", "content": ans})
        st.chat_message("assistant").markdown(ans)
        st.rerun()
        