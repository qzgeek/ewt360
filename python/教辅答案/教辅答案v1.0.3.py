import requests
import json
import re
from html import unescape
if __name__ != '__main__':
    import streamlit as st
    from bs4 import BeautifulSoup
"""
✨升学e网通  教辅 | 作业 答案查看脚本✨
  --版本：v1.0.3
  --作者：黔中极客 & Code_S96
  --项目地址：https://github.com/qzgeek/ewt360
  --许可证：https://www.gnu.org/licenses/gpl-3.0.html#license-text
  --使用教程：
      1、pip安装requests；
      2、抓包获取cookie并填入下方第264行附近（记得打缩进）；
      3、运行。
  --作者的话：
        本脚本仅个人学习使用，禁止传播，误下请尽快删除！！
"""
if __name__ == '__main__':
    contentid = int(input("请输入题目contentid值："))

# 获取题目的reportId，需要用到下面括号里这一坨
def get_reportId(url_b, params_b, cookies):
    try:
        # 以get方式从url_b获取返回数据
        response_b = requests.get(url_b, params=params_b, cookies=cookies)
        # 如果成功
        if response_b.status_code == 200:
            # 解析返回数据为json
            response_b_json = response_b.json()
            # 如果能从返回数据里找到success（能找到就说明操作成功了）
            if response_b_json.get('success'):
                # 如果能从返回数据里找到data和在data里的reportId
                if response_b_json.get('data') and 'reportId' in response_b_json['data']:
                    # 那么就将返回数据中data下的reportId赋值给变量reportId
                    reportId = response_b_json["data"]["reportId"]
                    # 将上面的reportId输出
                    return reportId
                # 否则报错
                else:
                    if __name__ == '__main__':
                        print("解析的JSON数据中缺少必要的键或data为None")
                    else:
                        st.error("解析的JSON数据中缺少必要的键或data为None")
            # 否则报错
            else:
                if __name__ == '__main__':
                    print("请求未成功，错误信息：", response_b_json.get('msg'))
                else:
                    st.error("请求未成功，错误信息：", response_b_json.get('msg'))
        # 否则报错
        else:
            if __name__ == '__main__':
                print("请求失败，状态码：", response_b.status_code)
            else:
                st.error("请求失败，状态码：", response_b.status_code)
    # 下面的是捕捉错误信息并打印以及输出None
    except json.JSONDecodeError:
        if __name__ == '__main__':
            print("响应内容不是有效的JSON")
        else:
            st.error("响应内容不是有效的JSON")
    except Exception as e:
        if __name__ == '__main__':
            print("发生错误：", str(e))
        else:
            st.error("发生错误：", str(e))
    return None

# 获取题目排列后的ID
def get_sorted_question_ids(url_a, params, cookies):
    try:
        # 发起GET请求
        response_a = requests.get(url_a, params=params, cookies=cookies)

        # 检查响应状态码
        if response_a.status_code == 200:
            # 尝试解析响应内容
            response_a_json = response_a.json()

            # 首先检查success字段
            if response_a_json.get('success'):
                # 检查解析后的数据是否包含必要的键且data不为None
                if response_a_json.get('data') and 'questions' in response_a_json['data']:

                    # 提取题目id
                    questions = response_a_json["data"]["questions"]

                    # 按照questionNo排序
                    sorted_questions = sorted(questions, key=lambda x: x["questionNo"])

                    # 提取排序后的id列表
                    sorted_ids = [question["id"] for question in sorted_questions]

                    return sorted_ids
                else:
                    if __name__ == '__main__':
                        print("解析的JSON数据中缺少必要的键或data为None")
                    else:
                        st.error("解析的JSON数据中缺少必要的键或data为None")
            # 否则报错
            else:
                if __name__ == '__main__':
                    print("请求未成功，错误信息：", response_b_json.get('msg'))
                else:
                    st.error("请求未成功，错误信息：", response_b_json.get('msg'))
        # 否则报错
        else:
            if __name__ == '__main__':
                print("请求失败，状态码：", response_b.status_code)
            else:
                st.error("请求失败，状态码：", response_b.status_code)
    # 下面的是捕捉错误信息并打印以及输出None
    except json.JSONDecodeError:
        if __name__ == '__main__':
            print("响应内容不是有效的JSON")
        else:
            st.error("响应内容不是有效的JSON")
    except Exception as e:
        if __name__ == '__main__':
            print("发生错误：", str(e))
        else:
            st.error("发生错误：", str(e))
    return None

# 获取题目排列后的PID
def get_questions_list(url_c, params_c, cookies):
    try:
        response_c = requests.post(url_c, json=params_c, cookies=cookies)
        if response_c.status_code == 200:
            response_c_json = response_c.json()
            if response_c_json.get('success'):
                if response_c_json.get('data') and 'questionInfoList' in response_c_json['data']:
                    # 把题目pid以index大小顺序列为列表
                    questionInfoList = response_c_json["data"]["questionInfoList"]
                    sorted_ql = sorted(questionInfoList, key=lambda x: x["questionNumber"])
                    sorted_subjective = [question["subjective"] for question in sorted_ql]
                    sorted_pids = [question["questionId"] for question in sorted_ql]
                    return sorted_pids, sorted_subjective
                else:
                    if __name__ == '__main__':
                        print("解析的JSON数据中缺少必要的键或data为None")
                    else:
                        st.error("解析的JSON数据中缺少必要的键或data为None")
            # 否则报错
            else:
                if __name__ == '__main__':
                    print("请求未成功，错误信息：", response_b_json.get('msg'))
                else:
                    st.error("请求未成功，错误信息：", response_b_json.get('msg'))
        # 否则报错
        else:
            if __name__ == '__main__':
                print("请求失败，状态码：", response_b.status_code)
            else:
                st.error("请求失败，状态码：", response_b.status_code)
    # 下面的是捕捉错误信息并打印以及输出None
    except json.JSONDecodeError:
        if __name__ == '__main__':
            print("响应内容不是有效的JSON")
        else:
            st.error("响应内容不是有效的JSON")
    except Exception as e:
        if __name__ == '__main__':
            print("发生错误：", str(e))
        else:
            st.error("发生错误：", str(e))
    return None

# 自动做选择题，选择题选项全选A
# 自动做选择题和主观题
def auto_do_homework(url_d, params_d, data_to_send, cookies):
    try:
        response_d = requests.get(url_d, params=params_d, cookies=cookies)
        response_d_a = requests.post(url_d_a, json=data_to_send, cookies=cookies)
        """
        if response_d.status_code == 200:
            if response_d_a.status_code == 200:
                print("请求成功，响应数据：", response_d_a.json())
            else:
                print("请求失败，状态码：", response_d_a.status_code)
        else:
            print("请求失败，状态码：", response_d.status_code)
        """
    except json.JSONDecodeError:
        if __name__ == '__main__':
            print("响应内容不是有效的JSON")
        else:
            st.error("响应的内容不是有效的JSON")
    except Exception as e:
        if __name__ == '__main__':
            print("发生错误：", str(e))
        else:
            st.error("发生错误：", str(e))
    return None

# 自动提交
def auto_submit_homework(url_e, data_get, cookies):
    try:
        response_e = requests.post(url_e, json=data_get, cookies=cookies)
        if response_e.status_code != 200:
            print("请求失败，状态码：", response_e.status_code)
    except json.JSONDecodeError:
        if __name__ == '__main__':
            print("响应内容不是有效的JSON")
        else:
            st.error("响应的内容不是有效的JSON")
    except Exception as e:
        if __name__ == '__main__':
            print("发生错误：", str(e))
        else:
            st.error("发生错误：", str(e))
    return None

# 获取正确答案
def get_right_answer(url, data, cookies):
    try:
        # 发起POST请求
        response = requests.post(url, json=data, cookies=cookies)

        # 检查响应状态码
        if response.status_code == 200:
            # 解析响应内容
            response_json = response.json()
            return response_json.get('data', {}).get('rightAnswer', [])
        else:
            print("Failed to retrieve data, status code:", response.status_code)
            return None
    except json.JSONDecodeError:
        if __name__ == '__main__':
            print("响应内容不是有效的JSON")
        else:
            st.error("响应的内容不是有效的JSON")
    except Exception as e:
        if __name__ == '__main__':
            print("发生错误：", str(e))
        else:
            st.error("发生错误：", str(e))
    return None

# 请求的URL
url_a = 'https://web.ewt360.com/api/answerprod/app/answer/summaryReport'
url_b = 'https://web.ewt360.com/api/answerprod/web/answer/report'
url_c = 'https://web.ewt360.com/api/answerprod/common/answer/answerSheetInfo'
url_d = 'https://web.ewt360.com/api/answerprod/app/answer/paper/questions'
url_d_a = 'https://web.ewt360.com/api/answerprod/web/answer/submitAnswer'
url_e = 'https://web.ewt360.com/api/answerprod/web/answer/submitpaper'
url = 'https://web.ewt360.com/api/answerprod/web/answer/simple/question/info'

# 检测本代码是否被作为模块引入（用以实现模块功能）
if __name__ == '__main__':
    """
    将cookie填入下方
    格式应该为：
    cookies = {
        "xxx": "xxxxx",
        "xxx": "xxxxx",
        ………
        "xxx": "xxxxx"
    }
    """
    cookies = {

    }

    # 将token从cookies中提取出来
    token = cookies.get('token')

    params_b = {
        "paperId":contentid,
        "reportId":"0",
        "platform":"1",
        "bizCode":"204",
        "isRepeat":"1",
        "homeworkId":"0",
        "token":token
    }

    reportId = get_reportId(url_b, params_b, cookies)

    params_c = {
        "paperId": contentid,
        "reportId": reportId,
        "platform": "1",
        "bizCode": "204",
        "homeworkId": "0",
        "client": "4"
    }

    sorted_pids, sorted_subjective = get_questions_list(url_c, params_c, cookies)

    index = 0

    for index, question_pid in enumerate(sorted_pids, start=1):
        params_d = {
            "paperId": contentid,
            "reportId": reportId,
            "platform": "1",
            "questionIds": question_pid,
            "bizCode": "204",
            "homeworkId": "0",
            "token": token
        }
        
        # 判断题目是否是主观题
        if sorted_subjective[index - 1]:
            # 如果是主观题，构造主观题的答案数据
            data_to_send = {
                "paperId": contentid,
                "reportId": reportId,
                "platform": "1",
                "questionList": [
                    {
                        "id": question_pid,  # 动态获取主观题的id
                        "totalSeconds": 14,
                        "attachmentImages": [
                            "http://file.ewt360.com/file/1918218053226168959"
                        ],
                        "questionNo": index,
                        "cateId": 5
                    }
                ],
                "bizCode": "204",
                "homeworkId": 0,
                "assignPoints": False
            }
        else:
            # 如果是选择题，构造选择题的答案数据
            data_to_send = {
                "paperId": contentid,
                "reportId": reportId,
                "platform": "1",
                "questionList": [
                    {
                        "id": question_pid,  # 动态获取选择题的id
                        "myAnswers": [
                            "A"
                        ],
                        "totalSeconds": 14,
                        "questionNo": index,
                        "cateId": 1,
                        "assignPoints": False
                    }
                ],
                "bizCode": "204",
                "homeworkId": 0,
                "assignPoints": False
            }
        
        do_d = auto_do_homework(url_d, params_d, data_to_send, cookies)

    data_get = {
        "paperPackageId": 0,
        "paperId": contentid,
        "reportId": reportId,
        "bizCode": "204",
        "platform": "1",
        "totalSeconds": 14 * index,
        "homeworkId": 0
    }

    do_e = auto_submit_homework(url_e, data_get, cookies)

    # 要发送的数据（将作为查询字符串附加到URL上）
    params = {
        "bizCode": "204",
        "chapterId": "0",
        "classId": "0",
        "homeworkId": "0",
        "paperId": contentid,
        "platform": "1",
        "reportId": reportId,
        "resourceBizType": "0",
        "scheduleId": "0",
        "token": token
    }

    # 调用函数并获取ID列表
    id_list = get_sorted_question_ids(url_a, params, cookies)

    # 初始化结果列表
    right_answers = []

    # 对每个ID分别发起POST请求
    for index, question_id in enumerate(id_list, start=1):
        # 更新数据中的questionId
        data = {
            "paperId": contentid,
            "reportId": reportId,
            "platform": "2",
            "questionId": question_id,
            "bizCode": "204",
            "homeworkId": "0"
        }
        
        # 获取rightAnswer的值
        right_answer = get_right_answer(url, data, cookies)
        
        # 检查答案是否为主观题
        if right_answer and isinstance(right_answer, list) and len(right_answer) == 1 and isinstance(right_answer[0], str):
            # 假设主观题的答案是一个列表，其中包含一个字符串
            answer_content = right_answer[0]
            # 提取文本内容和图片URL
            text_content = re.sub('<.*?>', '', answer_content)
            # 移除所有HTML标签
            text_content = unescape(text_content)  # 将HTML实体转换为对应的字符
        #"""
            image_urls = re.findall('src="([^"]+)"', answer_content)
            print(f"问题{index}: {text_content}")
            for i, img_url in enumerate(image_urls, start=1):
                print(f"  图片{i}: {img_url}")
        else:
            # 正常打印答案
            print(f"问题{index}: {right_answer}")
        #"""
else:
    s = 16

    def extract_answer(html_content, list):
        if not isinstance(html_content, (str, bytes)):
            st.error("提取答案时，html_content 不是字符串或字节流")
            return

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 提取所有被标签包裹的文本内容
        tag_texts = soup.find_all(text=True)

        # 筛选出所有文本内容
        for text in tag_texts:
            # 使用正则表达式提取所有文本内容
            text_parts = re.findall(r'[\s\S]+', text)
            if text_parts:
                list.extend(text_parts)

    def extract_images(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        # 检测并展示图像
        images = soup.find_all('img')
        for img in images:
            src = img.get('src')
            if src:
                try:
                    response = requests.get(src, stream=True)
                    if response.status_code == 200:
                        # 检查内容类型是否为图像
                        content_type = response.headers.get('Content-Type')
                        if 'image' in content_type:
                            st.markdown(f"<div style='width:100%;'>{response.text}</div>", unsafe_allow_html=True)
                        else:
                            st.error(f"链接 {src} 返回的内容类型不是图像: {content_type}")
                    else:
                        st.error(f"无法加载图像: {src} (HTTP状态码: {response.status_code})")
                except Exception as e:
                    st.error(f"无法加载图像: {src} (错误: {e})")
                    st.error("请检查你的网络状态并稍后重试。")
    
    def genshin_launch(contentid, cookies):
        pbar = st.progress(0, text='正在获取答案')
        global sorted_pids, sorted_subjective, index, do_e, do_d, right_answers
        contentid = contentid
        cookies = cookies
        token = cookies.get('token')
        params_b = {
            "paperId": contentid,
            "reportId": "0",
            "platform": "1",
            "bizCode": "204",
            "isRepeat": "1",
            "homeworkId": "0",
            "token": token
        }
        pbar.progress(s * 1, text='get_reportId')
        reportId = get_reportId(url_b, params_b, cookies)

        params_c = {
            "paperId": contentid,
            "reportId": reportId,
            "platform": "1",
            "bizCode": "204",
            "homeworkId": "0",
            "client": "4"
        }
        pbar.progress(s * 2, text='get_questions_list')
        sorted_pids, sorted_subjective = get_questions_list(url_c, params_c, cookies)

        index = 0
        pbar.progress(s * 3, text='auto_do_homework')
        for index, question_pid in enumerate(sorted_pids, start=1):
            params_d = {
                "paperId": contentid,
                "reportId": reportId,
                "platform": "1",
                "questionIds": question_pid,
                "bizCode": "204",
                "homeworkId": "0",
                "token": token
            }

            if sorted_subjective[index - 1]:
                data_to_send = {
                    "paperId": contentid,
                    "reportId": reportId,
                    "platform": "1",
                    "questionList": [
                        {
                            "id": question_pid,
                            "totalSeconds": 14,
                            "attachmentImages": [
                                "http://file.ewt360.com/file/1918218053226168959"
                            ],
                            "questionNo": index,
                            "cateId": 5
                        }
                    ],
                    "bizCode": "204",
                    "homeworkId": 0,
                    "assignPoints": False
                }
            else:
                data_to_send = {
                    "paperId": contentid,
                    "reportId": reportId,
                    "platform": "1",
                    "questionList": [
                        {
                            "id": question_pid,
                            "myAnswers": [
                                "A"
                            ],
                            "totalSeconds": 14,
                            "questionNo": index,
                            "cateId": 1,
                            "assignPoints": False
                        }
                    ],
                    "bizCode": "204",
                    "homeworkId": 0,
                    "assignPoints": False
                }
            
            do_d = auto_do_homework(url_d, params_d, data_to_send, cookies)

        data_get = {
            "paperPackageId": 0,
            "paperId": contentid,
            "reportId": reportId,
            "bizCode": "204",
            "platform": "1",
            "totalSeconds": 14 * index,
            "homeworkId": 0
        }
        pbar.progress(s * 4, text='auto_submit_homework')
        do_e = auto_submit_homework(url_e, data_get, cookies)

        params = {
            "bizCode": "204",
            "chapterId": "0",
            "classId": "0",
            "homeworkId": "0",
            "paperId": contentid,
            "platform": "1",
            "reportId": reportId,
            "resourceBizType": "0",
            "scheduleId": "0",
            "token": token
        }

        pbar.progress(s * 5, text='get_sorted_question_ids')
        id_list = get_sorted_question_ids(url_a, params, cookies)

        right_answers = []
        for index, question_id in enumerate(id_list, start=1):
            data = {
                "paperId": contentid,
                "reportId": reportId,
                "platform": "2",
                "questionId": question_id,
                "bizCode": "204",
                "homeworkId": "0"
            }

            right_answer = get_right_answer(url, data, cookies)
            if right_answer:
                if sorted_subjective[index - 1]:
                    print_answer = []
                    if right_answer:
                        st.success(f"问题{index}的答案:")
                        for answer in right_answer:
                            soup = BeautifulSoup(answer, 'html.parser')
                            text_content = soup.get_text()
                            print_answer.append(text_content)
                            extract_images(answer)
                        for answer_text in print_answer:
                            st.write(answer_text)
                    else:
                        st.error(f"问题{index}: 没有找到主观题答案")
                else:
                    right_answer_print = ''.join(right_answer)
                    st.success(f"问题{index}: {right_answer_print}")
            else:
                st.error(f"问题{index}: 未获取到答案")
        pbar.progress(100, text='答案获取成功！')

