from flask import Flask
from flask import render_template, url_for, request, redirect, session, flash
import csv
from joblib import load
import numpy as np
import os
from test_dass import DASS
import logging
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret"
nb_model = load('model.joblib')

questions = {}
questions['D_score'] = 0
questions['A_score'] = 0
questions['S_score'] = 0
questions['current_q'] = 1
questions['nama'] = ""

dass = DASS()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hasiltest"
    )

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/info' , methods=['POST', 'GET'])
def info():
    ip_addr = request.remote_addr
    if request.method == 'POST':
        answer = request.form.get('username')
        if not answer:
            flash('Nama Harus DIISI YAAAAA', 'error')
        else:
            
            print(ip_addr)
            ketemu = False
            mycursor = mydb.cursor()

            sql = "SELECT * from user"

            mycursor.execute(sql)
            # get all records
            records = mycursor.fetchall()
            print(records)
            mycursor.close()
            for find in records:
                if ip_addr == find[0] and find[6]==0:
                    ketemu = True
                
            if not ketemu :
                insertsql(ip_addr,answer)

            return redirect(url_for('test'))
    return render_template('info.html',ip_addr=ip_addr)

@app.route('/hasil', methods=['GET'])
def hasil():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    final_features = np.array([questions['D_score'],  questions['A_score'], questions['S_score']])
    prediction = nb_model.predict([final_features])
    if prediction[0] == 'A':
        prediction = 'Jaga Kesehatan Mental'
        explain = 'Tetap jaga Kesehatan mental kamu dan hindari hal yang membuat kamu depressi,anxiety atau stress '
    elif prediction[0] == 'AB':
        prediction = 'Jaga Kesehatan Mental dan Nutrisi Makanan'
        explain = 'konsumsi makanan bergizi seperti alpukat, oatmeal, sayuran, dan dark cokelat untuk mereduce stress dan depresi kamu'
    elif prediction[0] == 'AC':
        prediction = 'Jaga Kesehatan Mental dan Olahraga'
        explain = 'Berolahraga teratur seperti berjalan kaki, aktivitas aerobic dan berenang'
    elif prediction[0] == 'AD':
        prediction = 'Jaga Kesehatan Mental dan Tidur yang Cukup'
        explain = ''
    elif prediction[0] == 'AE':
        prediction = 'Jaga Kesehatan Mental dan Kegiatan yang menyenangkan'
        explain = 'Seperti healing di tempat bernuansa alam, menonton komedi, memasak dan bermain game,'
    elif prediction[0] == 'AF':
        prediction = 'Jaga Kesehatan Mental dan Journaling'
        explain = 'Mencoba membuat journal atau buku harian untuk melatih diri dalam mengeksplorasi pikiran dan perasaan'
    elif prediction[0] == 'AG':
        prediction = 'Jaga Kesehatan Mental dan Yoga'
        explain = ''
    elif prediction[0] == 'AH':
        prediction = 'Jaga Kesehatan Mental dan Meditasi'
        explain = ''
    elif prediction[0] == 'AI':
        prediction = 'Jaga Kesehatan Mental dan Art Terapi'
        explain = 'Seperti menggambar atau melukis, mewarnai gambar dan merangkai bunga...'
    elif prediction[0] == 'AL':
        prediction = 'Jaga Kesehatan Mental dan Terapi Musik'
        explain = 'Mendengarkan musik klasik dapat membuat kamu merasa tenang dan lebih relax'
    elif prediction[0] == 'AM':
        prediction = 'Jaga Kesehatan Mental dan Menggunakan Aroma therapy'
        explain = 'Menggunakan aroma therapy saat tidur seperti esensial oil  akan membantu menenangkan pikiran kamu'
    elif prediction[0] == 'AN':
        prediction = 'Jaga Kesehatan Mental dan Manajemen waktu dengan baik'
        explain = 'Manajemen waktu yang baik dapat mengurangi distress kamu dan jangan terlalu memaksakan diri terhadap aktivitas yang terlalu berat '
    elif prediction[0] == 'AO':
        prediction = 'Jaga Kesehatan Mental dan Gaya Hidup sehat'
        explain = 'Makan makanan yang sehat, Kurangi kafein dan gula, Hindari alkohol, rokok, dan obat-obatan '
    elif prediction[0] == 'HA':
        prediction = 'Meditasi dan Jaga Kesehatan Mental  '
        explain = ''
    elif prediction[0] == 'HB   ':
        prediction = 'Meditasi dan Nutrisi Makanan '
        explain = ''
    elif prediction[0] == 'HC':
        prediction = 'Meditasi dan Olahraga  '
        explain = ''
    elif prediction[0] == 'HD':
        prediction = 'Meditasi dan Tidur yang cukup  '
        explain = ''
    elif prediction[0] == 'HE':
        prediction = 'Meditasi dan Kegiatan yang menyenangkan  '
        explain = ''
    elif prediction[0] == 'HF':
        prediction = 'Meditasi dan Jounaling  '
        explain = ''
    elif prediction[0] == 'HG':
        prediction = 'Meditasi dan Yoga  '
        explain = ''
    elif prediction[0] == 'HI':
        prediction = 'Meditasi dan Art Terapi  '
        explain = ''
    elif prediction[0] == 'HL':
        prediction = 'Meditasi dan Terapi Musik '
        explain = ''
    elif prediction[0] == 'HM':
        prediction = 'Meditasi dan Menggunakan Aroma Terapi '
        explain = ''
    elif prediction[0] == 'HN':
        prediction = 'Meditasi dan Manajemen waktu dengan baik '
        explain = ''
    elif prediction[0] == 'HO':
        prediction = 'Meditasi dan Gaya hidup sehat  '
        explain = ''
    elif prediction[0] == 'IA':
        prediction = 'Art Terapi dan Tetap jaga kesehatan Mental  '
        explain = ''
    elif prediction[0] == 'IB':
        prediction = 'Art Terapi dan Nutrisi Makanan  '
        explain = ''
    elif prediction[0] == 'IC':
        prediction = 'Art Terapi dan Olahraga '
        explain = ''
    elif prediction[0] == 'ID':
        prediction = 'Art Terapi dan Tidur yan cukup '
        explain = ''
    elif prediction[0] == 'IE':
        prediction = 'Art Terapi dan Kegiatan yang menyenangkan '
        explain = ''
    elif prediction[0] == 'IF':
        prediction = 'Art Terapi dan Journaling  '
        explain = ''
    elif prediction[0] == 'IG':
        prediction = 'Art Terapi dan Yoga  '
        explain = ''
    elif prediction[0] == 'IL':
        prediction = 'Art Terapi dan Terapi Musik  '
        explain = ''
    elif prediction[0] == 'IM':
        prediction = 'Art Terapi  dan Menggunakan aroma terapi  '
        explain = ''
    elif prediction[0] == 'IN':
        prediction = 'Art Terapi dan Manajemen waktu dengan baik  '
        explain = ''
    elif prediction[0] == 'IO':
        prediction = 'Art Terapi  dan Gaya hidup sehat '
        explain = ''
    elif prediction[0] == 'KA':
        prediction = 'Tulis kekhawatiran kamu dan Tetap jaga kesehatan Mental  '
        explain = ''
    elif prediction[0] == 'KB':
        prediction = 'Tulis kekhawatiran kamu dan Nutrisi Makanan '
        explain = ''
    elif prediction[0] == 'KC':
        prediction = 'Tulis kekhawatiran kamu dan Olahraga  '
        explain = ''
    elif prediction[0] == 'KD':
        prediction = 'Tulis kekhawatiran kamu dan Tidur yang cukup  '
        explain = ''
    elif prediction[0] == 'KE':
        prediction = 'Tulis kekhawatiran kamu dan Kegiatan yang menyenangkan  '
        explain = ''
    elif prediction[0] == 'KF':
        prediction = 'Tulis kekhawatiran kamu dan Journaling '
        explain = ''
    elif prediction[0] == 'KG':
        prediction = 'Tulis kekhawatiran kamu dan Yoga'
        explain = ''
    elif prediction[0] == 'KH':
        prediction = 'Tulis kekhawatiran kamu dan Meditasi '
        explain = ''
    elif prediction[0] == 'KI':
        prediction = 'Tulis kekhawatiran kamu dan Art Terapi  '
        explain = ''
    elif prediction[0] == 'KJ':
        prediction = 'Tulis kekhawatiran kamu dan Tetap bangun hubungan '
        explain = ''
    elif prediction[0] == 'KL':
        prediction = 'Tulis kekhawatiran kamu dan Terapi Musik'
        explain = ''
    elif prediction[0] == 'KM':
        prediction = 'Tulis kekhawatiran kamu dan Menggunakan Aroma Terapi '
        explain = ''
    elif prediction[0] == 'KN':
        prediction = 'Tulis kekhawatiran kamu dan Manajemen waktu dengan baik '
        explain = ''
    elif prediction[0] == 'KO':
        prediction = 'Tulis kekhawatiran kamu dan Gaya Hidup Sehat'
        explain = ''
    elif prediction[0] == 'PA':
        prediction = 'Latihan pernapasan kamu dan Tetap jaga kesehatan Mental  '
        explain = ''
    elif prediction[0] == 'PB':
        prediction = 'Latihan pernapasan kamu dan Nutrisi Makanan  '
        explain = ''
    elif prediction[0] == 'PC':
        prediction = 'Latihan pernapasan kamu dan Olahraga '
        explain = ''
    elif prediction[0] == 'PD':
        prediction = 'Latihan pernapasan kamu dan Tidur yang cukup  '
        explain = ''
    elif prediction[0] == 'PE':
        prediction = 'Latihan pernapasan kamu dan Kegiatan yang menyenangkan '
        explain = ''
    elif prediction[0] == 'PF':
        prediction = 'Latihan pernapasan kamu dan Journaling  '
        explain = ''
    elif prediction[0] == 'PG':
        prediction = 'Latihan pernapasan kamu dan Yoga '
        explain = ''
    elif prediction[0] == 'PH':
        prediction = 'Latihan pernapasan kamu dan Tetap Meditasi  '
        explain = ''
    elif prediction[0] == 'PI':
        prediction = 'Latihan pernapasan kamu dan Art terapi '
        explain = ''
    elif prediction[0] == 'PJ':
        prediction = 'Latihan pernapasan kamu dan Tetap bangun hubungan  '
        explain = ''
    elif prediction[0] == 'PL':
        prediction = 'Latihan pernapasan kamu dan Terapi musik  '
        explain = ''
    elif prediction[0] == 'PM':
        prediction = 'Latihan pernapasan kamu dan Menggunakan Aroma Terapi  '
        explain = ''
    elif prediction[0] == 'PN':
        prediction = 'Latihan pernapasan kamu dan Manajemen waktu dengan baik '
        explain = ''
    elif prediction[0] == 'PO':
        prediction = 'Latihan pernapasan kamu dan Gaya hidup sehat  '
        explain = ''
    
    #Depresi
    if questions['D_score'] >= 0 and questions['D_score'] <= 9:
        questions['d_score'] = "Normal"
    if questions['D_score'] >= 10 and questions['D_score'] <= 13:
        questions['d_score'] = "Ringan"
    if questions['D_score'] >= 14 and questions['D_score'] <= 20:
        questions['d_score'] = "Sedang"
    if questions['D_score'] >= 21 and questions['D_score'] <= 27:
        questions['d_score'] = "Parah"
    if questions['D_score'] >= 28:
        questions['d_score'] = "Sangat Parah"

    #Ax
    if questions['A_score'] >= 0 and questions['A_score'] <= 7:
        questions['a_score'] = "normal"
    if questions['A_score'] >= 8 and questions['A_score'] <= 9:
        questions['a_score'] = "ringan"
    if questions['A_score'] >= 10 and questions['A_score'] <= 14:
        questions['a_score'] = "sedang"
    if questions['A_score'] >= 15 and questions['A_score'] <= 19:
        questions['a_score'] = "parah"
    if questions['A_score'] >= 20:
        questions['a_score'] = "sangat parah"

    #Stress
    if questions['S_score'] >= 0 and questions['S_score'] <= 14:
        questions['s_score'] = "normal"
    if questions['S_score'] >= 15 and questions['S_score'] <= 18:
        questions['s_score'] = "ringan"
    if questions['S_score'] >= 19 and questions['S_score'] <= 25:
        questions['s_score'] = "sedang"
    if questions['S_score'] >= 26 and questions['S_score'] <= 33:
        questions['s_score'] = "parah"
    if questions['S_score'] >= 33:
        questions['s_score'] = "sangat parah"

    dass = DASS()
    update_to_sql(ip_addr,questions['nama'],questions['D_score'],questions['A_score'],questions['S_score'],questions['d_score'],questions['a_score'],questions['s_score'],prediction,explain)
    dass.reset()
    return render_template('hasil.html', 
    questions=questions, 
    prediction=prediction, 
    explaim=explain,ip_addr=ip_addr
    )


@app.route('/test', methods=['POST', 'GET'])
def test():
    ip_addr = request.environ['REMOTE_ADDR']
    dass.getalldata(ip_addr)
    total = dass.total
    if request.method == 'POST':
        answer = request.form.get('rad')
        answer1 = request.form.get('rad1')
        answer2 = request.form.get('rad2')
        answer3 = request.form.get('rad3')
        answer4 = request.form.get('rad4')
        if not answer:
            flash('Pertanyaan pertama belum dijawab', 'error')
        elif not answer1:
            flash('Pertanyaan kedua belum dijawab', 'error')
        elif not answer2 and total < 40:
            flash('Pertanyaan ketiga belum dijawab', 'error')
        elif not answer3 and total < 40:
            flash('Pertanyaan keempat belum dijawab', 'error')
        elif not answer4 and total < 40:
            flash('Pertanyaan kelima belum dijawab', 'error')
        else:
            if answer:
                dass.add_score(int(answer),ip_addr)
            if answer1:
                dass.add_score(int(answer1),ip_addr)    
            if answer2:
                dass.add_score(int(answer2),ip_addr)
            if answer3:
                dass.add_score(int(answer3),ip_addr)
            if answer4:
                dass.add_score(int(answer4),ip_addr)
            
            dass.next_question(ip_addr)
        
        if dass.is_finished(ip_addr):
            questions['D_score'],  questions['A_score'], questions['S_score'], questions['nama'] = dass.get_score(ip_addr)
            return redirect(url_for('hasil'))
    qnum = 42
    quest = dass.question_num
    print(quest)
    qnum = qnum - quest
    if(qnum == 2):
        return render_template('test.html',
                            quest_num=qnum,
                            question_num=dass.question_num + 2,
                            total_num=len(dass.question_bank),
                            question=dass.get_question_text(0),
                            question1=dass.get_question_text(1),ip_addr=ip_addr) 
    else:
        return render_template('test.html',
                                quest_num=qnum,
                                question_num=dass.question_num + 5,
                                total_num=len(dass.question_bank),
                                question=dass.get_question_text(0),
                                question1=dass.get_question_text(1),
                                question2=dass.get_question_text(2),
                                question3=dass.get_question_text(3),
                                question4=dass.get_question_text(4),ip_addr=ip_addr)

#MYSQL FUNCTION
def insertsql(ip,nama):
    cur = mydb.cursor()
    cur.execute("INSERT INTO user (IP,nama) VALUES (%s,%s)", (
        ip,nama
    ))
    mydb.commit()

def update_to_sql(dat0,dat1,dat2,dat3,dat4,dat5,dat6,dat7,dat8,dat9):
    mycursor = mydb.cursor()

    sql = "INSERT INTO depresi (IP,nama,Score_Depresi, Score_Anxiety, Score_Stress, TK_Depresi, TK_Anxiety, TK_Stress, Prediksi, Penjelasan) VALUES (%s,%s, %s,%s, %s,%s, %s,%s,%s,%s)"
    val = (dat0,dat1,dat2,dat3,dat4,dat5,dat6,dat7,dat8,dat9)

    mycursor.execute(sql, val)

    mydb.commit()

#SETTING HOST
if __name__ == "__main__":
   app.run(host="0.0.0.0", port = 80)
