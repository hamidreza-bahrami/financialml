import streamlit as st
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import time

st.set_page_config(page_title='مشاور مالی هوشمند - RoboAi', layout='centered', page_icon='🤖')

def load_model():
    with open('saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data1 = load_model()

rfc = data1['model']
x = data1['x']

def show_page():
    st.write("<h2 style='text-align: center; color: blue;'>مشاور اقتصادی هوشمند 📊</h2>", unsafe_allow_html=True)
    st.write("<h5 style='text-align: center; color: gray;'>Robo-Ai.ir طراحی شده توسط</h5>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")

    with st.sidebar:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(' ')
        with col2:
            st.image('img.png')
        with col3:
            st.write(' ')
        st.divider()
        st.write("<h4 style='text-align: center; color: black;'>مشاوره مالی و اعتباری با هوش مصنوعی 🎯</h4>", unsafe_allow_html=True)
        st.write("<h4 style='text-align: center; color: gray;'>پیش بینی احتمال رشد یا ورشکستگی کسب و کار اینترنتی شما</h4>", unsafe_allow_html=True)
        st.write("<h4 style='text-align: center; color: gray;'>از جنبه های مالی و اعتباری</h4>", unsafe_allow_html=True)
        st.write("<h4 style='text-align: center; color: gray;'>به همراه ارائه راه حل های پیشنهادی</h4>", unsafe_allow_html=True)
        st.divider()
        st.write("<h5 style='text-align: center; color: black;'>طراحی و توسعه</h5>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: center; color: black;'>حمیدرضا بهرامی</h5>", unsafe_allow_html=True)
    
    container = st.container(border=True)
    container.write("<h6 style='text-align: right; color: gray;'>بررسی احتمال موفقیت یا شکست کسب و کار اینترنتی شما 📋</h6>", unsafe_allow_html=True)
        
    g = ('مرد' , 'زن')
    g = st.selectbox('مشتری های شما اغلب مرد هستند یا زن؟', g)
    if g == 'مرد':
        gender = 1.0
    else:
        gender = 0.0

    p = ('بله' , 'خیر')
    p = st.selectbox('مشتری های شما شریک دارند؟', p)
    if p == 'بله':
        Partner = 1.0
    else:
        Partner = 0.0

    d = ('بله' , 'خیر')
    d = st.selectbox('مشتری های شما ، واسطه بین شما و دیگران هستند؟ به این معنا که خدمات یا کالای شما را به بقیه می فروشند؟', d)
    if d == 'بله':
        Dependents = 1.0
    else:
        Dependents = 0.0

    tenure = st.slider('هر مشتری چند ماه با کسب و کار شما همراه است؟', 0.0, 72.0, 1.0)

    ps = ('بله' , 'خیر')
    ps = st.selectbox('آیا در کسب و کار خود با مشتری ها تماس می گیرید؟', ps)
    if ps == 'بله':
        PhoneService = 1.0
    else:
        PhoneService = 0.0

    ml = ('یک راه' , 'بیش از یک راه')
    ml = st.selectbox('چند راه ارتباطی با مشتری ها دارید؟', ml)
    if ml == 'بله':
        MultipleLines = 1.0
    else:
        MultipleLines = 0.0

    ins = ('فیبر نوری' , 'DSL')
    ins = st.selectbox('اینترنت مورد استفاده ی مشتریان شما چیست؟', ins)
    if ins == 'بله':
        InternetService = 1.0
    else:
        InternetService = 0.0

    ons = ('بله' , 'خیر')
    ons = st.selectbox('آیا امنیت مشتریان خود را در فضای مجازی تامین کرده اید؟', ons)
    if ons == 'بله':
        OnlineSecurity = 1.0
    else:
        OnlineSecurity = 0.0

    onb = ('بله' , 'خیر')
    onb = st.selectbox('آیا از داده ها و سرویس مشتریان خود بطور مستمر نسخه پشتیبان تهیه می کنید؟', onb)
    if onb == 'بله':
        OnlineBackup = 1.0
    else:
        OnlineBackup = 0.0

    ts = ('بله' , 'خیر')
    ts = st.selectbox('آیا کسب و کار شما پشتیبانی فنی برای مشتریان دارد؟', ts)
    if ts == 'بله':
        TechSupport = 1.0
    else:
        TechSupport = 0.0

    c = ('یک ماهه' , 'سالانه', 'بیش از یک سال')
    c = st.selectbox('قرارداد مشتریان با شما چند ماهه/سالانه است؟', c)
    if c == 'یک ماهه':
        Contract = 0.0
    elif c == 'سالانه':
        Contract = 1.0
    else:
        Contract = 2.0

    pb = ('اینترنتی' , 'کاغذی')
    pb = st.selectbox('صورتحسابی که به مشتریان می فرستید ، اینترنتی است یا کاغذی؟', pb)
    if pb == 'بله':
        PaperlessBilling = 1.0
    else:
        PaperlessBilling = 0.0

    pm = ('اینترنتی' , 'چک نقدی', 'کسر از حساب')
    pm = st.selectbox('روش تسویه حساب شما چگونه است؟', pm)
    if pm == 'اینترنتی':
        PaymentMethod = 0.0
    elif pm == 'چک نقدی':
        PaymentMethod = 1.0
    else:
        PaymentMethod = 2.0

    MonthlyCharges = st.slider('هزینه ای که بطور میانگین ، بصورت ماهانه از مشتریان دریافت می کنید چقدر است؟ (مبلغ به دلار)', 18.25, 118.75, 19.0)    
    container = st.container(border=True)
    if MonthlyCharges:
        toman = MonthlyCharges * 45000
        container.write("<h6 style='text-align: right; color: gray;'>:مبلغ به تومان برابر است با</h6>", unsafe_allow_html=True)
        container.markdown(toman)
    
    button = st.button('پیش بینی رشد / نزول')
    if button:
        with st.chat_message("assistant"):
                with st.spinner('''درحال بررسی لطفا صبور باشید'''):
                    time.sleep(2)
                    st.success(u'\u2713''تحلیل انجام شد')
                    x = np.array([[gender, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity,
                                   OnlineBackup, TechSupport, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges]])
                    
        x = x.astype(float)
        y = rfc.predict(x)
        if y == 1:
            text1 = 'بر اساس تحلیل من ، کسب و کار اینترنتی شما در حال پسرفت است'
            text2 = 'ادامه ی روند به شکل بالا ، موجب از دست دادن مشتریان و کاهش درآمد شما خواهد شد'
            def stream_data1():
                for word in text1.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)
            def stream_data2():
                for word in text2.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data2)

        elif y == 0:
            text1 = 'بر اساس تحلیل من ، کسب و کار اینترنتی شما در وضعیت مناسبی بوده و جای نگرانی نیست'
            text2 = 'در صورت ادامه ی کار به شکل بالا ، شاهد رشد کسب و کار خود در درازمدت خواهید بود'
            def stream_data1():
                for word in text1.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)
            def stream_data2():
                for word in text2.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data2)

    st.divider()

    container = st.container(border=True)
    container.write("<h6 style='text-align: right; color: gray;'>تحلیل نقاط قوت و ضعف کسب و کار اینترنتی شما ⚡</h6>", unsafe_allow_html=True)
    button01 = st.button('تحلیل کسب و کار')

    text01 = '''طبق تحقیقات ، مشتری های خانم راحت تر خرید می کنند و مشتری های آقا در موعد مقرر ، قسط های خود را پرداخت می کنند. 
            هر کدام از این دو دسته خصوصیات خود را دارند'''
    
    text02 = '''طبق تحقیقات ، مشتری های خانم راحت تر خرید می کنند و مشتری های آقا در موعد مقرر ، قسط های خود را پرداخت می کنند. 
            هر کدام از این دو دسته خصوصیات خود را دارند'''
    
    text03 = '''این بخش از کسب و کارتان ، مانند یکی از موارد قبلی ، دست شما نیست.
            کسب و کار شما ممکن است عمده فروشی باشد ، در این صورت احتمال اینکه مشتریان شما شریک داشته باشند ، بالاتر است.
            داشتن آگاهی از این موضوع می تواند سودمند باشد ؛ هرچقدر اجناس و خدمات کسب و کار شما ، پایه ای تر و عمده تر باشد ، شرکای مشتریان شما بیشتر خواهد بود و برعکس.
            در پرداخت های مالی ، بهتر است طرف حساب شما یک مشتری که نماینده اشخاص دیگر است باشد تا مجبور نباشید به دیگران مراجعه کنید
            '''

    text04 = '''گاهی یک مشتری کالای عمده‌ی خود را از شما تهیه کرده و در کسب و کار خود به فروش می رساند.
            در این حالت می گوییم مشتری شما واسطه بین شما و دیگران است.
            این مورد هم مانند مورد قبلی ، برای کسب و کارهایی که محصولات و خدمات پایه و عمده دارند ، رایج است.
            این مورد به نفع شما است ، تنها کاری که باید بکنید ، تبلیغات بیشتر است
            '''

    text05 = '''باید برای جلب اعتماد مشتریان و افزایش فروش با آن ها تماس بگیرید. این تماس می تواند در قالب یک مکالمه تلفنی یا چت کردن از طریق ایتا یا تلگرام باشد.
            مشتریان باید متوجه حضور شما شوند تا با خیال راحت تر هزینه های خود را پرداخت کنند. از طریق تماس تلفنی می توانید محصولات و خدمات جدید را هم به آن ها معرفی کرده و فروش خود را بیشتر کنید'''

    
    text06 = ''' بر اساس آنچه فهمیدم ، شما با مشتریان تماس می گیرید و این یکی از مزیت های کسب و کار اینترنتی شماست. این روش را ادامه دهید''' 
    
    
    text07 = '''شما راه ارتباطی کافی برای مشتریان و کاربران تامین نکرده اید. باید از جانب خود برای مشتری راه ارتباطی تامین کنید.
            هرچقدر کاربران راحت تر به شما دسترسی داشته باشند ، راحت تر به شما ، خدمات و کالاهای شما اعتماد می کنند و بیشتر خرید می کنند.
            همچنین داشتن راه های ارتباطی بیشتر از طرف مشتریان ، باعث راحتی و تسریع دسترسی شما به آن ها می گردد.
            بدین شکل در صورت قطعی تلفن آن ها ، می توانید تبلیغ یا محتوای خود را به ایمیل آن ها ارسال کنید
            '''
    
    text08 = '''شما راه های ارتباطی مناسبی برای برقراری ارتباط با کاربران و مشتریان دارید.
            سعی کنید از طریق همه ی آن ها با مشتریان خود در ارتباط باشید
            '''

    text09 = '''این بخش هم دست شما نیست.
            شما بعنوان مالک کسب و کار تسلطی بر نوع ، سرعت و کیفیت اینترنت مشتریان ندارید ، اما آگاهی از آن می تواند سودمند باشد.
            فیبر نوری پرسرعت ترین ، اینترنت سیم کارت دارای سرعت متوسط و اینترنت خانگی دارای کمترین سرعت در میان اینترنت های موجود در ایران است.
            تحقیقات نشان داده که هرچقدر سرعت اینترنت کاربران بیشتر باشد ، احتمال بازدید از سایت ، پرداخت موفق و موارد مشابه بیشتر است.
            '''

    text10 = '''منظور از تامین امنیت اطلاعات مشتری ، حفظ و نگهداری اطلاعات شخصی و بانکی مشتریان است.
            کسب و کار شما باید هرچه سریع تر به ابزارهای تامین امنیت مانند گواهینامه امنیتی اس اس ال ، نماد اعتماد و موارد مشابه مجهز گردد
            '''

    text11 = '''اگر کسب و کار شما بخوبی امنیت اطلاعات کاربران را تامین می کند ، جای نگرانی نیست''' 


    text12 = '''تهیه نسخه پشتیبان برای کسب و کارهای اینترنتی ضروری است ، بخصوص اگر بطور مستقیم با اطلاعات مشتریان سر و کار دارید ، مانند شرکت های هاستینگ.
            تهیه یا اجاره یک سرور اضافه برای ذخیره خودکار اطلاعات کاربران ، بصورت هفتگی ، موجب جلب توجه و افزایش اعتماد مردم و مشتریان خواهد شد '''

    
    text13 = '''کسب و کار شما دارای سیستم ذخیره اتوماتیک یا دستی نسخه پشتیبان بوده و این یک مزیت مهم برای کسب و کار شماست'''


    text14 = '''مشتریان به پشتیبانی فنی نیاز دارند ، مخصوصا اگر کار شما فنی و مهندسی باشد یا بخشی از کار به عهده مشتری باشد.
            بهتر است در اطلاعات موجود در سایت یا کانال ، درمورد پشتیبانی هم اطلاع رسانی کنید'''


    text15 = '''کسب و کارشما دارای پشتیبانی فنی بوده و این عالی است'''

    text16 = '''نحوه پرداخت یا بازه زمانی دریافت هزینه از مشتریان به میزان پولی که در کسب و کار خرج می کنید بستگی دارد.
            اگر در شروع کار برای مشتری به حجم بالایی از پول نیاز دارید ، بهتر است مبالغ را سالیانه دریافت کنید.
            در غیر این صورت بهتر است هزینه را بصورت ماهانه دریافت کنید.
            پیشنهاد من دریافت بصورت ماهانه و مدیریت درست دریافتی ها است چون مشتری ها با این زمان بندی راحت تر هستند
            '''


    text17 = '''صورتحساب کاغذی برای کسب و کارهای حضوری مانند فروشگاه های مواد غذایی یک مزیت محسوب می شود اما برای کسب و کار اینترنتی یک پسرفت است. لطفا صورتحساب کاغذی را به صورتحساب اینترنتی تغییر بدهید'''

    text18 = '''صورتحساب اینترنتی که به پرداخت اینترنتی منجر می شود ، بهترین راه برای ارائه صورتحساب هزینه ها به مشتریان است'''

    text19 = '''کسب و کار اینترنتی شما پرداخت اینترنتی ندارد.  در دنیای امروز راحتی و سرعت حرف اول را می زند. دریافت چک بصورت نقدی ، زمان بر و سنتی است. کسر از حساب بدون اطلاع مشتری هم عمل شایسته ای نیست. حتی ممکن است مشتری پول کافی در حساب خود نداشته باشد. لطفا برای انجام پرداخت ها توسط مشتری به راه اندازی درگاه پرداخت اینترنتی اقدام کنید و راه های دیگر تسویه را کنار بگذارید ، وگرنه در کوتاه مدت شاهد ریزش بیشتر مشتری ها خواهید بود'''

    text20 = '''اگر کسب و کار شما دارای درگاه پرداخت اینترنتی فعال است ، جای هیچ نگرانی نیست'''



    if button01:
        text00 = '''💡 اطلاعاتی که با تحلیل پرسشنامه شما بدست آوردم'''
        def stream_data1():
            for word in text00.split(" "):
                yield word + " "
                time.sleep(0.09)
        st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>جنسیت مشتریان 👨🏻‍💼👩🏻‍💼</h6>", unsafe_allow_html=True)

        if gender == 0.0 or 1.0:
            def stream_data1():
                for word in text01.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>شریک داشتن مشتریان 🤝🏻</h6>", unsafe_allow_html=True)

        if Partner == 0.0 or 1.0:
            def stream_data1():
                for word in text03.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)
        
        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>واسطه گری مشتریان 🔗</h6>", unsafe_allow_html=True)

        if Dependents == 0.0 or 1.0:
            def stream_data1():
                for word in text04.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'> تماس با مشتریان 📞</h6>", unsafe_allow_html=True)

        if PhoneService == 0.0:
            def stream_data1():
                for word in text05.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        if PhoneService == 1.0:
            def stream_data1():
                for word in text06.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'> تعداد راه های ارتباطی با مشتریان 📱📧</h6>", unsafe_allow_html=True)

        if MultipleLines == 0.0:
            def stream_data1():
                for word in text07.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        if MultipleLines == 1.0:
            def stream_data1():
                for word in text08.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>اینترنت مشتریان🔌</h6>", unsafe_allow_html=True)

        if InternetService == 0.0 or 1.0:
            def stream_data1():
                for word in text09.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>امنیت اطلاعات مشتریان 🔒</h6>", unsafe_allow_html=True)

        if OnlineSecurity == 0.0:
            def stream_data1():
                for word in text10.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        if OnlineSecurity == 1.0:
            def stream_data1():
                for word in text11.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>تهیه نسخه پشتیبان از اطلاعات مشتریان 💾</h6>", unsafe_allow_html=True)

        if OnlineBackup == 0.0:
            def stream_data1():
                for word in text12.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        if OnlineBackup == 1.0:
            def stream_data1():
                for word in text13.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>پشتیبانی فنی از مشتریان 👷🏻</h6>", unsafe_allow_html=True)

        if TechSupport == 0.0:
            def stream_data1():
                for word in text14.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        if TechSupport == 1.0:
            def stream_data1():
                for word in text15.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>مهلت پرداخت مشتریان 💲⏱️</h6>", unsafe_allow_html=True)

        if Contract == 0.0 or 1.0 or 2.0:
            def stream_data1():
                for word in text16.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>نوع صورتحساب 📝</h6>", unsafe_allow_html=True)

        if PaperlessBilling == 0.0:
            def stream_data1():
                for word in text17.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        if PaperlessBilling == 1.0:
            def stream_data1():
                for word in text18.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        container = st.container(border=True)
        container.write("<h6 style='text-align: right; color: gray;'>روش تسویه حساب مشتریان 💱</h6>", unsafe_allow_html=True)

        if PaymentMethod == 0.0:
            def stream_data1():
                for word in text19.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

        if PaymentMethod == 1.0 or 2.0:
            def stream_data1():
                for word in text20.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)

show_page()
