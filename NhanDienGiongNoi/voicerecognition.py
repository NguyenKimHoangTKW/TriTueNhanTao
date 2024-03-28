# Thư viện sử dụng để nhận diện giọng nói | cài đặt pip install SpeechRecognition và pip install pyaudio
import speech_recognition as sr
# Thư viện sử dụng để chuyển văn bản thành giọng nói | cài đặt pip install gtts
from gtts import gTTS
# Thư viện sử dụng để tương tác được với hệ điều hành trên máy tính
import os
# Thư viện sử dụng để lấy thông tin về thời gian hiện tại
from datetime import datetime
# Thư viện sử dụng để phát âm thanh | cài đặt pip install playsound --only-binary :all: và pip install --upgrade pip setuptools
import playsound
# Thư viện sử dụng để mở các trang web
import webbrowser as wb

# Tạo một đối tượng nhận dạng giọng nói
r = sr.Recognizer()
# Hàm speak này để này sử dụng để nhận văn bản và chuyển đổi nó thành giọng nói
def speak(text):
    # Lưu văn bản thành giọng nói vào một tập tin | lang ='vi' là hỗ trợ ngôn ngữ tiếng việt | sử dụng thư viện gTTS để chuyển văn bản thành giọng nói
    tts = gTTS(text=text, lang='vi')
    # Tạo ra 1 file âm thanh và đặt tên là voice.mp3
    filename = 'voice.mp3'
    # Lưu file âm thanh vừa tạo lại
    tts.save(filename)
    
    # Phát giọng nói đã lưu trong file âm thanh voice.mp3
    playsound.playsound(filename)
    # Khi phát xong thì sử dụng thư viện os.remove để yêu cầu máy xóa file voice.mp3 vừa tạo
    os.remove(filename)

# Hàm recognize_speech để giúp sử dụng microphone nhận diện giọng nói
def recognize_speech():
    # Dòng này sử dụng with sr.Microphone() as source: để sử dụng microphone để kiểm tra giọng nói | Dòng này sử dụng thư viện speech_recognition để nhận diện giọng nói
    with sr.Microphone() as source:
        print("Nói điều gì đó đi thưa chủ nhân ...")
        # Khai báo biến audio_data = r.listen ( r là thư viện nhận dạng giọng nói đã  khai báo ở dòng 15) để lặng nghe giọng nói từ source đã lưu giọng nói trong thời gian 5 giây 
        # và sau đó sẽ lưu dữ liệu âm thanh vào biến vừa khai bao audio_data
        audio_data = r.listen(source, timeout=5)
        print("Đang nhận diện giọng nói của chủ nhân ...")

        try:
            # Nhận diện giọng nói bằng Google Speech Recognition và language="vi" để chỉ định ngôn ngữ là tiếng việt và nhận diện giọng nói lưu vào text 
            # ( text này hiểu là sau khi nó nhận được giọng nói ở biến audio_data rồi thì chỗ text = r.recognize_google(audio_data, language="vi") sẽ chuyển văn bản đó thành giọng nói nói)
            # ở chỗ này sử dụng thư viện speech_recognition đã note ở dòng 1 và dòng 15
            text = r.recognize_google(audio_data, language="vi")
            # in ra màn hình kết quả vừa chuyển văn bản thành giọng nói
            print("Chủ nhân đã nói:", text)
            return text
            # sr.UnknownValueError là xử lý nếu không nhận được giọng nói nào và in ra lỗi
        except sr.UnknownValueError:
            print("Xin lỗi chủ nhân, tôi không thể hiểu chủ nhân nói gì.")
            return ""
        except sr.RequestError as e:
            print(f"Thưa chủ nhân, tôi không thể kết nối với dịch vụ nhận diện giọng nói của Google; {e}")
            return ""
# khai báo biến now = datetime.now để lưu dữ liệu thời gian hiện tại
now = datetime.now()
# biến listening này kiểm tra xem chương trình có lắng nghe giọng nói hay ko
listening = False
# sử dụng vòng lặp while True để cho phép người dùng sử dụng liên tục
while True:
    # if not listening: này là điều kiện để lắng nghe có False hày là không, nếu không lắng nghe thì thực hiện lênh trong khối lệnh này
    if not listening:
        # biến này để nhận diện giọng nói, sau đó chuyển giọng nói bằng văn bản và lưu vào biến text | chỗ này sử dụng thư viện dòng 1 và 2
        text = recognize_speech()
        # chỗ if này kiểm tra xem người dùng có thực hiện dòng lệnh nói "Chạy chương trình", nếu người dùng nói "Chạy chương trình"
        # Thì điều kiện listening sẽ bằng true ( nghĩa là nó lắng nghe được yêu cầu)
        # sau đó nó sẽ thoát khỏi khối lệnh từ dòng 60 đến 70 và nó sẽ chạy vào dòng 71 trở đi
        if "chạy chương trình" in text:
            listening = True
            speak("Chào chủ nhân! tôi có thể giúp được gì cho chủ nhân")
    else:
        # Nhận diện giọng nói khi đang lắng nghe ( cái này hoàng giải thích cũng nhiều ở phía trên)
        text = recognize_speech()
        # nếu văn bản text ko có thì sẽ lưu văn bản "Tôi giúp được gì cho chủ nhân!" vào biến  robot_brain
        # Sau đó sẽ sử dụng hàm speak để nó đọc văn bản ( hàm này đã giải thích ở dòng 17 đến 28)
        if text == "":
            robot_brain = "Tôi giúp được gì cho chủ nhân!"
            speak(robot_brain)
        # cái này cũng giống cái trên | in text có nghĩa là kiểm tra cái giọng nói mình đã lưu có giống như cái dòng chữ trong " " ko
        # nếu giống thì nó sẽ nói | chỗ này giải thích tương tự như cái trên
        elif "dự án này là của ai" in text:
            robot_brain = "dự án này là của Chủ nhân Lê Phi Hùng và Nguyễn Phi Hùng"
            speak(robot_brain)
        # cái này cũng vậy | thêm break để kết thúc vòng lặp thôi
        elif "kết thúc chương trình" in text:
            robot_brain = "Tạm biệt chủ nhân, hẹn gặp lại chủ nhân"
            speak(robot_brain)
            break
        elif "Xin chào trợ lý ảo" in text:
            speak("Chủ nhân đã nói 'Xin chào trợ lý ảo' rồi mà, cần giúp gì nữa không?")
        elif "Hôm nay là ngày mấy" in text:
            # Nếu điều kiện trên đúng, chương trình sẽ lấy ngày và giờ hiện tại thông qua biến now 
            # và định dạng theo chuỗi "hôm nay là ngày %d %m %Y" (với %d là ngày, %m là tháng, và %Y là năm). Kết quả sẽ được gán vào biến robot_brain.
            robot_brain = now.strftime("hôm nay là ngày %d %m %Y")
            speak(robot_brain)
        elif "Bây giờ là mấy giờ" in text:
            # Nếu điều kiện trên đúng, chương trình sẽ lấy giờ và phút hiện tại thông qua biến now 
            # và định dạng theo chuỗi "Thưa chủ nhân, bây giờ là %H:%M:%S" (với %H là giờ, %M là phút, và %S là giây). Kết quả sẽ được gán vào biến robot_brain.

            robot_brain = now.strftime("%H:%M:%S")
            speak(robot_brain)
            # từ dòng 91 đến 101 là sử dụng thư viện ở dòng 8 và biến now đã khai báo ở dòng 56

        elif "Mở Google" in text:
            print("Chủ nhân muốn tìm gì?")
            speak("Chủ nhân muốn tìm gì?")
            
            # Sử dụng thời gian làm việc ngắn hạn để người dùng trả lời
            # từ dòng 110 dên 123 là giống dòng 33 đến 54 nãy mới giải thích
            with sr.Microphone() as source:
                audio_data = r.record(source, duration=5)
                try:
                    search = r.recognize_google(audio_data, language="vi")
                except sr.UnknownValueError:
                    search = ""
                    
            if search:
                # Thay vì mở trình duyệt, mở tab mới trong trình duyệt mặc định
                url = f"http://www.google.com/search?q={search}"
                # sử dụng thư viện dòng 12 để mở 1 tab mới
                wb.open_new_tab(url)
                speak(f'Đây là kết quả tìm kiếm cho {search} trên Google thưa Chủ nhân')
            else:
                # nếu ko nói gì cho nó tìm thì nó sẽ chạy dòng này
                speak("Xin lỗi, không thể nhận diện nội dung tìm kiếm của Chủ nhân.")
        elif "Mở Excel" in text:
            # sử dụng thư viện ở dòng 6 để mở tệp có trong máy
            os.system("start excel")  # Mở Microsoft Excel
            speak("Đang mở Microsoft Excel thưa Chủ nhân.")
        elif "Mở Facebook" in text:
            # sử dụng thư viện ở dòng 12 để ở 1 web
            speak("Đang mở Facebook thưa Chủ nhân.")
            wb.get().open("https://www.facebook.com/")
        else:    
            # chỗ này là kiểm tra, nếu như mình nói từ mà không có trong chương trình thì nó sẽ chạy dòng này
            speak("Xin lỗi chủ nhân, từ khóa" + text +"không hỗ trợ trong chương trình")
