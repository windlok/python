## Soru nesnesi. Her bir soru için numara, metin, şıklar ve doğru cevabı tutar.
class Question:
    # Soru nesnesi oluşturulurken gerekli bilgiler alınır.
    def __init__(self,numara,text,choices,answer):
        self.numara=numara
        self.text =text
        self.choices=choices
        self.answer=answer
    # Kullanıcının verdiği cevabın doğru olup olmadığını kontrol eder.
    def checkAnswer(self ,answer):
        return self.answer==answer

## Quiz nesnesi. Soruları, puanı ve ilerlemeyi yönetir.
class Quiz:
    # Quiz başlatılırken sorular listesi alınır, skor ve index sıfırlanır.
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionsindex=0

    # Şu anki soruyu döndürür.
    def getQuestion(self):
        return self.questions[self.questionsindex]

    # Soruyu ekrana yazdırır, şıkları gösterir ve kullanıcıdan cevap alır.
    def displayQueation(self):
        question = self.getQuestion()
        print(f'Soru {self.questionsindex+1}: {question.text}')
        for q in question.choices:
            print('-'+q)
        answer = input("cevap: ")
        self.guess(answer)
    
    # Kullanıcının cevabını kontrol eder, doğruysa skoru artırır.
    # Sonra bir sonraki soruya geçmek için index'i artırır ve loadQuestion çağrılır.
    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionsindex += 1
        self.loadQuestion()

    # Quiz ilerlemesini kontrol eder. Sorular bittiyse skor gösterir, devam ediyorsa ilerleme ve yeni soru gösterir.
    def loadQuestion(self):
        if len(self.questions) == self.questionsindex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQueation()    
        
    # Quizde kaçıncı soruda olduğunuzu ve toplam soru sayısını gösterir.
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionsindex + 1
        print(f'Soru {questionNumber} / {totalQuestion}')
        

    # Quiz bittiğinde ekrana skorunuzu ve bitiş mesajını yazdırır.
    def showScore(self):
        print("Quiz bitti.")
        print("score: ",self.score)
        
## Sorular oluşturuluyor.
s1=Question("1","2+6 ?",['8','10','6'],"8")
s2=Question("2","2*6 ?",['26','10','12'],"12")
questi=[s1,s2]

## Quiz başlatılıyor.
quiz=Quiz(questi)
quiz.loadQuestion()





"""print(f'{s1.numara}.soru {s1.text}')
c1=input(f'{s1.choices}')
print(s1.checkAnswer(c1))

print(f'{s2.numara}.soru {s2.text}')
c2=input(f'{s2.choices}')
print(s1.checkAnswer(c2))
"""