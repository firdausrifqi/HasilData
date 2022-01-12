from question import Question


class DASS:
    def __init__(self):
        self.question_num = 0
        self.D_score = 0
        self.A_score = 0
        self.S_score = 0
        self.total = 0

        self.question_bank =[
        Question('Saya merasa bahwa diri saya menjadi marah karena hal-hal sepele','S'),
        Question('Saya merasa bibir saya sering kering','A'),
        Question('Saya sama sekali tidak dapat merasakan perasaan positif','D'),
        Question('Saya mengalami kesulitan bernafas (misalnya: seringkali terengah-engah atau tidak dapat bernafas padahal tidak melakukan aktivitas fisik sebelumnya)','A'),
        Question('Saya sepertinya tidak kuat lagi untuk melakukan suatu kegiatan.','D'),
        Question('Saya cenderung bereaksi berlebihan terhadap suatu situasi','S'),
        Question('Saya merasa goyah (misalnya, kaki terasa mau copot)','A'),
        Question('Saya merasa sulit untuk bersantai','S'),
        Question('Saya menemukan diri saya berada dalam situasi yang membuat saya merasa sangat cemas dan saya akan merasa sangat lega jika semua ini berakhir','A'),
        Question('Saya merasa tidak ada hal yang dapat diharapkan di masa depan','D'),
        Question('Saya menemukan diri saya mudah merasa kesal','S'),
        Question('Saya merasa telah menghabiskan banyak energi untuk merasa cemas','S'),
        Question('Saya merasa sedih dan tertekan','D'),
        Question('Saya menemukan diri saya menjadi tidak sabar ketika mengalami penundaan (misalnya: kemacetan lalu lintas, menunggu sesuatu)','S'),
        Question('Saya merasa lemas seperti mau pingsan','A'),
        Question('Saya merasa saya kehilangan minat akan segala hal','D'),
        Question('Saya merasa bahwa saya tidak berharga sebagai seorang manusia','D'),
        Question('Saya merasa bahwa saya mudah tersinggung','S'),
        Question('Saya berkeringat secara berlebihan (misalnya: tangan berkeringat), padahal temperatur tidak panas atau tidak melakukan aktivitas fisik sebelumnya','A'),
        Question('Saya merasa takut tanpa alasan yang jelas','A'),
        Question('Saya merasa bahwa hidup tidak bermanfaat','D'),
        Question('Saya merasa sulit untuk beristirahat','S'),
        Question('Saya mengalami kesulitan dalam menelan','A'),
        Question('Saya tidak dapat merasakan kenikmatan dari berbagai hal yang saya lakukan','D'),
        Question('Saya menyadari kegiatan jantung, walaupun saya tidak sehabis melakukan aktivitas fisik (misalnya: merasa detak jantung meningkat atau melemah)','A'),
        Question('Saya merasa putus asa dan sedih','D'),
        Question('Saya merasa bahwa saya sangat mudah marah','S'),
        Question('Saya merasa saya hampir panik','A'),
        Question('Saya merasa sulit untuk tenang setelah sesuatu membuat saya kesal.','S'),
        Question('Saya takut bahwa saya akan terhambat oleh tugas-tugas sepele yang tidak biasa saya lakukan','A'),
        Question('Saya tidak merasa antusias dalam hal apapun','D'),
        Question('Saya sulit untuk sabar dalam menghadapi gangguan terhadap hal yang sedang saya lakukan.','S'),
        Question('Saya sedang merasa gelisah','S'),
        Question('Saya merasa bahwa saya tidak berharga','D'),
        Question('Saya tidak dapat memaklumi hal apapun yang menghalangi saya untuk menyelesaikan hal yang sedang saya lakukan.','S'),
        Question('Saya merasa sangat ketakutan','A'),
        Question('Saya melihat tidak ada harapan untuk masa depan','D'),
        Question('Saya merasa bahwa hidup tidak berarti','D'),
        Question('Saya menemukan diri saya mudah gelisah','S'),
        Question('Saya merasa khawatir dengan situasi dimana saya mungkin menjadi panik dan mempermalukan diri sendiri','A'),
        Question('Saya merasa gemetar (misalnya: pada tangan)','A'),
        Question('Saya merasa sulit untuk meningkatkan inisiatif dalam melakukan sesuatu','D'),
        ]

    def next_question(self):
        if (self.question_num < len(self.question_bank) - 5):
            self.question_num += 5


    def get_question_text(self,num):
        return self.question_bank[self.question_num + num].item

    def get_score(self):
        return self.D_score, self.A_score, self.S_score

    def add_score(self, answer):
        self.total += 1
        if answer == 0:
            if self.question_bank[self.question_num].label == 'D':
                self.D_score += 0
            elif self.question_bank[self.question_num].label == 'A':
                self.A_score += 0
            elif self.question_bank[self.question_num].label == 'S':
                self.S_score += 0
        elif answer == 1:
            if self.question_bank[self.question_num].label == 'D':
                self.D_score += 1
            elif self.question_bank[self.question_num].label == 'A':
                self.A_score += 1
            elif self.question_bank[self.question_num].label == 'S':
                self.S_score += 1
        elif answer == 2:
            if self.question_bank[self.question_num].label == 'D':
                self.D_score += 2
            elif self.question_bank[self.question_num].label == 'A':
                self.A_score += 2
            elif self.question_bank[self.question_num].label == 'S':
                self.S_score += 2
        elif answer == 3:
            if self.question_bank[self.question_num].label == 'D':
                self.D_score += 3
            elif self.question_bank[self.question_num].label == 'A':
                self.A_score += 3
            elif self.question_bank[self.question_num].label == 'S':
                self.S_score += 3
        #return(self.D_score, self.A_score, self.)
    def is_finished(self):
        if self.total == len(self.question_bank):
            print("Now returning true")
            return True
        else:
            print("Pertanyaan yang sudah dijawab: " + str(self.total))
            return False

    def reset(self):
        self.question_num = 0