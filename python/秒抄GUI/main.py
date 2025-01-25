import streamlit as st
import requests
import json
from PIL import Image
from pyzbar.pyzbar import decode
from urllib.parse import parse_qs, unquote_plus
import re
import strtojs as stj
import ewtcmd as ewt

st.set_page_config(
    # 可恶的Streamlit, 为什么设置页面标题函数的一定要是第一行代码？！
    page_title="EWTcrackerGUI",  # 标签页标题
    page_icon="💯",  # 标签页图标，可以使用 Unicode 表情符号或图片路径
    layout="wide"  # 页面布局，可选 "wide" 或 "centered"
)
###
#✨升学e网通 *GUI版！* 教辅 | 作业 答案查看脚本✨
  #--版本：Beta1.0.0
  #--作者：黔中极客 & Code_S96
  #--项目地址：https://github.com/qzgeek/ewt360
  #--许可证：https://www.gnu.org/licenses/gpl-3.0.html#license-text
  #--作者的话：
    #本脚本仅个人学习使用，禁止传播，误下请尽快删除！！
###

contid = None
st.markdown(
    """
    <style>
        /* 调整整个页面的行间距 */
        body {
            line-height: 1; /* 设置行间距为 1 倍 */
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.caption("EWTwebver 1.0.0")
st.title("EWTwebver")
st.write("欢迎使用一网通教辅答案获取工具！")
st.write("GUI By Streamlit & Code_S96 | Program By Qzgeek")
textarea = st.text_area(label="在这里输入Cookies...")
upfile = st.file_uploader("在这里上传二维码照片...(限大小10M以内)", type=["jpg","png","gif"])
submit_button = st.button(label="提交并处理信息", key="process_button")
st.markdown("---")
st.write("以下是程序自动生成日志↓（答案会生成在最底下）")
if upfile is not None:
    file_size = upfile.size
    max_file_size_bytes = 10 * 1024 * 1024  # 10MB
    if file_size > max_file_size_bytes:
        st.error("文件大小不能超过10MB!")
        st.stop()
    st.write("开始尝试解析二维码图片...")
    try:
        # 使用Pillow打开图片
        img = Image.open(upfile)
        # 解码二维码
        deobj = decode(img)
        if deobj:
            # 显示解码结果
            st.write("二维码解析成功！")
            for obj in deobj:
                furl = requests.get(deobj[0].data.decode("utf-8"), allow_redirects=True).url
                st.write(f"完整链接: {furl}")
            st.write("开始提取ContentID字符串...")
            match = re.search(r'contentid=([^&]+)', furl)
            if match:
                contid = match.group(1)
                st.write(contid)
                st.write("ContentID已储存！")
                st.write(f"ContentID是: {contid}")
            else:
                st.error("未解析到ContentID，也许你用的不是E网通的链接？AwA")
        else:
            st.error("未检测到二维码，请检查图片是否无遮挡，清晰有效。")
    except Exception as e:
        st.error(f"解析失败: {e}")
if submit_button:
    if contid is None:
        st.error("未检测到ContentID，请上传二维码图片。")
        st.stop()
    st.write("开始处理信息...")
    st.write("开始转换Cookies....")
    cookies = stj.store_data(textarea)
    if cookies is not None:
        st.write("Cookies转换成功！")
        st.write("Cookie内容如下：")
        st.json(cookies)
    else:
        st.error("Cookies转换失败！请检查输入是否正确。")
        st.stop()
    if contid is not None:
        st.write("开始获取答案...")
        ewt.genshin_launch(contid, cookies)