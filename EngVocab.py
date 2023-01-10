from tkinter import *
from random import * 
from PIL import ImageTk, Image

root = Tk()
root.title('English Vocabulary')


#image
next_img = ImageTk.PhotoImage(Image.open('next.png'))
prev_img = ImageTk.PhotoImage(Image.open('prev.png'))


all_word = ['']
all_api = ['']
all_vocab = ['']
all_mean = ['']
all_topic = ['']
all_length = ['']
all_lesson_img = []
all_lesson_contain = []


def add_all(word, api, vocab, mean, topic):
    all_word.append(word)
    all_api.append(api)
    all_vocab.append(vocab)
    all_mean.append(mean)
    all_topic.append(topic)
    all_length.append(len(vocab))



def vocab(word, api):
    vocab = []
    for i in range(len(word)):
        vocab.append(word[i] + '\n' + api[i])
    return vocab



def image(lesson, mean):
    img = []
    for i in range(1, len(mean) + 1):
        my_img = ImageTk.PhotoImage(Image.open('img_unit' + str(lesson) + '/' + str(i) + '.png'))
        img.append([my_img, mean[i - 1]])
    return img



def lay_out(word):
    word_list = []
    for sentence in word:
        index = 0
        while index + 36 < len(sentence):
            if '\n' in sentence[index+1:index+37]:
                index = sentence.index('\n',index+1, index+37)

            if index + 36 >= len(sentence):
                break
            else:
                index += 36

            while sentence[index] != ' ':
                index -= 1
            sentence = sentence[:index] + '\n' + sentence[index+1:]
        word_list.append(sentence)
    return word_list




#Datasets

word_1 = ['niece', 'nephew', 'sister-in-law', 'brother-in-law', 'mother-in-law',
'father-in-law', 'son', 'grandson', 'daughter', 'granddaughter',
'husband', 'wife', 'cousin', 'great-aunt', 'great-uncle',
'great-grandfather', 'great-grandmother', 'great-grandparents', 'son-in-law', 'daughter-in-law']

api_1 = ['/niːs/', '/ˈnef.juː/', '/ˈsɪs.tɚ.ɪn.lɑː/', '/ˈbrʌð.ɚ.ɪn.lɑː/', '/ˈmʌð.ɚ.ɪn.lɑː/',
'/ˈfɑː.ðɚ.ɪn.lɑː/', '/sʌn/', '/ˈɡræn.sʌn/', '/ˈdɑː.t̬ɚ/', '/ˈɡræn.dɑː.t̬ɚ/',
'/ˈhʌz.bənd/', '/waɪf/', '/ˈkʌz.ən/', '/ˌɡreɪt ˈænt/', '/ˌɡreɪt ˈʌŋ.kəl/',
'/ˌɡreɪtˈɡræn.fɑː.ðɚ/', '/ˌɡreɪtˈɡræm.mʌð.ər/', '/ˌɡreɪtˈɡræn.per.ənt/', '/ˈsʌn.ɪn.lɑː/', '/ˈdɑː.t̬ɚ.ɪn.lɑː/']

vocab_1 = vocab(word_1, api_1)

mean_1 = ['cháu gái of (uncle/aunt)', 'cháu trai of (uncle/aunt)', 'chị/em dâu', 'anh/em rể', 'mẹ chồng/vợ',
'bố chồng/vợ', 'con trai', 'cháu trai của ông bà', 'con gái', 'cháu gái của ông bà',
'chồng', 'vợ', 'anh chị em họ', 'bà cô (chị/em của ông)', 'ông chú (anh/em của ông)',
'ông cố', 'bà cố', 'ông bà cố', 'con rể', 'con dâu']

topic_1 = 'The family'

add_all(word_1, api_1, vocab_1, mean_1, topic_1)








word_2 = ['widowed', 'divorced', 'bride', 'groom', 'honeymoon',
'died of', 'the funeral']

api_2 = ['/ˈwɪd.oʊd/', '/dɪˈvɔːrst/', '/braɪd/', '/ɡruːm/', '/ˈhʌn.i.muːn/',
'/daɪd əv/', '/ˈfjuː.nɚ.əl/']

vocab_2 = vocab(word_2, api_2)

mean_2 = ['góa', 'đã ly hôn', 'cô dâu', 'chú rể', 'tuần trăng mật',
'chết bởi', 'đám tang']

topic_2 = 'Birth, marriage and death'

add_all(word_2, api_2, vocab_2, mean_2, topic_2)








word_3 = ['forehead', 'eyebrows', 'eyelashes', 'eyelids', 'neck',
'iris', 'acne', 'pore', 'wrinkle', 'chin',
'cheek', 'tongue', 'thumb', 'knee', 'chest',
'breast', 'stomach', 'side', 'back', 'waist',
'hip', 'liver', 'lungs', 'intestine', 'saliva',
'sweat']

api_3 = ['/ˈfɔː.hed/', '/ˈaɪ.braʊ/', '/ˈaɪ.læʃ/', '/ˈaɪ.lɪd/', '/nek/',
'/ˈaɪ.rɪs/', '/ˈæk.ni/', '/pɔːr/', '/ˈrɪŋ.kəl/', '/tʃɪn/',
'/tʃiːk/', '/tʌŋ/', '/θʌm/', '/niː/', '/tʃest/',
'/brest/', '/ˈstʌm.ək/', '/saɪd/', '/bæk/', '/weɪst/',
'/hɪp/', '/ˈlɪv.ɚ/', '/lʌŋ/', '/ɪnˈtes.tɪn/', '/səˈlaɪ.və/',
'/swet/']

vocab_3 = vocab(word_3, api_3)

mean_3 = ['trán', 'lông mày', 'lông mi', 'mí mắt', 'cái cổ',
'con ngươi', 'mụn', 'lổ chân lông', 'nếp nhăn', 'cái cằm',
'gò má', 'cái lưỡi', 'ngón cái', 'đầu gối', 'ngực (nam/nữ)',
'ngực (nữ)', 'cái bụng', 'sườn', 'lưng', 'cái eo',
'cái hông', 'gan', 'phổi', 'ruột', 'nước miếng',
'mồ hôi']

topic_3 = 'Parts of the body'

add_all(word_3, api_3, vocab_3, mean_3, topic_3)








img_4 = []

word_4 = ['abaya', 'anorak', 'apparel', 'apron', 'ascot tie',
'attire', 'balaclava', 'ball gown', 'bandanna', 'baseball cap',
'bathing suit', 'battledress', 'beanie', 'beret', 'bell-bottoms',
'belt', 'bonnet', 'Bermuda shorts', 'bib', 'blazer',
'bloomers', 'blouse', 'bao', 'boot', 'bow',
'bow tie', 'boxer shorts', 'boxers', 'bra', 'bracelet',
'leather jacket', 'breeches', 'briefs', 'buckle', 'button',
'button-down shirt', 'caftan', 'camisole', 'camouflage', 'cap',
'cap and gown', 'cape', 'capris', 'cardigan', 'chemise',
'cloak', 'clogs', 'clothing', 'coat', 'collar',
'corset', 'zoris', 'coveralls', 'cowboy boots', 'cowboy hat',
'cravat', 'crown', 'cuff', 'cufflinks', 'culottes',
'cummerbund', 'dashiki', 'diaper', 'dinner jacket', 'dirndl',
'drawers', 'dress', 'dress shirt', 'windbreaker', 'dungarees',
'earmuffs', 'earrings', 'zipper', 'wrap', 'wig',
'fatigues', 'fedora', 'fez', 'flak jacket', 'flannel shirt',
'flip-flops', 'wetsuit', 'frock', 'fur', 'fur coat',
'gabardine', 'gaiters', 'galoshes', 'waistcoat', 'wedding gown',
'tuxedo (tux)', 'waders', 'Wellingtons', 'gilet', 'visor',
'glasses', 'gloves', 'gown', 'halter top', 'handbag',
'handkerchief', 'hat', 'Hawaiian shirt', 'hazmat suit', 'headscarf',
'helmet', 'vest', 'high heels', 'hoodie', 'hook and eye',
'veil', 'uniform', 'hospital gown', 'toga', 'housecoat',
'jacket', 'jeans', 'jersey', 'jewelry', 'jodhpurs',
'jumper', 'jumpsuit', 'kerchief', 'khakis', 'kilt',
'kimono', 'twinset', 'tweed jacket', 'lab coat', 'tutu']

api_4 = ['/əˈbaɪ.ə/', '/ˈæn.ə.ræk/', '/əˈper.əl/', '/ˈeɪ.prən/', '/ˈæs.kɑːt taɪ/',
'/əˈtaɪr/', '/ˌbæl.əˈklɑː.və/', '/bɑːl ɡaʊn/', '/bænˈdæn.ə/', '/ˈbeɪs.bɑːl kæp/',
'/ˈbeɪ.ðɪŋ suːt/', '/ˈbæt̬.əl.dres/', '/ˈbiː.ni/', '/bəˈreɪ/', '/ˈbel.bɑː.t̬əmz/',
'/belt/', '/ˈbɑː.nɪt/', '/bɚˈmjuː.də ʃɔːrts/', '/bɪb/', '/ˈbleɪ.zɚ/',
'/ˈbluː.mɚs/', '/blaʊs/', '/ˈboʊ.ə/', '/buːt/', '/baʊ/',
'/baʊ taɪ/', '/ˈbɑːk.sɚ ʃɔːrts/', '/ˈbɑːk.sɚ /', '/brɑː/', '/ˈbreɪ.slət/',
'/ˈleð.ɚ ˈdʒæk.ɪt/', '/ˈbrɪtʃ.ɪz/', '/brifs/', '/ˈbʌk.əl/', '/ˈbʌt̬.ən/',
'/ˈbʌt·ənˌdɑʊn ʃɝːt/', '/ˈkæf.tæn/', '/ˈkæm.ɪ.soʊl/', '/ˈkæm.ə.flɑːʒ/', '/kæp/',
'/kæp ænd ɡaʊn/', '/keɪp/', '/kəˈpriːz/', '/ˈkɑːr.dɪ.ɡən/', '/ʃəˈmiːz/',
'/kloʊk/', '/klɑːɡs/', '/ˈkloʊ.ðɪŋ/', '/koʊt/', '/ˈkɑː.lɚ/',
'/ˈkɔːr.sət/', ' /ˈzôrē/', '/ˈkʌv.ɚ.ɑːlz/', '/ˈkaʊ.bɔɪ  buːts/', '/ˈkaʊ.bɔɪ hæt/',
'/krəˈvæt/', '/kraʊn/', '/kʌf/', '/ˈkʌf.lɪŋks/', '/ˈkuː.lɑːts/',
'/ˈkʌm.ɚ.bʌnd/', '/ˈdɑː ʃɪkɪ/', ' /ˈdaɪ.pɚ/', '/ˈdɪn.ɚ ˈdʒæk.ɪt/', '/ˈdɝːn.dəl/',
' /drɑːrs/', '/dres/', '/dres ʃɝːt/', '/ˈwɪndˌbreɪ.kɚ/', '/ˌdʌŋ.ɡəˈriːz/',
'/ˈɪr.mʌfs/', '/ˈɪr.ɪŋs/', '/ˈzɪp.ɚ/', '/ræp/', '/wɪɡ/',
'/fəˈtiɡz/', '/fəˈdɔːr.ə/', '/fez/', '/ˈflæk ˌdʒæk.ɪt/', '/ˈflæn.əl ʃɝːt/',
'/ˈflɪp.flɑːps/', '/ˈwet.suːt/', '/frɑːk/', '/fɝː/', '/fɝː koʊt/',
' /ˈɡæb.ɚ.diːn/', '/ˈɡeɪ.t̬ɚz/', '/ɡəˈlɑː.ʃɪz/', '/ˈweɪs.koʊt/', '/ˈwed.ɪŋ ɡaʊn/',
'/tʌkˈsiː.doʊ/', '/ˈweɪ.dɚs/', '/ˈwel.ɪŋ.tən/', '/ˈdʒɪl.eɪ/', '/ˈvaɪ.zɚ/',
'/ˈɡlæs·əz/', '/ɡlʌvs/', '/ɡaʊn/', '/ˈhɑːl.t̬ɚ tɑːp/', '/ˈhænd.bæɡ/',
'/ˈhæŋ.kɚ.tʃiːf/', '/hæt/', '/həˌwaɪ.ən ˈʃɝːt/', '/ˈhæz.mæt suːt/', '/ˈhed.skɑːrf/',
'/ˈhel.mət/', '/vest/', '/ˌhaɪ ˈhiːlz/', '/ˈhʊd.i/', '/hʊk ən aɪ/',
'/veɪl/', '/ˈjuː.nə.fɔːrm/', '/ˈhɑː.spɪ.t̬əl ɡaʊn/', '/ˈtoʊ.ɡə/', '/ˈhaʊs.koʊt/',
'/ˈdʒæk.ɪt/', '/dʒiːnz/', '/ˈdʒɝː.zi/', '/ˈdʒuː.əl.ri/', '/ˈdʒɑːd.pɚz/',
'/ˈdʒʌm.pɚ/', '/ˈdʒʌmp.suːt/', '/ˈkɝː.tʃɪf/', '/ˈkɑː.ki/', '/kɪlt/',
'/kəˈmoʊ.noʊ/', '/ˈtwɪn.set/', '/twiːd ˈdʒæk.ɪt/', '/læb koʊt/', '/ˈtuː.tuː/']

mean_4 = vocab(word_4, api_4)

img_4 = image(4, mean_4)

topic_4 = 'Clothes'

add_all(word_4, api_4, img_4, mean_4, topic_4)

all_lesson_img.append(4)





word_5 = ['abuse', 'acrimonious', 'aggression', 'agitate', 'antagonism',
'bristle', 'exasperated', 'confrontational','cranky', 'crotchety', 'disgruntled',
'enrage']

api_5 = ['/əˈbjuːz/', '/ˌæk.rəˈmoʊ.ni.əs/', '/əˈɡreʃ.ən/', '/ˈædʒ.ə.teɪt/', '/ænˈtæɡ.ən.ɪ.zəm/',
'/ˈbrɪs.əl/', '/ɪɡˈzæs.pə.reɪ.t̬ɪd/', '/ˌkɑːn.trəˈvɝː.ʃəl/','/ˈkræŋ.ki/', '/ˈkrɑː.tʃə.t̬i/', '/dɪsˈɡrʌn.t̬əld/',
'/ɪnˈreɪdʒ/']

vocab_5 = vocab(word_5, api_5)

mean_5 = ['lạm dụng', 'cay gắt', 'gây hấn', 'kích động', 'đối kháng',
'nổi da gà', 'bực tức', 'đối đầu','cáu kỉnh', 'lăn tăn', 'bất bình',
'tức giận']



topic_5 = 'Feelings'

add_all(word_5, api_5, vocab_5, mean_5, topic_5)



word_6 = ['lipstick', 'comb', 'hairbrush', 'needle', 'hands (clock)',
'put something on', 'take something off', 'ordinary', 'hay fever', 'sneeze',
'asthma', 'malaria', 'cholera', 'cancer', 'heart attack',
'panic', 'take a aspirin', 'traffic fumes', 'actually', "it doesn't matter",
"it's up to you", "Why don't we go…", 'What a pity!', 'Look out! / Be careful!', 'Absolutely!',
'Oh dear!', 'around', 'pepper', 'salt', 'pasta',
'vegetarian', 'mushroom', 'garlic', 'onion', 'strawberry',
'grape', 'beans', 'peas', 'spice', 'sausage',
'potato', 'tomato', 'tap', 'sink', 'freezer',
'fridge', 'bin', 'washing machine', 'oven', 'cupboard',
'shelf', 'kitchen counter', 'dish soap', 'tea towel = dishtowel', 'saucepan',
'skillet = frying pan', 'teapot', 'cloth', 'coffee maker', 'plate',
'bowl', 'fork', 'chopsticks', 'mug']

api_6 = ['/ˈlɪp.stɪk/', '/koʊm/', '/ˈher.brʌʃ/', '/ˈniː.dəl/', ' /hænds/',
'/pʊt ɑːn/', '/teɪk ɑːf/', '/ˈɔːr.dən.er.i/', '/ˈheɪ ˌfiː.vɚ/', '/sniːz/',
'/ˈæz.mə/', '/məˈler.i.ə/', '/ˈkɑː.lɚ.ə/', '/ˈkæn.sɚ/', '/ˈhɑːrt əˌtæk/',
'/ˈpæn.ɪk/', '/teɪk ə ˈæs.prɪn/', '/ˈtræf.ɪk fjuːmz/', '/ˈæk.tʃu.ə.li/', '/ɪt ˈdʌznt ˈmætər/',
'/ɪts ʌp tə jə/', '...', '.../ˈpɪt̬.i/', '...', '...',
'...', '/əˈraʊnd/', '/ˈpep.ɚ/', '/sɑːlt/', '/ˈpɑː.stə/',
'/ˌvedʒ.əˈter.i.ən/', '/ˈmʌʃ.ruːm/', '/ˈɡɑːr.lɪk/', '/ˈʌn.jən/', '/ˈstrɑːˌber.i/',
'/ɡreɪp/', '/biːns/', '/piː/', '/spaɪs/', '/ˈsɑː.sɪdʒ/',
'/pəˈteɪ.t̬oʊ/', '/təˈmeɪ.t̬oʊ/', '/tæp/', '/sɪŋk/', '/ˈfriː.zɚ/',
'/frɪdʒ/', '/bɪn/', '/ˈwɑː.ʃɪŋ məˈʃiːn/', '/ˈʌv.ən/', '/ˈkʌb.ɚd/',
'/ʃelf/', '/ˈkɪtʃ.ən ˈkaʊn.t̬ɚ/', '/ˈdɪʃ ˌsoʊp/', '/ˈtiː ˌtaʊəl/ /ˈdɪʃ.taʊəl/', '/ˈsɑː.spən/',
'/ˈskɪl.ɪt/', '/ˈtiː.pɑːt/', '/klɑːθ/', '/ˈkɑː.fi ˌmeɪ.kɚ/', '/pleɪt/',
'/boʊl/', ' /fɔːrk/', '/ˈtʃɑːp.stɪk/', '/mʌɡ/']

vocab_6 = vocab(word_6, api_6)

mean_6 = ['son môi', 'lược', 'bàn chải tóc', 'cây kim', 'kim đồng hồ',
'mặc vào', 'cởi ra', 'bình thường', 'sốt mùa hè', 'hắt hơi',
'hen suyễn', 'bệnh sốt rét', 'dịch tả', 'ung thư', 'đau tim',
'hoảng loạn', 'uống thuốc', 'khói bụi giao thông', 'thực ra', 'không vấn đề gì đâu',
'tùy bạn', 'How/what about going…', 'Tiếc quá!', 'Cẩn thận!', 'Chắc chắn rồi!',
'Trời ơi!', 'khoảng hoặc xấp xỉ', 'tiêu', 'muối', 'mì ống',
'ăn chay/người ăn chay', 'nấm', 'tỏi', 'củ hành', 'dâu tây',
'nho', 'hạt đậu', 'đậu Hà Lan', 'gia vị', 'xúc xích, lạp xưởng',
'khoai tây', 'cà chua', 'vòi nước', 'bồn rửa', 'tủ đông',
'tủ lạnh', 'thùng rác', 'máy giặt', 'lò nướng', 'tủ đựng chén, gia vị,…',
'cái kệ', 'kệ, bàn trong nhà bếp', 'nước rửa chén', 'khăn lót', 'cái nồi',
'cái chảo', 'ấm trà', 'khăn lau', 'máy pha ca phê', 'đĩa',
'tô', 'nĩa', 'đũa', 'cái ca']

topic_6 = 'Things'

add_all(word_6, api_6, vocab_6, mean_6, topic_6)




all_topic.extend(['Describing people','Heath and illness','Conversation','Food and drink','In the kitchen',
'In the bedroom and bathroom','In the living room','Jobs','At school and university','Communications',
'Holidays','Shops and shopping','Eating out','Sports'])




def clearFrame(frame):
    for widget in frame.winfo_children():
       widget.destroy()



#Multiple-choice in Menu
def button_exit(frame, row, column):
    button_exit = Button(frame, text = "Exit", font = ("Cambria", 10), padx = 40, pady = 20, command = root.quit, bg = "red").grid(row = row, column = column)



def button_menu(frame, row, column, sticky = ''):
    back = Button(frame, text = "Menu", font = ("Cambria", 10), bg = '#d8d81c', command = lambda : menu(frame), padx = 50, pady = 20)
    if sticky != '':
        back.grid(row = row, column = column, sticky = sticky)
    else:
        back.grid(row = row, column = column)



def button_lesson(frame, lesson):
    if lesson % 2 == 0:
        if ((lesson - 1) // 10) % 2 == 0:
            bg = '#40dddd'
        else:
            bg = '#45e045'
    else:
        if ((lesson - 1) // 10) % 2 == 0:
            bg = '#45e045'
        else:
            bg = '#40dddd'
        
    button_lesson = Button(root, text = "Unit " + str(lesson) + ': ' + str(all_topic[lesson]), anchor = W, font = ("Cambria", 20), bg = bg, fg = '#111147', width = 30, command = lambda : setup(lesson)).grid(row = (lesson - 1) % 10 + 1, column = (lesson - 1) // 10)



def setup(lesson):
    global wrong_word
    global wrong_mean
    global wrong_choice
    global wrong_image
    global list_number
    wrong_word = []
    wrong_mean = []
    wrong_choice = []
    wrong_image = []
    list_number = [i for i in range(0, len(all_vocab[lesson]))]
    shuffle(list_number)
    if lesson in all_lesson_img:
        multiple_choice_play_image(root, lesson)
    else:
        multiple_choice_play(root, lesson)



def select_vocab(lesson, number_real):
    mean_real = all_mean[lesson][number_real]
    words = [mean_real]
    while len(words) != 4:
        k = randint(0, len(all_vocab[lesson]) - 1)
        if all_mean[lesson][k] not in words:
            words.append(all_mean[lesson][k])
    shuffle(words)
    return words



def check(words, real_number, lesson):
    if all_mean[lesson][real_number] != words:
        if lesson == 5:
            wrong_word.append(all_word[lesson][real_number])
            wrong_mean.append(all_vocab[lesson][real_number])
            wrong_choice.append(words)
        else:
            wrong_word.append(all_word[lesson][real_number])
            wrong_mean.append(all_mean[lesson][real_number])
            wrong_choice.append(words)
    clearFrame(root)
    multiple_choice_play(root, lesson)



def check_image(words, real_number, lesson):
    if all_vocab[lesson][real_number][1] != words:
        wrong_image.append(all_vocab[lesson][real_number][0])
        wrong_mean.append(all_vocab[lesson][real_number][1])
        wrong_choice.append(words)
    clearFrame(root)
    multiple_choice_play_image(root, lesson)



def result(root, length_lesson):
    root.geometry("920x780")
    clearFrame(root)
    if len(wrong_word) == 0:
        congra = Label(root, text = "CONGRATULATION!!!!!!!! 100%", font = ("Cambria", 35)).grid(row = 0, column = 1)
        
    for i in range(len(wrong_word)):
        new_label = Label(root, text = wrong_word[i] + " : " + wrong_mean[i], font = ("Cambria", 15)).grid(row = i, column = 0)  
        new_label1 = Label(root, text = "Your choice: " + wrong_choice[i], font = ("Cambria", 15)).grid(row = i, column = 2) 
    label = Label(root, text = "Your Score = " + str(length_lesson - len(wrong_word)) + "/" + str(length_lesson), font = ("Cambria", 23), bg = "green").grid(row = len(wrong_word) + 1, column = 1)
    button_menu(root, len(wrong_word) + 1, 0)
    button_exit(root, len(wrong_word) + 1, 2)



def check_result(root, length_lesson, index, lesson, real_number):
    list_number.insert(0, real_number)
    result_image(root, length_lesson, index, lesson)



def result_image(root, length_lesson, index, lesson):
    root.geometry("1053x780")
    clearFrame(root)
    if len(wrong_mean) == 0:
        congra = Label(root, text = "CONGRATULATION!!!!!!!! 100%",font = ("Cambria", 35)).grid(row = 0, column = 1)
    else:
        correct_word = Label(root, text = wrong_mean[index], font = ("Cambria", 33), width = 30, fg = "green").grid(row = 0, column = 1)
        image = Label(root, image = wrong_image[index], width = 450, height = 300).grid(row = 1,column = 1)
        your_choice = Label(root, text = "Your choice:", font = ("Cambria", 23)).grid(row = 2, column = 0)
        wrong_word = Label(root, text = wrong_choice[index], font = ("Cambria", 23)).grid(row = 2, column = 1)
        remain = Label(root, text = str(index + 1) + "/" + str(len(wrong_mean)), font = ("Cambria", 18)).grid(row = 9, column = 1)

    if index < len(wrong_mean) - 1:
        next_button = Button(root, text = "Next", font = ("Cambria", 23), padx = 30, pady = 10, bg = "#76b538", command = lambda : result_image(root, length_lesson, index + 1, lesson)).grid(row = 9, column =  2)
    if index > 0:    
        back_button = Button(root, text = "Back", font = ("Cambria", 23), padx = 30, pady = 10, bg = "#76b538", command = lambda : result_image(root, length_lesson, index - 1, lesson)).grid(row = 9, column =  0)
    button_menu(root, 10, 0)
    button_exit(root, 10, 2)
    
    if list_number:
        score = Label(root, text = "Your Score = " + str(length_lesson - len(wrong_mean) - len(list_number)) + "/" + str(length_lesson - len(list_number)), font = ("Cambria", 23), bg = "green").grid(row = 11, column = 1)
        cont = Button(root, text = "Continue", font = ("Cambria", 23), padx = 30, pady = 10, bg = "gray", command = lambda : multiple_choice_play_image(root, lesson)).grid(row = 12, column = 1)   
    else:
        score = Label(root, text = "Your Score = " + str(length_lesson - len(wrong_mean)) + "/" + str(length_lesson), font = ("Cambria", 23),bg = "green").grid(row = 11, column = 1)



def multiple_choice(root):
    clearFrame(root)
    root.geometry("920x650")
    lesson_label = Label(root, text = "Your lesson", font = ("Cambria", 30), width = 20).grid(row = 0, column = 0, columnspan = 2)
    #v = StringVar()
    #lesson = Entry(root, font = ("Cambria", 40), width = 5, borderwidth = 5, bg = "white", fg = "black", textvariable = v).grid(row = 0, column = 1)
    #Enter = Button(root, text = "Enter", font = ("Cambria", 30), width = 4, command = lambda: setup(int(v.get()))).grid(row = 1, column = 1)
    unit1 = button_lesson(root, 1)
    unit2 = button_lesson(root, 2)
    unit3 = button_lesson(root, 3)
    unit4 = button_lesson(root, 4)
    unit5 = button_lesson(root, 5)
    unit6 = button_lesson(root, 6)
    unit7 = button_lesson(root, 7)
    unit8 = button_lesson(root, 8)
    unit9 = button_lesson(root, 9)
    unit10 = button_lesson(root, 10)
    unit11 = button_lesson(root, 11)
    unit12 = button_lesson(root, 12)
    unit13 = button_lesson(root, 13)
    unit14 = button_lesson(root, 14)
    unit15 = button_lesson(root, 15)
    unit16 = button_lesson(root, 16)
    unit17 = button_lesson(root, 17)
    unit18 = button_lesson(root, 18)
    unit19 = button_lesson(root, 19)
    unit20 = button_lesson(root, 20)    



def multiple_choice_play(root, lesson):
    clearFrame(root)
    root.geometry("980x1000")
    length_lesson = len(all_vocab[lesson])
    index_number = 0

    while True:
        if len(list_number) != 0:
            global real_number
            real_number = list_number[index_number]
        else:
            break

        if real_number >= length_lesson:
            list_number.pop(0)
        else:
            break
    

    if len(list_number) == 0:
        result(root, length_lesson)
    else:
        list_number.pop(0)
        words = select_vocab(lesson, real_number)
        word_size = 24
        width = 20 

        left = Label(root, text = " " * 62).grid(row = 0,column = 0) 
        top = Label(root, text = '\n' * 3).grid(row = 0,column = 1)

        topic = Label(root, text = "Topic : " + all_topic[lesson], font = ("Cambria", 28), width = 30, height = 0, bg = "white", fg = "#841f50").grid(row = 0,column = 1)

        word = Label(root, text = all_vocab[lesson][real_number], font = ("Cambria", word_size), width = 30, height = 0, bg = "green", fg = "black").grid(row = 1,column = 1)
        option1 = Button(root, text = words[0], font = ("Cambria", word_size), width = width, height = 0, bg = "#330066", fg = "black", command = lambda : check(words[0], real_number, lesson)).grid(row = 2, column = 1)
        option2 = Button(root, text = words[1], font = ("Cambria", word_size), width = width, height = 0, bg = "#330066", fg = "black", command = lambda : check(words[1], real_number, lesson)).grid(row = 3, column = 1)
        option3 = Button(root, text = words[2], font = ("Cambria", word_size), width = width, height = 0, bg = "#330066", fg = "black", command = lambda : check(words[2], real_number, lesson)).grid(row = 4, column = 1)
        option4 = Button(root, text = words[3], font = ("Cambria", word_size), width = width, height = 0, bg = "#330066", fg = "black", command = lambda : check(words[3], real_number, lesson)).grid(row = 5, column = 1)

        remain = Label(root, text = str(all_length[lesson] - len(list_number)) + "/" + str(all_length[lesson]), font = ("Cambria", 18)).grid(row = 10, column = 1)

        space = Label(root, text = ' ' * 8).grid(column = 5)

        button_menu(root, 10, 0)
        button_exit(root, 10, 10)



def multiple_choice_play_image(root, lesson):
    clearFrame(root)
    root.geometry("980x1000")
    length_lesson = len(all_vocab[lesson])
    index_number = 0

    while True:
        if len(list_number) != 0:
            real_number = list_number[index_number]
        else:
            break

        if real_number >= length_lesson:
            list_number.pop(0)
        else:
            break
    

    if len(list_number) == 0:
        result_image(root, length_lesson, 0, lesson)
    else:
        list_number.pop(0)

        words = select_vocab(lesson, real_number)

        width = 20
        padx = 100
        pady = 40
        size_word = 20
        left = Label(root, text = " " * 62).grid(row = 0, column = 0) 
        top = Label(root, text = "\n" * 3).grid(row = 0, column = 1)

        topic = Label(root, text = "Topic : " + all_topic[lesson], font = ("Cambria", 28), width = 30, height = 0, bg = "white", fg = "#841f50").grid(row = 0,column = 1)

        image = Label(root, image = all_vocab[lesson][real_number][0],width = 450,height = 300).grid(row = 1,column = 1)
        option1 = Button(root, text = words[0], font = ("Cambria", size_word), width = width, height = 0, bg = "#330066", fg = "black", command = lambda : check_image(words[0], real_number, lesson)).grid(row = 2, column = 1)
        option2 = Button(root, text = words[1], font = ("Cambria", size_word), width = width, height = 0, bg = "#330066", fg = "black", command = lambda : check_image(words[1], real_number, lesson)).grid(row = 3, column = 1)
        option3 = Button(root, text = words[2], font = ("Cambria", size_word), width = width, height = 0, bg = "#330066", fg = "black", command = lambda : check_image(words[2], real_number, lesson)).grid(row = 4, column = 1)
        option4 = Button(root, text = words[3], font = ("Cambria", size_word), width = width, height = 0, bg = "#330066", fg = "black", command = lambda : check_image(words[3], real_number, lesson)).grid(row = 5, column = 1)

        remain = Label(root, text = str(all_length[lesson] - len(list_number)) + "/" + str(all_length[lesson]), font = ("Cambria", 18)).grid(row = 10, column = 1)

        space = Label(root, text = ' ' * 8).grid(column = 5)

        button_menu(root, 10, 0)
        if len(list_number) != length_lesson - 1:
            check = Button(root, text="Check", command = lambda : check_result(root, length_lesson, 0, lesson, real_number), padx = 50, pady = 20).grid(row = 10, column = 2)

    

#Your Vocabulary
def show_vocab(root, lesson):
    if lesson not in all_lesson_img:
        show_vocab_normal(root, lesson, 0)
    elif lesson :
        show_vocab_img(root, lesson, 0)



def show_vocab_normal(root, lesson, index):
    clearFrame(root)
    root.geometry("1120x880")
    space = Label(root, text = ' ' * 9).grid(row = 0, column = 0)
    space_ = Label(root, text = ' ' * 9).grid(row = 0, column = 5)
    your_vocab = Label(root, text = 'Vocabulary in topic: ' + all_topic[lesson], font = ("Cambria", 33)).grid(row = 0, column = 1, columnspan = 4)
    number = Label(root, text = 'number', anchor = W, font = ("Cambria", 23), width = 8).grid(row = 1, column = 1)
    words = Label(root, text = 'words', anchor = W, font = ("Cambria", 23), width = 16).grid(row = 1, column = 2)
    apis = Label(root, text = 'API', anchor = W, font = ("Cambria", 23), width = 16).grid(row = 1, column = 3)
    meaning = Label(root, text = 'meaning', anchor = W, font = ("Cambria", 23), width = 20).grid(row = 1, column = 4)

    if all_length[lesson] - 15 >= index:
        last_index = index + 15
    else:
        last_index = all_length[lesson]

    for i in range(index, last_index):
        if i % 2 == 0:
            bg = 'black'
            fg = 'white'
        else:
            bg = 'white'
            fg = 'black'

        num = Label(root, text = str(i + 1), anchor = W, font = ("Cambria", 23), width = 8).grid(row = 2 + (i - index), column = 1)
        word = Label(root, text = all_word[lesson][i], anchor = W, font = ("Cambria", 23), width = 16, fg = fg, bg = bg).grid(row = 2 + (i - index), column = 2)
        api = Label(root, text = all_api[lesson][i], anchor = W, font = ("Cambria", 23), width = 16, fg = fg, bg = bg).grid(row = 2 + (i - index), column = 3)
        mean = Label(root, text = all_mean[lesson][i], anchor = W, font = ("Cambria", 23), width = 20, fg = fg, bg = bg).grid(row = 2 + (i - index), column = 4)
    
    if last_index != all_length[lesson]:
        next_button = Button(root , image = next_img , font = ("Cambria", 23), anchor = W, command = lambda : show_vocab_normal(root, lesson, index + 15)).grid(row = 69, column = 4, sticky = E)

    if index != 0:
        back_button = Button(root, image = prev_img , font = ("Cambria", 23), command = lambda : show_vocab_normal(root, lesson, index - 15)).grid(row = 69, column = 1 , sticky = W)
    else:
        menu = button_menu(root, 69, 1)



def show_vocab_img(root, lesson, index):
    clearFrame(root)
    root.geometry("2000x2000+0+0")
    fg = 'black'
    bg = 'white'
    space = Label(root, text = ' ' * 9).grid(row = 0, column = 0)
    space_ = Label(root, text = ' ' * 9).grid(row = 0, column = 5)
    enter = Label(root, text = '\n' * 4).grid(row = 4, column = 0)
    your_vocab = Label(root, text = 'Vocabulary in topic: ' + all_topic[lesson] + '\n' * 1, font = ("Cambria", 33)).grid(row = 0, column = 1, columnspan = 3)

    if all_length[lesson] - 3 >= index:
        last_index = index + 3
    else:
        last_index = all_length[lesson]

    for i in range(index, last_index):
        num = Label(root, text = str(i + 1), font = ("Cambria", 23)).grid(row = 1, column = 1 + (i - index))
        word = Label(root, image = all_vocab[lesson][i][0], font = ("Cambria", 23), width = 450, height = 300).grid(row = 2, column = 1 + (i - index))
        mean = Label(root, text = all_mean[lesson][i], font = ("Cambria", 23), fg = fg, bg = bg).grid(row = 3, column = 1 + (i - index))

    if last_index != all_length[lesson]:
        next_button = Button(root , image = next_img , font = ("Cambria", 23), anchor = W, command = lambda : show_vocab_img(root, lesson, index + 3)).grid(row = 69, column = 3, sticky = E)

    if index != 0:
        menu = button_menu(root, 70, 2)
        back_button = Button(root, image = prev_img , font = ("Cambria", 23), command = lambda : show_vocab_img(root, lesson, index-3)).grid(row = 69, column = 1 , sticky = W)
    else:
        menu = button_menu(root, 69, 1, W)



def button_lesson_vocab(frame, lesson):
    if lesson % 2 == 0:
        if ((lesson - 1) // 10) % 2 == 0:
            bg = '#a3a349'
        else:
            bg = '#98e2e2'
    else:
        if ((lesson - 1) // 10) % 2 == 0:
            bg = '#98e2e2'
        else:
            bg = '#a3a349'
        
    button_lesson = Button(root, text = "Unit " + str(lesson) + ': ' + str(all_topic[lesson]), anchor = W, font = ("Cambria", 20), bg = bg, fg = '#111147', width = 30, command = lambda : show_vocab(root, lesson)).grid(row = (lesson - 1) % 10 + 1, column = (lesson - 1) // 10)



def your_vocab(root):
    clearFrame(root)
    root.geometry("920x650")
    lesson_label = Label(root, text = "Your lesson", font = ("Cambria", 30), width = 20).grid(row = 0, column = 0, columnspan = 2)
    #v = StringVar()
    #lesson = Entry(root, font = ("Cambria", 40), width = 5, borderwidth = 5, bg = "white", fg = "black", textvariable = v).grid(row = 0, column = 1)
    #Enter = Button(root, text = "Enter", font = ("Cambria", 30), width = 4, command = lambda: setup(int(v.get()))).grid(row = 1, column = 1)
    unit1 = button_lesson_vocab(root, 1)
    unit2 = button_lesson_vocab(root, 2)
    unit3 = button_lesson_vocab(root, 3)
    unit4 = button_lesson_vocab(root, 4)
    unit5 = button_lesson_vocab(root, 5)
    unit6 = button_lesson_vocab(root, 6)
    unit7 = button_lesson_vocab(root, 7)
    unit8 = button_lesson_vocab(root, 8)
    unit9 = button_lesson_vocab(root, 9)
    unit10 = button_lesson_vocab(root, 10)
    unit11 = button_lesson_vocab(root, 11)
    unit12 = button_lesson_vocab(root, 12)
    unit13 = button_lesson_vocab(root, 13)
    unit14 = button_lesson_vocab(root, 14)
    unit15 = button_lesson_vocab(root, 15)
    unit16 = button_lesson_vocab(root, 16)
    unit17 = button_lesson_vocab(root, 17)
    unit18 = button_lesson_vocab(root, 18)
    unit19 = button_lesson_vocab(root, 19)
    unit20 = button_lesson_vocab(root, 20)



#Games

def setup_enter_word(root, lesson):
    global list_number
    global list_fault
    global wrong_word_i3t
    global wrong_word_it4
    wrong_word_i3t = []
    wrong_word_it4 = []
    list_fault = [1,2,3] 
    list_number = [i for i in range(0, len(all_vocab[lesson]))]
    shuffle(list_number)
    if lesson in all_lesson_img:
        enter_your_choice_play_image(root, lesson, 0)
    else:
        enter_your_choice_play(root, lesson, 0)

def result_enter_your_choice():
    clearFrame(root)
    width = 240 + max(len(wrong_word_i3t),len(wrong_word_it4))*30
    root.geometry("1050x"+str(width))
    space = Label(root, text = ' '*14).grid(row=0,column=0)
    correct = Label(root, text = "You are correct " + str(len(list_number)-len(wrong_word_it4))+"/"+str(len(list_number)), font = ("Cambria",40)).grid(row=0, column= 1, columnspan=3)
    i3t = Label(root, text = "Wrong words in 3 times", font = ("Cambria",20)).grid(row = 1, column = 1)
    space = Label(root, text=' '*40).grid(row=1,column=2)
    it4 = Label(root, text = "Wrong words after 4 attempts", font = ("Cambria",20)).grid(row=1, column = 3)
    for i in range(len(wrong_word_i3t)):
        wrong_w = Label(root, text = wrong_word_i3t[i], font = ("Cambria",20)).grid(row=i+2, column=1)

    for i in range(len(wrong_word_it4)):
        wrong_w = Label(root, text = wrong_word_it4[i], font = ("Cambria",20)).grid(row=i+2, column=3)

    menu = button_menu(root, 69, 0)
        

def continue_enter(*args):
    if i+1 == len(list_number):
        result_enter_your_choice()
    else:
        enter_your_choice_play(root, l, i+1)

def onReturn(*args):
    if v.get() == all_word[l][list_number[i]]:
        if len(list_fault) != 3:
            wrong_word_i3t.append(all_word[l][list_number[i]])
        while len(list_fault) != 3:
            list_fault.append(1)
        your_word = Entry(root, font = ("Cambria", 40), width = 20, borderwidth = 5, bg = "white", fg = "green", textvariable = v)
        your_word.grid(row=2,column=1)
        root.bind("<Return>", continue_enter)

    elif len(list_fault) != 0:
        list_fault.pop()
        your_word = Entry(root, font = ("Cambria", 40), width = 20, borderwidth = 5, bg = "white", fg = "red", textvariable = v)
        your_word.grid(row=2,column=1)

    else:
        correct_word = Label(root, text = all_word[l][list_number[i]], font = ("Cambria", 30)).grid(row = 3, column = 1)
        wrong_word_it4.append(all_word[l][list_number[i]])
        while len(list_fault) != 3:
            list_fault.append(1)
        root.bind("<Return>", continue_enter)

def enter_your_choice_play(root, lesson, index):
    clearFrame(root)
    root.geometry('850x500')
    space = Label(root, text = ' '*20).grid(row = 1, column = 0)
    mean = Label(root, text = all_mean[lesson][list_number[index]], font = ("Cambria", 30)).grid(row = 1, column = 1)
    topic = Label(root, text = "Topic : " + all_topic[lesson], font = ("Cambria", 28), width = 30, height = 0, bg = "white", fg = "#841f50").grid(row = 0,column = 1)
    number = Label(root, text = str(index+1) + '/' + str(len(list_number)),font = ("Cambria", 14)).grid(row = 4, column = 1)
    global v
    v = StringVar()
    your_word = Entry(root, font = ("Cambria", 40), width = 20, borderwidth = 5, bg = "white", fg = "black", textvariable = v)
    your_word.focus()
    your_word.grid(row=2,column=1)
    global i
    i = index
    global l
    l = lesson

    root.bind("<Return>", onReturn)

    menu = button_menu(root,69,0)



def button_lesson_enter(frame, lesson):
    if lesson % 2 == 0:
        if ((lesson - 1) // 10) % 2 == 0:
            bg = '#98ea98'
        else:
            bg = '#c96897'
    else:
        if ((lesson - 1) // 10) % 2 == 0:
            bg = '#c96897'
        else:
            bg = '#98ea98'
    button_lesson = Button(root, text = "Unit " + str(lesson) + ': ' + str(all_topic[lesson]), anchor = W, font = ("Cambria", 20), bg = bg, fg = '#111147', width = 30, command = lambda : setup_enter_word(root, lesson)).grid(row = (lesson - 1) % 10 + 1, column = (lesson - 1) // 10)



def enter_your_choice(root):
    clearFrame(root)
    root.geometry("920x650")    
    lesson_label = Label(root, text = "Your lesson", font = ("Cambria", 30), width = 20).grid(row = 0, column = 0, columnspan = 2)
    unit1 = button_lesson_enter(root, 1)
    unit2 = button_lesson_enter(root, 2)
    unit3 = button_lesson_enter(root, 3)
    unit4 = button_lesson_enter(root, 4)
    unit5 = button_lesson_enter(root, 5)
    unit6 = button_lesson_enter(root, 6)
    unit7 = button_lesson_enter(root, 7)
    unit8 = button_lesson_enter(root, 8)
    unit9 = button_lesson_enter(root, 9)
    unit10 = button_lesson_enter(root, 10)
    unit11 = button_lesson_enter(root, 11)
    unit12 = button_lesson_enter(root, 12)
    unit13 = button_lesson_enter(root, 13)
    unit14 = button_lesson_enter(root, 14)
    unit15 = button_lesson_enter(root, 15)
    unit16 = button_lesson_enter(root, 16)
    unit17 = button_lesson_enter(root, 17)
    unit18 = button_lesson_enter(root, 18)
    unit19 = button_lesson_enter(root, 19)
    unit20 = button_lesson_enter(root, 20)


        
    
def game(root):
    clearFrame(root)
    enter = Button(root, text = 'Enter your choice', font = ("Cambria", 30), width = 25, command = lambda: enter_your_choice(root)).grid(row=1,column=1)


def menu(root):
    root.geometry("835x600+300+0")
    clearFrame(root)
    width = 25
    font_size = 43

    button_choice = Button(root, text = "Multiple-choice", font = ("Cambria", font_size), width = width, fg = "green", bg = "yellow", command = lambda : multiple_choice(root))
    button_fc = Button(root, text = "Flash cards", font = ("Cambria", font_size),  width = width, fg = "green", bg = "yellow")
    button_vocab = Button(root, text = "Your vocabulary", font = ("Cambria", font_size),  width = width, fg = "green", bg = "yellow", command = lambda : your_vocab(root))
    button_game = Button(root, text = "Practice", font = ("Cambria", font_size),  width = width, fg = "green", bg = "yellow", command = lambda : enter_your_choice(root))
    button_exit = Button(root, text = "Exit", font = ("Cambria", font_size), width = width, command = root.quit, bg = "red")

    left = Label(root, text = ' ' * 20).grid(row = 0, column = 1)
    top = Label(root, text='\n' * 6).grid(row = 0, column = 1)

    button_choice.grid(row = 1, column = 3)
    button_fc.grid(row = 2, column = 3)
    button_vocab.grid(row = 3, column = 3)
    button_game.grid(row = 4, column = 3)
    button_exit.grid(row = 5, column = 3)




menu(root)
root.mainloop()
