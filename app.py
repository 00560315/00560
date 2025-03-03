import streamlit as st
import time
 
# 配置页面
st.set_page_config(page_title="To My Love", page_icon="💖", layout="centered")
 
# 隐藏菜单和页脚
st.markdown("""
<style>
#MainMenu, footer {visibility: hidden;}
.stButton>button {width: 100%;}
</style>
""", unsafe_allow_html=True)
 
# 主界面
st.markdown("""
<div style='text-align:center'>
<h1 style='color:#ff69b4'>💌 致亲爱的宝贝</h1>
</div>
""", unsafe_allow_html=True)
 
if st.button("点击接收我的心意💌"):
    st.balloons()
    with st.spinner('正在生成道歉协议...'):
        time.sleep(1)
        st.success("""
        **协议内容：**  
        1. 承包所有家务（包括洗碗拖地）  
        2. 每月一次惊喜日🎁  
        3. 手机壁纸必须用合影📸  
        """)
 
# 确认按钮
if st.checkbox("我接受以上条款 💍"):
    st.markdown("""
    <div style='text-align:center; padding:20px; background:#fff5f7'>
    💕 生效时间：立刻！  
    💻 技术支持：你的专属程序员
    </div>
    """, unsafe_allow_html=True)